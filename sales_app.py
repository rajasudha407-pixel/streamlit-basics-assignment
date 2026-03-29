# --- Task 1: build the app ---
import streamlit as st
import pandas as pd
# Title and subheader
st.title("📊 Sales Summary Dashboard")
st.subheader("Filter and visualize sales data by category")
# Hardcoded dataset (5 rows, 3 columns)
data = {
    "Product": ["Laptop", "Phone", "Tablet", "Headphones", "Monitor"],
    "Category": ["Electronics", "Electronics", "Electronics", "Accessories", "Electronics"],
    "Sales": [50000, 30000, 20000, 10000, 25000]
}
df = pd.DataFrame(data)

# --- Task 2: Sidebar filter ---
st.sidebar.header("Filter Options")
categories = df["Category"].unique()
selected_category = st.sidebar.selectbox("Select Category", categories)
# Filter data
filtered_df = df[df["Category"] == selected_category]
# --- Main Content ---
st.write("### Filtered Sales Data")
st.dataframe(filtered_df)
# Line chart (as required)
st.write("### Sales Trend")
st.line_chart(filtered_df.set_index("Product")["Sales"])
