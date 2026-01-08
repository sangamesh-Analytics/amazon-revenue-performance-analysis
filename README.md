# 📦 Amazon Revenue Performance Analysis (2020–2024)

<div align="center">

![Project Status](https://img.shields.io/badge/Status-Complete-success)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?logo=powerbi&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)

*Transforming quarterly sales data into strategic business insights for e-commerce growth*

</div>

---

## 📌 Project Overview

This comprehensive revenue performance analysis examines Amazon's sales patterns across a 4-year period (2020–2024), delivering actionable insights into revenue trends, category performance, and growth dynamics. Through advanced data visualization and business intelligence techniques, this project identifies key revenue drivers and opportunities for strategic optimization.

**Analysis Period**: Q1 2020 – Q4 2024  
**Role**: Business Data Analyst  
**Focus**: Revenue optimization, trend forecasting, category performance analysis

---

## 🎯 Business Problem Statement

In the competitive e-commerce landscape, understanding revenue dynamics is essential for sustainable growth and market positioning. This analysis addresses critical business questions:

### Key Business Questions
- **Revenue Trajectory**: How has overall revenue performed quarter-over-quarter and year-over-year?
- **Category Performance**: Which product categories are revenue champions vs. underperformers?
- **Growth Patterns**: Where are growth accelerations, slowdowns, or concerning volatility occurring?
- **Seasonal Trends**: What cyclical patterns exist that can inform inventory and marketing strategies?
- **Risk Identification**: Which quarters or categories show declining performance requiring intervention?

### Business Impact
Understanding these patterns enables:
- Strategic resource allocation across product categories
- Proactive identification of revenue risks
- Data-driven forecasting for inventory and demand planning
- Optimized marketing spend based on category performance
- Early warning system for market shifts

---

## 📂 Dataset Information

### Dataset Characteristics
- **Source**: Simulated Amazon sales data reflecting realistic e-commerce patterns
- **Time Span**: January 2020 – December 2024 (5 years)
- **Granularity**: Quarterly aggregation with drill-down to monthly details
- **Records**: [Add number of transactions/records]

### Data Schema
| Field | Description | Data Type |
|-------|-------------|-----------|
| **Order Date** | Transaction timestamp | DateTime |
| **Revenue** | Sale amount in USD | Decimal |
| **Category** | Product category classification | String |
| **Product** | Individual product identifier | String |
| **Quarter** | Fiscal quarter (Q1-Q4) | String |
| **Year** | Fiscal year | Integer |

### Data Quality Notes
- No missing values in critical fields
- Currency standardized to USD
- Outliers reviewed and validated
- Consistent category classification throughout period

---

## 🛠️ Tools & Technologies

### Primary Tools
```
Power BI Desktop
├── DAX (Data Analysis Expressions) for calculated metrics
├── Power Query for data transformation
├── Custom visualizations and KPI cards
└── Interactive drill-through capabilities

Python
├── Pandas for data manipulation and cleaning
├── Exploratory Data Analysis (EDA)
├── Data preprocessing and validation
└── Statistical analysis and profiling
```

### Key Technical Components
- **DAX Measures**: YoY Growth %, QoQ Growth %, Revenue Contribution %
- **Time Intelligence**: Date tables, quarter calculations, year comparisons
- **Conditional Formatting**: Dynamic visual cues for performance thresholds
- **Interactive Filters**: Year, quarter, category slicers for exploratory analysis

---

## 📊 Key Metrics & KPIs

### Primary Performance Indicators

**Total Revenue**: **$91.83M**  
*Aggregate revenue across entire analysis period*

**Year-over-Year Growth**: **+25%**  
*Average annual growth rate demonstrating strong performance trajectory*

**Quarter-over-Quarter Volatility**: **[Add if calculated]**  
*Measure of revenue stability across quarters*

### Supporting Metrics
- Revenue per Category
- Category Contribution % to Total Revenue
- Quarterly Growth Rate (QoQ %)
- Seasonal Index by Quarter
- Revenue Growth Momentum Score

---

## 🔍 Comprehensive Analysis & Insights

### 1️⃣ Overall Revenue Performance

**Multi-Year Trend Analysis**
- **2020**: Baseline year establishing foundation at [X]M
- **2021**: Growth acceleration phase with [Y]% increase
- **2022**: [Describe trend - continued growth/stabilization]
- **2023**: [Describe notable patterns]
- **2024**: [Current year performance]

**Key Observations**
- Revenue demonstrates overall upward trajectory with 25% YoY growth
- Quarterly fluctuations indicate seasonal demand patterns
- Periods of volatility align with external market factors (potential COVID impact in 2020-2021)
- Revenue stability improved in latter years, suggesting business maturation

### 2️⃣ Category Performance Deep Dive

**Top Performing Categories**

📱 **Electronics**
- Consistent revenue leader across all quarters
- Contributes approximately [X]% to total revenue
- Shows strong Q4 seasonal peaks (holiday shopping)
- Growth rate: [Add specific %]

🏠 **Home & Kitchen**
- Second highest revenue contributor
- Steady performance with less volatility than Electronics
- Revenue share: [X]%
- Notable growth periods: [Identify quarters]

**Other Category Insights**
- [Category 3]: Shows emerging growth potential with [X]% increase in recent quarters
- [Category 4]: Declining trend requiring strategic attention
- Seasonal categories show predictable quarterly patterns

**Category Contribution Analysis**
```
Electronics:       [X]% of total revenue
Home & Kitchen:    [Y]% of total revenue
[Other categories]: [Z]% combined
```

### 3️⃣ Growth Dynamics & Trends

**Year-over-Year Growth Patterns**
- **2021 vs 2020**: [X]% growth - [Explain drivers]
- **2022 vs 2021**: [Y]% growth - [Explain changes]
- **2023 vs 2022**: [Z]% growth - [Note trends]
- **2024 vs 2023**: [Current growth rate]

**Quarter-over-Quarter Volatility**
- Q1: Typically slower post-holiday period
- Q2: Recovery phase with [characteristic pattern]
- Q3: [Describe seasonal behavior]
- Q4: Peak season with [X]% average increase over Q3

**Critical Findings**
- YoY growth fluctuates by quarter, indicating sensitivity to market conditions
- Highest growth quarters: [List specific Q/Year combinations]
- Slowdown periods identified in [specific quarters] requiring investigation
- Growth momentum suggests [positive/cautious/concerning] outlook

### 4️⃣ Seasonal & Cyclical Patterns

**Identified Patterns**
- Strong Q4 performance driven by holiday shopping (November-December)
- Q1 revenue dips consistent with post-holiday consumer behavior
- Mid-year stability in Q2-Q3 across most categories
- Electronics category shows pronounced seasonality vs. consistent Home & Kitchen demand

---

## 💡 Strategic Business Recommendations

### 🎯 Immediate Actions (Next Quarter)

**1. Optimize High-Performing Categories**
- **Action**: Increase inventory and marketing spend for Electronics and Home & Kitchen during Q4
- **Expected Impact**: Capture additional 5-10% revenue during peak season
- **Investment Priority**: High

**2. Address Growth Slowdowns**
- **Action**: Investigate declining categories with targeted analysis
- **Focus Areas**: Customer feedback, competitive positioning, pricing strategy
- **Timeline**: Complete within 30 days

**3. Enhance Forecasting Accuracy**
- **Action**: Use established seasonal patterns for next-quarter demand planning
- **Tools**: Implement rolling forecasts based on 5-year trend data
- **Benefit**: Reduce stockouts and overstock by 15-20%

### 📊 Short-Term Initiatives (3-6 Months)

**4. Category Diversification Strategy**
- Reduce revenue concentration risk by developing underperforming categories
- Test new product lines in high-growth segments
- Target: Increase non-top-2 category contribution from [X]% to [Y]%

**5. Promotional Calendar Optimization**
- Align promotional campaigns with identified seasonal peaks
- Develop off-season engagement strategies for Q1 revenue lift
- A/B test promotional intensity in different categories

**6. Customer Segmentation by Category**
- Analyze customer behavior patterns within high-revenue categories
- Develop category-specific retention strategies
- Implement cross-selling initiatives between complementary categories

### 🚀 Long-Term Strategic Initiatives (6-12 Months)

**7. Advanced Predictive Analytics**
- Build forecasting models incorporating external factors (market trends, economic indicators)
- Develop real-time revenue dashboards for executive monitoring
- Implement automated alerts for growth anomalies

**8. Market Expansion Opportunities**
- Leverage insights from high-performing categories for market expansion
- Identify geographic or demographic segments with untapped potential
- Pilot test new categories showing early growth signals

**9. Revenue Optimization Framework**
- Establish quarterly revenue review process using this analysis as template
- Create category manager KPIs tied to growth targets
- Develop data-driven pricing strategies based on revenue patterns

---

## 🖼️ Dashboard Preview

### Revenue Performance Overview Dashboard
*Executive summary featuring total revenue, YoY growth, and quarterly trend analysis*

![Revenue Overview Dashboard](https://github.com/sangamesh-Analytics/amazon-revenue-performance-analysis/blob/main/amazon-revenuee-performance-analysis/screenshots/Ap1.png)

**Key Features**:
- Total revenue KPI card with YoY comparison
- Quarterly revenue trend line (2020-2024)
- Year-over-year growth percentage visualization
- Interactive date range filters

---

### Category Analysis & Growth Dashboard
*Deep-dive into category performance with comparative analysis and growth metrics*

![Category & Growth Analysis Dashboard](https://github.com/sangamesh-Analytics/amazon-revenue-performance-analysis/blob/main/amazon-revenuee-performance-analysis/screenshots/Ap2.png)

**Key Features**:
- Revenue by category bar chart
- Category contribution pie chart
- Quarter-over-quarter growth trends by category
- Interactive category filters for drill-down analysis

---

## 📁 Project Structure

```
amazon-revenue-analysis/
│
├── data/
│   ├── amazon_sales_data.csv
│   └── data_dictionary.md
│
├── dashboards/
│   └── amazon.pbix (Power BI file)
│
├── screenshots/
│   ├── AP1.png (Revenue Overview)
│   └── AP2.png (Category Analysis)
│
├── documentation/
│   ├── dax_measures.md
│   ├── insights_summary.pdf
│   └── methodology.md
│
└── README.md
```

---

## ▶️ Getting Started

### Prerequisites
- **Power BI Desktop** (Version 2.0 or later) - [Download here](https://powerbi.microsoft.com/desktop/)
- **Python 3.x** (with pandas library for viewing/analyzing source data)
- Basic understanding of business metrics (revenue, growth rates)

### Installation & Usage

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/amazon-revenue-analysis.git
   cd amazon-revenue-analysis
   ```

2. **Open the Dashboard**
   - Navigate to `dashboards/` folder
   - Double-click `amazon.pbix` to open in Power BI Desktop

3. **Explore the Analysis**
   - Use the interactive filters (Year, Quarter, Category) to drill down
   - Hover over visualizations for detailed tooltips
   - Click on data points for cross-filtering across visuals

4. **Refresh Data** (Optional)
   - If you update the source CSV: Home → Refresh
   - Power BI will reload and recalculate all metrics

### Dashboard Navigation Tips
- Start with the **Revenue Overview** page for executive summary
- Navigate to **Category Analysis** for detailed breakdowns
- Use the **Reset** button to clear all filters
- Export visuals using the "..." menu on any chart

---

## 📖 Methodology

### Data Preparation Process

**1. Exploratory Data Analysis (Python)**
- Conducted initial EDA using pandas for data profiling
- Statistical analysis of revenue distributions and patterns
- Data quality checks and validation
- Outlier detection and treatment

**2. Data Transformation**
- Created Date dimension table for time intelligence
- Generated calculated columns: Quarter, Year, Month Name
- Established relationships between fact and dimension tables

**3. Metric Development**
```dax
Total Revenue = SUM('Sales'[Revenue])

YoY Growth % = 
DIVIDE(
    [Total Revenue] - CALCULATE([Total Revenue], SAMEPERIODLASTYEAR('Date'[Date])),
    CALCULATE([Total Revenue], SAMEPERIODLASTYEAR('Date'[Date])),
    0
)

QoQ Growth % = 
DIVIDE(
    [Total Revenue] - CALCULATE([Total Revenue], DATEADD('Date'[Date], -1, QUARTER)),
    CALCULATE([Total Revenue], DATEADD('Date'[Date], -1, QUARTER)),
    0
)

Category Contribution % = 
DIVIDE(
    [Total Revenue],
    CALCULATE([Total Revenue], ALL('Sales'[Category])),
    0
)
```

### Analysis Framework

**Step 1: Trend Identification**
- Time series analysis of quarterly revenue
- Pattern recognition for seasonal effects
- Anomaly detection for unusual fluctuations

**Step 2: Comparative Analysis**
- Year-over-year comparisons across all quarters
- Category benchmarking against total revenue
- Growth rate variance analysis

**Step 3: Insight Generation**
- Statistical correlation between categories and time periods
- Root cause analysis for performance variations
- Predictive pattern identification

---

## 📊 Key Takeaways

### Business Value Delivered

✅ **Comprehensive Revenue Understanding**: Complete visibility into 5-year performance trends

✅ **Category Strategy Insights**: Data-driven identification of high-value product categories

✅ **Growth Monitoring Framework**: Early warning system for revenue slowdowns

✅ **Seasonal Intelligence**: Actionable patterns for demand and inventory planning

✅ **Executive Decision Support**: Clear, interactive dashboards for strategic planning

### Skills Demonstrated

- **Business Analytics**: Revenue analysis, trend identification, KPI development
- **Data Visualization**: Creating executive-level dashboards with Power BI
- **Python & EDA**: Data exploration, cleaning, and preprocessing with pandas
- **DAX Proficiency**: Complex time intelligence and growth calculations
- **Business Acumen**: Translating data into strategic recommendations
- **Storytelling**: Presenting complex data in accessible, actionable format

---

## 🎓 Lessons Learned

### Technical Insights
- Importance of proper date tables for time intelligence functions
- Value of calculated measures vs. calculated columns for performance
- Power of interactive filters for exploratory analysis

### Business Insights
- Seasonal patterns are strong predictors of future performance
- Category diversification reduces overall revenue risk
- Early identification of trend changes enables proactive management

### Future Enhancements
- Integrate external data (market trends, competitor analysis)
- Add predictive forecasting models
- Incorporate customer segmentation analysis
- Develop mobile-optimized dashboard version

---

## 🔗 Connect & Collaborate

**Sangamesh Dadge**  
📧 Email: sangameshdadge2003@gmail.com  
💼 LinkedIn: https://www.linkedin.com/in/sangamesh-dadge-736050251/ 
🐙 GitHub: sangamesh-Analytics
📊 Portfolio: [Your Portfolio Website]

**Interested in discussing this project or potential opportunities?** I'm always open to conversations about data analytics, business intelligence, and data-driven decision-making.

---

## 📝 License

This project is available for educational and portfolio purposes. Feel free to reference the methodology, but please provide appropriate attribution.

---

## 🙏 Acknowledgments

- **Dataset**: Simulated data reflecting realistic e-commerce patterns
- **Tools**: Microsoft Power BI Desktop, Python (pandas)
- **Inspiration**: Real-world business analytics challenges in e-commerce

---

## 📌 Version History

- **v1.0** (Current) - Initial analysis covering 2020-2024
- Future updates will incorporate additional years and enhanced analytics

---

<div align="center">

**⭐ If this analysis provided valuable insights, please consider starring this repository!**

*Transforming data into decisions, one dashboard at a time.*

---

**Last Updated**: January 2026

</div>
