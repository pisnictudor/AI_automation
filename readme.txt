# AI Automation Project

## 📌 Description
This project demonstrates an automated workflow using Python and AI.

It performs:
- Data extraction from a public API
- AI-based text analysis using Gemini
- Automatic report generation in CSV format

---

## ⚙️ Technologies Used
- Python
- Requests (API calls)
- Google Gemini API
- CSV handling

---

## 🚀 Features
- Fetches data from an external API
- Processes and filters information
- Uses AI to generate:
  - Summary
  - Tone classification
- Saves structured results into a CSV report

---

## 📂 Project Structure

AI_Automation_Project/
│
├── main.py
├── report_ai.csv
├── requirements.txt
└── README.md

---

## ▶️ How to Run

1. Install dependencies:
```bash
pip install -r requirements.txt

Set your Gemini API key (PowerShell):
$env:GEMINI_API_KEY="YOUR_API_KEY"

Run the script:
python main.py