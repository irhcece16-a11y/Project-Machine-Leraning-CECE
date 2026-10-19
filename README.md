# Project Machine Learning - Deployment & Modeling

Repositori ini berisi proyek pembelajaran mesin (Machine Learning) untuk regresi menggunakan model Gradient Boosting Regressor, lengkap dengan skrip deployment menggunakan **Flask** dan pengujian melalui **Jupyter Notebook**.

## Struktur File dalam Repositori
* `testing_deploy.py`: Berisi skrip backend server Flask untuk menjalankan API model *machine learning*.
* `tugasml.ipynb`: Jupyter Notebook utama untuk pengolahan data, pelatihan model, dan pengujian API menggunakan library `requests`.
* `gbr_model.joblib` & `gbr_model.pkl`: File model hasil pelatihan (*trained model*) yang siap digunakan untuk prediksi.
* `dataset_regresi_lokal.csv`, `train.csv`, `test.csv`: Berkas kumpulan data (*dataset*) yang digunakan.

## Cara Menjalankan Proyek
1. Pastikan library yang dibutuhkan sudah terinstal (`flask`, `joblib`, `scikit-learn`, `pandas`, `requests`).
2. Jalankan server Flask terlebih dahulu melalui terminal:
   ```bash
   python testing_deploy.py
