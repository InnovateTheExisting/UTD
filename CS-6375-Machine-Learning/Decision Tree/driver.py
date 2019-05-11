from DecisionTree import *
import pandas as pd
from sklearn import model_selection

header = ['SepalL', 'SepalW', 'PetalL', 'PetalW', 'Class']
df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None, names=['SepalL','SepalW','PetalL','PetalW','Class'])
#df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data', header=None, names=['buying','paint','doors','persons','lug_boot',"safety"])
lst = df.values.tolist()
t = build_tree(lst, header)
print_tree(t)

print("********** Leaf nodes ****************")
leaves = getLeafNodes(t)
for leaf in leaves:
    print("id = " + str(leaf.id) + " depth =" + str(leaf.depth))
print("********** Non-leaf nodes ****************")
innerNodes = getInnerNodes(t)
for inner in innerNodes:
    print("id = " + str(inner.id) + " depth =" + str(inner.depth))

trainDF, testDF = model_selection.train_test_split(df, test_size=0.2)
train = trainDF.values.tolist()
test = testDF.values.tolist()

t = build_tree(train, header)
print("*************Tree before pruning*******")
#print_tree(t)
acc = computeAccuracy(test, t)
print("Accuracy on test = " + str(acc))
## TODO: You have to decide on a pruning strategy
t_pruned = prune_tree(t, [26, 11, 5])
#leaf
#t_pruned = prune_tree(t, [5,26,12,13,0,6])
#random
#t_pruned = prune_tree(t, [26, 11, 5,4,6,13])
# Remove false node of root
#t_pruned = prune_tree(t, [1])
#Remove All False leaf nodes
#t_pruned = prune_tree(t, [1, 11,25,53,27])
#Car_dataset
#t_pruned=prune_tree(t,[5,8,24,30])

print("*************Tree after pruning*******")
print_tree(t_pruned)
acc = computeAccuracy(test, t)
print("Accuracy on test = " + str(acc))
