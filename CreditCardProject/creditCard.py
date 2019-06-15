import pandas as pd # import pandas to read file
import numpy as np # import numpy for some math
from sklearn import tree # import sklearn.tree for use of decision trees
from sklearn.model_selection import cross_val_score
d = pd.read_csv('creditCard.csv') # import dataset
d = d.drop(['RowNumber','CustomerId','Surname'], axis = 1) # drop irrelevant values
#print(d.head()) # debugging
d = pd.get_dummies(d, columns =['Geography','Gender'])
#print(d.head()) # debugging
'''
d_test = d[9000:] # last 1000 for testing
d_test_att = d_test.drop(['Exited'],axis=1) # features for testing set
d_test_exited = d_test['Exited'] # predicted values for testing set
d_att = d.drop(['Exited'],axis =1 ) # features for entire set
d_exited = d['Exited'] # predicted values for entire set
d = d.sample(frac=1) # shuffle rows
d_train = d[:9000] # first 9000 for training
d_train_att = d_train.drop(['Exited'],axis=1) # features for training set
d_train_exited = d_train['Exited'] # predicted values for training set
'''
d_test = d[9000:] # last 1000 for testing
d_test_att = d_test.drop(['Exited'],axis=1) # features for testing set
d_test_exited = d_test['Exited'] # predicted values for testing set
d_att = d.drop(['Exited'],axis =1 ) # features for entire set
d_exited = d['Exited'] # predicted values for entire set
d = d.sample(frac=1) # shuffle rows
d_train = d[:9000] # first 9000 for training
d_train_att = d_train.drop(['Exited'],axis=1) # features for training set
d_train_exited = d_train['Exited'] # predicted values for training set
# below finds percent exited for ref
#print('Percent Exited: %d out of %d (%.2f%%)' % (np.sum(d_exited),len(d_exited),100*float(np.sum(d_exited))/len(d_exited))) 
for max_depth in range(20,31): # checks to see what is the best max depth from 1 to 24
	# Accuracy keeps getting better until a depth ~ 20, then plateaus
	t = tree.DecisionTreeClassifier(criterion="entropy", max_depth=max_depth) # set up tree
	t = t.fit(d_train_att, d_train_exited) # train model with training set
	print('Accuracy:',t.score(d_test_att,d_test_exited),'depth:',max_depth) # determine accuracy of model using testing set
#print(d.head()) # debugging
#CreditScore,Age,Tenure,Balance,NumOfProducts,HasCrCard,IsActiveMember,
#EstimatedSalary,Geography_France,Geography_Germany,Geography_Spain,
#Gender_Female,Gender_Male
#tree.export_graphviz(t,out_file="treeVisualize.dot",label="all",impurity=False,proportion=True,feature_names=list(d_train_att), class_names=["Exited","Not Exited"],filled=True,rounded=True) # export tree to .dot file
predictValue = t.predict([[619,42,2,0,1,1,1,101348.9,1,0,0,1,0]]) # predict value based on features
print(predictValue) # print predicted value

depth_acc = np.empty((30,3),float)
i = 0
for max_depth in range(1,31):
	t=tree.DecisionTreeClassifier(criterion="entropy",max_depth=max_depth)
	scores = cross_val_score(t,d_att,d_exited,cv=5)
	print("Max depth: %d, Accuracy: %0.2f (+/- %0.2f)" % (max_depth,scores.mean(),scores.std() *2))
	depth_acc[i,0]=max_depth
	depth_acc[i,1] = scores.mean()
	depth_acc[i,2] = scores.std() * 2
	i+=1
#print(depth_acc)
import matplotlib.pyplot as plt
fig,ax = plt.subplots()
ax.errorbar(depth_acc[:,0],depth_acc[:,1], yerr=depth_acc[:,2])
plt.show()
'''
import pandas as pd # import pandas to read file
import numpy as np # import numpy for some quick maths
from sklearn import tree # import sklearn.tree for use of decision trees
from sklearn.model_selection import cross_val_score
d = pd.read_csv('creditCardFile.csv') # import dataset
d = d.drop(['ID'], axis = 1) # drop irrelevant values

d_train = d[:27000] # first 9000 for training
d_train_att = d_train.drop(['default payment next month'],axis=1) # features for training set
d_train_exited = d_train['default payment next month'] # predicted values for training set
d_test = d[27000:] # last 1000 for testing
d_test_att = d_test.drop(['default payment next month'],axis=1) # features for testing set
d_test_exited = d_test['default payment next month'] # predicted values for testing set
d_att = d.drop(['default payment next month'],axis =1 ) # features for entire set
d_exited = d['default payment next month'] # predicted values for entire set
d = d.sample(frac=1) # shuffle rows
# below finds percent exited for ref
print('Percent Exited: %d out of %d (%.2f%%)' % (np.sum(d_exited),len(d_exited),100*float(np.sum(d_exited))/len(d_exited))) 
for max_depth in range(3,4): # checks to see what is the best max depth from 1 to 24
	# Accuracy keeps getting better until a depth ~ 20, then plateaus
	t = tree.DecisionTreeClassifier(criterion="entropy", max_depth=max_depth) # set up tree
	t = t.fit(d_train_att, d_train_exited) # train model with training set
	print('Accuracy:',t.score(d_test_att,d_test_exited),'depth:',max_depth) # determine accuracy of model using testing set
#print(d.head()) # debugging
#tree.export_graphviz(t,out_file="treeVisualize.dot",label="all",impurity=False,proportion=True,feature_names=list(d_train_att), class_names=["Exited","Not Exited"],filled=True,rounded=True) # export tree to .dot file
predictValue = t.predict([[20000,2,2,1,24,2,2,-1,-1,-2,-2,3913,3102,689,0,0,0,0,689,0,0,0,0]]) # predict value based on features
print(predictValue) # print predicted value
depth_acc = np.empty((19,3),float)
i = 0
for max_depth in range(1,20):
	t=tree.DecisionTreeClassifier(criterion="entropy",max_depth=max_depth)
	scores = cross_val_score(t,d_att,d_exited,cv=5)
	#print("Max depth: %d, Accuracy: %0.2f (+/- %0.2f)" % (max_depth,scores.mean(),scores.std() *2))
	depth_acc[i,0]=max_depth
	depth_acc[i,1] = scores.mean()
	depth_acc[i,2] = scores.std() * 2
	i+=1
print(depth_acc)
import matplotlib.pyplot as plt
fig,ax = plt.subplots()
ax.errorbar(depth_acc[:,0],depth_acc[:,1], yerr=depth_acc[:,2])
plt.show()'''
