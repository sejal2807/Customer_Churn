import streamlit as st
import numpy as np
import pandas as pd
import openpyxl
import pickle
from sklearn.preprocessing import StandardScaler


age_list = []
def for_age_list(age_list):
    for i in range(18,71,1):
        age_list.append(i)
for_age_list(age_list)

subscription_month_list = []
def for_subscription_month_list(subscription_month_list):
    for i in range(1,25,1):
        subscription_month_list.append(i)
for_subscription_month_list(subscription_month_list)

total_usage_gb_list = []
def for_total_usage_gb__list(total_usage_gb__list):
    for i in range(50,501,1):
        total_usage_gb__list.append(i)
for_total_usage_gb__list(total_usage_gb_list)

location_list = ['Chicago','Houston','Los Angeles','Miami','New Work']

st.write("""
         # Customer Churn Prediction App
         """)
age = st.selectbox(
        'what is your age?', age_list)
gender = st.selectbox(
        'what is your gender?',['Male','Female']
    )
subscription_length_months = st.selectbox(
        'what is your subscription length months?',subscription_month_list
    )
monthly_bill = st.slider("what is your monthly bill?", 30.00,50.00,100.00)

total_usage_gb = st.selectbox(
    'what is your usage GB?', total_usage_gb_list)

location = st.selectbox(
    'what is your location?',location_list
)


if location=='Chicago':
    New_York,Los_Angeles,Houston,Miami=0,0,0,0
if location=='Houston':
    New_York, Los_Angeles, Houston, Miami = 0, 0, 1, 0
if location=='Los Angeles':
    New_York, Los_Angeles, Houston, Miami = 0, 1, 0, 0
if location=='Miami':
    New_York, Los_Angeles, Houston, Miami = 0, 0, 0, 1
if location=='New York':
    New_York, Los_Angeles, Houston, Miami = 1, 0, 0, 0


if gender == 'Male':
    gender = 1
else:
    gender = 0

data = {
    'Age' : age,
    'Gender' : gender,
    'Subscription_Length_Months': subscription_length_months,
    'Monthly_Bill' : monthly_bill,
    'Total_Usage_GB' : total_usage_gb,
    'Houston':Houston,
    'Los Angeles' : Los_Angeles,
    'Miami' : Miami,
    'New York' : New_York

}

features = pd.DataFrame(data,index=[0])
model = pickle.load(open('Customer_Churn.pickle','rb'))
df = pd.read_excel('customer_churn_large_dataset.xlsx')
df1 = df.drop(['CustomerID','Name'],axis='columns')
df1['Gender'].replace(['Female','Male'],[0,1],inplace=True)
dummies = pd.get_dummies(df1.Location)
df2 = pd.concat([df1,dummies.drop('Chicago',axis='columns')],axis='columns')
df3=df2.drop('Location',axis='columns')
df3 =df3.drop('Churn',axis='columns')
mapping = { True : 1 , False : 0}
df3['Houston'] = df3['Houston'].map(mapping)
df3['Los Angeles'] = df3['Los Angeles'].map(mapping)
df3['Miami'] = df3['Miami'].map(mapping)
df3['New York'] = df3['New York'].map(mapping)

st.write('The Data You Entered')
st.write(features)
scaler = StandardScaler()
scaler.fit(df3)
_user_input = scaler.transform(features)


output = model.predict(_user_input)
if output[0]==0.0:
    st.header('The Prediction Output is- Customer Has Not Churned')
else:
    st.header('The Prediction Output is- Customer Has Churned')
