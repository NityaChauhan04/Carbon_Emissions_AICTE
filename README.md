# Carbon_Emissions_AICTE
# AICTE Internship Project: Carbon Emission Prediction System

The project focuses on predicting carbon emissions. It involves cleaning and transforming datasets and removing the missing values.

---

## 📅 Week 1: Data Preprocessing

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
