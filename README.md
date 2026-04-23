# 📊 CSV Data Cleaner & EDA Tool

A comprehensive **Streamlit-based web application** for data cleaning and exploratory data analysis (EDA) with advanced visualizations. Perfect for data scientists, analysts, and anyone working with CSV files!

## 🌟 Features

### 1. **Data Overview** 📊
- Raw data preview (first 10 rows)
- Dataset statistics (rows, columns, duplicates, memory usage)
- Column data types and missing values analysis
- Visual representation of missing values distribution

### 2. **Advanced Data Cleaning** 🧹
- **Remove Duplicates** - Eliminate duplicate rows
- **Handle Missing Values** - Multiple strategies:
  - Mean, Median, Mode
  - Forward Fill (ffill)
  - Backward Fill (bfill)
  - Drop rows with missing values
- **Remove Outliers** - IQR (Interquartile Range) method
- **Clean Text** - Remove leading/trailing whitespace
- **Data Type Conversion** - Convert columns to: int, float, string, category, datetime

### 3. **Exploratory Data Analysis (EDA)** 📈
- Summary statistics (mean, median, std, min, max, quartiles)
- Distribution characteristics (Skewness, Kurtosis)
- Correlation matrix heatmap
- Highly correlated pairs detection (>0.7 threshold)
- Categorical data analysis with value counts

### 4. **Advanced Visualizations** 🎨
- **Box Plots** - Outlier detection
- **Histograms** - Feature distribution
- **Density Plots** - Probability density functions
- **Scatter Plots** - Relationship between two variables
- **Pair Plots** - Multi-feature relationships
- **Violin Plots** - Distribution comparison by category

### 5. **Data Export** ⬇️
- Download cleaned data as **CSV**
- Download cleaned data as **Excel**
- Generate and download **Data Quality Report** (text file)

## 📋 Requirements

Before you begin, ensure you have Python 3.8 or higher installed on your system.

### Dependencies:
- streamlit >= 1.28.0
- pandas >= 2.0.0
- numpy >= 1.24.0
- matplotlib >= 3.7.0
- seaborn >= 0.12.0
- scipy >= 1.10.0
- openpyxl >= 3.10.0

## 🚀 Installation & Setup

### Option 1: Local Installation

#### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/File-handling-Project.git
cd File-handling-Project
```

#### Step 2: Create a Virtual Environment (Optional but Recommended)
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

#### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

#### Step 4: Run the Application
```bash
streamlit run App.py
```

The app will open in your default browser at `http://localhost:8501`

---

### Option 2: Deploy on Streamlit Cloud

#### Prerequisites:
- GitHub account
- Streamlit account

#### Steps:
1. Push your project to GitHub:
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. Go to [Streamlit Cloud](https://streamlit.io/cloud)

3. Click **"New app"**

4. Select your GitHub repository, branch, and main file (`App.py`)

5. Click **"Deploy"**

Your app will be live and accessible via a unique Streamlit Cloud URL!

---

## 📖 How to Use

### Step 1: Upload Your CSV File
- Click on the **"Upload your CSV file"** button
- Select a CSV file from your computer

### Step 2: Explore Data (Tab 1: Overview)
- View raw data preview
- Check dataset statistics
- Analyze data types and missing values
- See visual representation of missing data

### Step 3: Clean Data (Tab 2: Data Cleaning)
- **Remove duplicates** - Check to drop duplicate rows
- **Fill missing values** - Choose a strategy (Mean, Median, Mode, ffill, bfill, or Drop)
- **Remove outliers** - Use IQR method to detect and remove statistical outliers
- **Clean text** - Remove whitespace from text columns
- **Convert data types** - Select columns and convert to desired types

### Step 4: Analyze Data (Tab 3: EDA)
- View summary statistics
- Check distribution characteristics (Skewness & Kurtosis)
- Analyze correlations between numeric columns
- Identify highly correlated pairs
- Analyze categorical data distribution

### Step 5: Visualize Data (Tab 4: Advanced Visualizations)
- **Box Plot** - Detect outliers across all numeric columns
- **Histograms & Density Plots** - Analyze feature distributions
- **Scatter Plots** - Compare relationships between two variables
- **Pair Plots** - Multi-variable relationship exploration
- **Violin Plots** - Distribution comparison by category

### Step 6: Export Results (Tab 5: Export)
- Download cleaned data as CSV
- Download cleaned data as Excel
- View data quality report
- Download detailed text report of changes

---

## 📁 Project Structure

```
File-handling-Project/
├── App.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── LICENSE               # Project license
```

---

## 💡 Tips & Best Practices

1. **Data Preview**: Always check the raw data preview first to understand your dataset
2. **Missing Values**: Choose the filling method based on your data distribution
3. **Outliers**: Be cautious when removing outliers - they might be important
4. **Correlation**: Look for highly correlated features; they might indicate multicollinearity
5. **Visualization**: Use multiple visualization types to get different perspectives on your data
6. **Export**: Download the data quality report to track all changes made

---

## ⚠️ Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'streamlit'"
**Solution**: Install dependencies using:
```bash
pip install -r requirements.txt
```

### Issue: "No numeric columns available for visualizations"
**Solution**: Your dataset might contain only text columns. Add numeric data or ensure proper data type conversion.

### Issue: Excel export not working
**Solution**: Ensure `openpyxl` is installed:
```bash
pip install openpyxl
```

### Issue: App crashes when uploading large files
**Solution**: Try with a smaller sample of your data first, or increase Streamlit's file upload limit in your configuration.

---

## 🤝 Contributing

Contributions are welcome! Please feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👨‍💻 Author

Created with ❤️ for data enthusiasts and analysts.

---

## 📞 Support

If you encounter any issues or have questions:
1. Check the Troubleshooting section above
2. Review the code comments in App.py
3. Open an issue on GitHub

---

## 🎯 Future Enhancements

Planned features for future versions:
- Machine learning model recommendations
- Advanced statistical tests
- Custom visualization themes
- Database connectivity
- Real-time data streaming
- Multi-file processing

---

Happy Data Cleaning! 🎉