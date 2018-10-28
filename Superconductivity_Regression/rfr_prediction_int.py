
# coding: utf-8

# The code in this notebook holds the codified version of calculating the prediction intervals for predictions made using a Random Forest Regression model. The measures used for the determination of such intervals are the Mean Squared Prediction Error 1 and 2 (MSPE1/MSPE2). These measures were developed by Benjamin Lu, with advisement from Dr. Jo Hardin, of Pomona College as part of his Senior Thesis in Mathematics. The entire reserach paper can be found [here](http://pages.pomona.edu/~jsh04747/Student%20Theses/BenjiLu17.pdf).
# 
# Note, only the MSPE1 is codified.

# In[ ]:


# Required packages

'''
sklearn.ensemble.RandomForestRegressor
'''


# In[ ]:


# Other requirements

'''
- The RFR must be fit with the 'oob_score' = True
'''


# Mean Squared Prediciton Error 1 (MSPE1)

# ![name](img/mspe1.png)

# In[ ]:


def mspe_one(train_sample, train_labels, rfr):
    
    # This function serves to calculate the mean squared prediction error of a Random Forest Regression (RFR) model.
    # This measure is nonspecific to the independent values.
    
    # train_sample = sample used to train the RFR
    # train_labels = true dependent values of train samples
    # rfr = trained RFR model
    
    n = train_sample.shape[0] # setting the sample size
    oob_preds = rfr.oob_prediction_ # an array of the predictions for each point in the train sample using out-of-bag trees
    
    oob_diff = oob_preds - train_labels # calculate the difference between each oob prediction and true value
    
    mspe = (sum((oob_diff)**2))/n # calculate the MSPE using the oob true-prediction differences
    
    return(mspe) # return the MSPE


# The 95% prediction interval is calculated by using the MSPE in the following formulas:
#     ![name](img/95_pred_int.png)
#     
# 
