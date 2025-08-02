# 🏡 Risk, Rent, and Buy — Housing Analysis

This project uses machine learning and visualization techniques to analyze housing data across U.S. counties, focusing on:

- 💰 Purchase Price
- 📉 Rent Price
- ⚠️ Risk Score

We combine and normalize these features to identify:
- Top 100 counties for **profitable renting**
- Top 100 counties for **smart buying**
- Counties with **high risk** to avoid

---

## 🔍 Objectives

- Normalize housing metrics across counties
- Create custom indices:
  - **BuyIndex** = PurchasePrice + Risk
  - **RentIndex** = RentPrice + Risk
- Visualize locations on an interactive map (Folium)
- Perform regression analysis to explore relationships between risk, rent, and purchase
- Export results to CSV

---

## 📁 Project Files

| File | Description |
|------|-------------|
| `risk_rent_buy.ipynb` | Main Jupyter Notebook with code, analysis, and visualizations |
| `housing_risk.csv` | Raw housing data (price, rent, risk) |
| `us_county_latlng.csv` | Latitude and longitude by U.S. county |
| `final_risk_housing_analysis.csv` | Cleaned and processed output with index scores |
| `README.md` | This file: project overview and instructions |

---

## 📊 Technologies Used

- **Python**: core programming language
- **Pandas**: data analysis
- **Scikit-learn**: normalization & regression
- **Folium**: interactive maps
- **Matplotlib & Seaborn**: visualization

---

## 📈 Visualizations

- ✅ Top counties for rent and buy shown on a **Folium map**
- ✅ Custom indices visualized with **barplots**
- ✅ Relationships between variables shown using **linear regression models**

---

## 🚀 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/Love-Cherepanova/Risk_Rent_Buy_housing_analysis.git
   cd Risk_Rent_Buy_housing_analysis
   ```

2. Install dependencies (recommended: via Anaconda)
   ```bash
   pip install pandas matplotlib seaborn folium scikit-learn
   ```

3. Launch the notebook:
   ```bash
   jupyter notebook
   ```

4. Open `risk_rent_buy.ipynb` and run the cells step-by-step.

---

## 🧠 Future Ideas

- Add demographic data (e.g., income, population)
- Use clustering (e.g., KMeans) for location segmentation
- Apply advanced models (e.g., XGBoost) for risk prediction

---

## 📬 Author

**Love Cherepanova**  
GitHub: [Love-Cherepanova](https://github.com/Love-Cherepanova)
