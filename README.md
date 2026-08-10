# Analisis Regresi Linear Berganda untuk Efisiensi Bahan Bakar (Auto MPG)

Proyek ini menganalisis pengaruh karakteristik fisik dan mekanis kendaraan terhadap konsumsi bahan bakar (Mil Per Galon / **MPG**) menggunakan dataset Auto MPG. Analisis ini bertujuan memberikan estimasi kuantitatif untuk mendukung efisiensi desain kendaraan.

---

## Latar Belakang & Masalah Bisnis

Dalam industri otomotif, regulasi emisi dan efisiensi energi menuntut produsen meminimalkan konsumsi bahan bakar tanpa mengorbankan keamanan dan performa. Rekayasa fisik—seperti penambahan bobot kendaraan atau kapasitas mesin—memiliki efek langsung terhadap efisiensi bahan bakar.

Melalui pendekatan berbasis data, metode **Regresi Linear Berganda (Multiple Linear Regression)** dengan teknik *Forward Stepwise Selection* digunakan untuk:
1. Mengidentifikasi variabel spesifikasi mesin dan fisik kendaraan yang memengaruhi MPG secara signifikan.
2. Membangun persamaan prediktif matematika sebagai alat simulasi pra-prototipe.
3. Merumuskan rekomendasi teknis berbasis angka untuk perancangan kendaraan.

---

## Ringkasan Eksekutif

- **Metodologi**: Model regresi dibangun menggunakan seleksi maju bertahap (*forward stepwise selection*) berbasis signifikansi Uji-F. Dari 5 prediktor yang diuji, seluruhnya memberikan kontribusi signifikan terhadap model.
- **Kesesuaian Model**: Model akhir menjelaskan **70,77%** variabilitas nilai MPG ($R^2 = 0,7077$, $\text{Adjusted } R^2 = 0,7039$) dengan nilai F-statistic sebesar 186,91.
- **Faktor Utama**: Seluruh variabel memiliki koefisien negatif. Berdasarkan koefisien terstandarisasi, **bobot kendaraan (weight)** menjadi penurun efisiensi terbesar (**-0,5645**), diikuti oleh **tenaga kuda (horsepower)** (**-0,2232**).

---

## Persamaan Regresi Linear

Berdasarkan estimasi OLS (*Ordinary Least Squares*), persamaan matematika efisiensi bahan bakar dirumuskan sebagai berikut:

$$\text{MPG} = 46,2643 - 0,0052(\text{weight}) - 0,0453(\text{horsepower}) - 0,3979(\text{cylinders}) - 0,0291(\text{acceleration}) - 0,0001(\text{displacement})$$

### Variabel Prediktor:
- $\text{MPG}$: Konsumsi bahan bakar (Mil Per Galon)
- $\text{weight}$: Bobot total kendaraan (lbs)
- $\text{horsepower}$: Tenaga kuda mesin (HP)
- $\text{cylinders}$: Jumlah silinder mesin
- $\text{acceleration}$: Waktu akselerasi 0–60 mph (detik)
- $\text{displacement}$: Kapasitas mesin (inci kubik)

---

## Evaluasi Statistik & Pengujian Asumsi

### 1. Uji Multikolinearitas (VIF)
Tingkat independensi antar variabel diukur menggunakan *Variance Inflation Factor* (VIF):

| Fitur / Variabel | Nilai VIF | Status Multikolinearitas | Interpretasi |
| :--- | :---: | :--- | :--- |
| **displacement** | **19,54** | Kolinearitas Ekstrem (VIF > 10) | Redundansi tinggi dengan silinder dan bobot. |
| **cylinders** | **10,63** | Kolinearitas Ekstrem (VIF > 10) | Kolinearitas sebanding dengan kapasitas mesin. |
| **weight** | **10,43** | Kolinearitas Ekstrem (VIF > 10) | Terikat erat dengan dimensi fisik mesin. |
| **horsepower** | **8,92** | Kolinearitas Tinggi (Mendekati 10) | Terikat pada kapasitas dan jumlah silinder. |
| **acceleration** | **2,61** | Kolinearitas Rendah (Aman) | Tidak mengalami masalah multikolinearitas. |

**Catatan Evaluasi**: Nilai VIF > 10 pada variabel mesin (`displacement`, `cylinders`, `weight`) mengindikasikan adanya multikolinearitas antar prediktor. Meskipun estimasi $R^2$ model tetap valid, varians dari koefisien individu ($\beta$) menjadi lebih sensitif terhadap perubahan dataset.

### 2. Uji Normalitas Residual (Shapiro-Wilk)
- **Statistik W**: `0,9718`
- **p-value**: $6,72 \times 10^{-7}$
- **Analisis**: Dengan $p\text{-value} < 0,05$, hipotesis nol ditolak. Residual tidak berdistribusi normal sempurna, yang mengindikasikan adanya pola non-linear pada rentang nilai ekstrem.

---

## Visualisasi Hasil Pemodelan

### 1. Matrix Korelasi
Heatmap korelasi memperlihatkan hubungan negatif yang kuat antara MPG dengan bobot kendaraan (**-0,83**), kapasitas mesin (**-0,81**), dan tenaga kuda (**-0,78**).
![Heatmap Korelasi](images/correlation_heatmap.png)

### 2. Hubungan Bobot vs Efisiensi (MPG)
Scatter plot dan garis tren regresi menunjukkan penurunan MPG secara konstan seiring bertambahnya bobot kendaraan.
![MPG vs Weight](images/mpg_vs_weight.png)

### 3. Nilai Aktual vs Prediksi
Sebaran nilai prediksi model dibandingkan terhadap nilai aktual mengelompok di sekitar garis referensi $y=x$.
![Aktual vs Prediksi](images/actual_vs_predicted.png)

### 4. Plot Sebaran Residual
Plot residual menunjukkan pola homoskedastisitas yang cukup konsisten pada mayoritas rentang prediksi.
![Grafik Residual](images/residuals_plot.png)

---

## Rekomendasi Teknis Otomotif

1. **Pengurangan Bobot Kendaraan (*Lightweighting*)**:
   - Bobot kendaraan merupakan variabel paling dominan dalam menurunkan MPG (koefisien terstandarisasi **-0,5645**). Penggunaan bahan komposit ringan (seperti aluminium atau baja berkekuatan tinggi) menjadi strategi utama peningkatan efisiensi.
2. **Optimasi Mesin & Downsizing**:
   - Mengingat tingginya redundansi pada variabel kapasitas mesin dan silinder, perancangan mesin disarankan beralih ke konfigurasi *downsized turbocharged* (silinder lebih kecil dengan bantuan turbocharger) untuk menjaga efisiensi tanpa mengorbankan akselerasi.
3. **Simulasi Pra-Prototipe**:
   - Persamaan regresi ini dapat dimanfaatkan sebagai model kalkulator awal (*pre-prototype*) untuk mengevaluasi estimasi MPG berdasarkan bobot dan daya mesin sebelum pembuatan prototipe fisik.

---

## Struktur Direktori
```text
├── data/
│   ├── auto_mpg_raw.csv     # Dataset mentah
│   └── auto_mpg_clean.csv   # Dataset setelah imputasi data kosong
├── images/
│   ├── actual_vs_predicted.png
│   ├── correlation_heatmap.png
│   ├── mpg_vs_weight.png
│   └── residuals_plot.png
├── references/
│   ├── TE000322.pdf            # Berkas laporan tugas
│   └── slide.pdf               # Slide presentasi
├── notebook.ipynb  # Notebook pengolahan data dan pemodelan OLS
└── README.md       # Laporan utama
```
