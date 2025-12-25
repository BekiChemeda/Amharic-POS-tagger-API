import pickle
import re
import os
from app.core.config import settings

class AmharicTagger:
    def __init__(self, model_path: str):
        self.model_path = model_path
        self.crf_model = None
        self.punctuations = "፥፤፡።፣!?፨፠።፡፣፤"
        self._load_model()

    def _load_model(self):
        if not os.path.exists(self.model_path):
            print(f"Warning: Model file {self.model_path} not found.")
            return
        
        try:
            with open(self.model_path, "rb") as f:
                self.crf_model = pickle.load(f)
            print(f"Model loaded successfully from {self.model_path}")
        except Exception as e:
            print(f"Error loading model: {e}")

    def tokenize(self, text: str):
        return re.findall(rf'[\w]+|[{self.punctuations}]', text)

    def _extract_word_features(self, sent, i):
        word = sent[i]
        prevword = sent[i - 1] if i > 0 else '<START>'
        prev2word = sent[i - 2] if i > 1 else '<START>'
        nextword = sent[i + 1] if i < len(sent) - 1 else '<END>'

        return {
            'word': word,
            'prevword': prevword,
            'nextword': nextword,
            'prev2word': prev2word
        }

    def _sent2features(self, sent):
        return [self._extract_word_features(sent, i) for i in range(len(sent))]

    def predict(self, text: str):
        if not self.crf_model:
            return None, None
        
        tokens = self.tokenize(text)
        if not tokens:
            return [], []
            
        features = self._sent2features(tokens)
        pos_tags = self.crf_model.predict([features])[0]
        return tokens, pos_tags

# Singleton instance
tagger_service = AmharicTagger(settings.MODEL_PATH)
