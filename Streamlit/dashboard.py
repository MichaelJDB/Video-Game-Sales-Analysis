import pandas as pd 
import streamlit as st
import matplotlib.pyplot as plt 

#Load datbase
data = pd.read_csv('../Data/vgsales_cleaned.csv')


st.title('Video Game Sales Dashboard')

#Sidebar filters
genre = st.sidebar.selectbox('Select Genre', options=data['Genre'].unique()) 
platform = st.sidebar.selectbox("Select Platform", options=data['Platform'].unique())

#Filtered data
filtered = data[(data['Genre'] == genre) & (data['Platform'] == platform)]

#Show table
st.write("Filtered Data", filtered)

#Plot total global sales by year
sales_by_year = filtered.groupby('Year')['Global'].sum().reset_index()

top_platforms = data.groupby('Platform')['Global'].sum().sort_values(ascending=False).head(10)

fig, ax = plt.subplots()
top_platforms.plot(kind='barh', ax=ax, color='blue')
ax.set_title("Top 10 Platforms by Global Sales")
ax.set_xlabel("Global Sales (millions)")
ax.set_ylabel("Platform")
st.pyplot(fig)

