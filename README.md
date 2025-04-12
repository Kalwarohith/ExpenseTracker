<h1 align="center">💼 Expense Tracker</h1>
<p align="center">📊 A Command-Line Application to Track, Categorize & Analyze Expenses</p>

<p align="center">
  🔥 Built with Python • 🧠 Designed for Expenses• 🧾 JSON-Based Storage
</p>

---

## 🧠 About the Project

Welcome to the **Expense Tracker**, developed as part of **Week 3 of the Python Programming Internship**. This project is aimed at helping me understand file handling, data analysis, user interaction, and modular Python programming — all wrapped into one real-world application. 💡

---

## 🚀 Features

✅ Add daily expenses with description, amount, and category  
📂 Store data persistently using `expenses.json`  
📊 View total spent in the current month  
📑 Get a summary of category-wise spending  
🧾 Simple command-line interface  
🛡️ Error handling for user input  
🧩 Modular codebase and detailed comments  

---

## 🛠️ Tech Stack

| 💡 Component         | 🔍 Purpose                          |
|----------------------|-------------------------------------|
| 🐍 Python 3.x         | Core programming language           |
| 📁 JSON               | Data storage                        |
| ⏱️ `datetime`         | Timestamps for expense entries       |
| 📊 `collections`      | Data grouping for analysis           |

---

## 📁 Folder Structure
expense_tracker/                # 📁 Main project folder
│
├── main.py                    # 🎮 App entry point & CLI menu
├── data_handler.py            # 📁 Handles reading/writing to expenses.json
├── analysis.py                # 📊 Functions for summaries & insights
├── expenses.json              # 🗃️ Stored expense data (auto-generated)
├── README.md                  # 📄 Project documentation
└── requirements.txt (optional) # 📦 List of required Python packages

output:
==== Expense Tracker ====

1️⃣  Add Expense
2️⃣  View Monthly Summary
3️⃣  View Category-wise Total
4️⃣  Exit

Enter your choice: 1
Amount spent: ₹300
Category: Travel
Description: Uber ride
✅ Expense added successfully!
example:
View Monthly Summary:
🧾 Total spent this month: ₹1450.00

View Category-wise Total:
🍔 Food: ₹650.00
🚗 Travel: ₹500.00
🎮 Entertainment: ₹300.00
