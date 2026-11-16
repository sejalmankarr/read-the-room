from transformers import pipeline

_classifier = None


def get_classifier():
    # Load the model only once, the first time it's needed
    global _classifier
    if _classifier is None:
        _classifier = pipeline(
            "sentiment-analysis",
            model="cardiffnlp/twitter-roberta-base-sentiment-latest",
        )
    return _classifier


def analyze_text(text):
    result = get_classifier()(text, truncation=True, max_length=512)[0]
    return {
        "label": result["label"].lower(),
        "score": round(result["score"] * 100, 1),
    }