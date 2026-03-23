AI Automation Workflow (Python + Gemini)

Description
This project demonstrates an end-to-end AI automation workflow built with Python.

It simulates a real-world business process where data is:
- fetched from an external API
- analyzed using AI (Google Gemini)
- transformed into structured insights
- saved as a CSV report
- and triggers email alerts for high-priority items

--------------------------------------------------

Technologies Used
- Python
- Requests (API calls)
- Google Gemini API (google-genai)
- CSV module
- SMTP (email automation)

--------------------------------------------------

Features
- Fetches data from a public API
- Processes and filters text data
- Uses AI to generate:
  - Summary
  - Tone classification
  - Priority level
  - Recommended action
- Saves structured output into CSV
- Sends automated email alerts when high-priority items are detected

--------------------------------------------------

Project Structure

AI_automation/
│
├── main.py
├── config.py
├── requirements.txt
├── README.txt
├── report_ai_v2.csv
│── get.py
│── save_csv.py
│── email_service.py
│── parse.py

--------------------------------------------------

How to Run

1. Clone the repository

git clone https://github.com/pisnictudor/AI_automation.git
cd AI_automation

--------------------------------------------------

2. Install dependencies

pip install -r requirements.txt

--------------------------------------------------

3. Set environment variables

Gemini API key (PowerShell):

$env:GEMINI_API_KEY="YOUR_API_KEY"

Email credentials (recommended):

$env:SENDER_EMAIL="your_email@gmail.com"
$env:APP_PASSWORD="your_app_password"
$env:RECEIVER_EMAIL="receiver@gmail.com"

--------------------------------------------------

4. Run the script

python main.py

--------------------------------------------------

Output

The script generates a CSV file:

report_ai_v2.csv

With the following columns:
- ID
- Title
- Summary
- Tone
- Priority
- Recommended Action

--------------------------------------------------

Email Automation Logic

The system sends an email only if high-priority items are detected.

Behavior:
- No "high" priority → No email sent
- At least one "high" → Email alert triggered

Email contains:
- ID
- Title
- Summary
- Recommended action

--------------------------------------------------

Example Use Case

This project simulates a real business workflow such as:
- marketing content analysis
- customer feedback triage
- lead prioritization
- automated reporting and alerting systems

--------------------------------------------------

Key Concepts Demonstrated

- API integration
- AI-powered data analysis
- prompt engineering
- data parsing and structuring
- CSV report generation
- event-driven automation
- email notifications

--------------------------------------------------

Future Improvements

- Add logging system
- Add retry mechanisms for API calls
- Export data to Google Sheets
- Build a dashboard (Streamlit)
- Schedule execution (cron / task scheduler)
- Improve AI response validation

--------------------------------------------------

Portfolio Value

This project demonstrates the ability to:
- build automation pipelines
- integrate AI into real workflows
- design modular Python applications
- create business-oriented solutions

--------------------------------------------------

Author

Tudor Pisnic
GitHub: https://github.com/pisnictudor