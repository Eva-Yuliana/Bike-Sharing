import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Konfigurasi Dashboard
st.set_page_config(page_title="🚲 Bike Sharing Dashboard", layout="wide")
st.title("📊 Bike Sharing Dashboard")

@st.cache_data
def load_data():
    data = pd.read_csv("data\hour.csv")  
    data["dteday"] = pd.to_datetime(data["dteday"])
    data["hour"] = data["hr"]  
    data["month"] = data["dteday"].dt.month  
    data["day_of_week"] = data["dteday"].dt.day_name()  
    return data

df = load_data()

st.sidebar.header("🔎 Filter Data")

# Filter Musim
season_mapping = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
df["season_name"] = df["season"].map(season_mapping)
selected_season = st.sidebar.multiselect("🌤 Pilih Musim", options=df["season_name"].unique(), default=df["season_name"].unique())

# Filter Hari Kerja vs Akhir Pekan
day_type_mapping = {0: "Akhir Pekan", 1: "Hari Kerja"}
df["day_type"] = df["workingday"].map(day_type_mapping)
selected_day_type = st.sidebar.radio("📅 Pilih Jenis Hari", options=df["day_type"].unique(), index=0)

# Filter Berdasarkan Bulan
selected_month = st.sidebar.slider("📆 Pilih Bulan", min_value=1, max_value=12, value=(1, 12))

filtered_df = df[
    (df["season_name"].isin(selected_season)) &
    (df["day_type"] == selected_day_type) &
    (df["month"] >= selected_month[0]) & (df["month"] <= selected_month[1])
]

col1, col2 = st.columns(2)

# **Pertanyaan 1: Faktor utama yang mempengaruhi penyewaan sepeda**
with col1:
    st.subheader("📈 Faktor yang Mempengaruhi Penyewaan Sepeda")

    correlation_matrix = filtered_df[["cnt", "temp", "hum", "windspeed"]].corr()
    
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
    st.pyplot(fig)

# **Pertanyaan 2: Tren penggunaan sepeda dalam sehari**
with col2:
    st.subheader("⏰ Tren Penggunaan Sepeda per Jam")

    avg_hourly_usage = filtered_df.groupby("hour")["cnt"].mean().reset_index()
    
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.lineplot(data=avg_hourly_usage, x="hour", y="cnt", marker="o", color="red")
    plt.xticks(range(0, 24))
    plt.xlabel("Jam")
    plt.ylabel("Rata-rata Penyewaan Sepeda")
    plt.title("Tren Penggunaan Sepeda dalam Sehari")
    plt.grid(True)
    st.pyplot(fig)

# **Visualisasi Penyewaan Sepeda Berdasarkan Cuaca**
st.subheader("🌦 Penyewaan Sepeda Berdasarkan Cuaca")
weather_mapping = {1: "Cerah", 2: "Mendung", 3: "Hujan", 4: "Cuaca Ekstrem"}
filtered_df["weather_name"] = filtered_df["weathersit"].map(weather_mapping)

weather_avg = filtered_df.groupby("weather_name")["cnt"].mean().reset_index()

fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(data=weather_avg, x="weather_name", y="cnt", palette="Blues", ax=ax)
plt.xlabel("Kondisi Cuaca")
plt.ylabel("Rata-rata Penyewaan Sepeda")
plt.title("Pengaruh Cuaca terhadap Penyewaan Sepeda")
st.pyplot(fig)

# **Perbandingan Penyewaan Sepeda antara Hari Kerja vs Akhir Pekan**
st.subheader("📅 Perbandingan Penyewaan Sepeda: Hari Kerja vs Akhir Pekan")
day_type_avg = df.groupby("day_type")["cnt"].mean().reset_index()

fig, ax = plt.subplots(figsize=(6, 4))
sns.barplot(data=day_type_avg, x="day_type", y="cnt", palette="coolwarm", ax=ax)
plt.xlabel("Jenis Hari")
plt.ylabel("Rata-rata Penyewaan Sepeda")
plt.title("Perbandingan Hari Kerja vs Akhir Pekan")
st.pyplot(fig)

# **Tren Penyewaan Sepeda Berdasarkan Hari dalam Seminggu**
st.subheader("📆 Tren Penyewaan Sepeda per Hari dalam Seminggu")
day_week_avg = df.groupby("day_of_week")["cnt"].mean().reset_index()

fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(data=day_week_avg, x="day_of_week", y="cnt", palette="viridis", ax=ax)
plt.xlabel("Hari dalam Seminggu")
plt.ylabel("Rata-rata Penyewaan Sepeda")
plt.title("Tren Penyewaan Sepeda per Hari dalam Seminggu")
st.pyplot(fig)

# **Distribusi Jumlah Penyewaan Sepeda**
st.subheader("📊 Distribusi Penyewaan Sepeda")
fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(filtered_df["cnt"], bins=30, kde=True, color="purple", ax=ax)
plt.xlabel("Jumlah Penyewaan Sepeda")
plt.ylabel("Frekuensi")
plt.title("Distribusi Penyewaan Sepeda")
st.pyplot(fig)

st.sidebar.markdown("📌 **Gunakan filter untuk menyesuaikan tampilan dashboard!**")
