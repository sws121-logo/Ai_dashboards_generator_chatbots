# AI Employee Prototype

## Overview
The AI Employee prototype automates the process of data ingestion, cleaning, analysis, and visualization, specifically for insurance purchase data. It leverages popular Python libraries including `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, and `streamlit` to deliver an interactive, user-friendly data analysis experience.

## Purpose of the Project
The project aims to provide a comprehensive data analysis solution for insurance-related datasets. It enables users to ingest, clean, analyze, and visualize data, making it easier to derive insights and make data-driven decisions.

## System Architecture
The system architecture consists of several key components:

- **Data Ingestion**: Supports file inputs in CSV, JSON, and Excel formats.
- **Data Cleaning**: Removes missing values and ensures data integrity.
- **Data Analysis**:
  - **Linear Regression**: For predictive modeling.
  - **KMeans Clustering**: For segmenting data into distinct groups.
- **Visualizations**: Generates scatter plots and other visual aids to interpret clustering results.
- **Dashboard**: An interactive interface developed with Streamlit that presents analysis results and facilitates user interaction.

## Data Extraction
The project allows users to upload datasets in various formats, including CSV, JSON, and Excel. The `ingest_data` method is responsible for reading these files and storing the data in a Pandas DataFrame. This flexibility ensures that users can work with their preferred data format.

## Models Used

1. **Linear Regression**: 
   - The project employs linear regression to predict the likelihood of individuals purchasing insurance based on various features in the dataset. The model is trained and tested using an 80-20 split of the data.
   - The Mean Squared Error (MSE) metric is used to evaluate the model's performance.

2. **KMeans Clustering**: 
   - KMeans clustering is applied to group the data into clusters based on similarities in the features. This helps in identifying patterns or segments within the dataset.
   - The number of clusters is set to 3, but this can be adjusted based on user requirements.

## Code Explanation

### Class Definition
- **AIEmployee**: Central class containing methods to perform the full range of tasks, from data ingestion to dashboard creation.

### Methods
- **ingest_data(file_path)**: Reads and loads data from the specified file format.
- **clean_data()**: Cleans the dataset by dropping rows with missing values.
- **analyze_data()**: Performs both linear regression and KMeans clustering.
- **generate_visualizations()**: Creates visual representations of the analysis results.
- **create_dashboard()**: Builds an interactive dashboard using Streamlit.
- **run(file_path)**: Orchestrates the complete workflow, from data ingestion to visualization.

## Challenges Faced
- **Data Quality**: Ensuring consistent and clean input data was challenging due to variations in data formats.
- **Model Selection**: Selecting the most appropriate models required careful consideration of the data’s characteristics.
- **User Interface**: Developing an intuitive and accessible user interface for users with varying technical skills posed a significant challenge.

## Potential Improvements
- **Enhanced Data Cleaning**: Implement advanced techniques such as outlier detection and handling categorical variables.
- **Model Optimization**: Explore hyperparameter tuning to improve the accuracy of machine learning models.
- **User Customization**: Provide users with more flexibility in customizing analyses and visualizations to meet their specific needs.

## Conclusion
Through the analysis, users can gain insights into the relationships between different features and the target variable (insurance purchase). The MSE provides a quantitative measure of the regression model's performance, while the clustering results help in understanding customer segments. The visualizations generated from the analysis enhance the interpretability of the results, making it easier for users to communicate findings.

## Deployment
The project is deployed using **Streamlit**, a popular framework for building interactive web applications for data science projects. The application provides a user-friendly interface where users can:

- Upload their datasets.
- View the data and its summary.
- Trigger data cleaning, analysis, and visualization processes.
- Interact with the results through buttons and charts.

## Getting Started

### Prerequisites
- Python 3.x
- Libraries: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `streamlit`

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/sws121-logo/Ai_dashboards_generator_chatbots/tree/main
   ```

