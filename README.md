# Multiple Linear Regression for Automotive Fuel Efficiency Analysis (Auto MPG)

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Regression-orange.svg)](https://scikit-learn.org/)
[![Statsmodels](https://img.shields.io/badge/Statsmodels-Econometrics-green.svg)](https://www.statsmodels.org/)
[![Domain](https://img.shields.io/badge/Domain-Automotive%20Analytics-blue.svg)](#)
[![Tests](https://img.shields.io/badge/Tests-Pytest%20Passing-brightgreen.svg)](#)

Repositori ini menyajikan analisis ekonometrika dan regresi linear berganda (*Multiple Linear Regression*) untuk membedah dan memprediksi faktor-faktor teknis yang mempengaruhi efisiensi konsumsi bahan bakar kendaraan (*Miles Per Gallon / MPG*). Analisis ini mencakup pengujian asumsi klasik Gauss-Markov (Multikolinearitas VIF, Heteroskedastisitas, dan Normalitas Residual).

---

## 1. Pembahasan Bisnis & Konteks Industri Otomotif

Efisiensi bahan bakar merupakan indikator utama dalam perancangan kendaraan dan kepatuhan terhadap standar emisi global (*Corporate Average Fuel Economy / CAFE*). Produsen otomotif perlu memahami *trade-off* teknis antara:
1. **Bobot Kendaraan vs Efisiensi**: Pengaruh peningkatan bobot bodi kendaraan (*Vehicle Weight*) terhadap pemborosan konsumsi energi.
2. **Kapasitas Mesin & Tenaga Kuda**: Pengaruh volume silinder (*Displacement*) dan *Horsepower* terhadap *fuel economy*.
3. **Optimasi Desain Rancang Bangun**: Menemukan rasio kompromi optimal untuk mencapai target MPG tanpa mengorbankan performa akselerasi.

---

## 2. Struktur Proyek

```
├── .gitignore          # Konfigurasi pengabaian cache Git
├── data/               # Dataset kendaraan mentah & bersih (CSV)
├── images/             # Visualisasi plot komputasi 300 DPI
│   ├── correlation_heatmap.png
│   ├── mpg_vs_weight.png
│   ├── actual_vs_predicted.png
│   └── residuals_plot.png
├── src/                # Modular Python model engine (FuelEfficiencyModel)
├── tests/              # Automated unit tests (Pytest)
├── notebook.ipynb      # Mesin pemrosesan: Pembersihan data, OLS, uji asumsi klasik, dan evaluasi
├── requirements.txt    # Pinned stable dependencies
└── README.md           # Laporan utama: Pembahasan bisnis, rumus, tabel metrik, dan visualisasi
```

---

## 3. Metodologi & Formulasi Regresi Berganda

Pengolahan data pada `notebook.ipynb` dan `src/fuel_model.py` menerapkan spesifikasi model regresi OLS (*Ordinary Least Squares*):

### A. Persamaan Regresi Linear
$$\text{MPG}_i = \beta_0 + \beta_1 \text{Cylinders}_i + \beta_2 \text{Displacement}_i + \beta_3 \text{Horsepower}_i + \beta_4 \text{Weight}_i + \beta_5 \text{Acceleration}_i + \epsilon_i$$

### B. Variance Inflation Factor (Uji Multikolinearitas)
Mengukur tingkat inflasi varians koefisien akibat korelasi antar variabel independen (ambang batas aman $\text{VIF} < 10$):

$$\text{VIF}_j = \frac{1}{1 - R_j^2}$$

### C. Koefisien Determinasi ($R^2$ & Adjusted $R^2$)
Proporsi varians efisiensi bahan bakar yang mampu dijelaskan oleh model:

$$R^2 = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}$$

---

## 4. Hasil Kuantitatif & Pembahasan Visualisasi

### A. Matriks Korelasi & Korelasi Bobot vs MPG
Korelasi linier antar variabel teknis mesin kendaraan.

![Matriks Korelasi](images/correlation_heatmap.png)
![MPG vs Weight](images/mpg_vs_weight.png)

*   **Pembahasan**: Bobot kendaraan (*Weight*) memiliki korelasi negatif paling kuat dengan efisiensi bahan bakar (**$r = -0.83$**), diikuti oleh *Displacement ($r = -0.80$)* dan *Horsepower ($r = -0.78$)*.

### B. Evaluasi Model (Actual vs Predicted & Residuals)
Pemeriksaan akurasi prediksi dan pemenuhan asumsi homoskedastisitas residual.

![Actual vs Predicted](images/actual_vs_predicted.png)
![Residuals Plot](images/residuals_plot.png)

*   **Pembahasan**: Model regresi menghasilkan nilai **$R^2 = 0.818$** (mampu menjelaskan 81,8% varians efisiensi MPG). Plot residual menunjukkan sebaran acak di sekitar sumbu nol, membuktikan tidak adanya pola heteroskedastisitas yang parah.

---

## 5. Implementasi Modular & Pengujian Otomatis

Modul regresi linear tersedia di `src/fuel_model.py`:

```python
from src.fuel_model import FuelEfficiencyModel
import pandas as pd

model = FuelEfficiencyModel()
# Fit dan inferensi terstandarisasi
```

Jalankan automated test:
```bash
pytest tests/
```

---

## 6. Rekomendasi Rekayasa Otomotif

1. **Prioritas *Lightweighting* Material**: Pengurangan bobot kendaraan sebesar 500 lbs (~226 kg) terbukti meningkatkan efisiensi hingga 3-4 MPG, menjadikannya prioritas rekayasa utama melalui penggunaan paduan aluminium dan komposit serat karbon.
2. **Penggunaan Turbocharging Ukuran Kecil (*Downsizing*)**: Mengganti mesin 8 silinder berkapasitas besar dengan mesin 4 silinder ber-turbocharger terbukti mempertahankan tenaga kuda sekaligus memangkas konsumsi bahan bakar secara signifikan.
3. **Penyelarasan Rasio Transmisi**: Optimasi rasio gigi transmisi untuk menjaga RPM mesin tetap rendah pada kecepatan jelajah jalan tol (*highway cruise*).

---

## 7. Cara Menjalankan

1. **Pasang Dependensi**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Eksekusi Notebook**:
   ```bash
   jupyter notebook notebook.ipynb
   ```

---
*Fuel Efficiency Multiple Linear Regression Project.*
