from sklearn import datasets, metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split


irisdataset = datasets.load_iris()     # Loading the iris dataset
x = irisdataset.data                   # Reading the data
y = irisdataset.target                 # reading the target

# split the data for training and testing using model_selection
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

gnb = GaussianNB()                     # Defining Gaussian Naive Bayes model
y_pred = gnb.fit(x_train, y_train).predict(x_test)         # Fitting the model and predicting for y_test
print(metrics.accuracy_score(y_test, y_pred))              #Calculating the accuracy
