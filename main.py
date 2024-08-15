import pandas as pd
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.naive_bayes import MultinomialNB

from sklearn.pipeline import make_pipeline
from sklearn import metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
from Backend.preprocessing import getReceipt

def ml_model(receipt):

    # Load the dataset
    data = pd.read_csv('sample_dataset.csv')

    X = data['item']
    y = data['is_food']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create a pipeline that combines the TF-IDF vectorizer and a Naive Bayes classifier
    model = make_pipeline(CountVectorizer(),  RandomForestClassifier())

    # Train the model
    model.fit(X_train, y_train)

    # Predict the categories of the test data
    predicted_categories = model.predict(X_test)

    # Evaluate the model
    accuracy = metrics.accuracy_score(y_test, predicted_categories)
    print(f"Accuracy: {accuracy}")

    # Print a classification report
    print(metrics.classification_report(y_test, predicted_categories, target_names=['Not Food', 'Food']))


    #Printing the false negatives
    false_negatives = X_test[(y_test == False) & (predicted_categories == True)]
    print("False Negatives:")
    for item in false_negatives:
        print(item)

    print("\n")
    print(model.predict(["fdsdfssfd","Banana","Apple"]))

"""     validLines = []

    lines = receipt.split('\n')

   for line in lines:
        print(line + '\n')
        words = line.split()
        for word in words:
            print(word + ": " + model.predict([word]))
            if model.predict([word]) == 1:
                validLines.append(line)
                break

    print(validLines) """

"""     # Plot the confusion matrix
    conf_mat = metrics.confusion_matrix(y_test, predicted_categories)
    sns.heatmap(conf_mat, annot=True, fmt='d', cmap='Blues', xticklabels=['Not Food', 'Food'], yticklabels=['Not Food', 'Food'])
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.title('Confusion Matrix')
    plt.show() """

ml_model(getReceipt())