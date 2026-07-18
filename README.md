# Analisis Regresi Linear Berganda untuk Efisiensi Bahan Bakar (Auto MPG)

Laporan proyek ini berfokus pada pemodelan statistik pengaruh karakteristik fisik dan mekanis kendaraan terhadap konsumsi bahan bakar (diukur dalam Mil Per Galon / **MPG**). Analisis ini bertujuan membantu perancang otomotif mengoptimalkan desain kendaraan demi memenuhi standar efisiensi bahan bakar yang ketat.

---

## 🎯 Pembahasan Bisnis & Pernyataan Masalah

Dalam industri otomotif modern, regulasi emisi karbon yang ketat dan tuntutan pasar akan kendaraan hemat energi mengharuskan produsen untuk meminimalkan konsumsi bahan bakar. Bagi tim rekayasa (engineering), tantangannya adalah memahami bagaimana keputusan desain fisik—seperti meningkatkan bobot kendaraan demi keamanan atau menaikkan tenaga kuda (*horsepower*) untuk performa—berdampak secara kuantitatif pada efisiensi bahan bakar.

Melalui pendekatan berbasis data ini, kami menggunakan **Regresi Linear Berganda (Multiple Linear Regression)** dengan metode *Forward Stepwise Selection* untuk:
1. Mengidentifikasi variabel spesifikasi mesin dan fisik kendaraan yang secara signifikan memengaruhi nilai MPG.
2. Membangun model matematika prediktif sebagai alat simulasi pra-prototipe.
3. Memberikan rekomendasi berbasis angka untuk memandu desain kendaraan masa depan.

---

## 📌 Ringkasan Eksekutif (Pembacaan 30 Detik)

*   **Metodologi**: Model regresi dibangun menggunakan seleksi maju bertahap (*forward stepwise selection*) berbasis signifikansi Uji-F. Dari 5 kandidat prediktor, semuanya terpilih karena memberikan kontribusi signifikansi yang kuat.
*   **Kesesuaian Model**: Model akhir menjelaskan **70,77%** variabilitas MPG ($R^2 = 0,7077$, $\text{Adjusted } R^2 = 0,7039$) dengan signifikansi keseluruhan model yang sangat tinggi (F-statistic = 186,91).
*   **Faktor Dampak**: Semua variabel memiliki koefisien negatif, artinya peningkatan pada spesifikasi mesin atau bobot akan menurunkan nilai MPG (memperboros bahan bakar).
*   **Pendorong Utama**: Berdasarkan koefisien terstandarisasi, **bobot kendaraan (weight)** memiliki dampak negatif terkuat (**-0,5645**), disusul oleh **tenaga kuda (horsepower)** (**-0,2232**).

---

## 📐 Rumus Persamaan Regresi

Berdasarkan hasil pemodelan OLS (Ordinary Least Squares) pada dataset Auto MPG, rumus matematika estimasi efisiensi bahan bakar adalah sebagai berikut:

$$\text{MPG} = 46,2643 - 0,0052(\text{weight}) - 0,0453(\text{horsepower}) - 0,3979(\text{cylinders}) - 0,0291(\text{acceleration}) - 0,0001(\text{displacement})$$

### Detail Variabel:
*   $\text{MPG}$: Efisiensi konsumsi bahan bakar (Mil Per Galon)
*   $\text{weight}$: Bobot total kendaraan (dalam lbs)
*   $\text{horsepower}$: Tenaga kuda mesin
*   $\text{cylinders}$: Jumlah silinder mesin
*   $\text{acceleration}$: Waktu akselerasi (detik dari 0 ke 60 mph)
*   $\text{displacement}$: Kapasitas mesin (inci kubik)

---

## 📊 Tabel Metrik Evaluasi & Asumsi Regresi

Untuk memastikan validitas statistik dari model regresi linear berganda, dilakukan serangkaian pengujian asumsi klasik:

### 1. Uji Multikolinearitas (VIF)
Independensi antar prediktor diuji menggunakan *Variance Inflation Factor* (VIF):

| Fitur / Variabel | Nilai VIF | Status Multikolinearitas | Interpretasi |
| :--- | :---: | :--- | :--- |
| **displacement** | **19,54** | Kolinearitas Ekstrem (VIF > 10) | Terjadi redundansi informasi yang sangat kuat dengan silinder/bobot. |
| **cylinders** | **10,63** | Kolinearitas Ekstrem (VIF > 10) | Redundansi tinggi karena jumlah silinder sebanding dengan displacement. |
| **weight** | **10,43** | Kolinearitas Ekstrem (VIF > 10) | Menunjukkan keterkaitan fisik yang kuat dengan dimensi mesin. |
| **horsepower** | **8,92** | Kolinearitas Tinggi (Mendekati 10) | Tenaga kuda sangat terikat dengan kapasitas dan silinder mesin. |
| **acceleration** | **2,61** | Kolinearitas Rendah (Aman) | Tidak menunjukkan masalah multikolinearitas yang berarti. |

> [!WARNING]
> **Catatan Teknis**: Adanya nilai VIF > 10 menunjukkan multikolinearitas yang parah di antara variabel mesin (`displacement`, `cylinders`, `weight`). Meskipun kemampuan prediksi model secara keseluruhan ($R^2$) tetap tinggi dan valid, estimasi koefisien regresi individu ($\beta$) dapat menjadi tidak stabil (sensitif terhadap perubahan kecil pada data).

### 2. Uji Normalitas Residual (Shapiro-Wilk)
Distribusi sisaan (residual) diuji untuk memvalidasi interval kepercayaan:
*   **Statistik W Shapiro-Wilk**: `0,9718`
*   **p-value**: $6,72 \times 10^{-7}$
*   **Analisis**: Karena p-value jauh di bawah tingkat signifikansi $\alpha = 0,05$, kami menolak hipotesis nol. Residual **tidak berdistribusi normal secara sempurna**. Hal ini menunjukkan adanya pola non-linear pada rentang data ekstrem yang belum tertangkap oleh model linear sederhana.

---

## 📈 Grafik Visualisasi Hasil Pemodelan

Seluruh grafik dihasilkan dengan resolusi tinggi (300 DPI) untuk memastikan ketajaman visual dalam laporan bisnis:

### 1. Korelasi Antar Variabel
Heatmap korelasi menunjukkan korelasi negatif yang sangat kuat antara MPG dengan bobot kendaraan (**-0,83**), kapasitas mesin (**-0,81**), dan tenaga kuda (**-0,78**).
![Heatmap Korelasi](images/correlation_heatmap.png)

### 2. Hubungan Bobot Kendaraan vs. Efisiensi (MPG)
Garis tren regresi memperlihatkan penurunan tajam nilai MPG seiring bertambahnya bobot kendaraan secara linear.
![MPG vs Weight](images/mpg_vs_weight.png)

### 3. Nilai Aktual vs. Prediksi MPG
Visualisasi kedekatan nilai prediksi model dengan nilai aktual di sepanjang garis ideal $y=x$. Sebagian besar titik mengelompok dengan baik di sekitar garis referensi.
![Aktual vs Prediksi](images/actual_vs_predicted.png)

### 4. Analisis Sebaran Sisaan (Residuals Plot)
Sebaran residual di sekitar garis nol menunjukkan homoskedastisitas yang relatif baik pada sebagian besar rentang prediksi, meskipun terdapat deviasi kecil di ujung kanan.
![Grafik Residual](images/residuals_plot.png)

---

## 💡 Rekomendasi Bisnis & Rekayasa Otomotif

Berdasarkan hasil analisis kuantitatif di atas, kami merumuskan rekomendasi praktis berikut bagi tim pengembangan produk:

1.  **Prioritaskan Pengurangan Bobot (Weight Reduction)**:
    *   *Temuan*: Bobot kendaraan adalah faktor penurun efisiensi terbesar (koefisien standar **-0,5645**).
    *   *Tindakan*: Rekayasa bodi kendaraan harus fokus pada substitusi material ke alternatif yang lebih ringan (seperti aluminium berkekuatan tinggi, baja boron, atau serat karbon) tanpa mengorbankan standar keselamatan tabrakan.
2.  **Optimasi Konfigurasi Mesin (Downsizing & Turbocharging)**:
    *   *Temuan*: Tenaga kuda (*horsepower*) memiliki dampak negatif terbesar kedua (**-0,2232**), dan kapasitas mesin (`displacement`) berlebihan bersifat redundan secara statistik.
    *   *Tindakan*: Beralihlah dari mesin naturally-aspirated berkapasitas besar (misalnya V8 atau V6 silinder banyak) ke mesin 3 atau 4 silinder yang didukung turbocharger (*downsized turbocharged engines*), atau integrasikan sistem hibrida (hybrid drivetrain) untuk mempertahankan tenaga tanpa memperboros bahan bakar.
3.  **Simulasi Desain Menggunakan Rumus Regresi**:
    *   *Temuan*: Persamaan regresi berhasil menangkap 70.77% variabilitas data riil.
    *   *Tindakan*: Manfaatkan rumus matematika regresi sebagai alat kalkulator cepat pada tahap awal perencanaan produk (*pre-prototype*) untuk mengevaluasi *trade-off* antara target akselerasi, bobot target, daya mesin, dan dampaknya terhadap efisiensi bahan bakar rata-rata sebelum memproduksi prototipe fisik yang mahal.

---

## 📂 Struktur Berkas Proyek

Proyek ini terorganisasi dengan struktur bersih sebagai berikut:
```text
├── data/
│   ├── auto_mpg_raw.csv     # Dataset mentah asli hasil konversi dari Excel
│   └── auto_mpg_clean.csv   # Dataset bersih setelah penanganan missing values (NaN)
├── images/
│   ├── actual_vs_predicted.png # Plot nilai aktual vs prediksi
│   ├── correlation_heatmap.png # Heatmap korelasi antar fitur
│   ├── mpg_vs_weight.png       # Scatter plot bobot vs MPG dengan garis regresi
│   └── residuals_plot.png      # Plot residual model
├── references/
│   ├── TE000322.pdf            # PDF referensi utama laporan tugas
│   └── slide.pdf               # PDF referensi bahan presentasi
├── notebook.ipynb  # Mesin pemrosesan: HANYA berisi impor, olah data, perhitungan statistik, dan ekspor grafik
└── README.md       # Laporan utama (dokumen ini)
```
