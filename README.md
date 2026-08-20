# Tata Virtual Internship - Data Visualisation Project

An end-to-end data analysis and visualization project built using Microsoft Power BI on the Online Retail transaction dataset.

---

## 📊 Business Questions & Visual Insights

### 1. Monthly Revenue Trend (2011)
Analysis of monthly revenue growth throughout 2011 to identify seasonal peaks and sales trajectory.
![Monthly Revenue](images/Q1_Trend.png)

### 2. Top 10 Countries by Revenue & Quantity (Excl. UK)
Side-by-side comparison of total units sold versus revenue generated across top-performing international markets.
![Top 10 Countries](images/Q2_TopCountries.png)

### 3. Top 10 Customers by Revenue
Identification and ranking of the highest-spending customers (excluding unassigned guest IDs).
![Top 10 Customers](images/Q3_TopCustomers.png)

### 4. Global Unit Demand Map (Excl. UK)
Geographic distribution of order volumes across international territories to support global expansion planning.
![Global Map](images/Q4_GlobalMap.png)

---

## 🛠️ Data Cleaning & Transformations
- Filtered out negative transaction quantities (returns/cancellations) and zero unit prices ($Quantity > 0$, $UnitPrice > 0$).
- Created custom calculated column: `Revenue = Quantity * UnitPrice`.
- Handled missing and unassigned `CustomerID` entries.
- Filtered geographic outliers (UK domestic volume) to focus on international market expansion.

---

## 📁 Repository Structure
- `Tata_Data_Visualisation_Task.pbix`: Power BI source report
- `Online Retail Data Set.xlsx`: Source dataset
- `Report.pdf`: Exported multi-page report
- `images/`: Visual assets for documentation
