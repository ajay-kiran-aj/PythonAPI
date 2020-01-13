from flask_restful import Resource
#import constant as con
import numpy as np
from sklearn import preprocessing 
import pickle
from sklearn.svm import SVC 






class PythonAPI(Resource):

  


  def get(self, val):

    Income=[{"result" :'<=50K'}, {"result":'>50K'}]


    with open("/app/resources/scaler.pkl", 'rb') as file1:
    #scaler_pkl = pickle.load(file1)
      SCALER_PKL = pickle.load(file1)

    with open("/app/resources/adultincome.pkl", 'rb') as file2:
    #svc_pkl = pickle.load(file2)
      SVC_PKL = pickle.load(file2)

    values = val.split("_")

    #reshape values
    valarray=np.asarray(values[:10])
    valarray=valarray.reshape(10,1).T

    #scale values
    scaled_values=SCALER_PKL.transform(valarray)
    #predict output
    output=SVC_PKL.predict(scaled_values)

    #convert output into categorical variable
    incomerange=Income[output[0]]

    #return output
    return(incomerange) , 200

  def put(self, val):
    values = val.split("_")

    #reshape values
    valarray=np.asarray(values[:10])
    valarray=valarray.reshape(10,1).T

    #scale values
    scaled_values=SCALER_PKL.transform(valarray)
    #predict output
    output=SVC_PKL.predict(scaled_values)

    #convert output into categorical variable
    incomerange=Income[output[0]]

    #return output
    return(incomerange) , 200
    