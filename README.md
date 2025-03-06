# E-Commerce Dashboard 📊

Dashboard ini merupakan aplikasi interaktif berbasis **Streamlit** yang digunakan untuk menganalisis data e-commerce, termasuk harga produk, waktu pengiriman, dan metode pembayaran.

## 📌 Persyaratan
Pastikan Anda telah menginstal **Python 3.9+** dan memiliki paket yang diperlukan. Anda bisa menginstalnya menggunakan **pip** atau **conda**.

## 🛠️ Setup Lingkungan

### 1. Menggunakan Virtual Environment (Opsional)
Disarankan untuk menggunakan virtual environment agar dependensi lebih terorganisir.

#### Dengan `venv` (bawaan Python)
```sh
python -m venv venv
type venv/Scripts/activate (Windows)
source venv/bin/activate (Mac/Linux)
```

#### Dengan `conda`
```sh
conda create --name ecommerce_dashboard python=3.9
conda activate ecommerce_dashboard
```

### 2. Instalasi Dependensi
Pastikan semua dependensi terinstal dengan menjalankan perintah berikut:
```sh
pip install streamlit pandas seaborn matplotlib
```

### 3. Menjalankan Aplikasi
Pastikan Anda berada dalam direktori yang sama dengan `dashboard.py`, lalu jalankan:
```sh
streamlit run D:\submission\dashboard\dashboard.py

## 🗂️ Struktur Data
Pastikan Anda memiliki dataset yang diperlukan di dalam folder yang sesuai:
- `orders_dataset.csv`
- `order_items_dataset.csv`
- `products_dataset.csv`
- `order_payments_dataset.csv`

Jika file dataset berada di lokasi lain, sesuaikan path dalam file `dashboard.py`.

## 📢 Catatan
- Gunakan sidebar untuk memfilter data sesuai kebutuhan.
- Pastikan semua dataset tersedia agar visualisasi dapat berjalan dengan baik.

🎯 Selamat menganalisis! 🚀

