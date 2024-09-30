conda create --name main-ds python=3.9
conda activate main-ds

# Persiapan
"""

pip install streamlit

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

"""# Mempersiapkan Dataframe"""

def create_yearly_weather_df(df):
    yearly_weather_df = df.resample(rule='Y', on='date').agg({
        "TEMP": "mean",
        "RAIN": "mean"
    })
    yearly_weather_df = yearly_weather_df.reset_index()
    yearly_weather_df.rename(columns={
        "TEMP": "avg_temp",
        "RAIN": "avg_rain"
    }, inplace=True)

    return yearly_weather_df

def create_yearly_air_quality_df(df):
    yearly_air_quality_df = df.resample(rule='Y', on='date').agg({
        "PM2.5": ["mean", "max"],
        "PM10": ["mean", "max"],
        "SO2": ["mean", "max"],
        "NO2": ["mean", "max"],
        "CO": ["mean", "max"]
    })
    yearly_air_quality_df = yearly_air_quality_df.reset_index()
    yearly_air_quality_df.rename(columns={
        "PM2.5_mean": "avg_pm25",
        "PM2.5_max": "max_pm25",
        "PM10_mean": "avg_pm10",
        "PM10_max": "max_pm10",
        "SO2_mean": "avg_so2",
        "SO2_max": "max_so2",
        "NO2_mean": "avg_no2",
        "NO2_max": "max_no2",
        "CO_mean": "avg_co",
        "CO_max": "max_co"
    }, inplace=True)

    return yearly_air_quality_df

def create_bystation_df(df):
    bystation_df = df.groupby(by="station")["No"].nunique().reset_index()
    bystation_df.rename(columns={
        "No": "data_count"
    }, inplace=True)

    return bystation_df

def create_byyear_df(df):
    byyear_df = df.groupby(by="year")["No"].nunique().reset_index()
    byyear_df.rename(columns={
        "No": "data_count"
    }, inplace=True)

    return byyear_df

all_df = pd.read_csv("mixed_dataset.csv")
all_df.head()

all_df.tail(10)

all_df['date'] = pd.to_datetime(all_df[['year', 'month', 'day']])

all_df.head()

"""# Membuat Komponen Filter"""

min_date = all_df["date"].min()
max_date = all_df["date"].max()

with st.sidebar:
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

main_df = all_df[(all_df["date"] >= str(start_date)) &
                (all_df["date"] <= str(end_date))]

yearly_weather_df = create_yearly_weather_df(main_df)
yearly_air_quality_df = create_yearly_air_quality_df(main_df)
bystation_df = create_bystation_df(main_df)
byyear_df = create_byyear_df(main_df)

"""# Visualisasi Data"""

st.header('Air Quality in Gucheng and Huairou :sparkles:')

st.subheader('Yearly Weather Data')

col1, col2 = st.columns(2)

with col1:
    average_temp = round(yearly_weather_df["avg_temp"].mean(), 2)
    st.metric("Average Temperature", f"{average_temp}°C")

with col2:
    average_rain = round(yearly_weather_df["avg_rain"].mean(), 2)
    st.metric("Average Rainfall", f"{average_rain} mm")

# Create a figure and axes for the combined line graph
fig, ax = plt.subplots(figsize=(16, 8))

# Plot `avg_temp`
ax.plot(
    yearly_weather_df["date"],
    yearly_weather_df["avg_temp"],
    marker='o',
    linewidth=2,
    label="Average Temperature",
    color="blue"
)

# Plot `avg_rain`
ax.plot(
    yearly_weather_df["date"],
    yearly_weather_df["avg_rain"],
    marker='o',
    linewidth=2,
    label="Average Rainfall",
    color="green"
)

# Add labels, legend, and grid
ax.set_xlabel("Date")
ax.set_ylabel("Value")
ax.set_title("Yearly Weather Data")
ax.legend()
ax.grid(True)

# Display the plot
st.pyplot(fig)

# Calculate average temperature by year-month
average_temp_by_year_month = all_df.groupby(['year', 'month'])['TEMP'].mean().reset_index()

# Create the line plot with seaborn
plt.figure(figsize=(12, 6))
sns.lineplot(x='month', y='TEMP', hue='year', data=average_temp_by_year_month, marker='o')
plt.title('Average Temperature Overall')
plt.xlabel('Month')
plt.ylabel('Temperature')
plt.xticks(range(1, 13))  # Set x-axis ticks to represent months
plt.grid(True)
plt.legend(title='Year')

# Display the plot in Streamlit
st.subheader("Average Temperature by Year and Month")
st.pyplot(plt)

st.subheader('Yearly Air Quality Data')

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    average_PM2_5 = round(yearly_air_quality_df["PM2.5"].mean(), 2)
    st.metric("Average PM2.5 level", f"{average_PM2_5}mikron")
    max_PM2_5 = round(yearly_air_quality_df["PM2.5"].max(), 2)
    st.metric("Max PM2.5 level", f"{max_PM2_5}mikron")

with col2:
    average_PM10 = round(yearly_air_quality_df["PM10"].mean(), 2)
    st.metric("Average PM10 level", f"{average_PM10}mikron")
    max_PM10 = round(yearly_air_quality_df["PM10"].max(), 2)
    st.metric("Max PM10 level", f"{max_PM10}mikron")

with col3:
    average_SO2 = round(yearly_air_quality_df["SO2"].mean(), 2)
    st.metric("Average SO2 level", f"{average_SO2}mikron")
    max_SO2 = round(yearly_air_quality_df["SO2"].max(), 2)
    st.metric("Max SO2 level", f"{max_SO2}mikron")

with col4:
    average_NO2 = round(yearly_air_quality_df["NO2"].mean(), 2)
    st.metric("Average NO2 level", f"{average_NO2}mikron")
    max_NO2 = round(yearly_air_quality_df["NO2"].max(), 2)
    st.metric("Max NO2 level", f"{max_NO2}mikron")

with col5:
    average_CO = round(yearly_air_quality_df["CO"].mean(), 2)
    st.metric("Average CO level", f"{average_CO}mikron")
    max_CO = round(yearly_air_quality_df["CO"].max(), 2)
    st.metric("Max CO level", f"{max_CO}mikron")

# Create a figure and axes for the combined line graph
fig, ax = plt.subplots(figsize=(16, 8))

# Plot `PM2.5`
ax.plot(
    yearly_air_quality_df["date"],
    yearly_air_quality_df["PM2.5"],
    marker='o',
    linewidth=2,
    label="PM2.5 level",
    color="blue"
)

# Plot `PM10`
ax.plot(
    yearly_air_quality_df["date"],
    yearly_air_quality_df["PM10"],
    marker='o',
    linewidth=2,
    label="PM10 level",
    color="green"
)

# Plot `SO2`
ax.plot(
    yearly_air_quality_df["date"],
    yearly_air_quality_df["SO2"],
    marker='o',
    linewidth=2,
    label="SO2 level",
    color="red"
)

# Plot `NO2`
ax.plot(
    yearly_air_quality_df["date"],
    yearly_air_quality_df["NO2"],
    marker='o',
    linewidth=2,
    label="NO2 level",
    color="orange"
)

# Plot `CO`
ax.plot(
    yearly_air_quality_df["date"],
    yearly_air_quality_df["CO"],
    marker='o',
    linewidth=2,
    label="CO level",
    color="purple"
)

# Add labels, legend, and grid
ax.set_xlabel("Date")
ax.set_ylabel("Value")
ax.set_title("Yearly Air Quality Data")
ax.legend()
ax.grid(True)

# Display the plot
st.pyplot(fig)

gases = ['SO2', 'NO2', 'CO', 'O3', 'PM2.5', 'PM10']

plt.figure(figsize=(15, 10))

for i, gas in enumerate(gases):
    plt.subplot(2, 3, i + 1)
    sns.lineplot(x='year', y=gas, hue='station', data=all_df, marker='o')  # Use lineplot for trend, add hue for station
    plt.title(f'{gas} Levels Over Time')
    plt.xlabel('Year')
    plt.ylabel(gas + ' Concentration')
    plt.grid(True)

plt.tight_layout()
plt.show()

st.subheader('Gas Levels Over Time')
st.pyplot(plt)
