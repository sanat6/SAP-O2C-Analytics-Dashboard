import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sales_data.csv", parse_dates=["Order_Date"])
df["Month"] = df["Order_Date"].dt.month

# Revenue by Region
region_revenue = df.groupby("Region")["Revenue"].sum()
region_revenue.plot(kind="bar", color="skyblue", title="Revenue by Region")
plt.ylabel("Total Revenue")
plt.show()

# Monthly Sales Trend
monthly_revenue = df.groupby("Month")["Revenue"].sum()
monthly_revenue.plot(kind="line", marker="o", color="green", title="Monthly Sales Trend")
plt.ylabel("Revenue")
plt.show()

# Top 5 Customers
customer_revenue = df.groupby("Customer_ID")["Revenue"].sum().sort_values(ascending=False).head(5)
customer_revenue.plot(kind="bar", color="orange", title="Top 5 Customers by Revenue")
plt.ylabel("Revenue")
plt.show()

# Paid vs Unpaid
payment_status = df["Payment_Status"].value_counts()
payment_status.plot(kind="pie", autopct='%1.1f%%', title="Paid vs Unpaid Orders")
plt.show()
