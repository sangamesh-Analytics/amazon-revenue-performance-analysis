# 📦 Amazon E-Commerce Revenue Analysis, Forecasting & Business Intelligence

> End-to-end data analysis of an Amazon-style e-commerce dataset (2020–2024) — from exploratory analysis and SQL business querying to predictive forecasting and interactive Power BI dashboards.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-Analysis-orange?logo=mysql&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow?logo=powerbi&logoColor=white)
![DAX](https://img.shields.io/badge/DAX-Time%20Intelligence-red?logo=powerbi&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-green?logo=scikit-learn&logoColor=white)
![Excel](https://img.shields.io/badge/Excel-Data%20Prep-217346?logo=microsoftexcel&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

---

## 📌 Table of Contents

- [Project Overview](#project-overview)
- [Project Phases](#project-phases)
- [Business Objective](#business-objective)
- [Dataset Description](#dataset-description)
- [Project Structure](#project-structure)
- [Phase 1 — Power BI & DAX Dashboard](#phase-1--power-bi--dax-revenue-dashboard)
- [Phase 2 — Exploratory Data Analysis](#phase-2--exploratory-data-analysis-python)
- [Phase 2 — SQL Business Analysis](#phase-2--sql-business-analysis)
- [Phase 3 — Revenue Forecasting](#phase-3--revenue-forecasting-machine-learning)
- [Phase 3 — Forecasting Dashboard](#phase-3--forecasting-power-bi-dashboard)
- [Key Business Insights](#key-business-insights)
- [Recommendations](#recommendations)
- [Skills Demonstrated](#skills-demonstrated)
- [Tools & Technologies](#tools--technologies)
- [Future Improvements](#future-improvements)

---

## Project Overview

This project is a progressive, end-to-end analysis of Amazon-style e-commerce transaction data spanning 2020–2024. It was built in three phases — starting with a Power BI executive dashboard, extended with Python EDA and SQL business querying, and finally augmented with machine learning forecasting and enhanced BI reporting.

The objective across all phases was the same: transform raw transaction data into actionable business insights that support revenue strategy, inventory planning, and decision making.

| Tool | Purpose |
|------|---------|
| **Power BI + DAX** | Executive KPI dashboards & time intelligence |
| **Python** (Pandas, Matplotlib) | Exploratory data analysis & visualisation |
| **Scikit-learn** | Predictive revenue forecasting |
| **SQL** | Business data querying & aggregation |
| **Excel** | Initial data preparation |

---

## Project Phases

| Phase | Focus | Status |
|-------|-------|--------|
| ✅ **Phase 1** | Power BI Executive Dashboard & DAX Time Intelligence | Complete |
| ✅ **Phase 2** | Python Exploratory Data Analysis & SQL Business Queries | Complete |
| ✅ **Phase 3** | ML Revenue Forecasting & Enhanced Power BI Dashboards | Complete |

---

## Business Objective

Raw sales and revenue datasets are difficult to interpret for decision-makers. Across all phases, this project was designed to:

- Track revenue performance over time (yearly & quarterly)
- Compare current performance against previous year (YoY)
- Identify high-performing categories, brands, and top-demand products
- Detect category growth volatility and seasonality patterns
- Analyse customer purchasing behaviour and spending concentration
- Forecast short-term revenue trends to support forward planning
- Support marketing, inventory, and business strategy decisions

---

## Dataset Description

The dataset contains **100,000 transaction records** representing an Amazon-style e-commerce platform across **2020–2024**.

| Column | Description |
|--------|-------------|
| `OrderID` | Unique order identifier |
| `OrderDate` | Date of purchase |
| `CustomerID` | Unique customer identifier |
| `ProductName` | Purchased product |
| `Category` | Product category |
| `Brand` | Product brand |
| `Quantity` | Number of items ordered |
| `UnitPrice` | Price per unit |
| `TotalAmount` | Total transaction value |
| `Country` | Customer location |
| `OrderStatus` | Order fulfilment status |

---

## Project Structure

```
amazon-revenue-analysis/
│
├── data/
│   └── amazon_sales_data.csv
│
├── phase_1_powerbi/
│   └── Amazon_Revenue_Performance.pbix
│
├── phase_2_eda/
│   └── python_eda.ipynb
│
├── phase_3_forecasting/
│   └── forecasting_model.py
│
├── sql/
│   └── business_queries.sql
│
├── screenshots/
│   ├── dashboard_executive.png
│   ├── dashboard_category.png
│   └── dashboard_forecast.png
│
├── README.md
└── requirements.txt
```

---

## Phase 1 — Power BI & DAX Revenue Dashboard

**Role:** Data Analyst (Business Intelligence Reporting)
**Tools:** Power BI, DAX, Excel

### Key KPIs

| Metric | Value |
|--------|-------|
| 💰 Total Revenue (2020–2024) | $91.83M |
| 📈 Previous Year Revenue (PY) | $73.66M |
| 🚀 YoY Growth | 25% |
| ⭐ Top Product Revenue Range | ~$0.30M – $0.34M per product |

### DAX Measures Built
- `Total Revenue` — overall revenue aggregation
- `Previous Year Revenue (PY)` — time intelligence comparison
- `YoY Growth %` — year-over-year performance tracking
- Segment-based breakdowns by category and product

### Dashboard 1 — Executive Summary
- 💰 Total Revenue & PY Revenue KPI cards
- 📈 YoY Growth %
- 📉 Quarterly revenue trend (2020–2024)

### Dashboard 2 — Category & Product Deep Dive
- 🏷️ Quarterly category contribution analysis
- 🌟 Top demand products ranked by revenue
- 📊 YoY Growth trend by category
- 🎯 Category slicer for drill-down exploration

### Dashboard Preview

![Executive Summary](https://github.com/sangamesh-Analytics/amazon-revenue-performance-analysis/blob/main/amazon-revenuee-performance-analysis/AP3.png)
![Category & Product](screenshots/dashboard_category.png)

---

## Phase 2 — Exploratory Data Analysis (Python)

**Libraries used:** `Pandas`, `Matplotlib`

### Steps Performed
1. Data loading and inspection
2. Data type correction and date conversion
3. Time-based feature engineering (Year, Quarter)
4. Revenue aggregation by quarter
5. Trend visualisation

```python
df['Year'] = df['OrderDate'].dt.year
df['Quarter'] = df['OrderDate'].dt.quarter

quarterly_revenue = df.groupby(['Year', 'Quarter'])['TotalAmount'].sum()
```

### Findings
- Revenue remained relatively stable across quarters with minor fluctuations
- Balanced product demand observed across all categories
- Seasonal patterns reflect moderate quarterly variation in sales performance

---

## Phase 2 — SQL Business Analysis

### Revenue by Category
```sql
SELECT Category,
       SUM(TotalAmount) AS Revenue
FROM amazon
GROUP BY Category
ORDER BY Revenue DESC;
```
> Revenue is distributed evenly across categories, indicating diversified demand.

---

### Order Volume by Category
```sql
SELECT Category,
       COUNT(*) AS Total_Orders
FROM amazon
GROUP BY Category;
```
> Orders range between **911 – 927 per category**, showing balanced purchasing behaviour.

---

### Average Order Value
```sql
SELECT Category,
       AVG(TotalAmount) AS Avg_Order_Value
FROM amazon
GROUP BY Category;
```
> Highest AOV: **Clothing (~$927)** | Lowest AOV: **Books (~$911)** — minimal pricing differences across categories.

---

### Revenue by Country
```sql
SELECT Country,
       SUM(TotalAmount) AS Revenue
FROM amazon
GROUP BY Country
ORDER BY Revenue DESC;
```

| Country | Revenue |
|---------|---------|
| 🇺🇸 United States | ~$64M |
| 🇮🇳 India | ~$13.8M |
| 🇦🇺 Australia | ~$3.7M |

> The US market dominates revenue contribution.

---

### Top 10 Revenue-Generating Brands
```sql
SELECT Brand,
       SUM(TotalAmount) AS Revenue
FROM amazon
GROUP BY Brand
ORDER BY Revenue DESC
LIMIT 10;
```

| Rank | Brand |
|------|-------|
| 1 | Coretech |
| 2 | Kiddofun |
| 3 | Readmore |
| 4 | UrbanStyle |
| 5 | Zenith |
| 6 | Apex |
| 7 | Nexpro |
| 8 | Fitlife |
| 9 | BrightLux |
| 10 | HomeEase |

---

### Customer Spending Analysis
```sql
SELECT CustomerID,
       SUM(TotalAmount) AS Total_Spent
FROM amazon
GROUP BY CustomerID
ORDER BY Total_Spent DESC
LIMIT 10;
```
> Top customers show up to ~30% spending difference between ranks, suggesting a **Pareto-like revenue distribution** — a key segment to retain and grow.

---

## Phase 3 — Revenue Forecasting (Machine Learning)

**Model used:** Linear Regression (`Scikit-learn`)

### Feature Engineering

| Feature | Purpose |
|---------|---------|
| `Quarter_Index` | Captures overall revenue trend over time |
| Seasonal Dummies (`Q2`, `Q3`, `Q4`) | Captures quarter-specific seasonality |

> Q1 is treated as the base category.

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X, y)
```

### Forecast Result
Revenue was forecasted for **four future quarters (2025)**. Predicted values showed stable revenue with moderate seasonal variation, consistent with the historical trends identified in Phase 2.

---

## Phase 3 — Forecasting Power BI Dashboard

Three updated dashboard views were built to incorporate forecast results:

### 📈 Revenue Performance Dashboard
- Quarterly revenue trend (historical)
- Historical vs forecast revenue comparison

### 🗂️ Category Analysis Dashboard
- Sales distribution by product category
- Category performance comparison

### 🔮 Forecast Dashboard
- Predicted revenue trends for 2025
- Future business performance outlook

### Dashboard Preview

![Forecast Dashboard](screenshots/dashboard_forecast.png)

---

## Key Business Insights

1. 📦 **Balanced category demand** — Revenue is evenly distributed across product categories, indicating a diversified and resilient product portfolio.
2. 🌍 **US market dominance** — The United States is the largest revenue market, contributing the majority of total sales (~$64M).
3. 🏆 **Leading brand** — Coretech leads brand revenue, highlighting strong customer brand preference.
4. 💰 **Consistent pricing** — Average order value remains uniform across categories, reflecting a standardised pricing strategy.
5. 👤 **High-value customer concentration** — Revenue shows a Pareto-like distribution among top customers — a critical segment for retention and growth.
6. 📈 **25% YoY Growth** — Strong year-over-year growth confirms positive revenue momentum across the analysis period.
7. 🔮 **Stable 2025 forecast** — ML modelling confirms a steady revenue outlook for 2025 with moderate seasonal variation.

---

## Recommendations

| Priority | Recommendation |
|----------|---------------|
| 🎯 High | Focus marketing and inventory investment toward consistent high-performing categories during peak quarters |
| ⭐ High | Prioritise top-demand products (~$0.30M–$0.34M revenue range) for promotion, bundling, and supply optimisation |
| 📊 Medium | Monitor categories with volatile YoY trends to refine pricing strategy and promotional timing |
| 👤 Medium | Develop retention strategies targeting high-value customers identified through Pareto analysis |
| 💰 Future | Extend analysis with profitability KPIs (Cost, Profit Margin) for stronger strategic decision-making |

---

## Skills Demonstrated

- Data Cleaning & Transformation
- Exploratory Data Analysis
- Time-based Feature Engineering
- Revenue Trend & YoY Growth Analysis
- DAX Time Intelligence (Power BI)
- Predictive Modelling (Linear Regression)
- SQL Business Querying & Aggregation
- Dashboard Design & BI Reporting
- Data-driven Business Insight Generation

---

## Tools & Technologies

| Tool | Purpose |
|------|---------|
| Python | Data analysis & scripting |
| Pandas | Data manipulation |
| Matplotlib | Data visualisation |
| Scikit-learn | Machine learning / forecasting |
| SQL | Business queries & aggregations |
| Power BI | Executive & forecast dashboards |
| DAX | Time intelligence & KPI measures |
| Excel | Initial data preparation |

---

## Future Improvements

- [ ] Customer segmentation (RFM analysis)
- [ ] Product recommendation systems
- [ ] Advanced time-series forecasting (ARIMA / Prophet)
- [ ] Profitability analysis (Cost, Profit, Margin KPIs)
- [ ] Marketing campaign performance analytics
- [ ] Geographic / region-based revenue analysis
- [ ] Customer churn prediction

---

*Analysis performed on a simulated Amazon-style e-commerce dataset of 100,000 transactions spanning 2020–2024.*

## 👤 Author

<div align="center">

**Sangamesh Dadge**

[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-orange?style=for-the-badge&logo=google-chrome&logoColor=white)](https://sangamesh-analytics.github.io/Sangamesh.github.io/)
[![Email](https://img.shields.io/badge/Email-sangameshdadge2003%40gmail.com-red?style=for-the-badge&logo=gmail&logoColor=white)](mailto:sangameshdadge2003@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/sangamesh-dadge-736050251/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=for-the-badge&logo=github)](https://github.com/sangamesh-Analytics)

</div>

---

<div align="center">

### ⭐ Star this repository if you found it useful!

**Turning raw data into business decisions — one dashboard at a time.**


---

*© 2025 Sangamesh Dadge. All rights reserved.*

</div>
