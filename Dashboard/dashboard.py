import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import altair as alt
sns.set(style='white')

st.title("Bike Sharing Analysis Dashboard")

season_rent = pd.DataFrame({
    'season_day': ['Spring', 'Summer', 'Fall', 'Winter'],
    'cnt_day': [471348, 918589, 1061129, 841613],
})
highrent_season = season_rent.loc[season_rent['cnt_day'].idxmax()]

dataUser = {
    'casual_hour': [620017],
    'registered_hour': [2672662]
}
merged_hourday = pd.DataFrame(dataUser)
totaluserCasual = merged_hourday['casual_hour'].sum()
totaluserRegistered = merged_hourday['registered_hour'].sum()

user_data = pd.DataFrame({
    'user_type': ['Casual', 'Registered'],
    'total_users': [totaluserCasual, totaluserRegistered]
})

workday_rental = pd.DataFrame({
    'workingday_hour': ['Weekend', 'Weekday'],
    'cnt_hour': [1000269, 2292410]
})

#pertanyaan1
st.header("Jumlah Penyewaan Sepeda Setiap Musim")
st.write(f"Musim dengan jumlah sewa terbanyak: {highrent_season['season_day']}")
st.write(f"Jumlah sewa: {highrent_season['cnt_day']}")

# Seasonal Rental Chart
season_chart = alt.Chart(season_rent).mark_bar().encode(
    x='season_day',
    y='cnt_day'
).properties(
    title='Jumlah Sewa Berdasarkan Musim'
)
st.altair_chart(season_chart, use_container_width=True)

#pertanyaan2
st.header("Total Pengguna")
st.write(f"Total pengguna casual: {totaluserCasual}")
st.write(f"Total pengguna registered: {totaluserRegistered}")

user_chart = alt.Chart(user_data).mark_bar().encode(
    x='user_type',
    y='total_users'
).properties(
    title='Total Pengguna Casual dan Registered'
)
st.altair_chart(user_chart, use_container_width=True)

#pertanyaan3
st.header("Perbedaan Jumlah Sewa Sepeda Weekday dan Weekend")
st.write(workday_rental)

# Workday Rental Chart
workday_chart = alt.Chart(workday_rental).mark_bar().encode(
    x='workingday_hour',
    y='cnt_hour'
).properties(
    title='Jumlah Sewa Weekday vs Weekend'
)
st.altair_chart(workday_chart, use_container_width=True)
