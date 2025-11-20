import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Boston Housing Data App")

# Load dataset
df = pd.read_csv("housing.csv")

st.header("Data Overview")

if st.button("Show first 10 rows"):
    st.write(df.head(10))

if st.button("Show summary statistics"):
    st.write(df.describe())

if st.button("Show column names"):
    st.write(df.columns.tolist())

if st.button("Count missing values"):
    st.write(df.isnull().sum())

if st.button("Show shape (rows, columns)"):
    st.write(df.shape)

st.header("Filters")

if st.button("Houses with price > 30"):
    st.write(df[df['medv'] > 30])

if st.button("Houses with more than 6 rooms"):
    st.write(df[df['rm'] > 6])

if st.button("Houses where crime rate is low"):
    st.write(df[df['crim'] < 1])

# ---------------- VISUALIZATION SECTION ----------------

st.header("Visualization")

# 1️⃣ Price Distribution Histogram
st.subheader("Price Distribution")
fig1 = plt.figure(figsize=(8,5))
sns.histplot(df['medv'], bins=30)
plt.title('Price Distribution')
st.pyplot(fig1)

# 2️⃣ Rooms vs Price Scatter Plot
st.subheader("Rooms vs Price Scatter Plot")
fig2 = plt.figure(figsize=(8,5))
plt.scatter(df['rm'], df['medv'])
plt.xlabel("Number of Rooms")
plt.ylabel("Price")
plt.title("Rooms vs Price")
st.pyplot(fig2)

