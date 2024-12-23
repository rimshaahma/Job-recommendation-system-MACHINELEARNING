
# Job Recommendation System

## Project Overview
This project is a **Job Recommendation System** developed during my machine learning internship at EZITECH. The system suggests similar job titles based on a user-provided job title using machine learning techniques such as **TF-IDF** (Term Frequency-Inverse Document Frequency) and **Cosine Similarity**. The goal is to recommend jobs that closely match the user's job title by analyzing the similarity between job descriptions, titles, and positions.

---

## Table of Contents
1. [Project Description](#project-description)
2. [Dataset](#dataset)
3. [Technologies Used](#technologies-used)
4. [Installation](#installation)
5. [Project Structure](#project-structure)
6. [Steps to Run](#steps-to-run)
7. [How It Works](#how-it-works)
8. [Project Workflow](#project-workflow)
9. [Acknowledgements](#acknowledgements)

---

## Project Description
The **Job Recommendation System** uses natural language processing (NLP) techniques to recommend jobs that are similar to a given job title. By applying **TF-IDF** for feature extraction and **Cosine Similarity** for calculating the similarity between job titles, the system provides relevant job recommendations based on textual data. The system's interactive interface is built using **Streamlit**, allowing users to easily query the model.

---

## Dataset
The dataset used in this project contains job data with the following columns:
- **Job Description**: A detailed description of the job responsibilities.
- **Title**: The job title.
- **Position**: The job position or category.

The dataset was preprocessed to clean and structure the text, making it ready for analysis and recommendation.

---

## Technologies Used
- **Python**: The primary programming language for this project.
- **Streamlit**: For building the interactive web application.
- **Pandas**: For data manipulation and processing.
- **Scikit-learn**: For implementing the TF-IDF vectorizer and cosine similarity computation.
- **Pickle**: To save and load preprocessed data and model outputs.
- **Jupyter Notebook**: For initial data preprocessing and experimentation.

---

## Installation
### Prerequisites
- **Python 3.7** or higher is required.
- It's recommended to use a virtual environment for managing dependencies.

### Install Required Packages
1. Create a `requirements.txt` file containing:
    ```
    streamlit
    pandas
    scikit-learn
    pickle5
    ```

2. Install dependencies using pip:
    ```bash
    pip install -r requirements.txt
    ```

---

## Project Structure
The project directory is organized as follows:
```
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
```

---

## Steps to Run
1. **Data Preprocessing**:
    - Loaded the dataset using Pandas.
    - Cleaned text by removing special characters, stop words, and irrelevant information.
    - Combined relevant columns (Job Description, Title, and Position) into a single `clean_text` column for further processing.

2. **Feature Extraction**:
    - Used **TF-IDF** to convert the cleaned text data into numerical vectors.
    - Calculated the **Cosine Similarity** between job descriptions to identify similar jobs.

3. **Model Persistence**:
    - Saved the processed data and similarity matrix using **Pickle** for efficient loading and prediction.

4. **Building the Streamlit Web App**:
    - Created an interactive user interface using **Streamlit** to display job recommendations based on user input.

---

## How to Run the Project
1. **Start the Streamlit App**:
    ```bash
    streamlit run app.py
    ```

2. **Access the App**:
    - Open your browser and navigate to [http://localhost:8501](http://localhost:8501) to interact with the job recommendation system.

---

## How It Works
1. **TF-IDF Vectorizer**: 
    - Converts job descriptions into numerical vectors, capturing the importance of each term based on its frequency and uniqueness across the dataset.

2. **Cosine Similarity**: 
    - Computes the similarity between job descriptions by measuring the cosine of the angle between their TF-IDF vectors. The smaller the angle, the more similar the jobs are.

3. **Recommendation System**: 
    - The system retrieves the top 20 similar job titles based on cosine similarity, providing the user with relevant job recommendations.

---

## Project Workflow
1. **Data Preprocessing**: 
    - Imported the dataset and cleaned the text by removing unnecessary characters, stop words, and tokenized the cleaned text.

2. **Feature Extraction**: 
    - Used **TF-IDF Vectorizer** to transform the text into numerical vectors.
    - Created a **cosine similarity matrix** to find similar job descriptions.

3. **Streamlit Development**: 
    - Developed an interactive web interface using Streamlit to allow users to select a job title and get similar job recommendations.

4. **Debugging and Error Fixes**: 
    - Handled edge cases like empty inputs and data inconsistencies.
    - Fixed issues related to data types and standardized input and output formats.

---

## Acknowledgements
This project was developed as part of my machine learning internship at **EZITECH**. Special thanks to the **EZITECH** team for their support and guidance throughout this project.

---

This **Job Recommendation System** project efficiently showcases how **TF-IDF** and **Cosine Similarity** can be used in conjunction to recommend similar job titles. The project demonstrates practical applications of machine learning for real-world problems and offers a user-friendly interface to make job recommendations accessible to anyone.
