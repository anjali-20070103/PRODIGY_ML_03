import os
import cv2
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt

# Dataset path
dataset_path = "leapGestRecog"

# Store images and labels
images = []
labels = []

print("Loading Dataset...")

import os
import cv2
import numpy as np

# Dataset path
dataset_path = "leapGestRecog"

# Lists to store images and labels
images = []
labels = []

print("Loading Dataset...")

# Loop through each person's folder (00, 01, 02...)
for person in os.listdir(dataset_path):

    person_path = os.path.join(dataset_path, person)

    # Skip if it's not a folder
    if not os.path.isdir(person_path):
        continue

    # Loop through gesture folders
    for gesture in os.listdir(person_path):

        gesture_path = os.path.join(person_path, gesture)

        if not os.path.isdir(gesture_path):
            continue

        print("Reading:", gesture)

print("Dataset Read Successfully!")

import os
import cv2
import numpy as np

# Dataset path
dataset_path = "leapGestRecog"

# Lists to store images and labels
images = []
labels = []

print("Loading Dataset...")

# Loop through each person's folder
for person in os.listdir(dataset_path):

    person_path = os.path.join(dataset_path, person)

    if not os.path.isdir(person_path):
        continue

    # Loop through gesture folders
    for gesture in os.listdir(person_path):

        gesture_path = os.path.join(person_path, gesture)

        if not os.path.isdir(gesture_path):
            continue

        # Label is the first two digits of the folder name
        label = int(gesture.split("_")[0])

        # Read image files
        for image_name in os.listdir(gesture_path):

            image_path = os.path.join(gesture_path, image_name)

            # Read image
            image = cv2.imread(image_path)

            if image is None:
                continue

            # Convert to grayscale
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Resize image
            image = cv2.resize(image, (64, 64))

            # Flatten image into 1D array
            image = image.flatten()

            # Store image and label
            images.append(image)
            labels.append(label)

print("Dataset Loaded Successfully!")

print("Total Images :", len(images))
print("Total Labels :", len(labels))

# Convert lists into NumPy arrays
X = np.array(images)
y = np.array(labels)

print("\nPreparing Dataset...")

# Split dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training Images :", len(X_train))
print("Testing Images :", len(X_test))

# Create SVM model
model = SVC(kernel='linear')

print("\nTraining SVM Model...")

# Train the model
model.fit(X_train, y_train)

print("Model Trained Successfully!")

# Predict on test data
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", round(accuracy * 100, 2), "%")

# ------------------------------------------
# Classification Report
# ------------------------------------------

print("\nClassification Report\n")
print(classification_report(y_test, y_pred))

# ------------------------------------------
# Confusion Matrix
# ------------------------------------------

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix\n")
print(cm)

# ------------------------------------------
# Display Sample Predictions
# ------------------------------------------

plt.figure(figsize=(10,10))

for i in range(9):
    plt.subplot(3,3,i+1)
    image = X_test[i].reshape(64,64)
    plt.imshow(image, cmap="gray")
    plt.title("Predicted: " + str(y_pred[i]))
    plt.axis("off")

plt.tight_layout()
plt.show()


