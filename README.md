# 🚲 Bike Sharing Dashboard

## 📌 Deskripsi
Dashboard interaktif ini dibuat menggunakan **Streamlit** untuk menganalisis pola penyewaan sepeda berdasarkan berbagai faktor seperti musim, cuaca, dan waktu dalam sehari.

## 🛠 Persyaratan
Pastikan Anda telah menginstal dependensi berikut sebelum menjalankan aplikasi:

```bash
pip install streamlit pandas seaborn matplotlib
```

## 📂 Struktur File
```
D:/submission/
│── data/
│   └── hour.csv  # Dataset yang digunakan
│── dashboard.py  # File utama untuk menjalankan dashboard
│── README.md     # Dokumentasi proyek ini
```

## ▶ Cara Menjalankan Dashboard
1. **Pastikan dataset tersedia** di direktori yang benar (`D:/submission/data/hour.csv`).
2. **Jalankan aplikasi dengan perintah berikut:**

   ```bash
   streamlit run dashboard/dashboard.py
   ```

3. **Dashboard akan terbuka di browser secara otomatis.**

## 🔎 Fitur Dashboard
✅ **Filter Interaktif**: Sesuaikan tampilan berdasarkan musim, jenis hari, dan bulan.  
✅ **Visualisasi Tren**:
   - Penyewaan sepeda per musim & cuaca
   - Tren penggunaan sepeda dalam sehari
   - Perbandingan penyewaan antara hari kerja & akhir pekan
   - Distribusi jumlah penyewaan sepeda
✅ **Korelasi Faktor Cuaca**: Analisis dampak suhu, kelembaban, dan kecepatan angin terhadap jumlah penyewaan sepeda.

## ❗ Troubleshooting
- Jika dataset tidak ditemukan, pastikan file `hour.csv` berada di direktori yang benar.
- Jika ada error terkait pustaka Python, coba jalankan ulang perintah **pip install** di atas.

## 📌 Catatan
Gunakan **sidebar** di dashboard untuk mengatur filter dan melihat hasil analisis dengan lebih jelas! 🚴‍♂️

