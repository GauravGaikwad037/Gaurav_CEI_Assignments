# 🛍️ Week 1 – Shopping Dataset Exploration & Data Cleaning using Pandas

## 📌 Objective

The objective of this assignment is to understand the fundamentals of Python and Pandas by performing data loading, exploration, preprocessing, and cleaning operations on multiple shopping dataset CSV files. The assignment demonstrates practical data manipulation skills that are essential for data analysis and machine learning workflows.

---

## 🚀 Technologies Used

* Python 3.13
* Pandas
* OS Module
* Jupyter Notebook
* Visual Studio Code

---

## 📂 Project Structure

```
Week_1/
│
├── data/
│   ├── raw/
│   │   ├── *.csv
│   │   └── (Shopping Dataset Files)
│   │
│   └── cleaned/
│       └── cleaned_shopping_dataset.csv
│
├── week1.ipynb
└── README.md
```

---

## 📊 Tasks Performed

### ✅ Data Loading

* Loaded all shopping dataset CSV files from the `data/raw` directory.
* Combined multiple datasets into a single Pandas DataFrame for unified analysis.

### ✅ Data Exploration

Performed exploratory analysis using:

* `head()`
* `tail()`
* `shape`
* `columns`
* `dtypes`

to understand the dataset structure and contents.

### ✅ Missing Value Handling

* Identified missing values across all columns.
* Filled missing categorical values with `"Unknown"`.
* Filled missing numerical values with `0`.

### ✅ Data Cleaning

* Removed duplicate records.
* Improved dataset consistency for further analysis.

### ✅ Basic Data Operations

* Selected important columns for inspection.
* Filtered products based on rating conditions.

### ✅ Feature Engineering

Created new columns:

* `quantity`
* `total_amount = final_price × quantity`

to demonstrate derived feature creation.

### ✅ Export

Saved the cleaned and processed dataset as:

```
data/cleaned/cleaned_shopping_dataset.csv
```

---

## 📈 Outcome

Successfully performed end-to-end preprocessing and cleaning of multiple shopping datasets using Pandas, including:

* Data loading
* Data exploration
* Missing value handling
* Duplicate removal
* Row filtering
* Column selection
* Derived feature creation
* Cleaned dataset export

---

## 💡 Key Learning

Through this assignment, I gained hands-on experience in:

* Working with multiple CSV files
* Using Pandas for real-world data manipulation
* Data preprocessing techniques
* Feature engineering
* Preparing datasets for downstream analytics and machine learning tasks

---

## 👨‍💻 Author

**Gaurav Gaikwad**

B.Tech – Information Technology
