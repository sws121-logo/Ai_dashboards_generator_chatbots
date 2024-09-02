# AI Employee Prototype

## Overview
The AI Employee prototype automates the process of data ingestion, cleaning, analysis, and visualization, specifically for insurance purchase data. It leverages popular Python libraries including `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, and `streamlit` to deliver an interactive, user-friendly data analysis experience.

## System Architecture
The system architecture consists of several key components:

- **Data Ingestion**: Supports file inputs in `CSV`, `JSON`, and `Excel` formats.
- **Data Cleaning**: Removes missing values and ensures data integrity.
- **Data Analysis**:
  - **Linear Regression**: For predictive modeling.
  - **KMeans Clustering**: For segmenting data into distinct groups.
- **Visualizations**: Generates scatter plots and other visual aids to interpret clustering results.
- **Dashboard**: An interactive interface developed with `Streamlit` that presents analysis results and facilitates user interaction.

## Code Explanation

### Class Definition
- **AIEmployee**: Central class containing methods to perform the full range of tasks, from data ingestion to dashboard creation.

### Methods
- **`ingest_data(file_path)`**: Reads and loads data from the specified file format.
- **`clean_data()`**: Cleans the dataset by dropping rows with missing values.
- **`analyze_data()`**: Performs both linear regression and KMeans clustering.
- **`generate_visualizations()`**: Creates visual representations of the analysis results.
- **`create_dashboard()`**: Builds an interactive dashboard using `Streamlit`.
- **`run(file_path)`**: Orchestrates the complete workflow, from data ingestion to visualization.

## Challenges Faced
- **Data Quality**: Ensuring consistent and clean input data was challenging due to variations in data formats.
- **Model Selection**: Selecting the most appropriate models required careful consideration of the data’s characteristics.
- **User Interface**: Developing an intuitive and accessible user interface for users with varying technical skills posed a significant challenge.

## Potential Improvements
- **Enhanced Data Cleaning**: Implement advanced techniques such as outlier detection and handling categorical variables.
- **Model Optimization**: Explore hyperparameter tuning to improve the accuracy of machine learning models.
- **User Customization**: Provide users with more flexibility in customizing analyses and visualizations to meet their specific needs.

## Getting Started

### Prerequisites
- Python 3.x
- Libraries: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `streamlit`

### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/sws121-logo/Ai_dashboards_generator_chatbots/tree/main
