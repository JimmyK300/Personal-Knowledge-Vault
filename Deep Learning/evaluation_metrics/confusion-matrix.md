Confusion matrix
| |Pre|!Pre|
|Actual|TP|FN|
|!Actual|FP|TN|
chatgpt suggested confusion matrix is the right step because it lets us derive accuracy, precision, recall, and F1 score
accuracy is the overall correctness (TP+TN)/(TP+TN+FP+FN) = trace/total (overall); class wise separate it to TPa, FPa, FNa, TNa and so on 
precision is only when it say yes, how often can i trust it TP/(TP+FP) = 
Recall out of all positives, how many did the model find? (TP)/(TP+FN)
F1 is balance between precision and recall: 2PR/(P+R)
macro average: precision macro: sum(P(1->n)/n)

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

learning curves:
acc vs epochs
loss vs epochs
for training and testing
to measure overfitting, underfitting, or still learning
| Pattern        | Meaning      |
| -------------- | ------------ |
| train ↑ test ↑ | learning     |
| train ↑ test ↓ | overfitting  |
| both flat      | underfitting |

generalization gap = train acc - test acc
small gap: good generalization, large gap, overfitting

per class accuracy for classification

error analysis: show the examples where the model got wrong

writer bias: to show if model favors certain styles