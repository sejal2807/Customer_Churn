# Customer_Churn
#deployment link
https://customerchurn-gwa8nckvndhzjrzgzfbmlh.streamlit.app/

IMPORTING THE LIBRARIES- All the necessary libraries like PANDAS, NUMPY, MATPLOTLIB, SEABORN AND SCIKIT-LEARN are imported. 
LOADING THE DATA- The data is loaded by pandas method READ_EXCEL.
 
DATA EXPLORATION- I learned the location column only held 5 location data. I used describe method of pandas to know the statistics of each column. I learned about the min, max, std, mean and 25,50,75 percentile of each columns data. The data was not imbalanced too as numbers of both target values were almost equal. Further I have catagorized the Age data into less than 20,20-30,30-40,......,60-70 catagories and learned that each catagories contains almost equal number of customers and customers who have churned and who have not also churned are also almost same in each catagory. This information is concluded by plotting Histogram. Different kind of Bar Chart, Histogram and Pie Chart are plotted.

DATA PREPROCESSING TECHNIQUES- This consists of finding the outliers, handling missing values, preparing the raw data. There was not a single null value present in the dataset and also not a single column consisted zero values. I used seaborn's boxplot to find the outliers. I discovered there are no outliers present by plotting boxplot. Further I had removed the unncessary columns like CustomerID and Name that were of no use.

FEATURE ENGINEERING- Machine learning models don't understand the text data but gender and location columns consisted the same. So I have used replace method for gender data and converted male to 1 and female to 0. As location has total 5 different values so I had used get_dummies method to convert catagorical data into numerical data. Afterwards one column from dummies otherwise it will lead to the problem of collinearity and the other original location column is dropped as it is now of no use. SelectKBest and Chi2 are used to get the feature score with respect to each column. Total_Usage_GB data column had the highest feature score. Further correlation matrix is plotted using Heatmap. I have used StandrdScaler for scaling the data.

MODEL FITTING- Various machine learning models are loaded like Logistic Regression, Decision Tree Classifier and KNeighbour Classifier. I have used train_test_split to seperate it between training and testing data. Test data is 30 percent of training data. I got 50 percent accuracy from all three models. But Decision Tree Classifier was giving 100 percent accuracy on training data. So there was a problem of overfitting then I use Lasso and Ridge models for regularization. But they gave even bad accuracy. Further I used BaggingClassifier but it also gave 50 percent accuracy. 

MODEL OPTIMIZATION- I have used GRIDSEARCHCV and HYPER PARAMETER TUNING to optimize the model with various parameters even with ShuffleSplit. Logistic Regression, Decision Tree Classifier, Random Forest were used. They yet gave only 50 percent accuracy. I used Lime and Lime Tabular to explain the specific prediction of model with a diagram. Furthere I have plotted CONFUSION MATRIX and CLASSIFICATION REPORT which consists of Precison, Recall and F1 Score. 

DUMPING INTO PICKLE FILE- Further I transferred the model into a pickle file that is used in main.py file.
