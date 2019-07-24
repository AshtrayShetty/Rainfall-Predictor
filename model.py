import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
import os
    
list_files=os.listdir(".\\datasets")

total=0

with open('results.txt','w') as res:

    for file in list_files:
        dataset=pd.read_csv(f'.\\datasets\\{file}')

        wind_speed_difference=dataset['WindSpeed3pm']-dataset['WindSpeed9am']
        temperature_difference=dataset['Temp3pm']-dataset['Temp9am']
        humidity_difference=dataset['Humidity9am']-dataset['Humidity3pm']

        X=np.array([wind_speed_difference,temperature_difference,humidity_difference,dataset['RISK_MM']])
        y=np.array(dataset['RainTomorrow'])

        X=X.transpose()

        from sklearn.preprocessing import Imputer, LabelEncoder, StandardScaler

        imputer=Imputer(missing_values=np.nan,strategy='mean',axis=0)
        imputer=imputer.fit(X[:,:])
        X[:,:]=imputer.transform(X[:,:])

        labelencoder_y=LabelEncoder()
        y=labelencoder_y.fit_transform(y)

        X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)

        scaler=StandardScaler()
        X_train=scaler.fit_transform(X_train)
        X_test=scaler.transform(X_test)

        from sklearn.linear_model import LogisticRegression
        logreg=LogisticRegression()
        logreg.fit(X_train,y_train)
        
        file=file[:len(file)-4]
        score=logreg.score(X_test,y_test)
        total+=score
        res.write(f"{file}:{score}\n")

    average_accuracy=total/49
    res.write(f"Average Accuracy:{average_accuracy}")

    
    





