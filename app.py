import streamlit as st
import pandas as pd
import pickle

# Load the data
df = pickle.load(open('df.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Data cleaning to avoid comparison issues
df = df.dropna(subset=['Title'])  # Remove NaN values in the 'Title' column
df['Title'] = df['Title'].astype(str)  # Ensure all 'Title' entries are strings
df['Title'] = df['Title'].str.strip().str.lower()  # Strip whitespaces and lowercase for consistency


def recommendation(title):
    # Ensure the selected title is formatted correctly
    title = str(title).strip().lower()

    # Check if the title exists in the DataFrame
    if title not in df['Title'].values:
        st.error("The selected job title does not exist in the dataset.")
        return []

    idx = df[df['Title'] == title].index[0]
    idx = df.index.get_loc(idx)
    distances = sorted(list(enumerate(similarity[idx])), reverse=True, key=lambda x: x[1])[1:20]

    jobs = []
    for i in distances:
        jobs.append(df.iloc[i[0]].Title)

    return jobs


# Web app
st.title('Job Recommendation System')
title = st.selectbox('Search job', df['Title'].unique())

jobs = recommendation(title)

if jobs:
    st.write(jobs)
