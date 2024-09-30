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

## Setup Environment - Anaconda
```
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

## Setup Environment - Shell/Terminal
```
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Run streamlit app
```
streamlit run dashboard.py
```

## Kegunaan
```
Proyek ini berguna untuk memperlihatkan kualitas udara di Gucheng dan Huairou pada tahun 2013 - 2016. 
Data dapat digunakan untuk memproyeksikan kualitas udara di tahun-tahun yang akan datang.
Data juga dapat digunakan untuk mengevaluasi dan mengoreksi serta melakukan langkah-langkah tindak lanjut untuk memperbaiki kualitas udara.
```
