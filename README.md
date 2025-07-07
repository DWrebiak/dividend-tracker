# 📈 Dividend Tracker

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Version](https://img.shields.io/badge/version-v1.0.1-blue)
![Python](https://img.shields.io/badge/python-3.10%2B-yellow)
![Status](https://img.shields.io/badge/status-development-orange)

**Dividend Tracker** is a tool for analyzing dividend-paying stocks using real-time financial data from Yahoo Finance. It calculates key financial indicators such as:

* 📦 Payout ratio
* 🟢 Free Cash Flow (FCF)
* 📊 Dividend yield
* 📈 Dividend CAGR (1Y, 3Y, 5Y, 10Y)

It works with any list of tickers.

---

## 🚀 Features

* Analyze any set of companies by providing their stock tickers
* Automatically fetches data via `yfinance` and `yahoo_fin`
* Export results to a CSV file (`dividend_data.csv`)
* Handles edge cases (e.g. missing dividends or financial metrics)
* Easily extensible and modular architecture

---

## 🛠 Requirements

* Python 3.10+
* Dependencies listed in `requirements.txt`

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-user/dividend-tracker.git
   cd dividend-tracker
   ```

2. (Optional but recommended) Create a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Run the main script:

   Run the script with the default config:
   ```bash
   python3 main.py
   ```
   Run the script with a custom config file:
   ```bash
   python3 main.py --config config/config_sp500.json
   ```
   Run the script in automatic loop mode, once every 24 hours:
   ```bash
   python3 main.py --loop
   ```
   You can combine both arguments:
   ```bash
   python3 main.py --config config/config_sp500.json --loop
   ```

4. (Optional) Customize the list of tickers

   You can customize the list of companies to analyze by editing the `config/config.json` file or creating your own JSON config file with tickers. Then run the script specifying the config file path:

   ```bash
   python3 main.py --config config/your_config.json
   ```

---

## 📦 Project Structure

```
dividend-tracker/
├── CHANGELOG.md        # Changelog file
├── config/             # Configuration files for different setups
│ ├── config.json       # Default config file
│ └── config_sp500.json # Config for S&P 500 tickers
├── dividend_tracker/   # Core modules for data analysis and utilities
│ ├── init.py           # Package initializer
│ ├── analysis.py       # Data analysis functions
│ ├── data.py           # Data fetching and processing
│ ├── formatting.py     # Formatting utilities
│ └── utils.py          # Helper functions (e.g. config loading, CSV saving)
├── exports/            # Folder containing timestamped dividend CSV reports
├── LICENSE             # MIT License file
├── main.py             # Main entry point script
├── README.md           # Project documentation
├── requirements.in     # Python dependencies input file
└── requirements.txt    # Python dependencies lock file
```

---

## 📝 License & Distribution

This project is licensed under the MIT License.

See the LICENSE file for details.

You are free to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, subject to including the original copyright and license notice.

---

## ⚠️ Disclaimer

This tool is created solely for personal use and educational purposes. It is **not intended as financial or investment advice**.

All decisions based on the data or suggestions provided by this tool are made at the user's own risk.  
The author is **not a licensed financial advisor** and assumes no responsibility for any financial losses incurred through the use of this project.

Always conduct your own research or consult a certified financial professional before making any investment decisions.

---

## 🐛 Reporting Issues

If used collaboratively, bugs or suggestions can be tracked using GitHub Issues with appropriate labels (bug, enhancement, etc.).

---

## ❤️ Philosophy & Support

This project was created as a personal tool to better understand dividend stocks and make more informed investment decisions.

If it helps you save money or choose better companies to invest in — that's fantastic.

You're free to use, modify, and share it however you like.

If you’d like to show appreciation, you can support me via PayPal (any amount, any currency) and write why this tool is meaningful to you.
If it didn’t help — I’d still love your feedback to make it better.

✉️ Email: dariusz.wrebiak@gmail.com
💸 PayPal: dariusz.wrebiak@gmail.com
