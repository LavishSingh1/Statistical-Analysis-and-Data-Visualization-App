# Statistical Analysis and Data Visualization App

This Streamlit application provides tools for statistical analysis and data visualization on CSV datasets. It allows users to upload a CSV file, analyze its statistical properties, plot various types of graphs, generate pairplots, and interactively query the dataset using pandas AI.

## Features

1. **Upload CSV File**: Users can upload a CSV file for analysis.
   
2. **Statistical Data**: Upon clicking the "Show Statistical Data" button, the application calculates and displays the mean, median, standard deviation, and mode for each column in the dataset.

3. **Plot Graphs**: Users can choose a column and a graph type (Histogram, Boxplot, or Bar Chart) to plot. Upon clicking the "Plot" button, the selected graph is generated.

4. **Plot Pairplot**: Generates a pairplot of the entire dataset, showing pairwise relationships between variables.

5. **Ask LLM**: Uses the `pandasai` library to allow users to ask natural language queries about the dataset, providing insights based on the data.

## Setup Instructions

1. **Install Dependencies**:
   - Ensure you have Python 3.6 or later installed.
   - Install required Python packages using pip:
     ```
     pip install streamlit pandas numpy seaborn matplotlib pandasai
     ```

2. **Run the Application**:
   - Clone this repository to your local machine.
   - Navigate to the project directory and run the Streamlit app:
     ```
     streamlit run app.py
     ```
   - This command will launch a local server and provide a URL where you can access the application in your web browser (typically `http://localhost:8501`).

3. **Using the Application**:
   - Upload your CSV file using the file upload widget.
   - Explore statistical data by clicking the "Show Statistical Data" button.
   - Choose a column and plot type to visualize using the dropdowns and plot button under "Plot Graphs".
   - Generate a pairplot by clicking the "Plot Pairplot" button.
   - Ask questions about the dataset using the text input and "Ask LLM" button.

## Example Usage

- Upload a CSV file containing relevant data.
- Click "Show Statistical Data" to view basic statistics.
- Select a column and choose a graph type (Histogram, Boxplot, Bar Chart) to visualize distribution or trends.
- Generate a pairplot to explore relationships between variables.
- Ask questions about the data using natural language queries and "Ask LLM".

## About

This application is developed using Streamlit, a popular Python framework for building interactive web applications for data science and machine learning tasks. It integrates statistical analysis, visualization capabilities, and natural language processing using the pandasai library.
