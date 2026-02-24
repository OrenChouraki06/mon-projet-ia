import re

POSITIVE_WORDS = {
    'good', 'great', 'excellent', 'amazing', 'wonderful', 'fantastic', 'positive', 'happy', 'love'
}
NEGATIVE_WORDS = {
    'bad', 'terrible', 'awful', 'horrible', 'negative', 'sad', 'hate', 'worst', 'disappointing'
}

def normalize_text(text):
    """ Normalize the input text by converting it to lowercase and removing non alphanumeric characters."""

    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)

    words = re.findall(r'\w+', text, flags=re.UNICODE)
    return words

def predict_sentiment(text):
    """ Predict the sentiment of the input text based on the presence of positive and negative words."""

    words = normalize_text(text)

    positive_words = [word for word in words if word in POSITIVE_WORDS]
    negative_words = [word for word in words if word in NEGATIVE_WORDS]

    positive_count = len(positive_words)
    negative_count = len(negative_words)

    if positive_count > negative_count:
        label = "positive"
    elif negative_count > positive_count:
        label = "negative"
    else:
        label = "neutral"

    return {
        "label": label,
        "details" : {
            "positive_words": positive_words,
            "negative_words": negative_words
        }
    }