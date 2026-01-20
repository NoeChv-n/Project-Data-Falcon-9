# SpaceX Falcon 9 Landing Prediction

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Library](https://img.shields.io/badge/Library-Pandas%20|%20Scikit--Learn%20|%20Dash-orange)
![Status](https://img.shields.io/badge/Status-Completed-green)

##  Executive Summary

The commercial space age is here. Companies like SpaceX have revolutionized the industry by making space travel affordable through reusable rockets. To determine the cost of a launch, it is crucial to know if the first stage will land successfully.

**This project is an end-to-end data science pipeline** designed to predict the successful landing of the Falcon 9 first stage. By analyzing historical data and weather conditions, we trained machine learning models to classify the outcome of a launch.

*This project was built as the Capstone for the IBM Data Science Professional Certificate.*

---

##  Project Visuals

### 1. Interactive Analytics Dashboard (Dash)
<img width="972" height="489" alt="Capture d’écran 2026-01-13 à 11 08 26" src="https://github.com/user-attachments/assets/7a6b4fee-701c-434e-b844-3f28e8821de4" />
*An interactive dashboard allowing users to explore success rates by launch site and payload mass.*

### 2. Launch Site Analysis (Folium)
<img width="477" height="450" alt="Capture d’écran 2026-01-20 à 13 56 40" src="https://github.com/user-attachments/assets/229b4483-f152-4409-9475-e83da58e721a" />
*Geospatial analysis of launch sites and their proximity to coasts and railways.*

---

##  Methodology

The project follows a structured Data Science lifecycle:

### 1. Data Collection
* **SpaceX API:** Requested data from the SpaceX REST API to get launch details, rocket stats, and landing outcomes.
* **Web Scraping:** Scraped Wikipedia to gather Falcon 9 launch records and payload mass data using `BeautifulSoup`.

### 2. Data Wrangling (Pre-processing)
* Filtered data to include only Falcon 9 launches.
* Handled missing values (imputation) and standardized formats.
* Classified landing outcomes into binary values: `1` (Success) and `0` (Failure).

### 3. Exploratory Data Analysis (EDA)
* **SQL:** Queried the dataset to find insights like total payload mass per booster version and success rates by year.
* **Visualization:** Used `Matplotlib` and `Seaborn` to visualize relationships between Flight Number, Payload Mass, Orbit type, and Launch Site.

### 4. Interactive Visual Analytics
* Built a **Folium Map** to analyze the geographical distribution of launch sites.
* Developed a **Plotly Dash** web application to provide real-time interactive insights for stakeholders.

### 5. Machine Learning Prediction
* Standardized the data and split it into training/testing sets.
* Trained and hyperparameter-tuned (using `GridSearchCV`) four classification models:
    * Logistic Regression
    * Support Vector Machine (SVM)
    * Decision Tree Classifier
    * K-Nearest Neighbors (KNN)

---

##  Results

We compared the performance of all models based on accuracy on the test set.

| Model | Accuracy (Test Set) |
|-------|---------------------|
| Decision Tree | **94%** |
| SVM | 84% |
| Logistic Regression | 84% |
| KNN | 84% |

**Key Finding:** The **Decision Tree** performed best, successfully identifying the landing outcome with an accuracy of **94%**.

<img width="564" height="419" alt="Capture d’écran 2026-01-20 à 13 54 53" src="https://github.com/user-attachments/assets/20adcd73-a9f9-4fbd-8ef0-51e2d01c9c5e" />



---

## 💻 Tech Stack

* **Languages:** Python, SQL
* **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn
* **Web Scraping:** BeautifulSoup, Requests
* **Visualization:** Folium, Plotly Dash

---

##  File Structure

* `1_Data_Collection_API.ipynb`: Collecting data via SpaceX API.
* `2_Data_Collection_Scraping.ipynb`: Scraping Falcon 9 data from Wikipedia.
* `3_Data_Wrangling.ipynb`: Cleaning and formatting the dataset.
* `4_EDA_SQL.ipynb`: SQL queries for data exploration.
* `5_EDA_Visualization.ipynb`: Static visualizations using Seaborn/Matplotlib.
* `6_Interactive_Map.ipynb`: Folium map generation.
* `7_SpaceX_Dash_App.py`: Source code for the Dash web application.
* `8_Machine_Learning.ipynb`: Model training, tuning, and evaluation.
* `spacex_launch_dash.csv`: Processed dataset used for the dashboard.

---

##  How to Run

1.  Clone the repository:
    ```bash
    git clone [https://github.com/](https://github.com/)[YOUR_USERNAME]/SpaceX-Falcon9-Prediction.git
    ```
2.  Install dependencies:
    ```bash
    pip install pandas numpy scikit-learn matplotlib seaborn folium plotly dash requests beautifulsoup4
    ```
3.  Run the Dashboard:
    ```bash
    python 7_SpaceX_Dash_App.py
    ```

---

##  Author

**Noé Chauvin**
* LinkedIn: (https://www.linkedin.com/in/noe-chauvin/)

*This project is part of my journey to becoming a Data Scientist. Feel free to reach out for feedback!*
