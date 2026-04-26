# app.py
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from io import BytesIO

st.set_page_config(page_title="CSV Cleaner + EDA", layout="wide")

st.title("📊 CSV Data Cleaner & EDA Tool")
st.markdown("*Advanced data cleaning and exploratory data analysis*")

# Upload file
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df_original = df.copy()

    # Create tabs for organization
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["📊 Overview", "🧹 Data Cleaning", "📈 EDA", "🎨 Advanced Visualizations", "⬇️ Export"])

    # ==================== TAB 1: OVERVIEW ====================
    with tab1:
        st.subheader("🔍 Raw Data Preview")
        st.dataframe(df.head(10))

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Rows", df.shape[0])
        col2.metric("Columns", df.shape[1])
        col3.metric("Duplicate Rows", df.duplicated().sum())
        col4.metric("Memory Usage", f"{df.memory_usage().sum() / 1024:.2f} KB")

        # Data Types
        st.subheader("📋 Column Data Types")
        dtype_df = pd.DataFrame({
            'Column': df.columns,
            'Data Type': df.dtypes,
            'Non-Null Count': df.count(),
            'Null Count': df.isnull().sum()
        })
        st.dataframe(dtype_df, use_container_width=True)

        # Missing Values Analysis
        st.subheader("❗ Missing Values Analysis")
        missing_data = pd.DataFrame({
            'Column': df.columns,
            'Missing Count': df.isnull().sum(),
            'Missing %': (df.isnull().sum() / len(df) * 100).round(2)
        })
        missing_data = missing_data[missing_data['Missing Count'] > 0].sort_values('Missing Count', ascending=False)
        
        if not missing_data.empty:
            st.dataframe(missing_data, use_container_width=True)
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.bar(missing_data['Column'], missing_data['Missing %'])
            ax.set_xlabel('Columns')
            ax.set_ylabel('Missing %')
            ax.set_title('Missing Values Distribution')
            plt.xticks(rotation=45, ha='right')
            st.pyplot(fig)
        else:
            st.success("✅ No missing values found!")

    # ==================== TAB 2: DATA CLEANING ====================
    with tab2:
        st.subheader("🧹 Data Cleaning Operations")
        
        cleaning_col1, cleaning_col2 = st.columns(2)
        
        with cleaning_col1:
            st.write("**Step 1: Remove Duplicates**")
            if st.checkbox("Drop duplicate rows"):
                df = df.drop_duplicates()
                st.success(f"✅ Duplicates removed! Remaining rows: {len(df)}")
            
            st.write("**Step 2: Handle Missing Values**")
            if st.checkbox("Fill missing values"):
                strategy = st.selectbox("Select filling method", ["Mean", "Median", "Mode", "Forward Fill", "Backward Fill", "Drop"])
                
                if strategy == "Drop":
                    df = df.dropna()
                    st.success("✅ Rows with missing values removed!")
                else:
                    for col in df.select_dtypes(include=np.number).columns:
                        if df[col].isnull().sum() > 0:
                            if strategy == "Mean":
                                df[col].fillna(df[col].mean(), inplace=True)
                            elif strategy == "Median":
                                df[col].fillna(df[col].median(), inplace=True)
                            elif strategy == "Mode":
                                mode_val = df[col].mode()[0] if len(df[col].mode()) > 0 else df[col].mean()
                                df[col].fillna(mode_val, inplace=True)
                            elif strategy == "Forward Fill":
                                df[col] = df[col].ffill()
                            elif strategy == "Backward Fill":
                                df[col] = df[col].bfill()
                    st.success(f"✅ Missing values filled using {strategy}")
        
        with cleaning_col2:
            st.write("**Step 3: Handle Outliers**")
            if st.checkbox("Remove outliers (IQR method)"):
                numeric_cols = df.select_dtypes(include=np.number).columns
                outliers_removed = 0
                
                for col in numeric_cols:
                    Q1 = df[col].quantile(0.25)
                    Q3 = df[col].quantile(0.75)
                    IQR = Q3 - Q1
                    lower_bound = Q1 - 1.5 * IQR
                    upper_bound = Q3 + 1.5 * IQR
                    
                    outliers_mask = (df[col] < lower_bound) | (df[col] > upper_bound)
                    outliers_removed += outliers_mask.sum()
                    df = df[~outliers_mask]
                
                st.success(f"✅ {outliers_removed} outliers removed!")
            
            st.write("**Step 4: Handle Whitespace**")
            if st.checkbox("Remove leading/trailing whitespace"):
                for col in df.select_dtypes(include='object').columns:
                    df[col] = df[col].str.strip()
                st.success("✅ Whitespace removed from text columns!")
        
        st.write("**Step 5: Data Type Conversion**")
        cols_to_convert = st.multiselect("Select columns to convert", df.columns)
        
        if cols_to_convert:
            new_type = st.selectbox("Convert to:", ["int", "float", "string", "category", "datetime"])
            
            if st.button("Convert Selected Columns"):
                try:
                    for col in cols_to_convert:
                        if new_type == "datetime":
                            df[col] = pd.to_datetime(df[col], errors='coerce')
                        elif new_type == "int":
                            df[col] = pd.to_numeric(df[col], errors='coerce').astype(np.int64)
                        elif new_type == "float":
                            df[col] = pd.to_numeric(df[col], errors='coerce').astype(np.float64)
                        elif new_type == "string":
                            df[col] = df[col].astype("string")
                        elif new_type == "category":
                            df[col] = df[col].astype("category")
                    st.success(f"✅ Columns converted to {new_type}")
                except Exception as e:
                    st.error(f"❌ Conversion failed: {str(e)}")

    with tab3:
        st.subheader("📈 Exploratory Data Analysis")
        
        numeric_df = df.select_dtypes(include=np.number)
        categorical_df = df.select_dtypes(include='object')
        
        # Summary Statistics
        st.write("**Summary Statistics**")
        st.dataframe(df.describe().T, use_container_width=True)
        
        # Skewness and Kurtosis
        if not numeric_df.empty:
            st.write("**Distribution Characteristics**")
            dist_data = []
            for col in numeric_df.columns:
                dist_data.append({
                    'Column': col,
                    'Skewness': stats.skew(numeric_df[col].dropna()),
                    'Kurtosis': stats.kurtosis(numeric_df[col].dropna()),
                    'Mean': numeric_df[col].mean(),
                    'Std Dev': numeric_df[col].std()
                })
            
            dist_df = pd.DataFrame(dist_data)
            st.dataframe(dist_df, use_container_width=True)
        
        # Correlation Analysis
        if not numeric_df.empty:
            st.subheader("🔥 Correlation Analysis")
            corr = numeric_df.corr()
            
            fig, ax = plt.subplots(figsize=(10, 8))
            sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', center=0, ax=ax)
            ax.set_title('Correlation Matrix')
            st.pyplot(fig)
            
            # Highly correlated pairs
            st.write("**Highly Correlated Pairs (>0.7)**")
            corr_pairs = []
            try:
                corr_values = corr.values
                for i in range(len(corr.columns)):
                    for j in range(i+1, len(corr.columns)):
                        try:
                            corr_value = float(corr_values[i, j])
                            if abs(corr_value) > 0.7:
                                corr_pairs.append({
                                    'Feature 1': str(corr.columns[i]),
                                    'Feature 2': str(corr.columns[j]),
                                    'Correlation': round(corr_value, 4)
                                })
                        except (TypeError, ValueError):
                            continue
            except Exception as e:
                st.warning(f"⚠️ Could not compute all correlations: {str(e)}")
            
            if corr_pairs:
                st.dataframe(pd.DataFrame(corr_pairs), use_container_width=True)
            else:
                st.info("💡 No highly correlated pairs found (threshold > 0.7)")
        
        # Categorical Analysis
        if not categorical_df.empty:
            st.subheader("🏷️ Categorical Data Analysis")
            try:
                cat_col = st.selectbox("Select categorical column", categorical_df.columns)
                
                value_counts = df[cat_col].value_counts()
                st.write(f"**Unique values: {df[cat_col].nunique()}**")
                st.dataframe(value_counts, use_container_width=True)
                
                # Limit to top 20 categories for visualization
                if len(value_counts) > 20:
                    st.info(f"📊 Showing top 20 of {len(value_counts)} categories")
                    value_counts = value_counts.head(20)
                
                fig, ax = plt.subplots(figsize=(10, 5))
                value_counts.plot(kind='bar', ax=ax)
                ax.set_title(f'Distribution of {cat_col}')
                ax.set_xlabel(cat_col)
                ax.set_ylabel('Count')
                plt.xticks(rotation=45, ha='right')
                plt.tight_layout()
                st.pyplot(fig)
            except Exception as e:
                st.error(f"❌ Error in categorical analysis: {str(e)}")

    # ==================== TAB 4: ADVANCED VISUALIZATIONS ====================
    with tab4:
        st.subheader("🎨 Advanced Visualizations")
        
        numeric_cols = numeric_df.columns.tolist()
        
        if numeric_cols:
            # Box Plot
            st.write("**Box Plot - Outlier Detection**")
            try:
                box_col = st.selectbox("Select column for box plot", numeric_cols)
                
                fig, ax = plt.subplots(figsize=(10, 5))
                box_data = [df[numeric_cols].dropna()]
                ax.boxplot(box_data[0])
                ax.set_xticklabels(numeric_cols)
                ax.set_title('Box Plot - All Numeric Columns')
                plt.xticks(rotation=45, ha='right')
                plt.tight_layout()
                st.pyplot(fig)
            except Exception as e:
                st.error(f"❌ Error generating box plot: {str(e)}")
            
            # Distribution Plot
            st.write("**Distribution Analysis**")
            try:
                dist_col = st.selectbox("Select column for distribution", numeric_cols, key="dist_col")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    fig, ax = plt.subplots(figsize=(8, 5))
                    data_to_plot = df[dist_col].dropna()
                    if len(data_to_plot) > 0:
                        ax.hist(data_to_plot, bins=30, edgecolor='black', alpha=0.7)
                        ax.set_title(f'Histogram of {dist_col}')
                        ax.set_xlabel(dist_col)
                        ax.set_ylabel('Frequency')
                        st.pyplot(fig)
                    else:
                        st.warning(f"⚠️ No valid data for {dist_col}")
                
                with col2:
                    fig, ax = plt.subplots(figsize=(8, 5))
                    data_to_plot = df[dist_col].dropna()
                    if len(data_to_plot) > 0:
                        data_to_plot.plot(kind='density', ax=ax)
                        ax.set_title(f'Density Plot of {dist_col}')
                        ax.set_xlabel(dist_col)
                        plt.tight_layout()
                        st.pyplot(fig)
                    else:
                        st.warning(f"⚠️ No valid data for {dist_col}")
            except Exception as e:
                st.error(f"❌ Error generating distribution plots: {str(e)}")
            
            # Scatter Plot
            st.write("**Scatter Plot Analysis**")
            try:
                if len(numeric_cols) >= 2:
                    scatter_cols = st.multiselect("Select two columns for scatter plot", numeric_cols, default=numeric_cols[:2], max_selections=2)
                    
                    if len(scatter_cols) == 2:
                        scatter_data = df[scatter_cols].dropna()
                        
                        if len(scatter_data) > 0:
                            fig, ax = plt.subplots(figsize=(10, 6))
                            ax.scatter(scatter_data[scatter_cols[0]], scatter_data[scatter_cols[1]], alpha=0.6)
                            ax.set_xlabel(scatter_cols[0])
                            ax.set_ylabel(scatter_cols[1])
                            ax.set_title(f'Scatter Plot: {scatter_cols[0]} vs {scatter_cols[1]}')
                            plt.tight_layout()
                            st.pyplot(fig)
                        else:
                            st.warning("⚠️ No valid data for scatter plot")
            except Exception as e:
                st.error(f"❌ Error generating scatter plot: {str(e)}")
            
            # Pair Plot (for limited columns)
            st.write("**Pair Plot**")
            if st.checkbox("Generate Pair Plot (for up to 5 numeric columns)"):
                cols_for_pairplot = st.multiselect("Select columns for pair plot", numeric_cols, max_selections=5)
                
                if cols_for_pairplot and len(cols_for_pairplot) >= 2:
                    try:
                        # Check for missing values
                        subset_df = df[cols_for_pairplot].dropna()
                        
                        if len(subset_df) == 0:
                            st.warning("⚠️ No valid data available after removing missing values")
                        else:
                            # Generate pairplot and extract the underlying figure
                            pairgrid = sns.pairplot(subset_df, diag_kind='hist', plot_kws={'alpha': 0.6})
                            # Extract matplotlib figure from PairGrid
                            matplotlib_figure = pairgrid.figure
                            st.pyplot(matplotlib_figure)
                    except Exception as e:
                        st.error(f"❌ Error generating pair plot: {str(e)}")
                        st.info("💡 Tip: Ensure selected columns have numeric data without too many unique values")
            
            # Violin Plot
            st.write("**Violin Plot - Distribution Comparison**")
            if len(categorical_df.columns) > 0 and len(numeric_cols) > 0:
                try:
                    violin_cat = st.selectbox("Select categorical column", categorical_df.columns, key="violin_cat")
                    violin_num = st.selectbox("Select numeric column", numeric_cols, key="violin_num")
                    
                    # Check for missing values in selected columns
                    plot_data = df[[violin_cat, violin_num]].dropna()
                    
                    if len(plot_data) == 0:
                        st.warning("⚠️ No valid data available for violin plot")
                    else:
                        fig, ax = plt.subplots(figsize=(10, 6))
                        sns.violinplot(data=plot_data, x=violin_cat, y=violin_num, ax=ax)
                        ax.set_title(f'Violin Plot: {violin_num} by {violin_cat}')
                        plt.xticks(rotation=45, ha='right')
                        st.pyplot(fig)
                except Exception as e:
                    st.error(f"❌ Error generating violin plot: {str(e)}")
        else:
            st.warning("No numeric columns available for visualizations")

    # ==================== TAB 5: EXPORT ====================
    with tab5:
        st.subheader("⬇️ Download Cleaned Data")
        
        col1, col2 = st.columns(2)
        
        with col1:
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Download as CSV",
                data=csv,
                file_name='cleaned_data.csv',
                mime='text/csv',
            )
        
        with col2:
            excel_buffer = BytesIO()
            df.to_excel(excel_buffer, index=False, engine='openpyxl')
            excel_buffer.seek(0)
            st.download_button(
                label="📥 Download as Excel",
                data=excel_buffer.getvalue(),
                file_name='cleaned_data.xlsx',
                mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            )
        
        # Data Quality Report
        st.subheader("📋 Data Quality Report")
        
        report = {
            'Total Rows': len(df),
            'Total Columns': len(df.columns),
            'Duplicate Rows Removed': len(df_original) - len(df),
            'Missing Values': df.isnull().sum().sum(),
            'Memory Usage (KB)': df.memory_usage().sum() / 1024
        }
        
        for key, value in report.items():
            st.metric(key, value)
        
        # Export Report as Text
        report_text = f"""
DATA QUALITY REPORT
==================

Original Dataset:
  - Rows: {len(df_original)}
  - Columns: {len(df_original.columns)}

Cleaned Dataset:
  - Rows: {len(df)}
  - Columns: {len(df.columns)}
  - Rows Removed: {len(df_original) - len(df)}
  - Memory Usage: {df.memory_usage().sum() / 1024:.2f} KB
  - Total Missing Values: {df.isnull().sum().sum()}

Column Details:
{dtype_df.to_string()}
        """
        
        st.download_button(
            label="📄 Download Report as Text",
            data=report_text,
            file_name='data_quality_report.txt',
            mime='text/plain',
        )