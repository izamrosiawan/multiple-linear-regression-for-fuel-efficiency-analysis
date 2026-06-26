# Analisis Regresi Linier Berganda untuk Efisiensi Bahan Bakar (Auto MPG)

Proyek ini bertujuan untuk menganalisis faktor-faktor yang memengaruhi efisiensi konsumsi bahan bakar pada mobil (diukur dalam mil per galon / **MPG**) menggunakan **Model Regresi Linier Berganda**. Pemilihan fitur dilakukan secara sistematis melalui metode *Stepwise Regression* (khususnya *Forward Selection* berbasis signifikansi Uji F).

---

## 📂 Struktur Proyek

Berikut adalah struktur berkas di dalam repositori ini:

*   📄 `Auto_MPG.xlsx` - Dataset spesifikasi kendaraan (seperti bobot, tenaga kuda, silinder, akselerasi) beserta nilai efisiensi bahan bakar (MPG).
*   📄 `TE000322.pdf` - Dokumen penjelasan tugas atau laporan analisis regresi.
*   📓 `main.ipynb` - Jupyter Notebook berisi implementasi analisis korelasi, permodelan regresi dengan seleksi maju (*forward selection*), interpretasi koefisien, pengujian statistik, serta analisis akhir.

---

## 📈 Metodologi Analisis

1.  **Analisis Korelasi**: Menghitung matriks korelasi Pearson antara variabel target (`MPG`) dengan berbagai fitur prediktor untuk melihat kekuatan hubungan linier awal.
2.  **Stepwise Regression (Forward Selection)**: 
    *   Membangun model secara bertahap dengan memasukkan variabel yang memiliki kontribusi paling signifikan berdasarkan nilai signifikansi statistik (Uji F).
    *   Mengevaluasi nilai signifikansi ($p$-value) untuk memastikan hanya prediktor yang valid secara statistik yang masuk ke dalam model regresi akhir.
3.  **Interpretasi Koefisien**: Menganalisis nilai koefisien regresi ($\beta$) untuk memahami bagaimana pengaruh perubahan satu satuan nilai prediktor terhadap perubahan nilai MPG kendaraan.
4.  **Uji Statistik & Evaluasi Model**:
    *   Menganalisis koefisien determinasi ($R^2$ & *Adjusted* $R^2$) untuk mengukur seberapa besar variabilitas data MPG yang dapat dijelaskan oleh model.
    *   Menguji kecocokan model secara keseluruhan (*Goodness of Fit*) melalui Uji F.

