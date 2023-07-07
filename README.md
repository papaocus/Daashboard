# Daashboard

Here's a breakdown of the code:

Importing the necessary libraries:

streamlit: A library for creating interactive web applications.
pandas: A library for data manipulation and analysis.
matplotlib.pyplot: A library for creating data visualizations.
Loading the data:

The CSV file "mdf.csv" is read into a Pandas DataFrame (mdf).
The "Datetime" column is parsed as dates, and the "Datetime" column is set as the index of the DataFrame.
Creating the Streamlit application:

The title of the application is set using st.title.
The DataFrame is displayed using st.dataframe.
Adding a sidebar for analysis options:

A selectbox in the sidebar allows you to choose between "Summary" and "Visualizations" for analysis.
Performing analysis based on the selected option:

If "Summary" is selected:

Summary statistics are displayed using st.write and mdf.describe().
Missing values are displayed using st.write and mdf.isnull().sum().
The number of duplicates is displayed using st.write and mdf.duplicated().sum().
If "Visualizations" is selected:

Average and peak people count by floor are plotted as bar charts using matplotlib.pyplot and displayed using st.pyplot.
People count by department is plotted as a bar chart and displayed.
The top 5 desks with the most consistent occupancy are displayed in a DataFrame using st.dataframe.
People count by day of the week is plotted as a line chart and displayed.
People count over time is plotted as a line chart and displayed.
Outliers are displayed in a DataFrame using st.dataframe.
The distribution of people count is plotted as a histogram and displayed.
People count by floor and by department are plotted as bar charts and displayed.
