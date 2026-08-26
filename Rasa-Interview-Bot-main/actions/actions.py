import random
import re
import os
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from datetime import datetime
from .keys import *
from .questions import *

# Helper to normalize text
def normalize(text: Text) -> Text:
    return re.sub(r"\s+", " ", text.strip().lower())


def is_skip(text: Text) -> bool:
    t = normalize(text)
    if t in SKIP_PHRASES:
        return True
    return any(phrase in t for phrase in SKIP_PHRASES)

class ActionAskQuestions(Action):
    def name(self) -> Text:
        return "action_ask_questions"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        tech = tracker.get_slot("technology")
        if not tech:
            dispatcher.utter_message(text="Please specify Web Development, App Development, or AI.")
            return []

        q_list = questions.get(tech.lower(), [f"Tell me about your experience with {tech}"])
        selected_questions = random.sample(q_list, 5)

        dispatcher.utter_message(text=f"Great! Let's start your {tech} interview.")
        dispatcher.utter_message(text=f"First question: {selected_questions[0]}")

        return [
            {"event": "slot", "name": "questions", "value": selected_questions},
            {"event": "slot", "name": "current_question_index", "value": 0},
            {"event": "slot", "name": "answers", "value": []},
            {"event": "slot", "name": "scores", "value": []}
        ]


def calculate_score(question: Text, answer: Text) -> int:
    """Tiered scoring based on keyword matches."""
    keywords = ANSWER_KEYS.get(question, [])
    answer = answer.lower()

    match_count = sum(1 for key in keywords if key in answer)

    if match_count == 0:
        return 2
    if match_count == 1:
        return 4
    if match_count == 2:
        return 6
    if match_count == 3:
        return 8
    return 9  # 4+ matches

class ActionStoreAnswers(Action):
    def name(self) -> Text:
        return "action_store_answers"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_text = tracker.latest_message.get("text", "")
        answers = tracker.get_slot("answers") or []
        scores = tracker.get_slot("scores") or []
        questions = tracker.get_slot("questions") or []
        index = int(tracker.get_slot("current_question_index") or 0)

        if not questions or index >= len(questions):
            dispatcher.utter_message(text="No active question found. Restarting interview flow.")
            return [{"event": "slot", "name": "current_question_index", "value": 0}]

        question = questions[index]

        # ✅ Skip detection
        skip_phrases = ["skip", "i don't know", "pass", "move on", "next", "leave this one"]
        if any(phrase in user_text.lower() for phrase in skip_phrases):
            score = 0
            answers.append("Skipped")
            dispatcher.utter_message(text="Okay, noted as skipped. Score: 0/10.")
        else:
            # ✅ Use tiered keyword scoring
            score = calculate_score(question, user_text)
            answers.append(user_text)
            dispatcher.utter_message(text=f"Got it! I scored your answer {score}/10.")

        scores.append(score)
        next_index = index + 1

        if next_index < len(questions):
            dispatcher.utter_message(text=f"Next question: {questions[next_index]}")
            return [
                {"event": "slot", "name": "answers", "value": answers},
                {"event": "slot", "name": "scores", "value": scores},
                {"event": "slot", "name": "current_question_index", "value": next_index}
            ]
        else:
            return [
                {"event": "slot", "name": "answers", "value": answers},
                {"event": "slot", "name": "scores", "value": scores},
                {"event": "slot", "name": "current_question_index", "value": next_index},
                {"event": "followup", "name": "action_finalize_interview"}
            ]



class ActionFinalizeInterview(Action):
    def name(self) -> Text:
        return "action_finalize_interview"

    def run(self, dispatcher, tracker, domain):
        answers = tracker.get_slot("answers") or []
        scores = tracker.get_slot("scores") or []
        questions = tracker.get_slot("questions") or []

        total = sum(scores) if scores else 0
        skipped_count = sum(1 for a in answers if normalize(a) == "skipped")

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        os.makedirs("results", exist_ok=True)
        filename = f"results/interview-{timestamp}.txt"

        with open(filename, "w", encoding="utf-8") as f:
            for i, (q, ans, sc) in enumerate(zip(questions, answers, scores), 1):
                f.write(f"Q{i}: {q}\n")
                f.write(f"Answer: {ans}\n")
                f.write(f"Score: {sc}/10\n\n")

            f.write(f"Total: {total}/{10 * len(questions)}\n")
            f.write(f"Skipped: {skipped_count}\n")

        dispatcher.utter_message(
            text=f"All answers saved. File created: {filename}"
        )
        dispatcher.utter_message(text="Thanks for your time. Goodbye!")

        return []
