#Need to compare time of Lasso vs 
#also a table of k fold for differetn folds.

#%% Import some useful libraries
import pyreadstat
import numpy as np
import pandas as pd
import sklearn as sk
import sklearn.linear_model as skl
from sklearn.linear_model import LassoCV
from sklearn.model_selection import RepeatedKFold
import matplotlib.pyplot as plt

#from https://www.nrcs.usda.gov/wps/portal/nrcs/detail/?cid=nrcs143_013696
#Manually added DC
FIPSmap = {1: 'Alabama',2: 'Alaska',4: 'Arizona',5: 'Arkansas',6: 'California',8: 'Colorado',9: 'Connecticut',10: 'Delaware',12: 'Florida',13: 'Georgia',15: 'Hawaii',16: 'Idaho',17: 'Illinois',18: 'Indiana',19: 'Iowa',20: 'Kansas',21: 'Kentucky',22: 'Louisiana',23: 'Maine',24: 'Maryland',25: 'Massachusetts',26: 'Michigan',27: 'Minnesota',28: 'Mississippi',29: 'Missouri',30: 'Montana',31: 'Nebraska',32: 'Nevada',33: 'New Hampshire',34: 'New Jersey',35: 'New Mexico',36: 'New York',37: 'North Carolina',38: 'North Dakota',39: 'Ohio',40: 'Oklahoma',41: 'Oregon',42: 'Pennsylvania',44: 'Rhode Island',45: 'South Carolina',46: 'South Dakota',47: 'Tennessee',48: 'Texas',49: 'Utah',50: 'Vermont',51: 'Virginia',53: 'Washington',54: 'West Virginia',55: 'Wisconsin',56: 'Wyoming',60: 'American Samoa',66: 'Guam',69: 'Northern Mariana Islands',72: 'Puerto Rico',78: 'Virgin Islands', 11:'DC'}



#%% Load the data.
df, meta = pyreadstat.read_dta('2012_CPS_training_sample.dta')
#df, meta = pyreadstat.read_dta('2012_asec_clean.dta')
#print(meta.column_names_to_labels)
print(df.head())
def whatis(varname):
    return meta.column_names_to_labels[varname]







#%%Tweak the data a bit and setup predictors
#https://chrisalbon.com/python/data_wrangling/pandas_convert_categorical_to_dummies/

#seperate race categories and education categories in dummy vars
df = pd.get_dummies(df,columns=['race_cat','educ_cat','statefip'])

Y = np.log(df['wageinc'])


#Y = np.log(df["wageinc"]).values.reshape(-1,1)
#X = df[['age','educ_cat','male','race_cat','experience',]]


#TODO Normalize regressors. Zero mean. SD of one.
# sklearn scaler strips column titles?
#https://www.geeksforgeeks.org/data-normalization-with-pandas/
df_z_scaled = df.copy() 
for column in df_z_scaled.columns: 
    df_z_scaled[column] = (df_z_scaled[column] - df_z_scaled[column].mean()) / df_z_scaled[column].std()     




X = df_z_scaled.drop(['serial','wtsupp','wageinc','educ_cat_1.0',],axis=1)






#TODO age*education





#%%Set up and fit model

'''
The basic Mincer earnings function is 
ln(earnings) = f(education,age)
Description from egor pdf says
ln(earnings)=f(age,education,age*education,gender,state,race)
'''
#cv = RepeatedKFold(n_splits=10, n_repeats=3, random_state=1)
#model = LassoCV(alphas=np.arange(0.1, 1, 0.01), cv=10, n_jobs=-1)
model = LassoCV()
model.fit(X,Y)

# Make predictions using the testing set
predictions = model.predict(X)






#%% Show results
print('\lambda: ', model.alpha_, np.log10(model.alpha_))

# %% evaluate the model




# The coefficients
#print('Coefficients: \n', model.coef_)
# The mean squared error
print('Mean squared error: %.2f'
      % sk.metrics.mean_squared_error(Y, predictions))
# The coefficient of determination: 1 is perfect prediction
print('Coefficient of determination: %.2f'
      % sk.metrics.r2_score(Y, predictions))

for i in range(len(list(X))):
    if model.coef_[i] != 0:
        statename = ''
        if list(X)[i].startswith('state'):
            statename = FIPSmap[int(list(X)[i][-2:].strip('_'))]
        print(list(X)[i],': %.3f'%model.coef_[i], statename)






#%% graphs of path

print("Computing regularization path using the lasso...")
alphas_lasso, coefs_lasso, _ = skl.lasso_path(X, Y, eps=0.0000001 )

plt.figure(1)
#colors = cycle(['b', 'r', 'g', 'c', 'k'])
neg_log_alphas_lasso = np.log10(alphas_lasso)
for coef in coefs_lasso:
    l1 = plt.plot(neg_log_alphas_lasso, coef)

plt.xlabel('Log(alpha)')
plt.ylabel('coefficients')
plt.title('Lasso Path')


plt.legend(list(X))
plt.axis('tight')
#plt.axis([-5, 2, -1, 2])
plt.show()

# %%
