import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(page_title="Carbon Emission Predictor", layout="centered")
st.title("🌍 Carbon Emission Predictor")
st.write("Forecasting CO₂ emissions per capita for the given countries.")


@st.cache_data
def load_data():
    data = pd.read_csv("../WEEK1/data_cleaned.csv")
    model = joblib.load("forecasting_co2_emission.pkl")
    return data, model


data, model = load_data()


selected_countries = ['IND', 'USA', 'PAK', 'RUS', 'NZL']
country = st.selectbox("Select a Country", selected_countries)


selected_features = ['cereal_yield', 'gni_per_cap', 'en_per_cap',
                     'pop_urb_aggl_perc', 'prot_area_perc',
                     'pop_growth_perc', 'urb_pop_growth_perc']


country_data = data[data['country'] == country].sort_values('year')
start_year = country_data['year'].min()
end_year = country_data['year'].max()
years = end_year - start_year

growth_rates = {}
for feature in selected_features:
    start_val = country_data[country_data['year'] == start_year][feature].values
    end_val = country_data[country_data['year'] == end_year][feature].values
    if len(start_val) > 0 and len(end_val) > 0:
        cagr = (end_val / start_val) ** (1 / years) - 1
        growth_rates[feature] = float(cagr)
    else:
        growth_rates[feature] = 0.0


last_year = data['year'].max()
future_years = list(range(last_year + 1, last_year + 21))
forecast_results = []

if not country_data[selected_features].dropna().empty:
    latest_row = country_data[selected_features].dropna().iloc[-1].copy()

    for year in future_years:
        for feature in selected_features:
            latest_row[feature] *= (1 + growth_rates.get(feature, 0.0))
        input_features = latest_row.values.reshape(1, -1)
        predicted_co2 = model.predict(input_features)[0]
        forecast_results.append({
            'year': year,
            'co2_per_capita': predicted_co2
        })

    df_forecast = pd.DataFrame(forecast_results)

    st.subheader(f"📈 Forecasted CO₂ Emissions per Capita for {country}")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=df_forecast, x='year', y='co2_per_capita', marker='o', ax=ax)
    ax.set_title(f"Forecasted CO₂ Emissions per Capita for {country}", fontsize=14)
    ax.set_xlabel("Year")
    ax.set_ylabel("CO₂ per Capita (metric tons)")
    ax.grid(True)
    st.pyplot(fig)
    plt.close(fig)

    st.subheader("📊 Forecasted CO₂ Emissions (2040 - 2044)")
    st.dataframe(df_forecast.tail(5).reset_index(drop=True))
else:
    st.warning(f"Not enough data available for {country} to generate forecast.")
