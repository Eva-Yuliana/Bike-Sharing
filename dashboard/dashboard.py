import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Konfigurasi Dashboard
st.set_page_config(page_title="🚲 Bike Sharing Dashboard", layout="wide")
st.title("📊 Bike Sharing Dashboard")

@st.cache_data
def load_data():
    file_path = "data/day.csv"
    data = pd.read_csv(file_path)
    data["dteday"] = pd.to_datetime(data["dteday"])
    return data

df = load_data()

# Sidebar untuk Filter
st.sidebar.header("🔎 Filter Data")
season_mapping = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
df["season_name"] = df["season"].map(season_mapping)
selected_season = st.sidebar.multiselect("🌤 Pilih Musim", options=df["season_name"].unique(), default=df["season_name"].unique())

selected_month = st.sidebar.slider("📆 Pilih Bulan", min_value=1, max_value=12, value=(1, 12))

filtered_df = df[(df["season_name"].isin(selected_season)) & df["mnth"].between(*selected_month)]

# Visualisasi 1: Faktor yang Mempengaruhi Penyewaan Sepeda
st.subheader("📈 Korelasi Faktor yang Mempengaruhi Penyewaan Sepeda")
numeric_features = filtered_df[["cnt", "temp", "hum", "windspeed"]]
correlation_values = numeric_features.corr()["cnt"].drop("cnt").sort_values()
fig, ax = plt.subplots(figsize=(8, 5))
correlation_values.plot(kind='barh', color='blue', ax=ax)
plt.xlabel("Korelasi dengan Penyewaan Sepeda")
st.pyplot(fig)

# Visualisasi 2: Tren Penyewaan Sepeda per Jam
st.subheader("⏰ Tren Penggunaan Sepeda per Jam")
hour_df = pd.read_csv("data/hour.csv")
avg_hourly_usage = hour_df.groupby("hr")["cnt"].mean().reset_index()
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(data=avg_hourly_usage, x="hr", y="cnt", color='red', ax=ax)
plt.xlabel("Jam")
plt.ylabel("Rata-rata Penyewaan Sepeda")
st.pyplot(fig)

# Visualisasi 3: Pengaruh Cuaca terhadap Penyewaan
st.subheader("🌦 Penyewaan Sepeda Berdasarkan Cuaca")
weather_mapping = {1: "Cerah", 2: "Mendung", 3: "Hujan", 4: "Cuaca Ekstrem"}
filtered_df["weather_name"] = filtered_df["weathersit"].map(weather_mapping)
weather_avg = filtered_df.groupby("weather_name")["cnt"].mean().reset_index()
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(data=weather_avg, x="weather_name", y="cnt", palette="Blues", ax=ax)
st.pyplot(fig)

# Visualisasi 4: Distribusi Penyewaan Sepeda
st.subheader("📊 Distribusi Penyewaan Sepeda")
fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(filtered_df["cnt"], bins=30, kde=True, color="purple", ax=ax)
st.pyplot(fig)

st.sidebar.markdown("📌 **Gunakan filter untuk menyesuaikan tampilan dashboard!**")
