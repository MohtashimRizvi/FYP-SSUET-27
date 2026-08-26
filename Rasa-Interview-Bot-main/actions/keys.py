from typing import Dict, List

ANSWER_KEYS: Dict[str, List[str]] = {
    # --- Web Development ---
    "What is the difference between HTML and XHTML?": [
        "html", "xhtml", "syntax", "strict", "closing", "tags", "xml", "sgml", "case", "parsing"
    ],
    "Explain the concept of responsive design.": [
        "responsive", "design", "screen", "mobile", "layout", "media", "queries", "fluid", "grid", "flexible"
    ],
    "What are semantic HTML tags?": [
        "semantic", "tags", "meaning", "header", "footer", "article", "section", "nav", "seo", "accessibility"
    ],
    "How does CSS specificity work?": [
        "css", "specificity", "priority", "inline", "id", "class", "element", "selector", "rule", "conflict"
    ],
    "What is the difference between inline, internal, and external CSS?": [
        "inline", "internal", "external", "style", "tag", "linked", "reusable", "maintainability", "page", "override"
    ],
    "Explain the difference between GET and POST methods.": [
        "get", "post", "url", "body", "secure", "idempotent", "cached", "parameters", "fetch", "submit"
    ],
    "What is the DOM?": [
        "dom", "document", "object", "model", "html", "tree", "elements", "nodes", "javascript", "structure"
    ],
    "What are cookies, localStorage, and sessionStorage?": [
        "cookies", "localstorage", "sessionstorage", "persistent", "temporary", "client", "data", "storage", "expire", "browser"
    ],
    "Explain the difference between client-side and server-side rendering.": [
        "client", "server", "rendering", "browser", "html", "dynamic", "static", "seo", "load", "framework"
    ],
    "What is REST API?": [
        "rest", "api", "http", "methods", "get", "post", "stateless", "json", "xml", "resource"
    ],

    # --- App Development ---
    "What is the difference between native and hybrid apps?": [
        "native", "hybrid", "sdk", "wrapper", "performance", "ux", "hardware", "codebase", "platform", "cost"
    ],
    "Explain the concept of MVC architecture.": [
        "mvc", "model", "view", "controller", "pattern", "structure", "scalability", "modular", "maintainability", "coupling"
    ],
    "What are fragments in Android?": [
        "fragments", "android", "ui", "modular", "reusable", "dynamic", "container", "replaceable", "lightweight", "layout"
    ],
    "What is SwiftUI?": [
        "swiftui", "apple", "ui", "framework", "declarative", "modern", "reactive", "cross", "platform", "syntax"
    ],
    "Explain the difference between synchronous and asynchronous tasks.": [
        "sync", "async", "blocking", "nonblocking", "sequential", "parallel", "efficient", "scalable", "predictable", "concurrent"
    ],
    "What is dependency injection?": [
        "dependency", "injection", "ioc", "coupling", "testing", "pattern", "flexible", "modular", "reusable", "maintainable"
    ],
    "What are push notifications?": [
        "push", "notifications", "server", "device", "engagement", "permission", "fcm", "apns", "real", "time"
    ],
    "Explain the difference between SQLite and Realm.": [
        "sqlite", "realm", "relational", "object", "schema", "tables", "mobile", "lightweight", "developer", "friendly"
    ],
    "What is Flutter?": [
        "flutter", "google", "ui", "toolkit", "dart", "cross", "platform", "native", "widgets", "hotreload"
    ],
    "How do you handle app lifecycle events?": [
        "app", "lifecycle", "events", "states", "managed", "predictable", "important", "resume", "pause", "destroy"
    ],

    # --- AI ---
    "What is supervised learning?": [
        "supervised", "learning", "labeled", "data", "training", "prediction", "classification", "regression", "examples", "output"
    ],
    "Explain the difference between classification and regression.": [
        "classification", "regression", "categories", "values", "predict", "continuous", "discrete", "labels", "output", "target"
    ],
    "What is overfitting?": [
        "overfitting", "training", "memorize", "generalization", "test", "data", "model", "performance", "error", "complexity"
    ],
    "What is a neural network?": [
        "neural", "network", "layers", "nodes", "weights", "activation", "function", "deep", "learning", "connections"
    ],
    "Explain the concept of backpropagation.": [
        "backpropagation", "weights", "update", "error", "gradient", "descent", "training", "neural", "network", "optimization"
    ],
    "What is reinforcement learning?": [
        "reinforcement", "learning", "reward", "agent", "environment", "policy", "action", "state", "feedback", "decision"
    ],
    "What is the difference between AI, ML, and DL?": [
        "ai", "ml", "dl", "artificial", "intelligence", "machine", "learning", "deep", "neural", "network"
    ],
    "Explain the concept of natural language processing.": [
        "nlp", "natural", "language", "processing", "text", "speech", "understanding", "tokens", "semantics", "syntax"
    ],
    "What are embeddings?": [
        "embeddings", "representation", "vector", "words", "semantic", "space", "similarity", "dense", "features", "mapping"
    ],
    "What is transfer learning?": [
        "transfer", "learning", "pretrained", "model", "reuse", "fine", "tune", "knowledge", "adaptation", "domain"
    ]
}

SKIP_PHRASES = {
    "skip",
    "i don't know",
    "idk",
    "pass",
    "move on",
    "next",
    "leave this one",
    "i can't answer",
    "lets skip",
    "let's skip",
    "no idea",
    "not sure",
}