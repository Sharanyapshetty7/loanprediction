

 Loan Approval Prediction System

This repository contains the code and resources for a Loan Approval Prediction System. The system uses machine learning models to predict whether a loan application will be approved or not based on various applicant details.

## Table of Contents

- [Introduction](#introduction)
- [Dataset](#dataset)
- [Models Used](#models-used)
- [Results](#results)
- [Web Application](#web-application)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Loan Approval Prediction System is designed to predict the approval status of loan applications using machine learning techniques. It utilizes three different models: Support Vector Machine (SVM), Decision Tree, and Logistic Regression. The best performing model is integrated into a web application for ease of use.

## Dataset

The dataset used for this project is `loan_approval_dataset.csv`. It contains information on various features such as applicant income, co-applicant income, loan amount, loan term, credit history, and more. The target variable is the loan approval status.

## Models Used

1. **Support Vector Machine (SVM)**
2. **Decision Tree**
3. **Logistic Regression**
4. **Randomforest**
   
Google Colab Notebook
You can view and run the Loan Approval Prediction notebook on Google Colab by clicking the link below:https://colab.research.google.com/drive/1-Cz8iKTVJ8ItDKIp3_UWmFHphoiASa90#scrollTo=L-abXiFd9twD
## Results

The performance of each model was evaluated using  classification report, and accuracy score on both training and testing datasets. Based on the results, the best performing model was selected for deployment.

## Web Application

The prediction model is deployed using a Streamlit application, allowing users to input applicant details and get loan approval predictions in real-time.

## Installation

To run the project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/loan-approval-prediction.git
    cd loan-approval-prediction
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To start the Streamlit web application, run:
```bash
streamlit run app.py
```
This will launch the web application in your default web browser. You can then input applicant details and get loan approval predictions.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Feel free to customize this README file as per your specific project details.
