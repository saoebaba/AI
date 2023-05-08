import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import warnings
warnings.filterwarnings('ignore')
%matplotlib inline

# Importing the csv file
data = pd.read_excel('Employee Performance Analysis Dataset.xls')

data.shape

data.columns

data.head()

data.info()

dept = data.iloc[:,[5,27]].copy()
dept_per = dept.copy()

dept_per.groupby(by='EmpDepartment')['PerformanceRating'].mean()

plt.figure(figsize=(10,4.5))
sns.barplot(dept_per['EmpDepartment'],dept_per['PerformanceRating'])

dept_per.groupby(by='EmpDepartment')['PerformanceRating'].value_counts()

department = pd.get_dummies(dept_per['EmpDepartment'])
performance = pd.DataFrame(dept_per['PerformanceRating'])
dept_rating = pd.concat([department,performance],axis=1)

plt.figure(figsize=(15,10))
plt.subplot(2,3,1)
sns.barplot(dept_rating['PerformanceRating'],dept_rating['Sales'])
plt.subplot(2,3,2)
sns.barplot(dept_rating['PerformanceRating'],dept_rating['Development'])
plt.subplot(2,3,3)
sns.barplot(dept_rating['PerformanceRating'],dept_rating['Research & Development'])
plt.subplot(2,3,4)
sns.barplot(dept_rating['PerformanceRating'],dept_rating['Human Resources'])
plt.subplot(2,3,5)
sns.barplot(dept_rating['PerformanceRating'],dept_rating['Finance'])
plt.subplot(2,3,6)
sns.barplot(dept_rating['PerformanceRating'],dept_rating['Data Science'])
plt.show()

enc = LabelEncoder()
for i in (2,3,4,5,6,7,16,26):
 data.iloc[:,i] = enc.fit_transform(data.iloc[:,i])
data.head()

data.corr()

data.drop(['EmpNumber'],inplace=True,axis=1)

data.head()


y = data.PerformanceRating

X = data.iloc[:,[4,5,9,16,20,21,22,23,24]] # Taking only variables with correlation coef
X.head()

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=10)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

X_train.shape

X_test.shape

from sklearn.ensemble import RandomForestClassifier
classifier_rfg=RandomForestClassifier(random_state=33,n_estimators=23)
parameters=[{'min_samples_split':[2,3,4,5],'criterion':['gini','entropy'],'min_samples_l
model_gridrf=GridSearchCV(estimator=classifier_rfg, param_grid=parameters, scoring='accu
model_gridrf.fit(X_train,y_train)
                          
model_gridrf.best_params_
                          
y_predict_rf = model_gridrf.predict(X_test)
                         
print(accuracy_score(y_test,y_predict_rf))
print(classification_report(y_test,y_predict_rf))
                          
confusion_matrix(y_test,y_predict_rf)


