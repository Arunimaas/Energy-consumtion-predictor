# ⚡ Energy Consumption Predictor

An **Machine Learning-based Energy Consumption Prediction System** that predicts electricity consumption based on factors such as temperature, number of appliances, and usage hours.

The project uses **Multiple Linear Regression** to estimate energy consumption and categorizes the predicted consumption into different levels.

## 📌 About the Project

Electricity consumption depends on several factors such as temperature, appliance usage, and the number of hours appliances are operated.

This project uses historical energy consumption data to train a machine learning model that can predict electricity consumption for new input values.

The system also provides a simple classification of the predicted consumption:

* 🟢 **Low** — Less than 5 kWh
* 🟡 **Moderate** — 5 to 19 kWh
* 🔴 **High** — More than 19 kWh

## ✨ Features

* ⚡ Predict electricity consumption
* 🤖 Machine Learning-based prediction
* 📊 Multiple Linear Regression model
* 🔢 Uses multiple input features
* 🏷️ Categorizes consumption into Low, Moderate, and High
* 🌐 Streamlit-based user interface
* 📈 Easy-to-understand prediction results

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **Streamlit**
* **Joblib**
* **Matplotlib**

## 🧠 Machine Learning Model

The project uses **Multiple Linear Regression** to predict energy consumption.

The model considers different factors such as:

* 🌡️ Temperature
* 🏠 Number of appliances
* ⏱️ Usage hours
* 📅 Day-related information

Categorical features are processed using **One-Hot Encoding** before being provided to the model.

### Model Performance

| Metric            |      Score |
| ----------------- | ---------: |
| Training R² Score | **0.9111** |
| Testing R² Score  | **0.9143** |

The testing R² score of approximately **91.43%** indicates that the model explains a large portion of the variation in energy consumption in the test dataset.

## 🔄 How It Works

```text
User Input
    ↓
Input Data Processing
    ↓
One-Hot Encoding
    ↓
Trained Linear Regression Model
    ↓
Energy Consumption Prediction
    ↓
Consumption Classification
    ↓
Low / Moderate / High
```

## 📊 Dataset

The project uses a dataset containing approximately **4,000 records** related to electricity/energy consumption.

The dataset contains information related to factors that influence energy usage, which are used as input features for the prediction model.

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Arunimaas/Energy-consumtion-predictor.git
```

### 2. Navigate to the Project Folder

```bash
cd Energy-consumtion-predictor
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Application

```bash
streamlit run app.py
```

The application will open in your browser.

## 📁 Project Structure

```text
Energy-consumtion-predictor/
│
├── app.py
├── energy_model.pkl
├── requirements.txt
├── dataset/
│   └── ...
├── notebooks/
│   └── ...
└── README.md
```

> The exact folder structure may vary depending on the files currently present in the repository.

## 🎯 Example

The user provides information such as:

```text
Temperature: 28°C
Number of Appliances: 5
Usage Hours: 6
```

The trained model processes the input and predicts the expected energy consumption.

The result is then classified as:

```text
Predicted Consumption: XX kWh
Category: Moderate
```

## 🔮 Future Improvements

* Improve prediction accuracy with advanced ML models
* Add more real-world energy consumption features
* Add interactive graphs and visualizations
* Deploy the application online
* Add historical consumption analysis
* Implement personalized energy-saving recommendations
* Support real-time electricity monitoring

## 👩‍💻 Author

**Arunima A S**

B.Tech Computer Science / AI & ML Student

GitHub: [Arunimaas](https://github.com/Arunimaas)

## ⭐ Acknowledgement

This project was developed as an academic/learning project to explore **Machine Learning, data preprocessing, regression models, and Streamlit application development**.

If you found this project useful, consider giving it a ⭐ on GitHub!
