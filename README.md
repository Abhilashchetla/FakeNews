# Fake News Detection System

## Project Overview

The Fake News Detection System is a machine learning based web application that identifies whether a news article is **Real or Fake**.

Users can enter news content into the system, and the machine learning model analyzes the text and predicts the authenticity of the news.

This project demonstrates the integration of **Machine Learning with a Django web application**.

---

## Technologies Used

Python
Django
Machine Learning
Scikit-learn
NumPy
Pandas
HTML
CSS
JavaScript

---

## Features

* Detects whether news is **Fake or Real**
* User-friendly web interface
* Machine learning model for prediction
* Text preprocessing and feature extraction
* Fast prediction results

---

## How It Works

1. User enters a news article or text.
2. The system preprocesses the text.
3. The trained machine learning model analyzes the content.
4. The model predicts whether the news is **Fake** or **Real**.
5. The result is displayed to the user.

---

## Machine Learning Model

The model is trained using a labeled dataset of real and fake news articles.

Steps used in the model:

* Text cleaning
* Tokenization
* Feature extraction using **TF-IDF**
* Classification using **Logistic Regression**

---

## Project Structure

fake-news-detection
│
├── predictor
│   ├── model.pkl
│   ├── vectorizer.pkl
│
├── templates
│   ├── index.html
│   ├── result.html
│
├── static
│
├── views.py
├── urls.py
├── manage.py

---

## Installation

Clone the repository

git clone https://github.com/your-username/fake-news-detection.git

Move to the project folder

cd fake-news-detection

Install required packages

pip install -r requirements.txt

Run the server

python manage.py runserver

Open the application in browser

http://127.0.0.1:8000
---
## Future Improvements

* Add deep learning models
* Improve prediction accuracy
* Add news source verification
* Deploy the application online

---

## Author

Chetla Abhilash

LinkedIn:
https://www.linkedin.com/in/chetla-abhilash1903/
