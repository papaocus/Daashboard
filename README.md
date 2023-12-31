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


Install the necessary packages:

Make sure you have Python installed on your system.
Open a terminal or command prompt.
Use the following command to install Streamlit, pandas, and matplotlib: pip install streamlit pandas matplotlib
Create a new Python file:

Open Visual Studio.
Create a new Python file and give it a name (e.g., app.py).
Copy and paste the code into the Python file:

Copy the provided code and paste it into the newly created Python file in Visual Studio.
Save the file:

Save the Python file.
Run the Streamlit application:

Open a terminal or command prompt.
Navigate to the directory where the Python file is saved.
Use the following command to run the Streamlit application: streamlit run app.py
Streamlit will start a local development server and launch the application in your default web browser.

![Screenshot 2023-07-07 142936](https://github.com/papaocus/Daashboard/assets/115074006/fb9d8274-de84-460c-92b8-1d2ab5821d01)
![Screenshot 2023-07-07 142957](https://github.com/papaocus/Daashboard/assets/115074006/223d8b18-94ae-46d2-abf3-a47a08d07175)
![Screenshot 2023-07-07 143026](https://github.com/papaocus/Daashboard/assets/115074006/a7416298-e4bd-44db-a205-32c3af92b582)
![Screenshot 2023-07-07 143056](https://github.com/papaocus/Daashboard/assets/115074006/838088a5-f22b-40b5-94da-5b17e8de500c)
