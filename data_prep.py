import pandas as pd
import pickle
import numpy as np



# Load imputer
selected_model = pickle.load(open('abc.pkl', 'rb'))
# Load scaler
std_scaler = pickle.load(open('scaler.pkl', 'rb'))


def prep_data(data):
    df = data

    #Fill all the emapty values with 0
    df = df.fillna(value=0)
    df.drop(columns=["Player", "Tm", "Pos", "Lg", "Year"], axis = 1, inplace=True)

    data = df.drop(columns = ['Classification'])
     


    return ""
