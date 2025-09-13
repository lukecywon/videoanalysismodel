from transformers import pipeline
import torch

class SentimentAnalyzer:
    def __init__(self):
        self.model_name = "cardiffnlp/twitter-roberta-base-sentiment-latest"
        self.device_index = 0 if torch.cuda.is_available() else -1
        self.sentiment_pipeline = pipeline("sentiment-analysis", model=self.model, tokenizer=self.tokenizer)

    def analyze_sentiment(self, comments):
        results = self.sentiment_pipeline(comments)
        sentiments = [result['label'] for result in results]
        scores = [result['score'] for result in results]
        return sentiments, scores