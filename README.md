# Proyek Analisis Data Air Quality ✨
## Overview
```
Proyek ini adalah tugas akhir dari modul Belajar Analisis Data dengan Python
Dalam proyek ini, analisis yang dilakukan adalah terhadap kualitas udara (Air Quality) dari 2 tempat di China yaitu Gucheng dan Huairou.
Faktor yang dilihat adalah temperature, rainfall, partikel PM2.5, partikel PM10, konsentrasi gas CO, SO2 dan NO2
```

## Pertanyaan Bisnis
```
- Bagaimana melihat pola kualitas udara dalam 1 tahun di 2 tempat?
- Bagaimana hubungan antara curah hujan dengan konsentrasi gas SO2 dan NO2 di beberapa tempat?
```

## Setup Environment - Library
```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

## Data Wrangling
### Gathering Data
```
Dari kumpulan folder dataset air quality, dipilih 2 dataset yaitu: Gucheng dan Huairou. 
Kedua file csv dataset tersebut lalu diupload ke Google Colab
```
### Assessing Data
```
Dilakukan evaluasi pada dataset dengan mencari data duplikat serta data NULL/NA
Didapatkan bahwa tidak ada data duplikat pada kedua dataset
Didapatkan data NULL pada semua kolom kecuali No, year, month, date, hour, dan station
```
### Cleaning Data
```
Dilakukan pengisian data pada data NA dengan angka 0
Pada konsentrasi CO, setelah asesmen lebih lanjut, ditemukan bahwa data max = 10000 adalah benar sehingga tidak dilakukan proses penyiangan.
```

## Exploratory Data Analysis
### Explor Pola Kualitas Udara di Tiap Tempat
```
Dilakukan analisis data untuk kualitas udara di Gucheng dan Huairou secara terpisah.
Dilihat dari temperature, rainfall, PM2.5, PM10, SO2, NO2, CO
```
### Menggabungkan kedua tabel
```
Jumlah data pada dataset Gucheng dan Huairou sama sehingga tabel digabung.
Analisis lanjutan pada tabel gabungan untuk suhu max dan rainfall max.
```

## Explanatory Data Analysis
### Pertanyaan 1
```
Membuat tampilan tabel untuk suhu (temperature) dan curah hujan (rainfall)
Membuat tampilan tabel untuk membandingkan level partikel PM2.5, PM10, SO2, NO2, dan CO di kedua stasiun Gucheng dan Huairou.
```
### Pertanyaan 2
```
Membuat heatmap korelasi antara suhu, rainfall, dan partikel udara
Ditemukan tidak adanya korelasi antara suhu dan rainfall
```

## Analisis Lanjutan
```
Menggunakan Geopandas (gpd), disajikan peta China dengan lokasi Gucheng dan Huairou serta heatmap korelasi antara suhu dan rainfall
```

## Kegunaan
```
Proyek ini berguna untuk memperlihatkan kualitas udara di Gucheng dan Huairou pada tahun 2013 - 2016. 
Data dapat digunakan untuk memproyeksikan kualitas udara di tahun-tahun yang akan datang.
Data juga dapat digunakan untuk mengevaluasi dan mengoreksi serta melakukan langkah-langkah tindak lanjut untuk memperbaiki kualitas udara.
```

# Membuat Dashboard
## Setup Environment - Anaconda
```
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

## Mempersiapkan dataframe
```
Membuat dataframe baru untuk mengelompokkan data temperature dan rainfall per tahun
Membuat dataframe baru untuk mengelompokkan data partikel udara per tahun
```

## Membuat komponen filter
```
Menggabungkan kolom year, month, day menjadi satu kolom berbasis datetime
Berdasarkan date, filter dibuat
```

## Visualisasi Data
```
Judul: Air Quality in Gucheng and Huairou
Subtitle: Yearly weather data (menampilkan suhu dan rainfall)
Subtitle: Average temperature by year and month (menampilkan rata2 suhu sepanjang tahun)
Subtitle: Yearly air quality data (menampilkan rata-rata dan max konsentrasi partikel udara)
Subtitle: Gas level over time (menampilkan perbandingan konsentrasi partikel udara)
```

## Run streamlit app
```
streamlit run dashboard.py
```


