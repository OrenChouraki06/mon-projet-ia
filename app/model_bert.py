import json
import torch
import torch.nn.functional as F
from transformers import BertTokenizer, BertModel

from sentiment_classifier import SentimentClassifier

config = {
    "BERT_MODEL": "bert-base-cased",
    "PRE_TRAINED_MODEL": "model_state_dict.bin",
    "CLASS_NAMES": ["negative", "neutral", "positive"],
    "MAX_SEQUENCE_LENGTH": 160
}

class Model:
    def __init__(self):
        self.device = torch.device('cpu')
        self.tokenizer = BertTokenizer.from_pretrained(config["BERT_MODEL"])
        classifier = SentimentClassifier(len(config["CLASS_NAMES"]))
        classifier.load_state_dict(torch.load(config["PRE_TRAINED_MODEL"], map_location=self.device), strict=False)
        classifier = classifier.eval()
        self.classifier = classifier.to(self.device)

    def predict(self, text):
        encoded_text = self.tokenizer.encode_plus(
            text,
            max_length=config["MAX_SEQUENCE_LENGTH"],
            add_special_tokens=True,
            return_token_type_ids=False,
            pad_to_max_length=True,
            return_attention_mask=True,
            return_tensors='pt'
        )
        input_ids = encoded_text['input_ids'].to(self.device)
        attention_mask = encoded_text['attention_mask'].to(self.device)

        with torch.no_grad():
            outputs = self.classifier(input_ids, attention_mask)
            probabilities = F.softmax(outputs, dim=1)

        confidence, predicted_class = torch.max(probabilities, dim=1)
        predicted_class = predicted_class.cpu().item()
        confidence = confidence.cpu().item()
        proba = probabilities.flatten().cpu().numpy().tolist()

        return (
            config["CLASS_NAMES"][predicted_class],
            confidence,
            dict(zip(config["CLASS_NAMES"], proba))
        )

model = Model()

def get_model():
    return model
