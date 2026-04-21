import streamlit as st
import pandas as pd

# Load dataset
df = pd.read_csv("sales_data.csv", parse_dates=["Order_Date"])
df["Month"] = df["Order_Date"].dt.month

st.title("SAP O2C Analytics Dashboard")

# --- KPI Metrics ---
st.subheader("Key Performance Indicators (KPIs)")
avg_order_value = df["Revenue"].mean()
paid_ratio = (df["Payment_Status"] == "Paid").mean() * 100
total_revenue = df["Revenue"].sum()

col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"${total_revenue:,.2f}")
col2.metric("Average Order Value", f"${avg_order_value:,.2f}")
col3.metric("Paid Orders %", f"{paid_ratio:.1f}%")

# --- Interactive Filters ---
st.sidebar.header("Filters")
selected_region = st.sidebar.selectbox("Select Region", ["All"] + list(df["Region"].unique()))
selected_customer = st.sidebar.selectbox("Select Customer", ["All"] + list(df["Customer_ID"].unique()))

filtered_df = df.copy()
if selected_region != "All":
    filtered_df = filtered_df[filtered_df["Region"] == selected_region]
if selected_customer != "All":
    filtered_df = filtered_df[filtered_df["Customer_ID"] == selected_customer]

# --- Revenue by Region ---
st.subheader("Revenue by Region")
region_revenue = filtered_df.groupby("Region")["Revenue"].sum()
st.bar_chart(region_revenue)

# --- Monthly Sales Trend ---
st.subheader("Monthly Sales Trend")
monthly_revenue = filtered_df.groupby("Month")["Revenue"].sum()
st.line_chart(monthly_revenue)

# --- Top 5 Customers ---
st.subheader("Top 5 Customers by Revenue")
customer_revenue = filtered_df.groupby("Customer_ID")["Revenue"].sum().sort_values(ascending=False).head(5)
st.bar_chart(customer_revenue)

# --- Paid vs Unpaid Orders ---
st.subheader("Paid vs Unpaid Orders")
payment_status = filtered_df["Payment_Status"].value_counts()
st.write(payment_status)
