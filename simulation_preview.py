import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random

st.title("🌍 Economic & Political Simulation Preview")

st.sidebar.header("Simulation Parameters")
num_firms = st.sidebar.slider("Number of Firms", 5, 50, 20)
num_households = st.sidebar.slider("Number of Households", 10, 100, 50)
num_rounds = st.sidebar.slider("Number of Rounds", 5, 20, 10)
tax_rate = st.sidebar.slider("Government Tax Rate", 0.05, 0.3, 0.1)

initial_gdp = 1_000_000
base_growth_rate = 0.02

political_rounds = [{"Round": i + 1, "GDP Modifier": random.choice([-0.01, 0.0, 0.01])} for i in range(num_rounds)]

firm_data = {"Firm ID": [f"Firm_{i}" for i in range(num_firms)], "Initial Wealth": [random.randint(100000, 500000) for _ in range(num_firms)], "Production Capacity": [random.randint(1000, 5000) for _ in range(num_firms)]}

household_data = {"Household ID": [f"Household_{i}" for i in range(num_households)], "Initial Wealth": [random.randint(50000, 200000) for _ in range(num_households)], "Consumption Rate": [random.randint(800, 4000) for _ in range(num_households)]}

df_firms = pd.DataFrame(firm_data)
df_households = pd.DataFrame(household_data)

st.subheader("🏢 Firms Overview")
st.dataframe(df_firms.head(10))

st.subheader("🏠 Households Overview")
st.dataframe(df_households.head(10))

gdp_values = [initial_gdp]
for round_data in political_rounds:
    effective_growth = base_growth_rate + round_data["GDP Modifier"]
    new_gdp = gdp_values[-1] * (1 + effective_growth)
    gdp_values.append(new_gdp)

st.subheader("📈 GDP Growth Projection (Preview)")
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(range(len(gdp_values)), gdp_values, marker="o", linestyle="-", color="blue")
ax.set_xlabel("Rounds")
ax.set_ylabel("GDP Value")
ax.set_title("Projected GDP Growth Over Simulation Rounds")
ax.grid(True)
st.pyplot(fig)

st.subheader("⚖️ Political Influence Summary")
df_politics = pd.DataFrame(political_rounds)
st.dataframe(df_politics)

st.success("✅ Preview ready! The full version will be available with even more interactive features.")