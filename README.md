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

### Option 2: Deploy on Streamlit Cloud ⭐ **RECOMMENDED**

#### Prerequisites:
- GitHub account
- Streamlit account (free)

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

**Why Streamlit Cloud?** It's the official, easiest, and best-supported way to deploy Streamlit apps with zero configuration needed.

---

### ⚠️ Important: Vercel is NOT Compatible with Streamlit

**If you tried deploying to Vercel**, you'll get an error because:
- Vercel expects traditional web frameworks (Flask, Django, FastAPI)
- Streamlit is a framework designed for data apps, not REST APIs
- Streamlit requires a persistent server connection
- Vercel's serverless architecture doesn't support Streamlit's streaming protocol

**Solution**: Use **Streamlit Cloud** instead (recommended) or alternative platforms below.

---

### Option 3: Alternative Deployment Platforms

If you prefer not to use Streamlit Cloud, here are other options:

#### **Option A: Deploy on Heroku** (Requires Procfile)
Create a `Procfile` file in your project root:
```
web: streamlit run App.py --server.port=$PORT --server.address=0.0.0.0
```

Then push to Heroku:
```bash
heroku create your-app-name
git push heroku main
```

#### **Option B: Deploy on Railway**
1. Connect your GitHub repo to [Railway](https://railway.app)
2. Railway automatically detects Python projects
3. Set start command: `streamlit run App.py`
4. Deploy!

#### **Option C: Deploy on Render**
1. Go to [Render](https://render.com)
2. Create a new Web Service
3. Connect your GitHub repository
4. Set build command: `pip install -r requirements.txt`
5. Set start command: `streamlit run App.py --server.port 10000 --server.address 0.0.0.0`
6. Deploy!

#### **Option D: Deploy on AWS / Google Cloud / Azure**
These cloud platforms support Python applications but require more setup:
- **AWS EC2**: Run the app on a virtual machine
- **Google Cloud Run**: Deploy as a containerized service
- **Azure App Service**: Host as a Python app

---

**✅ BEST OPTION: Use Streamlit Cloud for the easiest deployment experience!**

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

### Issue: Streamlit Cloud Deployment Error - "installer returned a non-zero exit code"
**Solution**: This is usually caused by version conflicts. Try these steps:

1. **Clear Streamlit Cloud cache**:
   - Go to your app settings on Streamlit Cloud
   - Click "Manage app" → "Settings"
   - Scroll down and click "Reboot app"

2. **Update your local requirements.txt** (already done):
   ```
   streamlit==1.31.1
   pandas==2.1.4
   numpy==1.24.3
   matplotlib==3.8.2
   seaborn==0.13.1
   scipy==1.11.4
   openpyxl==3.11.0
   ```

3. **Push the update to GitHub**:
   ```bash
   git add requirements.txt
   git commit -m "Fix dependency versions for Streamlit Cloud"
   git push origin main
   ```

4. **Reboot your Streamlit Cloud app** from the app menu (three dots → Reboot app)

5. If it still fails, try deleting the app and redeploying:
   - Go to Streamlit Cloud dashboard
   - Delete the app
   - Redeploy by selecting your repository again

### Issue: Vercel Deployment Error - "No python entrypoint found"
**⚠️ IMPORTANT**: **Vercel does NOT support Streamlit apps!**

**Error Message**:
```
Error: No python entrypoint found. Add an 'app' script in pyproject.toml or define an entrypoint in one of: app.py, index.py, server.py, main.py, wsgi.py, asgi.py...
```

**Why?** Vercel is designed for traditional web frameworks (Flask, Django, FastAPI), not data apps like Streamlit.

**Solution**: Use **[Streamlit Cloud](https://streamlit.io/cloud)** instead (100% free and officially supported):
1. Go to https://streamlit.io/cloud
2. Connect your GitHub repository
3. Select your main file (`App.py`)
4. Click Deploy!

**Alternative Deployment Options**:
- **Heroku**, **Railway**, **Render**, **Google Cloud Run**, or **AWS** (see "Alternative Deployment Platforms" section above)

### Issue: "No numeric columns available for visualizations"
**Solution**: Your dataset might contain only text columns. Add numeric data or ensure proper data type conversion.

### Issue: Excel export not working
**Solution**: Ensure `openpyxl` is installed:
```bash
pip install openpyxl==3.11.0
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