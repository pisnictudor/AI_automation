import requests

def get_posts(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()[:5]
    except requests.exceptions.RequestException as e:
        print(f"Error while fetching posts: {e}")
        return []
    
def analyze_post(title, body,client):
    prompt = f"""
You are analyzing a business-related text.

Task:
1. Write a short summary in one sentence.
2. Classify the tone as exactly one of these:
informative
emotional
neutral

3. Classify the priority as exactly one of these:
high
medium
low

4. Choose the recommended action as exactly one of these:
review immediately
monitor
archive

Return the answer exactly in this format:
Summary: ...
Tone: ...
Priority: ...
Recommended Action: ...

Title: {title}
Body: {body}
"""

    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt
        )
        return response.text
    except Exception as e:
        print(f"Error while analyzing post with AI: {e}")
        return (
            "Summary: Error\n"
            "Tone: Error\n"
            "Priority: Error\n"
            "Recommended Action: Error"
        )
    