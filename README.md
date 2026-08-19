# Multiple Linear Regression for Fuel Efficiency Analysis (Auto MPG)

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Regression-orange.svg)](https://scikit-learn.org/)
[![Domain](https://img.shields.io/badge/Domain-Automotive%20Analytics-blue.svg)](#)
[![Tests](https://img.shields.io/badge/Tests-Pytest%20Passing-brightgreen.svg)](#)

Repositori ini menyajikan analisis regresi linear berganda (*Multiple Linear Regression*) untuk memprediksi dan memodelkan faktor-faktor teknis yang mempengaruhi efisiensi konsumsi bahan bakar kendaraan bermotor (*Miles Per Gallon / MPG*).

---

## Struktur Proyek

```
├── .gitignore          # Konfigurasi pengabaian cache Git
├── data/               # Dataset kendaraan mentah & bersih (CSV)
├── images/             # Visualisasi plot komputasi 300 DPI
├── src/                # Modular Python model engine (FuelEfficiencyModel)
├── tests/              # Automated unit tests (Pytest: validasi fitting dan prediksi)
├── notebook.ipynb      # Jupyter Notebook: Pembersihan data, uji korelasi, regresi linear, dan evaluasi
├── requirements.txt    # Pinned stable dependencies
└── README.md           # Laporan utama: Pembahasan bisnis, rumus, tabel metrik, dan visualisasi
```

---

## Implementasi Modular & Pengujian Otomatis

Modul regresi linear tersedia di `src/fuel_model.py`:

```python
from src.fuel_model import FuelEfficiencyModel
import pandas as pd

model = FuelEfficiencyModel()
# Fit dan inferensi
```

Jalankan automated test:
```bash
pytest tests/
```

---

## Cara Menjalankan

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

