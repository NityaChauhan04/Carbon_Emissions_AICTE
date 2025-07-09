# Carbon_Emissions_AICTE
# AICTE Internship Project: Carbon Emission Prediction System

The project focuses on predicting carbon emissions. It involves cleaning and transforming datasets and removing the missing values.

---
#### 🔗 Model Download: https://drive.google.com/file/d/1R08mOGPySz174lsbmb5J5W52HTeegP_L/view?usp=drive_link
## 📅 Week 1: Data Preprocessing
---
### ✅ Objectives:
- Load the raw dataset (`climate_change.xls`)
- Clean missing and inconsistent data
- Reshape the data to prepare it for analysis

### ✅ Tasks Completed:
1. **Loading Data:**
   - Read `.xls` format using `pandas.read_excel()` after installing `xlrd`.

2. **Cleaning Missing Values:**
   - Replaced blank strings (`''`) and `'..'` with `np.nan`.
   ```python
   data_clean.iloc[:, 2:] = data_clean.iloc[:, 2:].replace({'': np.nan, '..': np.nan})

3. **Suppressing Future Warnings:**
   - Used the `warnings` library to hide non-critical future warnings for cleaner output:
     ```python
     import warnings
     warnings.filterwarnings("ignore", category=FutureWarning)
     ```

---

## 📅 Week 2: Data Exploration

### ✅ Objectives:
- Understand the structure and patterns in the dataset
- Rename features for easier interpretation
- Perform summary statistics and multicollinearity checks

### ✅ Tasks Completed:
1. **Loaded Cleaned Data:**
   - Used `data_cleaned.csv` for analysis.

2. **Global Overview:**
   - Displayed shape, data types, first few rows, and statistical summaries:
     ```python
     data.shape
     data.dtypes
     data.head()
     data.describe().T
     ```
3. **Basic Visualizations:**
   - Created plots using `matplotlib` and `seaborn` for better understanding of variable distributions and relationships.

---
## 📅 Week 3: Model Building
### ✅ Objectives:
- Build a predictive ML model using Random Forest Regressor
- Perform feature selection using RFECV
- Tune hyperparameters with RandomizedSearchCV
- Forecast future CO₂ per capita emissions for the next 20 years

### ✅ Tasks Completed:
1. **Model Development:**
- Applied RandomForestRegressor with recursive feature elimination (RFECV)
- Tuned hyperparameters via cross-validation
- Evaluated with R², MSE, and RMSE metrics

2. **Forecasting:**
- Used Compound Annual Growth Rate (CAGR) for selected socio-economic indicators
- Forecasted emissions from last available year to next 20 years for selected countries

3. **Model Export:**
- Saved trained model using joblib as:
``` pyhton 
forecasting_co2_emission.pkl
```
---
## 🛠 Technologies Used:
- Python 
- Jupyter Notebook
- Pandas, NumPy
- Matplotlib, Seaborn
- Statsmodels

---
