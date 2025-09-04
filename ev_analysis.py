# ev_analysis.py
# Electric Vehicle Sales in India - Data Analysis Project

# === Imports ===
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# === Load Dataset ===
df = pd.read_csv("Electric Vehicle Sales by State in India.csv")

# === Basic Overview ===
print("Shape:", df.shape)  # rows, columns
print("Unique Columns:", df.columns.nunique())
print("Columns:", df.columns.tolist())
print("\nHead of Data:")
print(df.head())
print("\nTail of Data:")
print(df.tail())

# === Year Distribution ===
print("\nYear-wise counts:")
print(df["Year"].value_counts())

# === State Distribution ===
print("\nState-wise counts:")
print(df["State"].value_counts())

# === Vehicle Classes ===
print("\nVehicle Class distribution:")
print(df["Vehicle_Class"].value_counts())

# === Vehicle Categories ===
print("\nVehicle Category distribution:")
print(df["Vehicle_Category"].value_counts())

# === Vehicle Types ===
print("\nVehicle Type distribution:")
print(df["Vehicle_Type"].value_counts())

# === Descriptive Stats ===
print("\nDescriptive Statistics:")
print(df.drop(columns=["Year"]).describe())

# === Check for Duplicates & Missing Values ===
print("\nDuplicate rows:", df.duplicated().sum())
print("\nMissing Values:\n", df.isnull().sum())

# === Data Types ===
print("\nOriginal Data Info:")
print(df.info())

# === Fix datatypes ===
df["Year"] = df["Year"].astype(int)
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

categorical_columns = ["Month_Name", "State", "Vehicle_Class", "Vehicle_Category", "Vehicle_Type"]
df[categorical_columns] = df[categorical_columns].astype("category")

print("\nAfter Cleaning Data Info:")
print(df.info())

# === Visualizations ===

# Yearly EV Sales Trend
plt.figure(figsize=(6,4))
plt.title("Yearly Analysis of EV Sales in India")
sns.lineplot(x="Year", y="EV_Sales_Quantity", data=df, marker="o", color="b")
plt.xlabel("Year")
plt.ylabel("EV Sales")
plt.tight_layout()
plt.show()

# Monthly EV Sales Trend
plt.figure(figsize=(6,4))
plt.title("Monthly Analysis of EV Sales in India")
sns.lineplot(x="Month_Name", y="EV_Sales_Quantity", data=df, marker="o", color="r")
plt.xlabel("Month")
plt.ylabel("EV Sales")
plt.tight_layout()
plt.show()

# State-wise EV Sales
plt.figure(figsize=(10,7))
plt.title("State-Wise Analysis of EV Sales")
sns.barplot(y="State", x="EV_Sales_Quantity", data=df, dodge=False, palette="bright")
plt.xlabel("EV Sales")
plt.ylabel("States")
plt.tight_layout()
plt.show()

# Vehicle Class Analysis
plt.figure(figsize=(15,4))
sns.barplot(x="Vehicle_Class", y="EV_Sales_Quantity", data=df, palette="bright")
plt.title("Analysis by Vehicle Class")
plt.xlabel("Vehicle Class")
plt.ylabel("EV Sales")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Vehicle Category Analysis
plt.figure(figsize=(6,4))
sns.barplot(x="Vehicle_Category", y="EV_Sales_Quantity", data=df, palette="bright")
plt.title("Analysis by Vehicle Category")
plt.xlabel("Vehicle Category")
plt.ylabel("EV Sales")
plt.tight_layout()
plt.show()

# Vehicle Type Analysis
plt.figure(figsize=(10,4))
sns.barplot(x="Vehicle_Type", y="EV_Sales_Quantity", data=df, palette="bright")
plt.title("Analysis by Vehicle Type")
plt.xlabel("Vehicle Type")
plt.ylabel("EV Sales")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
