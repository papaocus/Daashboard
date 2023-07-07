import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
mdf = pd.read_csv("D:\Adaapt dashboard\mdf.csv", parse_dates=["Datetime"], index_col="Datetime")

# Title
st.title("Exploratory Data Analysis")

# Display the dataframe
st.subheader("Data")
st.dataframe(mdf)

# Sidebar options
analysis_option = st.sidebar.selectbox("Select Analysis", ("Summary", "Visualizations"))

if analysis_option == "Summary":
    # Summary statistics
    st.subheader("Summary Statistics")
    st.write(mdf.describe())

    # Missing values
    st.subheader("Missing Values")
    st.write(mdf.isnull().sum())

    # Duplicates
    st.subheader("Duplicates")
    st.write("Number of duplicates:", mdf.duplicated().sum())

elif analysis_option == "Visualizations":
    # Average and peak people count by floor
    st.subheader("Average and Peak People Count by Floor")
    average_count = mdf.groupby('floor')['peopleCount'].mean()
    peak_count = mdf.groupby('floor')['peopleCount'].max()
    fig, ax = plt.subplots()
    ax.bar(average_count.index, average_count, label='Average')
    ax.bar(peak_count.index, peak_count, label='Peak')
    ax.set_xlabel('Floor')
    ax.set_ylabel('People Count')
    ax.legend()
    st.pyplot(fig)

    # People count by department
    st.subheader("People Count by Department")
    department_count = mdf.groupby('department')['peopleCount'].sum()
    fig, ax = plt.subplots()
    ax.bar(department_count.index, department_count)
    ax.set_xlabel('Department')
    ax.set_ylabel('People Count')
    plt.xticks(rotation=90)
    st.pyplot(fig)

    # Top 5 Desks with Most Consistent Occupancy
    st.subheader("Top 5 Desks with Most Consistent Occupancy")
    consistent_occupancy = mdf.groupby('name')['peopleCount'].mean().sort_values(ascending=False)[:5]
    consistent_occupancy_table = pd.DataFrame(consistent_occupancy).reset_index()
    st.dataframe(consistent_occupancy_table)

    # People count by day of week
    st.subheader("People Count by Day of Week")
    mdf['day_of_week'] = mdf.index.dayofweek
    people_count_day_of_week = mdf.groupby('day_of_week')['peopleCount'].sum()
    fig, ax = plt.subplots()
    ax.plot(people_count_day_of_week.index, people_count_day_of_week)
    ax.set_xlabel('Day of Week')
    ax.set_ylabel('People Count')
    ax.set_xticks(range(7))
    ax.set_xticklabels(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
    st.pyplot(fig)

    # People count over time
    st.subheader("People Count Over Time")
    people_count_over_time = mdf.resample('1H')['peopleCount'].sum()
    fig, ax = plt.subplots()
    ax.plot(people_count_over_time.index, people_count_over_time)
    ax.set_xlabel('Time')
    ax.set_ylabel('People Count')
    st.pyplot(fig)

    # Outliers
    st.subheader("Outliers")
    outliers = mdf[mdf['peopleCount'] > mdf['peopleCount'].mean() + 2 * mdf['peopleCount'].std()]
    st.dataframe(outliers)

    # Distribution of People Count
    st.subheader("Distribution of People Count")
    plt.figure(figsize=(8, 6))
    plt.hist(mdf['peopleCount'], bins=20)
    plt.xlabel('People Count')
    plt.ylabel('Frequency')
    plt.title('Distribution of People Count')
    st.pyplot(plt)

    # People count by floor
    st.subheader("People Count by Floor")
    floor_counts = mdf['floor'].value_counts()
    plt.figure(figsize=(8, 6))
    plt.bar(floor_counts.index, floor_counts)
    plt.xlabel('Floor')
    plt.ylabel('Count')
    plt.title('People Count by Floor')
    st.pyplot(plt)

    # People count by department
    st.subheader("People Count by Department")
    department_counts = mdf['department'].value_counts()
    plt.figure(figsize=(10, 6))
    plt.bar(department_counts.index, department_counts)
    plt.xlabel('Department')
    plt.ylabel('Count')
    plt.title('People Count by Department')
    plt.xticks(rotation=90)
    st.pyplot(plt)

   