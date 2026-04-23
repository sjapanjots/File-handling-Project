# app.py

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="CSV Cleaner + EDA", layout="wide")

st.title("📊 CSV Data Cleaner & EDA Tool")

# Upload file
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("🔍 Raw Data Preview")
    st.dataframe(df.head())

    # Basic Info
    st.subheader("📌 Dataset Info")
    col1, col2, col3 = st.columns(3)
    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])
    col3.metric("Duplicate Rows", df.duplicated().sum())

    # Missing Values
    st.subheader("❗ Missing Values")
    missing = df.isnull().sum()
    st.dataframe(missing[missing > 0])

    # Cleaning Options
    st.subheader("🧹 Data Cleaning")

    if st.checkbox("Drop duplicate rows"):
        df = df.drop_duplicates()
        st.success("Duplicates removed")

    if st.checkbox("Fill missing values"):
        strategy = st.selectbox("Select method", ["Mean", "Median", "Mode"])

        for col in df.select_dtypes(include=np.number).columns:
            if strategy == "Mean":
                df[col].fillna(df[col].mean(), inplace=True)
            elif strategy == "Median":
                df[col].fillna(df[col].median(), inplace=True)
            elif strategy == "Mode":
                df[col].fillna(df[col].mode()[0], inplace=True)

        st.success(f"Missing values filled using {strategy}")

    # Updated Data Preview
    st.subheader("✅ Cleaned Data Preview")
    st.dataframe(df.head())

    # Summary Statistics
    st.subheader("📈 Summary Statistics")
    st.write(df.describe())

    # Correlation Heatmap
    st.subheader("🔥 Correlation Heatmap")

    numeric_df = df.select_dtypes(include=np.number)

    if not numeric_df.empty:
        corr = numeric_df.corr()

        fig, ax = plt.subplots()
        cax = ax.matshow(corr)
        plt.colorbar(cax)

        ax.set_xticks(range(len(corr.columns)))
        ax.set_yticks(range(len(corr.columns)))

        ax.set_xticklabels(corr.columns, rotation=90)
        ax.set_yticklabels(corr.columns)

        st.pyplot(fig)

    else:
        st.warning("No numeric columns available for correlation.")

    # Distribution Plot
    st.subheader("📊 Feature Distribution")

    numeric_cols = numeric_df.columns.tolist()

    if numeric_cols:
        selected_col = st.selectbox("Select column", numeric_cols)

        fig, ax = plt.subplots()
        ax.hist(df[selected_col], bins=20)
        ax.set_title(f"Distribution of {selected_col}")
        st.pyplot(fig)

    # Download cleaned file
    st.subheader("⬇️ Download Cleaned Data")

    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name='cleaned_data.csv',
        mime='text/csv',
    )