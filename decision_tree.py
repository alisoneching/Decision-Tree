#-------------------------------------------------------------------------
# AUTHOR: Alison Ching
# FILENAME: decision_tree.py
# SPECIFICATION: read the file contact_lens.csv and output a decision tree
# FOR: CS 4210- Assignment #1
# TIME SPENT: 1 hour
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)

#transform the original categorical training features into numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
X = []
for row in db:
  array = []  # empty array to store numerical values of each row in db
  # change attribute 'age' values into numerical
  age = row[0]
  if age == 'Young':
    array.append(1)
  elif age == 'Presbyopic':
    array.append(2)
  elif age == 'Prepresbyopic':
    array.append(3)
  # change attribute 'spectacle prescription' values into numerical
  spectacle = row[1]
  if spectacle == 'Myope':
    array.append(1)
  elif spectacle == 'Hypermetrope':
    array.append(2)
  # change attribute 'astigmatism' values into numerical
  astigmatism = row[2]
  if astigmatism == 'Yes':
    array.append(1)
  elif astigmatism == 'No':
    array.append(2)
  # change attribute 'tear production rate' values into numerical
  tear = row[3]
  if tear == 'Normal':
    array.append(1)
  elif tear == 'Reduced':
    array.append(2)
  # add array of numerical values into X array
  X.append(array)

#transform the original categorical training classes into numbers and add to the vector Y. For instance Yes = 1, No = 2
Y = []
for row in db:
  recommended = row[-1]   # take last value of every row for 'recommended lenses'
  if recommended == 'Yes':
    Y.append(1)
  elif recommended == 'No':
     Y.append(2)

#fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X, Y)

#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()