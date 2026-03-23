from google import genai
from get import get_posts, analyze_post
from parse import parse_ai_response
from save_csv import save_to_csv

# 1. Creating Gemini Client
client = genai.Client() 


# 6. Main function
def main():
    url = "https://jsonplaceholder.typicode.com/posts"
    posts = get_posts(url)

    if not posts:
        print("No posts were retreived")
        return
    
    results = []

    for post in posts:
        print(f"Processing post ID {post['id']}...")

        ai_result = analyze_post(post["title"], post["body"],client)
        summary, tone, priority, recommended_action = parse_ai_response(ai_result)

        results.append([
            post["id"],
            post["title"],
            summary,
            tone,
            priority,
            recommended_action
        ])

    save_to_csv("report_ai_v2.csv", results)
    print("Report saved successfully to report_ai_v2.csv")

# 7. Running the programm
if __name__ == "__main__":
    main()