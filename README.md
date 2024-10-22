Job Recommendation System
This project is a Job Recommendation System developed as my second project during an ML internship at EZITECH. The purpose of this project is to recommend jobs based on a selected job title using machine learning techniques such as TF-IDF and Cosine Similarity.

Table of Contents
Project Description
Dataset
Technologies Used
Installation
Project Structure
Steps to Run
How It Works
Project Workflow
Acknowledgements
Project Description
The Job Recommendation System recommends similar job titles based on the job title provided by the user. This recommendation is based on the similarity between job descriptions, titles, and positions using a machine learning-based similarity measure. The recommendation system uses TF-IDF (Term Frequency-Inverse Document Frequency) to transform the textual data into numerical features and Cosine Similarity to find similar jobs.

Dataset
The dataset used in this project contains the following fields:

Job Description: A detailed description of the job.
Title: The title of the job.
Position: The job position or category.
This dataset was cleaned and preprocessed to make it suitable for building a recommendation model.

Technologies Used
Python: Primary programming language.
Streamlit: Used to create a web-based interface for the recommendation system.
Pandas: For data manipulation and analysis.
Scikit-learn: To compute TF-IDF and cosine similarity.
Pickle: To save and load the preprocessed data.
Jupyter Notebook: For data preprocessing and initial model development.
Installation
To get started with the project, follow the steps below:

Prerequisites
Python 3.7 or higher
Recommended to create a virtual environment.
Install Required Packages
Create a requirements.txt file in your project folder and include the following dependencies:

plaintext
Copy code
streamlit
pandas
scikit-learn
pickle5
Use the following command to install the packages:

bash
Copy code
pip install -r requirements.txt
Project Structure
plaintext
Copy code
job-recommendation-system/
│
├── app.py                  # Main Streamlit app for job recommendation
├── df.pkl                  # Serialized DataFrame with job data
├── similarity.pkl          # Serialized similarity matrix
├── data/                   # Folder for the dataset (if applicable)
├── notebooks/              # Jupyter notebooks for preprocessing and experimentation
├── README.md               # Project readme file (this file)
├── requirements.txt        # Required packages
└── .gitignore              # Git ignore file (to exclude unnecessary files)
Steps to Run
Data Preprocessing:

Loaded the dataset using Pandas.
Removed special characters, cleaned the text, and removed stop words.
Combined relevant columns (Job Description, Title, and Position) into a single column called clean_text.
Feature Extraction:

Used TF-IDF Vectorizer from scikit-learn to convert the cleaned text into numerical vectors.
Computed Cosine Similarity between job descriptions to identify similar jobs.
Model Persistence:

Saved the preprocessed data (df.pkl) and the similarity matrix (similarity.pkl) using the pickle library.
Building the Streamlit Web App:

Created a Streamlit web interface using app.py.
Allowed users to select a job title from a dropdown menu.
Displayed similar job titles using the recommendation function.
How to Run the Project
Start the Streamlit App:

bash
Copy code
streamlit run app.py
Access the App:

Open your browser and navigate to http://localhost:8501.
How It Works
TF-IDF Vectorizer: Transforms job descriptions into numerical vectors by assigning importance to terms based on their frequency and uniqueness within the dataset.
Cosine Similarity: Measures the similarity between job descriptions by computing the cosine of the angle between their vectors.
Recommendation System: The system retrieves the top 20 similar job titles based on the cosine similarity scores.
Project Workflow
Data Preprocessing:

Imported the dataset using pandas.
Cleaned the data by removing unnecessary characters and stop words.
Tokenized the cleaned text.
Feature Extraction:

Utilized TfidfVectorizer to convert text to numerical vectors.
Computed a similarity matrix using cosine_similarity.
Streamlit Development:

Developed an interactive web interface using Streamlit.
Displayed job recommendations based on user input.
Debugging and Error Fixes:

Handled various edge cases like empty inputs and mismatched data.
Fixed potential data type errors by standardizing input and cleaned data.
Acknowledgements
This project was developed as my second machine learning project during the ML internship at EZITECH. Special thanks to the EZITECH team for their guidance and support throughout this project.
