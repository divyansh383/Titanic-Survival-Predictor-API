import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,classification_report,accuracy_score
from sklearn.linear_model import LogisticRegression


import pickle
import os

def pre_process(data):
    def get_title(name):
        if '.' in name:
            return name.split(',')[1].split('.')[0].strip()
        else:
            return 'Unknown'
        
    def title_map(title):
        if(title in ['Mr']):
            return 1
        elif(title in ['Master']):
            return 3
        elif(title in ['Ms','Malle','Miss']):
            return 4
        elif(title in ['Mme','Mrs']):
            return 5
        else:
            return 2
    
    data['title']=data['Name'].apply(get_title).apply(title_map)
    data=data.drop(['PassengerId','Name','Ticket'],axis=1)
    data["sex"]=data['Sex'].replace(['male','female'],[0,1])
    data['Cabin']=data['Cabin'].isna()
    data=pd.get_dummies(data)
    data['Age'][data['Age'].isna()]=data['Age'].mean()
    mf=data['Fare'].mean()
    data['Fare']=data["Fare"]>mf
    data['Fare']=data['Fare'].astype(int)
    return data

def training(df):
    #df=pd.read_csv('titanic.csv')
    df=pre_process(df)

    y=df['Survived']
    X=df.drop('Survived',axis='columns')

    dummyRow=pd.DataFrame(np.zeros(len(X.columns)).reshape(1,len(X.columns)),columns=X.columns)
    dummyRow.to_csv('dummyRow.csv',index=False)

    X_tr,X_ts,Y_tr,Y_ts=train_test_split(X,y)
    clf=LogisticRegression()
    clf.fit(X_tr,Y_tr)

    pkl_filename='ml_model.pkl'
    with open(pkl_filename,'wb') as file:
        pickle.dump(clf,file)

    print(clf.score(X_ts,Y_ts))
    Y_pred=clf.predict(X_ts)
    print('Survived',sum(Y_pred!=0))
    print('Not Survived',sum(Y_pred==0))
     
    print(confusion_matrix(Y_ts,Y_pred))
          
def pred(obj):
    d1=obj.to_dict()
    df=pd.DataFrame(d1,index=[0])
    df.drop('Survived',axis=1,inplace=True)
    df=pre_process(df)
    dummyRow_filename='./dummyRow.csv'
    dummyRow_filename=os.path.join(os.path.abspath(os.path.dirname(__file__)),dummyRow_filename)
    df2=pd.read_csv(dummyRow_filename)

    for c1 in df.columns:
        df2[c1]=df[c1]

    pkl_filename='./ml_model.pkl'
    pkl_filename=os.path.join(os.path.abspath(os.path.dirname(__file__)),pkl_filename)

    with open(pkl_filename,'rb') as file:
        model=pickle.load(file)
        pred=model.predict(df2)
        return pred

if __name__=="__main__":
    df=pd.read_csv("titanic.csv")
    training(df)
