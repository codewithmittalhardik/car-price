# 🚗 Car Price Predictor

A machine learning-powered web application that estimates the resale value of used cars based on their specifications. Built with **Python (Flask)** and **Scikit-Learn**, featuring a responsive and interactive user interface.

## 📋 Table of Contents
* [Overview](#overview)
* [Features](#features)
* [Tech Stack](#tech-stack)
* [Installation](#installation)
* [Usage](#usage)
* [Dataset](#dataset)
* [Contact](#contact)

## 🔎 Overview
Buying or selling a used car can be challenging when trying to determine a fair price. This application solves that problem by using a trained Machine Learning model to predict car prices based on historical data.

The user simply inputs details like:
* **Brand & Model**
* **Year of Purchase**
* **Fuel Type** (Petrol, Diesel, CNG, etc.)
* **Kilometers Driven**

...and the app provides an instant valuation.

## ✨ Features
* **Accurate Predictions:** Uses a trained regression model for reliable price estimates.
* **Dynamic Dropdowns:** Selecting a car company automatically filters the available models using JavaScript.
* **Responsive Design:** Clean, modern UI that works on mobile and desktop.
* **Real-time Interface:** Uses AJAX to fetch predictions without reloading the page.

## 🛠 Tech Stack
* **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
* **Backend:** Python, Flask
* **Machine Learning:** Scikit-Learn, Pandas, NumPy
* **Model Storage:** Pickle (`.pkl`)

## ⚙️ Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/codewithmittalhardik/car-price.git](https://github.com/codewithmittalhardik/car-price.git)
    cd car-price
    ```

2.  **Create a virtual environment (Recommended):**
    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # Mac/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application:**
    ```bash
    python app.py
    ```

5.  **Open in Browser:**
    Navigate to `http://127.0.0.1:8000/`

## 🚀 Usage
1.  Select the **Car Company** (e.g., Maruti, Hyundai).
2.  Select the specific **Car Model** (the list updates automatically).
3.  Choose the **Year of Purchase**.
4.  Select the **Fuel Type**.
5.  Enter the **Kilometers Driven**.
6.  Click **"Predict Price"** to see the estimated value instantly.

## 📊 Dataset & Model
The model was trained on a dataset of utilized cars containing features like name, company, year, kilometers driven, and fuel type.
* **Preprocessing:** Data cleaning involved handling missing values, converting object types to integers, and removing outliers.
* **Algorithm:** Linear Regression (with OneHotEncoding pipeline) achieved the highest accuracy of approx **0.84 R² score**.

## 👤 Contact
**Hardik Mittal**
* [LinkedIn](https://www.linkedin.com/in/mittalhardik)
* [GitHub](https://github.com/codewithmittalhardik)
