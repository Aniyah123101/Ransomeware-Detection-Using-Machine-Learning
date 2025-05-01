'''
    File name: mlrd_learn.py
    Author: Callum Lock
    Date created: 31/03/2018
    Date last modified: 31/03/2018
    Python Version: 3.6
'''
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import joblib

# Initialize lists to track accuracy and loss over different random forest configurations
train_accuracies = []
val_accuracies = []
train_losses = []
val_losses = []

# Different Random Forest configurations (varying number of trees in the forest)
forest_configs = [10, 50, 100, 200, 300]  # These will be on the x-axis (Random Forest configurations)

def plot_confusion_matrix(cm, config):
    ''' Function to plot the confusion matrix using Matplotlib '''
    plt.figure(figsize=(6, 4))
    plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
    plt.title(f'Confusion Matrix (n_estimators={config})')
    plt.colorbar()
    tick_marks = np.arange(2)
    plt.xticks(tick_marks, ['Benign', 'Ransomware'], rotation=45)
    plt.yticks(tick_marks, ['Benign', 'Ransomware'])

    # Print the values inside the confusion matrix
    thresh = cm.max() / 2
    for i, j in np.ndindex(cm.shape):
        plt.text(j, i, f"{cm[i, j]}", horizontalalignment="center", color="white" if cm[i, j] > thresh else "black")

    plt.ylabel('Actual')
    plt.xlabel('Predicted')
    plt.tight_layout()
    plt.show()

def main():
    global train_accuracies, val_accuracies, train_losses, val_losses

    print('\n[+] Training Ransomware Detector using Random Forest Algorithm with different configurations...')

    # Load the ransomware dataset
    df = pd.read_csv('data_file.csv', sep=',')  # Replace 'data_file.csv' with your ransomware dataset

    # Drops FileName, md5Hash and Label (Benign) from the dataset
    X = df.drop(['FileName', 'md5Hash', 'Benign'], axis=1).values
    y = df['Benign'].values  # Assuming 'Benign' is the target column where 1 = benign and 0 = ransomware

    # Splitting data into training and test data
    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2, random_state=42)

    # Print the number of training and testing samples.
    print("\n\t[*] Training samples: ", len(X_train))
    print("\n\t[*] Testing samples: ", len(X_test))

    # Iterate over different Random Forest configurations (varying n_estimators)
    for config in forest_configs:
        # Initialize Random Forest classifier with current configuration
        clf = RandomForestClassifier(n_estimators=config, random_state=42)

        # Train the model
        clf.fit(X_train, y_train)

        # Predictions for training and test data
        y_train_pred = clf.predict(X_train)
        y_test_pred = clf.predict(X_test)

        # Calculate accuracy for training and test data
        train_accuracy = accuracy_score(y_train, y_train_pred)
        val_accuracy = accuracy_score(y_test, y_test_pred)

        # Calculate loss (as 1 - accuracy)
        train_loss = 1 - train_accuracy
        val_loss = 1 - val_accuracy

        # Append accuracy and loss to the lists
        train_accuracies.append(train_accuracy)
        val_accuracies.append(val_accuracy)
        train_losses.append(train_loss)
        val_losses.append(val_loss)

        # Print the current configuration's accuracy and loss
        print(f"Random Forest (n_estimators={config}) - Train Accuracy: {train_accuracy:.4f}, Validation Accuracy: {val_accuracy:.4f}")
        print(f"                          - Train Loss: {train_loss:.4f}, Validation Loss: {val_loss:.4f}")

        # Generate and print the confusion matrix
        cm = confusion_matrix(y_test, y_test_pred)
        print(f"Confusion Matrix for Random Forest (n_estimators={config}):\n{cm}")

        # Plot the confusion matrix using Matplotlib
        plot_confusion_matrix(cm, config)

    # Plotting accuracy and loss for different Random Forest configurations
    plt.figure(figsize=(14, 6))

    # Plot Accuracy
    plt.subplot(1, 2, 1)
    plt.plot(forest_configs, train_accuracies, label='Training Accuracy', marker='o')
    plt.plot(forest_configs, val_accuracies, label='Validation Accuracy', marker='o')
    plt.title('Ransomware Detection - Accuracy by Random Forest Configuration')
    plt.xlabel('Random Forest (Number of Trees)')
    plt.ylabel('Accuracy')
    plt.legend()

    # Plot Loss
    plt.subplot(1, 2, 2)
    plt.plot(forest_configs, train_losses, label='Training Loss', marker='o', color='blue')
    plt.plot(forest_configs, val_losses, label='Validation Loss', marker='o', color='orange')
    plt.title('Ransomware Detection - Loss by Random Forest Configuration')
    plt.xlabel('Random Forest (Number of Trees)')
    plt.ylabel('Loss')
    plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
