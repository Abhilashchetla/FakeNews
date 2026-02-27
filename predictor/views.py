import os
import pickle
import re
from django.conf import settings
from django.shortcuts import render

MODEL_PATH = os.path.join(settings.BASE_DIR, "predictor", "model2.pkl")
VECTORIZER_PATH = os.path.join(settings.BASE_DIR, "predictor", "vectorizer.pkl")

model = pickle.load(open(MODEL_PATH, "rb"))
vectorizer = pickle.load(open(VECTORIZER_PATH, "rb"))

def clean(text):
    text = re.sub(r'\W', ' ', text)
    return text.lower()

def home(request):
    result = None

    if request.method == "POST":
        news = request.POST.get("news")
        cleaned = clean(news)
        vector = vectorizer.transform([cleaned])
        prediction = model.predict(vector)

        result = "REAL NEWS" if prediction[0] == 1 else "FAKE NEWS"

    return render(request, "index.html", {"result": result})
