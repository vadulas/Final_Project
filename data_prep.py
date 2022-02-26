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
     = train_df['Classification']
   

    df_selected_model = pd.DataFrame(selected_model.transform()
    df_scaler = pd.DataFrame(std_scaler.transform(df_imputed), columns=df_imputed.columns)

    # 3 create dummies

    dumb5 = pd.get_dummies(df['x5'], drop_first=False, prefix='x5', prefix_sep='_', dummy_na=True)
    df_imputed_std = pd.concat([df_imputed_std, dumb5], axis=1, sort=False)

    dumb31 = pd.get_dummies(df['x31'], drop_first=False, prefix='x31', prefix_sep='_', dummy_na=True)
    df_imputed_std = pd.concat([df_imputed_std, dumb31], axis=1, sort=False)

    dumb81 = pd.get_dummies(df['x81'], drop_first=False, prefix='x81', prefix_sep='_', dummy_na=True)
    df_imputed_std = pd.concat([df_imputed_std, dumb81], axis=1, sort=False)

    dumb82 = pd.get_dummies(df['x82'], drop_first=False, prefix='x82', prefix_sep='_', dummy_na=True)
    df_imputed_std = pd.concat([df_imputed_std, dumb82], axis=1, sort=False)


    del dumb5, dumb31, dumb81, dumb82

    variables = ['x5_saturday', 'x81_July', 'x81_December', 'x31_japan',
                 'x81_October', 'x5_sunday', 'x31_asia', 'x81_February',
                 'x91', 'x81_May', 'x5_monday', 'x81_September', 'x81_March',
                 'x53', 'x81_November', 'x44', 'x81_June', 'x12', 'x5_tuesday',
                 'x81_August', 'x81_January', 'x62', 'x31_germany', 'x58', 'x56']

    # Accounting for missing dummy variables
    for var in variables:
        if var not in df_imputed_std.columns:
            df_imputed_std[var] = 0

    return df_imputed_std[variables]
© 2022 GitHub, Inc.
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
