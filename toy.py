# TOY SALES DATA ANALYSIS PROJECT
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
 
# STEP 1: CREATE / LOAD DATASET
np.random.seed(42)
categories = {"Action Figures": 450, "Board Games": 650, "Dolls": 500,
              "Puzzles": 350, "Remote Cars": 1200, "Soft Toys": 400}
n = 200
df = pd.DataFrame({
    "OrderID": range(1, n + 1),
    "Category": np.random.choice(list(categories), n),
    "Quantity": np.random.randint(1, 6, n),
    "Region": np.random.choice(["North", "South", "East", "West"], n),
})
df["UnitPrice"] = df["Category"].map(categories)
 
# STEP 2: DATA CLEANING
print("Rows before cleaning:", len(df))
df = df.drop_duplicates().dropna()
print("Rows after cleaning :", len(df))
 
# STEP 3: SALES CALCULATION
df["Sales"] = df["Quantity"] * df["UnitPrice"]
print("\nTotal Orders  :", len(df))
print("Total Units   :", df["Quantity"].sum())
print("Total Revenue : Rs.", df["Sales"].sum())
 
# STEP 4: CATEGORY-WISE SALES
cat_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
print("\nCategory-wise Sales:")
print(cat_sales.to_string())
print("\nBest selling category :", cat_sales.idxmax())
print("Least selling category:", cat_sales.idxmin())
 
# STEP 5: REGION-WISE SALES
reg_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
print("\nRegion-wise Sales:")
print(reg_sales.to_string())
 
# STEP 6: BAR GRAPH
plt.figure(figsize=(8, 5))
plt.bar(cat_sales.index, cat_sales.values, color="#2E5C8A")
plt.title("Category-wise Toy Sales")
plt.xlabel("Toy Category"); plt.ylabel("Sales (Rs.)")
plt.xticks(rotation=30); plt.tight_layout()
plt.savefig("bar_chart.png", dpi=150)
 # STEP 7: PIE CHART
plt.figure(figsize=(6, 6))
plt.pie(reg_sales.values, labels=reg_sales.index, autopct="%1.1f%%", startangle=90)
plt.title("Region-wise Share of Toy Sales")
plt.tight_layout()

plt.savefig("pie_chart.png", dpi=150)
plt.show()

print("\nGraphs saved: bar_chart.png, pie_chart.png")