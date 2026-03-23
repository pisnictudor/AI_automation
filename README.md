# AI Automation Project

## Description
This project demonstrates an automated AI automation workflow using Python and Google Gemini.

The script:
- fetches data from a public API
- analyzes the text with Gemini
- extracts a summary and tone classification
- saves the results into a CSV report

## Technologies Used
- Python
- Requests
- Google Gemini API
- CSV

## Features
- Fetches posts from an external API
- Sends post data to Gemini for analysis
- Extracts:
  - Summary
  - Tone
- Saves structured output into `report_ai.csv`

## Project Structure
```text
AI_automation/
├── main.py
├── requirements.txt
├── report_ai.csv
└── README.md