import pandas as pd

# Load dataset
df = pd.read_csv("Sample - Superstore.csv", encoding='latin1')

# =========================
# DATA PREVIEW
# =========================
print("=== DATA PREVIEW ===")
print(df.head())

# =========================
# KEY PERFORMANCE METRICS
# =========================
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()

print("\n=== BUSINESS KPIs ===")
print(f"Total Sales: {total_sales:.2f}")
print(f"Total Profit: {total_profit:.2f}")
print(f"Total Orders: {total_orders}")

# =========================
# REGION PERFORMANCE
# =========================
region_sales = df.groupby("Region")["Sales"].sum()
print("\n=== SALES BY REGION ===")
print(region_sales)

# =========================
# CATEGORY PERFORMANCE
# =========================
category_profit = df.groupby("Category")["Profit"].sum()
print("\n=== PROFIT BY CATEGORY ===")
print(category_profit)

# =========================
# SEGMENT ANALYSIS
# =========================
segment_sales = df.groupby("Segment")["Sales"].sum()
print("\n=== SALES BY SEGMENT ===")
print(segment_sales)

# =========================
# LOSS ANALYSIS
# =========================
loss_categories = category_profit[category_profit < 0]

print("\n=== LOSS-MAKING CATEGORIES ===")
if len(loss_categories) > 0:
    print(loss_categories)
else:
    print("No categories are in loss")

# =========================
# TOP PERFORMERS
# =========================
top_region = region_sales.idxmax()
top_segment = segment_sales.idxmax()
worst_category = category_profit.idxmin()

# =========================
# BUSINESS INSIGHTS
# =========================
print("\n=== BUSINESS INSIGHTS ===")
print(f"Top performing region: {top_region}")
print(f"Top customer segment: {top_segment}")
print(f"Lowest profit category: {worst_category}")

if len(loss_categories) > 0:
    print("Some categories are running at a loss → cost optimization needed.")
else:
    print("Overall business is profitable.")

# =========================
# SAVE SUMMARY REPORT
# =========================
summary = pd.DataFrame({
    "Metric": ["Total Sales", "Total Profit", "Total Orders"],
    "Value": [total_sales, total_profit, total_orders]
})

summary.to_csv("summary_report.csv", index=False)

print("\n✅ Report saved as 'summary_report.csv'")