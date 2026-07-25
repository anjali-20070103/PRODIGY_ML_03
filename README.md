# PRODIGY_ML_03

# Hand Gesture Recognition using Support Vector Machine (SVM)

## 📌 Project Overview

This project was developed as part of my Machine Learning Internship at Prodigy InfoTech. The objective of this project is to develop a Hand Gesture Recognition System using the Support Vector Machine (SVM) algorithm. The model classifies different hand gestures from image data, enabling gesture-based human-computer interaction.

---

## 🎯 Objective

To develop a machine learning model that accurately identifies and classifies different hand gestures from images using Support Vector Machine (SVM).

---

## 📂 Dataset

Dataset Name: LeapGestRecog

Source: Kaggle

Dataset Link:
https://www.kaggle.com/datasets/gti-upm/leapgestrecog

**Note:** The dataset is not included in this repository because of its large size. Please download it from the Kaggle link above and extract it into the project folder before running the code.

---

## 🛠 Technologies Used

- Python
- NumPy
- OpenCV
- Matplotlib
- Scikit-learn

---

## 🤖 Machine Learning Algorithm

- Support Vector Machine (SVM)

---

## 🔄 Project Workflow

1. Import required libraries.
2. Load the LeapGestRecog dataset.
3. Read gesture images.
4. Convert images to grayscale.
5. Resize images to 64 × 64 pixels.
6. Flatten images into feature vectors.
7. Split the dataset into training and testing sets.
8. Train the Support Vector Machine (SVM) model.
9. Predict hand gestures.
10. Evaluate the model using Accuracy Score, Classification Report, and Confusion Matrix.
11. Display sample predictions using Matplotlib.

---

## 📊 Output

- Model Accuracy
- Classification Report
- Confusion Matrix
- Sample Hand Gesture Predictions

---

## 📁 Project Structure

```
PRODIGY_ML_04
│
├── hand_gesture_recognition.py
├── README.md
├── requirements.txt
├── prediction_results.png
└── leapGestRecog (Download separately from Kaggle)
```

---

## ▶️ How to Run

### 1. Install the required libraries

```bash
pip install -r requirements.txt
```

### 2. Download the dataset

Download the LeapGestRecog dataset from Kaggle and extract it into the project folder.

### 3. Run the program

```bash
python hand_gesture_recognition.py
```

---

## 📈 Results

The trained Support Vector Machine (SVM) model successfully classifies hand gestures from the dataset. The model performance is evaluated using:

- Accuracy Score
- Classification Report
- Confusion Matrix
- Sample Gesture Prediction Images

---

## 📚 Learning Outcomes

- Image Preprocessing
- Computer Vision Basics
- Feature Extraction
- Support Vector Machine (SVM)
- Image Classification
- Machine Learning Model Evaluation

---

## 👩‍💻 Author

**Batchala Anjali**

B.Tech – Computer Science and Engineering (AI & ML)

GMR Institute of Technology

Machine Learning Intern – Prodigy InfoTech

---
⭐ If you found this project useful, consider giving it a star on GitHub.
