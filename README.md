# 🚚 DeliverIQ

Food Delivery Time Prediction using Random Forest Regression and Streamlit.

🔗 **Live Demo:** https://supremeinferno-food-delivery.streamlit.app

---

## Overview

DeliverIQ predicts food delivery times based on order, traffic, weather, and courier-related factors.

The project explores machine learning techniques for estimating delivery duration and uses a tuned Random Forest Regressor to generate predictions. The goal is to simulate a real-world logistics problem where accurate delivery estimates can improve customer experience and operational efficiency.

---

## Dataset

The dataset contains **1000 delivery records** with the following features:

* Distance (km)
* Weather Conditions
* Traffic Level
* Time of Day
* Vehicle Type
* Preparation Time (minutes)
* Courier Experience (years)

Target Variable:

* Delivery Time (minutes)

---

## Screenshots

### Home Page

<p align="center">
  <img src="assets/Screenshot1.png" width="900">
</p>

### Prediction Result

<p align="center">
  <img src="assets/Screenshot2.png" width="900">
</p>

---

## Data Preprocessing

The following steps were performed:

* Data Cleaning
* Categorical Feature Encoding
* Feature Transformation
* Train-Test Split
* Hyperparameter Optimization using RandomizedSearchCV

---

## Model Development

The following model was trained:

| Model                   | Purpose     |
| ----------------------- | ----------- |
| Random Forest Regressor | Final Model |

### Best Parameters

```python
{
    'max_depth': 11,
    'max_features': 3,
    'min_samples_leaf': 3,
    'min_samples_split': 3,
    'n_estimators': 781
}
```

---

## Performance

| Metric   | Score |
| -------- | ----- |
| MAE      | 6.88  |
| RMSE     | 9.62  |
| R² Score | 0.79  |

The optimized Random Forest model was selected after hyperparameter tuning using RandomizedSearchCV.

---

## Tech Stack

* Python
* Pandas
* NumPy
* Scikit-Learn
* Streamlit

---

## Project Structure

```text
Randomforest-food-delivery/
│
├── app.py
├── model.ipynb
├── Food_Delivery_Times.csv
├── optimized_rf_model.pkl
├── label_encoders.pkl
├── requirements.txt
├── README.md
│
└── assets/
    ├── home.png
    └── prediction.png
```

---

## Installation

```bash
git clone https://github.com/supremeinferno/Randomforest-food-delivery.git

cd Randomforest-food-delivery

pip install -r requirements.txt

streamlit run app.py
```

---

## Future Improvements

* Route-based prediction features
* Real-time traffic integration
* Delivery cost estimation
* Feature importance visualization
* GPS-based analytics

---

## Author

**Pranav Garg**

GitHub: https://github.com/supremeinferno
