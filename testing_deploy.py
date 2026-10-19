from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Memuat model yang telah disimpan
joblib_model = joblib.load('gbr_model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    # Mengambil data dari request JSON
    req_data = request.get_json(force=True)
    
    # Mengubah data ke DataFrame agar sesuai format model
    input_data = pd.DataFrame(req_data['data'])
    
    # Melakukan prediksi menggunakan model
    prediction = joblib_model.predict(input_data)
    
    # Mengembalikan hasil prediksi sebagai JSON
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True, port=8080)