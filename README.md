
# 💎 Diamond Price Prediction Model

This project uses machine learning to predict the price of a diamond based on its physical attributes and quality characteristics. By analyzing key features such as **carat, cut, color, clarity, depth, table, x, y, and z**, the model provides accurate price estimations to support better decision-making in the gemstone market.

---

## 📌 Project Overview

The diamond market is complex and highly value-driven. Accurate price prediction is essential for buyers, sellers, and traders to avoid losses and make data-informed decisions. This model is trained using a real-world dataset and advanced preprocessing techniques (including scaling and encoding) to deliver reliable results.

---

## 🚀 Features

- Predicts diamond prices using regression models
- Accepts user input via a simple web interface built with **Flask**
- Pre-trained using **scikit-learn pipelines** with `StandardScaler` and `OneHotEncoder`
- Deployable on any local or cloud-based server

---

## 📊 Input Features

| Feature  | Description                     |
|----------|---------------------------------|
| `carat`  | Weight of the diamond           |
| `cut`    | Quality of the cut (e.g. Ideal) |
| `color`  | Color grade (from D to J)       |
| `clarity`| Clarity grade (e.g. SI1, VS2)   |
| `depth`  | Total depth percentage          |
| `table`  | Width of top facet              |
| `x`      | Length in mm                    |
| `y`      | Width in mm                     |
| `z`      | Depth in mm                     |

---

## 🛠️ Tech Stack

- **Python 3.10**
- **Flask** – Web framework
- **Pandas** – Data handling
- **scikit-learn** – Model training and preprocessing
- **joblib** – Model serialization

---

## 💻 How to Run Locally

1. **Clone the repo**
   ```bash
   git clone https://github.com/KarthikSarika/Diamond-Price-Prediction-Model.git
   cd diamond-price-prediction
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**
   ```bash
   python app.py
   ```

5. Open your browser and go to `http://127.0.0.1:5000`

---

## 📁 Project Structure

```
.
├── app.py
├── Diamond-Price-Prediction-Model-Project-Final.pkl
├── requirements.txt
└── src
    ├── form.html
    └── result.html
```

---

## 📈 Output

After submitting the form, the model will return a predicted price of the diamond in USD.

---

## 🧠 Future Improvements

- Deploy to Render or Railway
- Add support for batch predictions via CSV
- Implement model explainability (e.g., SHAP values)
