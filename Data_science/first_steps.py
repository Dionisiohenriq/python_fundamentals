import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

base_credit = pd.read_csv("credit_risk_dataset.csv")

pd.set_option('display.max_columns', None)

# show the first 10 registers
#print(base_credit.tail(10))

# show some math parameters for the DataSet, like min, max, medium, etc
#print(base_credit.describe())

#print(base_credit[base_credit['income'].max])
# income = base_credit.get('person_income')
# print(max(income))

# get the register based on max column value
print(base_credit.iloc[base_credit['person_income'].argmax()])
#print(base_credit.query('person_income == person_income.min()'))

# get the register based on min column value
print(base_credit.iloc[base_credit['loan_amnt'].argmin()])

print(np.unique(base_credit['loan_status'], return_counts=True))





