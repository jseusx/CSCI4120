import pandas as pd
import numpy as np
import random
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

def loadDataset(filename, split):
    df = pd.read_csv(filename, header=None)
    
    array = df.to_numpy()
    random.shuffle(array)
 
    # gets everything before the last colomn
    x = array[:, :-1]
    # gets the last colomn
    y = array[:, -1]
    
    # Split the dataset
    # x_train, x_test, y_train, y_test
    return train_test_split(x, y, test_size=1-split, random_state=42)
    
    
def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x] == predictions[x]:
            correct += 1
    return (correct/float(len(testSet))) * 100.0
    
def main():
    # prepare data
    split = 0.67
    url = 'https://raw.githubusercontent.com/ruiwu1990/CSCI_4120/master/KNN/iris.data'
    
    k_values = range(1, 21)
    num_repeats = 5

    # List with accuracies depending on k
    average_accuracies = []
    
    for k in k_values:
        # place holder for 5 values to average
        accuracies = []
        for _ in range(num_repeats): 
            trainingX, testX, trainingY, testY = loadDataset(url, split)	
            
            # trains the model
            neigh = KNeighborsClassifier(n_neighbors=k)
            neigh.fit(trainingX, trainingY)
    
            # predicts and gets accuracy per k
            predictions = neigh.predict(testX)
            accuracy = accuracy_score(testY, predictions)
            # puts the accuracy into a list for that k
            accuracies.append(accuracy)
   
        #finds current average ccuracy for k then appends it to overall list
        avg_accuracy = np.mean(accuracies)
        average_accuracies.append(avg_accuracy)

        print(f'k={k} Average Accuracy: {avg_accuracy:.2f}%')
    
    
    # chart setup
    plt.figure(figsize=(10, 6))
    plt.style.use('seaborn-whitegrid')
    plt.title('K values vs Average Accuracy')
    plt.xlabel('K values')
    plt.ylabel('Average Accuracy per K')
    plt.xticks(k_values)
    plt.grid(True)

    plt.plot(k_values, average_accuracies, marker='o')

    plt.show()

    
main()
