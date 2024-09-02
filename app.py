import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import streamlit as st
import pandas as pd


class AIEmployee:
    def _init_(self):
        self.data = None

    def ingest_data(self, file_path):
        if file_path.name.endswith('.csv'):
            self.data = pd.read_csv(file_path)
        elif file_path.name.endswith('.json'):
            self.data = pd.read_json(file_path)
        elif file_path.name.endswith('.xlsx'):
            self.data = pd.read_excel(file_path)
        else:
            raise ValueError("Unsupported file format.")
        st.success("Data ingested successfully.")

    def clean_data(self):
        self.data.dropna(inplace=True)  # Simple cleaning
        st.success("Data cleaned successfully.")

    def analyze_data(self):
        # Example: Linear Regression
        X = self.data.drop('bought_insurance', axis=1)  # Replace with your target column
        y = self.data['bought_insurance']  # Replace with your target column
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = LinearRegression()
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        st.write(f"Linear Regression MSE: {mse}")

        # KMeans Clustering
        kmeans = KMeans(n_clusters=3)
        self.data['Cluster'] = kmeans.fit_predict(X)
        st.success("KMeans clustering completed.")

    def generate_visualizations(self):
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=self.data, x='age', y='bought_insurance', hue='Cluster')  # Replace with your features
        plt.title('KMeans Clustering')
        plt.savefig('report.png')
        plt.close()
        st.image('report.png', caption='KMeans Clustering Visualization')

    def create_dashboard(self):
        st.title("Data Analysis Dashboard")
        st.write(self.data)

        if st.button('Show Clusters'):
            st.write(self.data['Cluster'].value_counts())
            st.bar_chart(self.data['Cluster'].value_counts())

        # Add more interactive elements as needed

    def run(self, file_path):
        self.ingest_data(file_path)
        self.clean_data()
        self.analyze_data()
        self.generate_visualizations()
        self.create_dashboard()


def main():
    st.sidebar.title("AI Employee Data Analysis")
    uploaded_file = st.sidebar.file_uploader("insurance_data.csv", type=['csv', 'json', 'xlsx'])

    if uploaded_file is not None:
        ai_employee = AIEmployee()
        ai_employee.run(uploaded_file)


if __name__ == "__main__":
    main()
