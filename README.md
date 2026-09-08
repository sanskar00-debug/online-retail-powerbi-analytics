# Tata Virtual Internship - Data Visualisation Project
An end-to-end data analysis and visualization project built using Microsoft Power BI on the Online Retail transaction dataset.

![Tableau](https://img.shields.io/badge/Tableau-E97627?style=for-the-badge&logo=Tableau&logoColor=white)
![Excel](https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-8.0+-00758F?style=for-the-badge&logo=mysql&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-Desktop-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Python](https://img.shields.io/badge/Python-3.14.7-blue?style=for-the-badge&logo=Python)
![Analytics](https://img.shields.io/badge/Data_Analytics-red?style=for-the-badge)
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

  ### 📊 Interactive Dashboard File
The complete data transformation pipeline, data models, and interactive visualizations are saved in the project file. 

👉 **[Click Here to Download the Power BI Project File (.pbix)](./The%20Power%20BI%20File/Tata_Data_Visualisation_Task.pbix)**  
*(To view this file, download it and open it locally using Power BI Desktop)*

---

### 📷 Visual Dashboard Preview
*If you do not have Power BI Desktop installed, here is a preview of the dynamic interface:*

![Dashboard View](./Visual%20Previews/Tata_Data_Visualisation_Task.png)
