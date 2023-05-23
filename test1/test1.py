import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

def spam_detector(train_df, valid_df, test_df):

    # Tf-idf text vectorization
    vectorizer = TfidfVectorizer(min_df=2, ngram_range=(1, 2))
    X_train = vectorizer.fit_transform(train_df['text'])
    X_valid = vectorizer.transform(valid_df['text'])
    X_test = vectorizer.transform(test_df['text'])

    # Train classifiers
    classifiers = {
        'LogisticRegression': LogisticRegression(random_state=0),
        'MultinomialNB': MultinomialNB(),
        'DecisionTreeClassifier': DecisionTreeClassifier(random_state=0),
        'LinearSVC': LinearSVC()
    }

    # Build confusion matrices and accuracies
    confusion_matrices = {}
    accuracies = {}
    y_train = train_df['label']
    y_valid = valid_df['label']
    y_test = test_df['label']
    for name, clf in classifiers.items():
        clf.fit(X_train, y_train)
        y_pred= clf.predict(X_valid)
        confusion_matrices[name] = confusion_matrix(y_valid, y_pred)
        accuracies[name] = accuracy_score(y_valid, y_pred)

    # Find the best classifier and the predictions
    best_classifier = max(classifiers.keys(), key=lambda name: accuracies[name])
    best_classifier_y_pred = classifiers[best_classifier].predict(X_test)

    # Return the results
    results = {
        "LogisticRegression": confusion_matrices['LogisticRegression'],
        "MultinomialNB": confusion_matrices['MultinomialNB'],
        "DecisionTreeClassifier": confusion_matrices['DecisionTreeClassifier'],
        "LinearSVC": confusion_matrices['LinearSVC'],
        "BestClassifier": best_classifier,
        "TfidfVectorizer": X_test,
        "Prediction": best_classifier_y_pred,
    }
    return results

train_df, valid_df, test_df = [pd.read_csv('test1/data/{}.csv'.format(t)) for t in ['train', 'valid', 'test']]
results = spam_detector(train_df, valid_df, test_df)
print('Best classifier: {}'.format(results['BestClassifier']))
print('Confusion matrix for Logistic Regression:\n{}'.format(results['LogisticRegression']))
print('Confusion matrix for Multinomial Naive Bayes:\n{}'.format(results['MultinomialNB']))
print('Confusion matrix for Decision Tree Classifier:\n{}'.format(results['DecisionTreeClassifier']))
print('Confusion matrix for Linear Support Vector Classifier:\n{}'.format(results['LinearSVC']))
print('TfidfVectorizer:\n{}'.format(results['TfidfVectorizer']))
print('Prediction:\n{}'.format(results['Prediction']))
