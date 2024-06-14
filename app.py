import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pandasai import Agent
import os

# Function to calculate mode
def mode(data):
    freq = {}
    for val in data:
        if val not in freq:
            freq[val] = 1
        else:
            freq[val] += 1
    max_count = max(freq.values())
    modes = [k for k, v in freq.items() if v == max_count]
    return modes

# Function to load CSV data
def load_data(file):
    return pd.read_csv(file)

# Function to calculate statistics
def calculate_stats(df):
    stats = {}
    for col in df.columns:
        stats[col] = {
            "Mean": np.mean(df[col]),
            "Median": np.median(df[col]),
            "Standard Deviation": np.std(df[col]),
            "Mode": mode(df[col].values)
        }
    return stats

# Function to plot different types of graphs
def plot_graph(df, col, graph_type):
    plt.figure(figsize=(8, 6))
    if graph_type == "Histogram":
        plt.hist(df[col], bins=10)
        plt.title(f"Histogram of {col}")
        plt.xlabel(col)
        plt.ylabel("Frequency")
        st.pyplot()
    elif graph_type == "Boxplot":
        sns.boxplot(df[col])
        plt.title(f"Boxplot of {col}")
        plt.xlabel(col)
        st.pyplot()
    elif graph_type == "Bar Chart":
        df[col].value_counts().plot(kind='bar')
        plt.title(f"Bar Chart of {col}")
        plt.xlabel(col)
        plt.ylabel("Count")
        st.pyplot()

# Function to plot pairplot
def plot_pairplot(df):
    sns.pairplot(df)
    st.pyplot()

# Main Streamlit application
def main():
    st.title("Statistical Analysis and Data Visualization")

    # File upload and loading data
    file = st.file_uploader("Upload a CSV file", type=["csv"])
    if file is not None:
        df = load_data(file)
        st.success("File uploaded successfully.")

        # Button to show statistical data
        if st.button("Show Statistical Data"):
            st.subheader("Statistical Data")
            st.write(calculate_stats(df))

        # Dropdowns for plotting graphs
        st.subheader("Plot Graphs")
        plot_type = st.selectbox("Select Plot Type", ["Histogram", "Boxplot", "Bar Chart"])
        column_to_plot = st.selectbox("Select Column to Plot", df.columns)

        # Button to plot selected graph
        if st.button("Plot"):
            plot_graph(df, column_to_plot, plot_type)

        # Button to plot pairplot
        if st.button("Plot Pairplot"):
            plot_pairplot(df)

        # Button to ask question to pandas AI
        st.subheader("Ask LLM")
        query = st.text_input("Enter your query")
        if st.button("Ask LLM"):
            # Replace YOUR_API_KEY with your actual API key
            YOUR_API_KEY = "$2a$10$WUXdxt0YBbsTbc2jkbLWx.gciPY7/6afonYh4PoOtwEI9bsTx9ZPe"
            os.environ["PANDASAI_API_KEY"] = YOUR_API_KEY
            agent = Agent(df)
            response = agent.chat(query)
            st.write(response)

if __name__ == '__main__':
    main()
