# 🏠 Mumbai House Rent Price Predictor

This project is a **Streamlit-based web app** that predicts the **house rent price in Mumbai** using a machine learning model. It features an elegant UI with a **glassmorphic input box** overlaying a **rotating background video** for a modern and immersive experience.

---

## 🧠 Project Overview

### 📊 Dataset
- **Original dataset**: Mumbai House Price Data
- **Preprocessed into**: `Cleaned_data.csv`
- **Features used**:
  - `bhk`: Number of bedrooms
  - `area`: Total square feet
  - `region`: Locality/Region in Mumbai

### 🧼 Preprocessing Steps
- Removed irrelevant/missing data
- Label encoding / OneHotEncoding of `region`
- Normalized numerical values
- Final processed data stored in `Cleaned_data.csv`

### 🔮 ML Model
- Built using `scikit-learn`
- **Pipeline includes**:
  - `StandardScaler` for normalization
  - `OneHotEncoder` for categorical features
  - `LinearRegression` as the model
- **Saved as**: `House_prediction_model.pkl`

---

## 📦 Project Structure

```
House Rent Prediction/
├── app.py                      # Streamlit web app
├── Cleaned_data.csv            # Preprocessed dataset
├── House_prediction_model.pkl  # Trained ML model
├── background.mp4              # Background video
├── venv/                       # (Optional) Virtual environment
└── requirements.txt            # Python dependencies
```

---

## 🚀 How to Run the App Locally

### 1. Clone this repository
```bash
git clone https://github.com/your-username/house-rent-prediction.git
cd house-rent-prediction
```

### 2. Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Mac/Linux
# .\venv\Scripts\activate  # On Windows
```

### 3. Install required libraries
```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt`, you can create it using:
```bash
pip freeze > requirements.txt
```

### 4. Run the Streamlit app
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

---

## 💡 Features

- ✨ **Clean and responsive UI** with a rotating video background
- 🔮 **Glassmorphic input box** for modern aesthetics
- ⚡ **Real-time price predictions** based on user input
- 📝 **Simple inputs**: Uses only 3 inputs - BHK, Area (sqft), and Region
- 🎯 **Accurate predictions** powered by machine learning

---

## 🛠️ Technologies Used

- **Frontend**: Streamlit
- **Machine Learning**: scikit-learn
- **Data Processing**: pandas, numpy
- **Model Persistence**: pickle
- **Styling**: Custom CSS for glassmorphic effects

---

## 📋 Requirements

```txt
streamlit
scikit-learn
pandas
numpy
pickle-mixin
```

---

## 🎨 UI/UX Features

- **Rotating Background Video**: Creates an immersive experience
- **Glassmorphic Design**: Modern frosted glass effect on input containers
- **Responsive Layout**: Works seamlessly on different screen sizes
- **Interactive Elements**: Smooth transitions and hover effects

---

## 📈 Model Performance

The machine learning model uses Linear Regression with preprocessing pipeline for optimal performance:
- **Preprocessing**: StandardScaler + OneHotEncoder
- **Features**: BHK, Area, Region
- **Output**: Predicted rent price in INR

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 👩‍💻 Made by

**Janhavi Khanvilkar** – Passionate about ML, design, and building cool user interfaces.

---

## 🙏 Acknowledgments

- Thanks to the Mumbai housing data providers
- Streamlit community for excellent documentation
- scikit-learn for powerful ML tools

---

*⭐ If you found this project helpful, please give it a star!*
