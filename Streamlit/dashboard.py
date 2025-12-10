import pandas as pd
import streamlit as st
import altair as alt

# Load dataset
data = pd.read_csv('../Data/vgsales_cleaned.csv')

st.title('🎮 Video Game Sales Dashboard')

# Sidebar filters
genre = st.sidebar.selectbox('Select Genre', options=data['Genre'].unique())
platform = st.sidebar.selectbox('Select Platform', options=data['Platform'].unique())

# Year range slider
year_range = st.slider(
    'Select Year Range',
    int(data['Year'].min()),
    int(data['Year'].max()),
    (1980, 2011)
)

# Genre multiselect (optional)
selected_genres = st.sidebar.multiselect(
    'Select Genres (optional)',
    options=data['Genre'].unique(),
    default=[genre]
)

# Filtered data
filtered = data[
    (data['Genre'].isin(selected_genres)) &
    (data['Platform'] == platform) &
    (data['Year'] >= year_range[0]) &
    (data['Year'] <= year_range[1])
]

st.subheader('Filtered Data')
st.dataframe(filtered)

# Top 10 platforms by global sales (from full dataset)
top_platforms = data.groupby('Platform')['Global'].sum().sort_values(ascending=False).head(10).reset_index()

platform_chart = alt.Chart(top_platforms).mark_bar(color='cornflowerblue').encode(
    x=alt.X('Global', title='Global Sales (millions)'),
    y=alt.Y('Platform', sort='-x'),
    tooltip=['Platform', 'Global']
).properties(
    title='Top 10 Platforms by Global Sales'
)

st.altair_chart(platform_chart, use_container_width=True)

# Global sales by year (from filtered data)
sales_by_year = filtered.groupby('Year')['Global'].sum().reset_index()

year_chart = alt.Chart(sales_by_year).mark_line(point=True).encode(
    x='Year',
    y=alt.Y('Global', title='Global Sales'),
    tooltip=['Year', 'Global (millions)']
).properties(
    title='Global Video Game Sales by Year'
)

st.altair_chart(year_chart, use_container_width=True)

