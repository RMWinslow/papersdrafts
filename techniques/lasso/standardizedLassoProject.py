#Need to compare time of Lasso vs 
#also a table of k fold for differetn folds.
#Wage earnings profile is quartic polynomial Murphy paper.
#Take lambda grid from log=-2 to -10
# adding occupation dummies makes male dummy dissapear?
#Where is self employed in the meta data?
#classwly contains self-employed data
#Should I add age square after I normalize age? I think so? No, wait, that will yield nonsense. Squareing negatives and all that.
# Normalization is default in LassoLarsCV but not LassoCV?!
# TODO: Clean it up so comparison runs automatically. Functions for running test and for getting most important variables
# TODO: Make pretty python output table for comparing runtimes
# https://stackoverflow.com/questions/8450472/how-to-print-a-string-at-a-fixed-width
# TODO: Make display of most important variables.


#%% Import some useful libraries- Don't really need all these. Will clean up later.
import pyreadstat
import numpy as np
import pandas as pd
import sklearn as sk
import sklearn.linear_model as skl
from sklearn.linear_model import LassoCV
from sklearn.model_selection import RepeatedKFold
import matplotlib.pyplot as plt
import time



#%% GLOBAL VARIABLES ARE ACTUALLY GOOD FOR THIS KIND OF APPLICATION
USE_LARS_CV = 0
USE_LASSO_CV = 1

alphaGrid = 10**(np.linspace(-10,-2,100))
#alphaGrid = None #sets to default

NUMBERCV = 5
















#%% Load the data.
df, meta = pyreadstat.read_dta('2012_asec_clean.dta')
print(df.head())
#labels in meta.column_names_to_labels
#dummy info found in meta.variable_value_labels
#what is the difference between that and meta.value_labels?

#%% deal with some missing entries in meta.variable_value_labels. (Not sure if this is correct)
meta.variable_value_labels['occ2010'][0] = "Missing data?"
meta.variable_value_labels['occ'] = meta.variable_value_labels['occ2010']
meta.variable_value_labels['occly'] = meta.variable_value_labels['occ2010']
meta.variable_value_labels['indly'] = meta.variable_value_labels['ind1990']

#%%Pull out the variables we're actually going to use.

#Independent variable : log(wageinc)
Y = np.log(df['wageinc'])

#Dependent variables: 
#    Numeric variables: age, age^2, (normalized)
#    Dummy variables: see attached file
dummies = ["educ_cat", "race_cat", "male", "hhtenure", "region", "metarea", "unitsstr", "nfams", "ncouples", "nmothers", "nfathers", "marst", "famsize", "ftype", "famkind", "yrimmig", "citizen", "nativity", "hispan", "occ", "ind", "educ", "lfproxy", "occly", "indly", "classwly", "pension_at_w_ly", "firmsize_ly", "actnlfly", "spmmort", "statefip", "state_ly", "whymove", "mig_stat_ly", "health", "vet1", "vet2", "csvisleg",  "paidhour",  "union",  "bpl",  "mbpl",  "fbpl",]
X = df[dummies]
#X['age2'] = np.square(df['age'])
X["age"] = df['age']#(df['age'] - df['age'].mean()) / df['age'].std()
X['age2'] = np.square(X['age'])
meta.column_names_to_labels['age2'] = 'age squared'


#%% Turn the dummy index variables into seperate dummy variables.
#https://chrisalbon.com/python/data_wrangling/pandas_convert_categorical_to_dummies/
X = pd.get_dummies(X,columns=dummies)














#%%Set up and fit model
start_time = time.time()



if USE_LARS_CV:
    model = skl.LassoLarsCV(normalize = True, cv = NUMBERCV)                        #LassoLarsCV or LassoCV
    model.fit(X,Y)
    predictions = model.predict(X)
    alpha = model.alpha_,

if USE_LASSO_CV:
    model = skl.LassoCV(normalize = True, cv = NUMBERCV, alphas = alphaGrid)                        #LassoLarsCV or LassoCV
    model.fit(X,Y)
    predictions = model.predict(X)
    alpha = model.alpha_,








end_time = time.time()
print("My program took", end_time - start_time, "to run")


#%% Show results
print("Time to run:", end_time - start_time, "to run")

print('\lambda: ', alpha, 'log10:', np.log10(alpha), 'ln:', np.log(alpha))
# The coefficients
print('Coefficients: \n', model.coef_)
# The mean squared error
print('Mean squared error: %.2f'
      % sk.metrics.mean_squared_error(Y, predictions))
# The coefficient of determination: 1 is perfect prediction
print('Coefficient of determination: %.2f'
      % sk.metrics.r2_score(Y, predictions))

for i in range(len(list(X))):
    description = ''
    if model.coef_[i] != 0:
        seperatorPosition = list(X)[i].rfind('_')
        if seperatorPosition != -1:
            dummyCategory = list(X)[i][:seperatorPosition]
            #print(list(X)[i])
            dummyNumber = int(float(list(X)[i][seperatorPosition+1:]))
            if dummyCategory in meta.variable_value_labels:
                if dummyNumber in meta.variable_value_labels[dummyCategory]:
                    description = meta.variable_value_labels[dummyCategory][dummyNumber]
        else:
            description = meta.column_names_to_labels[list(X)[i]]
        print(list(X)[i], '(', description,')',': %.3f'%model.coef_[i])


print('grid:',model.alphas_)


#%% Figure out most important variables

totalImportance = dict()
totalImportance['age'] = None #TODO












#%% 


#%%








