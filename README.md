<div align="center">

# 📦 Amazon Revenue Performance Analysis
### *2020–2024*

![Status](https://img.shields.io/badge/Status-Complete-success)
![Power BI](https://img.shields.io/badge/Tool-Power%20BI-F2C811?logo=powerbi&logoColor=black)
![DAX](https://img.shields.io/badge/Skill-DAX-blue)
![Python](https://img.shields.io/badge/Skill-Python-3776AB?logo=python&logoColor=white)
![Excel](https://img.shields.io/badge/Skill-Excel-217346?logo=microsoft-excel&logoColor=white)

**Transforming ecommerce revenue data into strategic business insights using Power BI & DAX**


</div>

---

## 📌 Project Overview

This project analyzes Amazon-style ecommerce sales performance from **2020–2024** using **Power BI + DAX time intelligence**.  
It delivers both an executive KPI view and a deep-dive into category & product performance to support better business decisions.

<table>
<tr>
<td><b>Role</b></td>
<td>Data Analyst (Business Intelligence Reporting)</td>
</tr>
<tr>
<td><b>Tools</b></td>
<td>Power BI, DAX, Python (EDA), Excel</td>
</tr>
<tr>
<td><b>Focus</b></td>
<td>Revenue trends, YoY growth, category contribution, demand analysis</td>
</tr>
</table>

---

## 🎯 Business Problem

Raw sales/revenue datasets are difficult to interpret for decision-makers.  
Stakeholders require a consolidated dashboard to:

<table>
<tr>
<td>✅</td>
<td>Track revenue performance over time (year & quarter)</td>
</tr>
<tr>
<td>✅</td>
<td>Compare current performance vs previous year (PY)</td>
</tr>
<tr>
<td>✅</td>
<td>Identify high-performing categories and top-demand products</td>
</tr>
<tr>
<td>✅</td>
<td>Detect category growth volatility and seasonality patterns</td>
</tr>
<tr>
<td>✅</td>
<td>Support marketing and inventory planning</td>
</tr>
</table>

---

## 📂 Dataset Summary

| Attribute | Description |
|-----------|-------------|
| **Type** | Simulated ecommerce dataset (Amazon-style) |
| **Time Period** | **2020 to 2024** |
| **Granularity** | Quarterly + Category + Product |
| **Key Fields** | Year, Quarter, Revenue, Category, Product, CustomerID |

---

## 📊 Key KPIs (Dashboard Metrics)

<div align="center">

| Metric | Value |
|:------:|:-----:|
| 💰 **Total Revenue (2020–2024)** | **$91.83M** |
| 📈 **Previous Year Revenue (PY)** | **$73.66M** |
| 🚀 **YoY Growth** | **25%** |
| ⭐ **Top Product Revenue Range** | **~$0.30M–$0.34M per product** |

</div>

---

## 🛠️ Tools & Techniques Used

### 🔧 BI Development
- **Power Query** for data cleaning, formatting, transformation
- **Data Modeling** with DateTable to enable time-intelligence calculations
- **KPI Cards + Trend visuals + Slicers** for interactive reporting

### 📐 DAX / Time Intelligence
- Total Revenue
- Previous Year Revenue (PY)
- YoY Growth %
- Segment-based breakdown (Category/Product visuals)

---

## 🖼️ Dashboard Preview

### 1️⃣ Executive Summary: Revenue Trend & YoY Growth

<div align="center">

![Revenue Overview Dashboard](https://github.com/sangamesh-Analytics/amazon-revenue-performance-analysis/blob/main/amazon-revenuee-performance-analysis/screenshots/Ap1.png)

</div>

**Features:**
- 💰 Total Revenue KPI
- 📊 Total Revenue PY KPI
- 📈 YoY Growth %
- 📉 Quarterly revenue trend (2020–2024)

---

### 2️⃣ Deep Dive: Category & Product Performance

<div align="center">

![Category & Growth Dashboard](https://github.com/sangamesh-Analytics/amazon-revenue-performance-analysis/blob/main/amazon-revenuee-performance-analysis/screenshots/Ap2.png)

</div>

**Features:**
- 🏷️ Quarterly category contribution analysis
- 🌟 Top demand products (revenue-based ranking)
- 📊 YoY Growth trend by category
- 🎯 Category slicer for drill exploration

---

## 🔍 Key Insights (Business Ready)

> 💡 **Seasonality & Planning**  
> Quarterly revenue trends indicate **seasonality patterns**, enabling improved planning for peak vs non-peak demand periods.

> 📈 **Growth Acceleration**  
> YoY Growth (%) provides deeper performance visibility than revenue alone — highlighting **growth acceleration vs slowdown**.

> ⚠️ **Revenue Concentration Risk**  
> Category contribution analysis highlights **revenue concentration risk** where few categories dominate total performance.

> ⭐ **Product Prioritization**  
> Product-level analysis identifies **top-demand products** driving a large portion of revenue, supporting prioritization in inventory and promotions.

---

## 💡 Recommendations

| Priority | Recommendation |
|:--------:|----------------|
| 🎯 **High** | Focus marketing + inventory investment toward consistent high-performing categories during peak quarters. |
| ⭐ **High** | Prioritize top-demand products (revenue range: **~$0.30M–$0.34M**) for promotion, bundling, and supply optimization. |
| 📊 **Medium** | Track categories with volatile YoY trends to plan pricing strategy and promotional timing. |
| 💰 **Future** | Extend dashboard using profitability KPIs (Cost, Profit, Margin) for stronger decision-making. |

---

## 🧠 DAX Measures Used (Core KPIs)

<details>
<summary><b>Click to expand DAX code</b></summary>

```DAX
Total Revenue = SUM(Amazon[Revenue])

Total Revenue PY =
CALCULATE(
    [Total Revenue],
    SAMEPERIODLASTYEAR('DateTable'[Date])
)

YoY Growth % =
DIVIDE(
    [Total Revenue] - [Total Revenue PY],
    [Total Revenue PY],
    0
)
```

</details>

---

## 📁 Project Structure

```
amazon-revenue-performance-analysis/
│
├── 📂 data/
│   └── amazon_sales_data.csv
│
├── 📂 dashboard/
│   └── Amazon_Revenue_Performance.pbix
│
├── 📂 screenshots/
│   ├── Ap1.png
│   └── Ap2.png
│
└── 📄 README.md
```

---

## ✨ Future Enhancements

<table>
<tr>
<td>💰</td>
<td><b>Profitability Analysis</b></td>
<td>Add Profit, Cost & Margin KPIs (profitability-focused analysis)</td>
</tr>
<tr>
<td>👥</td>
<td><b>Customer Segmentation</b></td>
<td>Customer segmentation (repeat vs new customers)</td>
</tr>
<tr>
<td>🔮</td>
<td><b>Revenue Forecasting</b></td>
<td>Forecasting for revenue prediction using time-series models</td>
</tr>
<tr>
<td>🌍</td>
<td><b>Geographic Analysis</b></td>
<td>Region/market-based analysis (if geography field is available)</td>
</tr>
</table>

---

## 👤 Author

<div align="center">

**Sangamesh Dadge**

[![Email](https://img.shields.io/badge/Email-sangameshdadge2003%40gmail.com-red?style=for-the-badge&logo=gmail&logoColor=white)](mailto:sangameshdadge2003@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/sangamesh-dadge-736050251/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=for-the-badge&logo=github)](https://github.com/sangamesh-Analytics)

</div>

---

<div align="center">

### ⭐ Star this repository if you found it useful!

**Turning raw data into business decisions — one dashboard at a time.**

[![Made with Power BI](https://img.shields.io/badge/Made%20with-Power%20BI-F2C811?style=flat-square&logo=powerbi&logoColor=black)](https://powerbi.microsoft.com/)
[![Built with DAX](https://img.shields.io/badge/Built%20with-DAX-blue?style=flat-square)](https://dax.guide/)

---

*© 2025 Sangamesh Dadge. All rights reserved.*

</div>
