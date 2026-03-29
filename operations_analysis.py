import pandas as pd


# DATA INGESTION
# Loading real-world business dataset

df = pd.read_csv("Sample - Superstore.csv", encoding='latin1')

print("=== DATA PREVIEW ===")
print(df.head())


# KPI CALCULATION
# Evaluating overall business performance

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()

print("\n=== BUSINESS KPIs ===")
print(f"Total Sales: {total_sales:.2f}")
print(f"Total Profit: {total_profit:.2f}")
print(f"Total Orders: {total_orders}")



# REGION-WISE ANALYSIS
# Identifying top-performing regions

region_sales = df.groupby("Region")["Sales"].sum()
print("\n=== SALES BY REGION ===")
print(region_sales)



# CATEGORY ANALYSIS
# Detecting profitable and low-performing categories

category_profit = df.groupby("Category")["Profit"].sum()
print("\n=== PROFIT BY CATEGORY ===")
print(category_profit)


# SEGMENT ANALYSIS
# Understanding customer contribution

segment_sales = df.groupby("Segment")["Sales"].sum()
print("\n=== SALES BY SEGMENT ===")
print(segment_sales)



# LOSS ANALYSIS
# Identifying business inefficiencies

loss_categories = category_profit[category_profit < 0]

print("\n=== LOSS-MAKING CATEGORIES ===")
if len(loss_categories) > 0:
    print(loss_categories)
else:
    print("No categories are in loss")


# INSIGHT GENERATION
# Converting data into actionable insights

top_region = region_sales.idxmax()
top_segment = segment_sales.idxmax()
worst_category = category_profit.idxmin()

print("\n=== BUSINESS INSIGHTS ===")
print(f"Top performing region: {top_region}")
print(f"Top customer segment: {top_segment}")
print(f"Lowest profit category: {worst_category}")


# REPORTING
# Exporting summary for management use

summary = pd.DataFrame({
    "Metric": ["Total Sales", "Total Profit", "Total Orders"],
    "Value": [
        round(total_sales, 2),
        round(total_profit, 2),
        int(total_orders)
    ]
})

summary.to_csv("summary_report.csv", index=False)

print("\n✅ Report saved as 'summary_report.csv'")


# DATA VISUALIZATION
# Visualizing sales performance across regions

import matplotlib.pyplot as plt

region_sales.plot(kind='bar')
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()