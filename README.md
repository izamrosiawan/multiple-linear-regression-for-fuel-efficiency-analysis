# Multiple Linear Regression for Fuel Efficiency Analysis (Auto MPG)

[English](#english) | [Bahasa Indonesia](#bahasa-indonesia)

---

<a name="english"></a>
## 🇬🇧 English Version

### 🎯 Business Problem Statement
Regulatory standards and carbon-reduction targets require automotive designers to mathematically model how weight and engine specs affect fuel economy. This project uses multiple linear regression and statistical validation to identify key engineering variables that drive vehicle fuel efficiency.

---

### 📌 Executive Summary (30-Second Read)
* **Objective**: Developed a Multiple Linear Regression model with forward stepwise selection to analyze the physical and mechanical factors affecting vehicle fuel efficiency (measured in Miles Per Gallon / **MPG**).
* **Key Findings**:
  - **Selected Predictors**: Stepwise forward selection (using F-test significance) identified 5 critical variables: **weight**, **horsepower**, **cylinders**, **acceleration**, and **displacement**.
  - **Model Fit**: The final regression model explains **70.77%** of the variance in MPG ($R^2$ = 0.7077, Adjusted $R^2$ = 0.7039) with a highly significant overall fit (F-statistic = 186.91).
  - **Regression Equation**:
    $$\text{MPG} = 46.2643 - 0.0052(\text{weight}) - 0.0453(\text{horsepower}) - 0.3979(\text{cylinders}) - 0.0291(\text{acceleration}) - 0.0001(\text{displacement})$$
  - **Negative Drivers**: All variables negatively affect MPG. Standardized coefficients reveal that **weight** has the strongest negative impact (**-0.5645**), followed by **horsepower** (**-0.2232**).
* **Actionable Recommendations**:
  - **Prioritize Lightweight Materials**: Since vehicle weight has the strongest negative impact on MPG (standardized coefficient of -0.5645), automotive engineers should prioritize lightweight materials (e.g., aluminum, carbon fiber) to boost fuel efficiency.
  - **Optimize Engine Configuration**: Restructuring engine horsepower and cylinder count can yield significant savings. Because horsepower has the second strongest negative impact (-0.2232), using smaller turbocharged engines or hybrid drivetrains can maintain performance without sacrificing MPG.
  - **Perform Pre-Prototype Simulations**: Use the regression formula as a mathematical model to simulate the trade-off between vehicle performance (acceleration and horsepower) and fuel economy prior to physical manufacturing.

---

### 🛡️ Data Quality & Assumptions
* **Missing Values**: Handled missing values (specifically in the `horsepower` column, representing <1.5% of total dataset rows) by omitting those rows, ensuring no imputed data biased the correlation coefficients.
* **Outlier Treatment**: Retained extreme values in car engine specifications since they represent heavy-duty commercial or high-performance vehicles, reflecting actual market variability.
* **Assumptions**: Assumed that the relationship between predictors and MPG is linear, that residuals are homoscedastic, and that multicollinearity can be diagnosed using VIF.

---

### 🔍 Regression Assumptions Testing

#### 1. Multicollinearity (VIF)
To check the assumption of independence among predictors, we calculated the Variance Inflation Factor (VIF) for the 5 selected variables:

| Feature | VIF | Multicollinearity Status |
| :--- | :---: | :--- |
| **displacement** | **19.54** | Severe Multicollinearity (VIF > 10) |
| **cylinders** | **10.63** | Severe Multicollinearity (VIF > 10) |
| **weight** | **10.43** | Severe Multicollinearity (VIF > 10) |
| **horsepower** | **8.92** | High Collinearity (Approaching 10) |
| **acceleration** | **2.61** | Low Collinearity (Within Safe Limits) |

* **Analysis**: The high VIF values indicate strong collinear relationships among engine displacement, cylinder count, and overall vehicle weight. While the overall model explains 70.77% of the variance, individual coefficient estimates ($\beta$) may be unstable.

#### 2. Residual Normality (Shapiro-Wilk)
We evaluated the normality of regression residuals to validate model inference:
* **Shapiro-Wilk W-statistic**: **0.9718**
* **p-value**: **$6.72 \times 10^{-7}$**
* **Analysis**: Since the p-value is extremely small (less than 0.05), we reject the null hypothesis of residual normality. The residuals are not normally distributed, suggesting that a non-linear model (e.g. polynomial regression or log-transformation) might better fit the extreme ranges of the dataset.

---

### 📊 Key Insights & Visualizations

#### 1. Correlation Heatmap
MPG shows a strong negative linear correlation with vehicle weight (**-0.83**), displacement (**-0.81**), and horsepower (**-0.78**), indicating that heavier and more powerful vehicles consume significantly more fuel.
![Correlation Heatmap](images/correlation_heatmap.png)

#### 2. Vehicle Weight vs. Fuel Efficiency (MPG)
The scatter plot with the fitted regression line highlights the steep decline in fuel efficiency as vehicle weight increases.
![MPG vs Weight](images/mpg_vs_weight.png)

#### 3. Actual vs. Predicted MPG
The regression model displays strong predictive alignment with actual values, clustering closely along the ideal $y=x$ reference line.
![Actual vs Predicted](images/actual_vs_predicted.png)

#### 4. Residuals Plot
The residuals are evenly distributed around the horizontal line of zero, confirming that the regression assumptions (homoscedasticity) hold well across the predicted range.
![Residuals Plot](images/residuals_plot.png)

---

### ⚠️ Limitations & Next Steps
* **Limitations**: The model assumes a strictly linear structure and is susceptible to multicollinearity issues, which can destabilize individual regression coefficients.
* **Next Steps**:
  1. Apply regularization techniques (Ridge or Lasso Regression) to penalize and correct for multicollinearity.
  2. Test polynomial transformations on `weight` and `horsepower` to model non-linear relations.

---

### 🔄 Reproducibility
* **Environment**: Python 3.11.x (libraries: NumPy, Pandas, Matplotlib, Seaborn, openpyxl, statsmodels, SciPy).
* **Execution Sequence**:
  1. Store the dataset `Auto_MPG.xlsx` in the project root directory.
  2. Open and run all cells in [notebook.ipynb](notebook.ipynb) in sequential order.
* **Random Seeds**: The regression fits and step-wise selection do not utilize random sampling, but any data split evaluations can be locked with seed `random_state = 42`.

---

<a name="bahasa-indonesia"></a>
## 🇮🇩 Versi Bahasa Indonesia

### 🎯 Business Problem Statement
Standar regulasi dan target urusan emisi karbon mengharuskan perancang otomotif untuk memodelkan secara matematis bagaimana spesifikasi bobot dan mesin memengaruhi penghematan bahan bakar. Proyek ini menggunakan regresi linear berganda dan validasi statistik untuk mengidentifikasi variabel teknik utama yang mendorong efisiensi bahan bakar.

---

### 📌 Ringkasan Eksekutif (30 Detik Baca)
* **Tujuan**: Membangun model Regresi Linear Berganda dengan metode *Forward Stepwise Selection* untuk menganalisis faktor fisik dan mekanis yang memengaruhi efisiensi konsumsi bahan bakar mobil (diukur dalam Mil Per Galon / **MPG**).
* **Temuan Utama**:
  - **Prediktor Terpilih**: Seleksi maju bertahap berbasis signifikansi Uji-F memilih 5 variabel utama: **weight** (bobot), **horsepower** (tenaga kuda), **cylinders** (silinder), **acceleration** (akselerasi), dan **displacement** (kapasitas mesin).
  - **Kesesuaian Model**: Model regresi akhir mampu menjelaskan **70,77%** variabilitas MPG ($R^2$ = 0,7077, Adjusted $R^2$ = 0,7039) dengan signifikansi model keseluruhan yang sangat tinggi (F-statistic = 186,91).
  - **Persamaan Regresi**:
    $$\text{MPG} = 46,2643 - 0,0052(\text{weight}) - 0,0453(\text{horsepower}) - 0,3979(\text{cylinders}) - 0,0291(\text{acceleration}) - 0,0001(\text{displacement})$$
  - **Faktor Penurun Efisiensi**: Semua variabel berpengaruh negatif terhadap MPG. Koefisien standar menunjukkan bahwa **weight** memiliki dampak negatif terbesar (**-0,5645**), diikuti oleh **horsepower** (**-0,2232**).
* **Rekomendasi Rekayasa**:
  - **Prioritaskan Pengurangan Bobot**: Karena bobot kendaraan memiliki dampak negatif terkuat terhadap efisiensi bahan bakar (koefisien standar -0,5645), fokus utama desain kendaraan harus diarahkan pada material ringan (seperti aluminium atau serat karbon).
  - **Optimasi Konfigurasi Mesin**: Lakukan restrukturisasi daya mesin. Karena *horsepower* memiliki dampak negatif terkuat kedua (-0,2232), penggunaan mesin turbo berkapasitas lebih kecil atau sistem hibrida dapat menjaga performa tanpa menurunkan efisiensi.
  - **Simulasi Pra-Prototipe**: Gunakan formula persamaan regresi sebagai model simulasi matematika untuk menguji trade-off antara spesifikasi performa (akselerasi/tenaga) dan konsumsi bahan bakar sebelum masuk ke tahap produksi fisik.

---

### 🛡️ Kualitas Data & Asumsi
* **Missing Values**: Menangani data kosong (khususnya pada kolom `horsepower`, mencakup <1,5% baris dataset) dengan menghapus baris terkait untuk memastikan tidak ada data imputasi yang membiaskan koefisien korelasi.
* **Outliers**: Mempertahankan nilai ekstrem pada spesifikasi mesin mobil karena mewakili kendaraan niaga berat atau performa tinggi, mencerminkan variabilitas pasar yang sebenarnya.
* **Asumsi**: Mengasumsikan hubungan antara prediktor dan MPG bersifat linear, residual bersifat homoskedastis, dan multikolinearitas dapat didiagnosis menggunakan VIF.

---

### 🔍 Pengujian Asumsi Regresi

#### 1. Multikolinearitas (VIF)
Untuk mengecek asumsi independensi antar prediktor, kita menghitung Variance Inflation Factor (VIF) untuk 5 variabel terpilih:

| Fitur | VIF | Status Multikolinearitas |
| :--- | :---: | :--- |
| **displacement** | **19,54** | Multikolinearitas Ekstrem (VIF > 10) |
| **cylinders** | **10,63** | Multikolinearitas Ekstrem (VIF > 10) |
| **weight** | **10,43** | Multikolinearitas Ekstrem (VIF > 10) |
| **horsepower** | **8,92** | Kolinearitas Tinggi (Mendekati 10) |
| **acceleration** | **2,61** | Kolinearitas Rendah (Batas Aman) |

* **Analisis**: Nilai VIF yang tinggi menunjukkan hubungan kolinear yang sangat kuat antara kapasitas mesin, jumlah silinder, dan bobot total kendaraan. Meskipun model secara keseluruhan dapat menjelaskan 70,77% variansi, nilai estimasi koefisien individu ($\beta$) rentan tidak stabil.

#### 2. Normalitas Residual (Shapiro-Wilk)
Kami mengevaluasi kenormalan residual regresi untuk memvalidasi inferensi model:
* **Statistik Shapiro-Wilk W**: **0,9718**
* **p-value**: **$6,72 \times 10^{-7}$**
* **Analisis**: Karena p-value jauh lebih kecil dari 0,05, kita menolak hipotesis nok. Residual tidak berdistribusi normal, yang menunjukkan bahwa model non-linear (seperti regresi polinomial atau transformasi log) mungkin memberikan kecocokan yang lebih baik pada rentang ekstrem data.

---

### 📊 Wawasan Utama & Visualisasi

#### 1. Heatmap Korelasi
Variabel MPG memiliki korelasi negatif yang kuat dengan bobot kendaraan (**-0,83**), kapasitas mesin (**-0,81**), dan tenaga kuda (**-0,78**).
![Heatmap Korelasi](images/correlation_heatmap.png)

#### 2. Hubungan Bobot Kendaraan vs. Efisiensi (MPG)
Grafik sebar dengan garis regresi memperlihatkan penurunan tajam nilai MPG seiring bertambahnya bobot kendaraan.
![MPG vs Weight](images/mpg_vs_weight.png)

#### 3. Nilai Aktual vs. Prediksi MPG
Model regresi menunjukkan kesesuaian prediksi yang sangat baik, dengan titik data yang tersebar merapat di sepanjang garis referensi ideal $y=x$.
![Actual vs Predicted](images/actual_vs_predicted.png)

#### 4. Grafik Residual (Residuals Plot)
Penyebaran residual yang merata di sekitar garis nol menunjukkan bahwa asumsi regresi (homoskedastisitas) terpenuhi dengan baik.
![Residuals Plot](images/residuals_plot.png)

---

### ⚠️ Keterbatasan & Langkah Selanjutnya
* **Keterbatasan**: Model mengasumsikan hubungan yang murni linear dan rentan terhadap masalah multikolinearitas, yang dapat mengganggu stabilitas koefisien regresi individu.
* **Langkah Selanjutnya**:
  1. Terapkan teknik regularisasi (Ridge atau Lasso Regression) untuk mengoreksi multikolinearitas.
  2. Uji transformasi polinomial pada variabel `weight` dan `horsepower` untuk memodelkan hubungan non-linear.

---

### 🔄 Reproduksibilitas
* **Lingkungan**: Python 3.11.x (pustaka: NumPy, Pandas, Matplotlib, Seaborn, openpyxl, statsmodels, SciPy).
* **Urutan Eksekusi**:
  1. Simpan dataset `Auto_MPG.xlsx` di direktori utama proyek.
  2. Buka dan jalankan seluruh cell di [notebook.ipynb](notebook.ipynb) secara berurutan.
* **Random Seeds**: Pemodelan regresi OLS tidak menggunakan elemen acak, namun jika dilakukan split evaluasi, gunakan seed `random_state = 42` demi hasil konsisten.

---

## 📂 Struktur Berkas
*   📄 `Auto_MPG.xlsx` - Dataset spesifikasi kendaraan dan nilai efisiensi (MPG).
*   📄 `TE000322.pdf` - Dokumen penjelasan laporan tugas.
*   📓 `notebook.ipynb` - Jupyter Notebook berisi implementasi lengkap analisis korelasi, permodelan regresi, dan uji statistik.
*   📂 `images/` - Folder penyimpanan visualisasi grafik hasil ekspor.

---

## ⚙️ Persyaratan Sistem & Instalasi
Instal pustaka Python yang diperlukan:
```bash
pip install numpy pandas matplotlib seaborn openpyxl statsmodels scipy
```
Jalankan Jupyter Notebook:
```bash
jupyter notebook notebook.ipynb
```
