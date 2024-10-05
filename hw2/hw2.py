import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from yellowbrick.cluster import KElbowVisualizer


X, y_true = make_blobs(n_samples=300, centers=4,
                       cluster_std=0.60, random_state=0)

model = KMeans()

visualizer = KElbowVisualizer(model, k=(1,12))
visualizer.fit(X)  # Fit the data to the visualizer
visualizer.show()       

#best k using KElbowVisualizer
best_k = visualizer.elbow_value_ 
print(f'Best k: {best_k}')

kmeans = KMeans(n_clusters=best_k, random_state=0)
y_pred = kmeans.fit_predict(X)

#will match predicted labels to true labels
labels = np.zeros_like(y_pred)
for i in range(best_k):
    mask = (y_pred == i)
    labels[mask] = np.bincount(y_true[mask]).argmax()

accuracy = accuracy_score(y_true, labels)
print(f'Accuracy: {accuracy:.2f}')


mat = confusion_matrix(y_true, labels)

plt.figure(figsize=(best_k, best_k))
sns.heatmap(mat, square=True, annot=True, fmt='d', cmap='GnBu', cbar=True,
            xticklabels=np.unique(y_true),
            yticklabels=np.unique(y_true))

plt.title('Confusion Matrix for best K')
plt.xlabel('True label')
plt.ylabel('predicted label')
plt.show()
