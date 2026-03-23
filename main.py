import csv
import requests
from google import genai

# 1. Creating Gemini Client
client = genai.Client() 

# 2. Get data from API
def get_posts(url):
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()[:5]
    else:
        print(f"API error: {response.status_code}")
        return []

# 3. Sending data to Gemini and getting the results
def analyze_post(title, body):
    prompt = f"""
You are analyzing a marketing-style text.

Task:
1. Write a short summary in one sentence.
2. Classify the tone as exactly one of these:
informative
emotional
neutral

Return the answer exactly in this format:
Summary: ...
Tone: ...

Title: {title}
Body: {body}
"""
    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt
        )
    except Exception as e:
        print(f"Error while analyzing post with AI: {e}")
        return "Summary error\nTone error"

    return response.text

# 4. Extracting Summary and Tone from AI response
def parse_ai_response(ai_text):
    summary = ""
    tone = ""

    lines = ai_text.splitlines()

    for line in lines:
        if line.startswith("Summary:"):
            summary = line.replace("Summary:", "").strip()
        elif line.startswith("Tone:"):
            tone = line.replace("Tone:", "").strip()

    return summary, tone

# 5. Saving data in CSV
def save_to_csv(filename, rows):
    try:
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            writer.writerow(["ID", "Title", "Summary", "Tone"])

            for row in rows:
                writer.writerow(row)
    except OSError as e:
        print(f"Error saving in csv file: {e}")


# 6. Main function
def main():
    url = "https://jsonplaceholder.typicode.com/posts"
    posts = get_posts(url)

    results = []

    for post in posts:
        print(f"Processing post ID {post['id']}...")

        ai_result = analyze_post(post["title"], post["body"])
        summary, tone = parse_ai_response(ai_result)

        results.append([
            post["id"],
            post["title"],
            summary,
            tone
        ])

    save_to_csv("report_ai.csv", results)
    print("Report saved in: report_ai.csv")

# 7. Running the programm
if __name__ == "__main__":
    main()