import pickle
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load the extracted features and labels from a pickle file.
data_dict = pickle.load(open('./extracted_features_labels.pickle', 'rb'))

# Convert the data and labels to numpy arrays for easier manipulation.
data = np.asarray(data_dict['data'])
labels = np.asarray(data_dict['labels'])

# Split the data into training and testing sets with 80% for training and 20% for testing.
x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, stratify=labels)

# Initialize the RandomForestClassifier model.
model = RandomForestClassifier()

# Train the model using the training data.
model.fit(x_train, y_train)

# Make predictions on the testing data.
y_predict = model.predict(x_test)

# Calculate the accuracy of the model's predictions.
score = accuracy_score(y_predict, y_test)

# Print the accuracy score in percentage format.
print('{}% of samples were classified correctly!'.format(score * 100))

# Generate a confusion matrix to evaluate the performance of the classification.
cm = confusion_matrix(y_test, y_predict)

# Print the confusion matrix.
print("\nConfusion Matrix: \n", cm)

# Print a detailed classification report with precision, recall, and f1-score.
print("\nClassification Report:\n", classification_report(y_test, y_predict))

# Calculate the number of true positives, false positives, false negatives, and true negatives.
true_positives = np.diag(cm).sum()  # Sum of diagonal elements (correctly predicted cases).
false_positives = cm.sum(axis=0) - np.diag(cm)  # Sum of false positives for each class.
false_negatives = cm.sum(axis=1) - np.diag(cm)  # Sum of false negatives for each class.
true_negatives = cm.sum() - (false_positives + false_negatives + true_positives)  # Remaining cells.

# Print the count of true positives, true negatives, false positives, and false negatives.
print(f"\nTrue Positives: {true_positives}")
print(f"True Negatives: {true_negatives}")
print(f"False Positives: {false_positives.sum()}")
print(f"False Negatives: {false_negatives.sum()}")

# Plot the confusion matrix using Matplotlib.
plt.figure(figsize=(8, 6))
plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)  # Display the confusion matrix as an image.
plt.title('Confusion Matrix')
plt.colorbar()  # Add a color bar to the plot.
tick_marks = np.arange(len(np.unique(labels)))  # Define tick marks for each unique label.
plt.xticks(tick_marks, np.unique(labels), rotation=45)  # Set x-axis ticks and rotate labels.
plt.yticks(tick_marks, np.unique(labels))  # Set y-axis ticks.

# Add text annotations to the confusion matrix cells.
thresh = cm.max() / 2  # Define a threshold for text color based on the max value in the matrix.
for i, j in np.ndindex(cm.shape):
    plt.text(j, i, cm[i, j], horizontalalignment="center", color="white" if cm[i, j] > thresh else "black")

plt.ylabel('True label')  # Label for y-axis.
plt.xlabel('Predicted label')  # Label for x-axis.
plt.tight_layout()  # Adjust layout for a cleaner look.
plt.show()  # Display the confusion matrix plot.

# Save the trained RandomForest model to a pickle file for later use.
f = open('random_forest.p', 'wb')
pickle.dump({'model': model}, f)
f.close()
