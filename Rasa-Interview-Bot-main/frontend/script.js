const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
recognition.lang = "en-US";

async function sendToRasa(text) {
    document.getElementById("you").innerText = text;

    const response = await fetch("http://localhost:5005/webhooks/rest/webhook", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            sender: "browser_user",
            message: text
        })
    });

    const data = await response.json();
    const botText = data.map(m => m.text).join(" ");

    document.getElementById("bot").innerText = botText;
    speak(botText);
}

function speak(text) {
    const speech = new SpeechSynthesisUtterance(text);
    speech.lang = "en-US";
    window.speechSynthesis.speak(speech);
}

recognition.onresult = (event) => {
    const text = event.results[0][0].transcript;
    sendToRasa(text);
};

function handleVoiceChat() {
    recognition.start();
}
