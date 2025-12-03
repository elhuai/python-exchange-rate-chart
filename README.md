# 美金與日幣匯率比較 | USD and JPY Exchange Rate Comparison

[English](#english) | [中文](#中文)

---

## 中文

### 📊 專案簡介

本專案使用 Python 自動從台灣銀行抓取美金（USD）和日幣（JPY）的即時匯率資料，並將資料匯入 Excel 檔案，自動生成折線圖展示近三個月的匯率走勢。

### ✨ 功能特色

- 🌐 自動從台灣銀行官網抓取最新匯率資料
- 📈 生成美金和日幣的匯率趨勢折線圖
- 📊 資料自動整理並匯出至 Excel 檔案
- 🔄 支援即時更新，隨時掌握匯率變化

### 🛠️ 技術需求

- Python 3.x
- requests - 用於網路請求
- openpyxl - 用於 Excel 檔案操作和圖表生成

### 📦 安裝步驟

1. 確保已安裝 Python 3.x

2. 安裝所需套件：
```sh
pip install requests openpyxl
```

### 🚀 使用方法

1. 複製專案到本地端：
```sh
git clone https://github.com/elhuai/python-exchange-rate-chart.git
```

2. 進入專案目錄：
```sh
cd python-exchange-rate-chart
```

3. 執行 Python 腳本：
```sh
python src/rate.py
```

### 📂 輸出結果

執行後會在專案目錄中生成 `匯率及時更新.xlsx` Excel 檔案，內容包含：
- 近三個月的美金和日幣匯率資料
- 美金匯率趨勢折線圖
- 日幣匯率趨勢折線圖

### 💡 成果展示
<img width="1506" alt="截圖 2025-01-25 晚上11 10 35" src="https://github.com/user-attachments/assets/04469588-69e4-4ede-b6d1-715ebb80669a" />
<img width="996" alt="截圖 2025-01-25 晚上10 45 09" src="https://github.com/user-attachments/assets/09183830-7e9e-43b4-8898-2bc441a1321c" />
<img width="993" alt="JPY" src="https://github.com/user-attachments/assets/667451dc-920d-44eb-b912-b275087f89b7" />

### 📝 資料來源

匯率資料來源：[台灣銀行牌告匯率](https://rate.bot.com.tw/)

---

## English

### 📊 Project Description

This project uses Python to automatically fetch real-time USD and JPY exchange rate data from the Bank of Taiwan, import the data into an Excel file, and generate line charts showing the exchange rate trends over the past three months.

### ✨ Features

- 🌐 Automatically fetch the latest exchange rate data from Bank of Taiwan's website
- 📈 Generate line charts for USD and JPY exchange rate trends
- 📊 Automatically organize and export data to Excel files
- 🔄 Support real-time updates to track exchange rate changes

### 🛠️ Requirements

- Python 3.x
- requests - for HTTP requests
- openpyxl - for Excel file manipulation and chart generation

### 📦 Installation

1. Ensure Python 3.x is installed

2. Install required packages:
```sh
pip install requests openpyxl
```

### 🚀 Usage

1. Clone the repository:
```sh
git clone https://github.com/elhuai/python-exchange-rate-chart.git
```

2. Navigate to the project directory:
```sh
cd python-exchange-rate-chart
```

3. Run the Python script:
```sh
python src/rate.py
```

### 📂 Output

The script generates an Excel file named `匯率及時更新.xlsx` in the project directory, containing:
- Exchange rate data for USD and JPY over the past three months
- Line chart showing USD exchange rate trends
- Line chart showing JPY exchange rate trends

### 💡 Preview
<img width="1506" alt="截圖 2025-01-25 晚上11 10 35" src="https://github.com/user-attachments/assets/04469588-69e4-4ede-b6d1-715ebb80669a" />
<img width="996" alt="截圖 2025-01-25 晚上10 45 09" src="https://github.com/user-attachments/assets/09183830-7e9e-43b4-8898-2bc441a1321c" />
<img width="993" alt="JPY" src="https://github.com/user-attachments/assets/667451dc-920d-44eb-b912-b275087f89b7" />

### 📝 Data Source

Exchange rate data source: [Bank of Taiwan Exchange Rates](https://rate.bot.com.tw/)

---

## License

MIT License

## Author

elhuai



