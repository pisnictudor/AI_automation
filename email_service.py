import smtplib
from email.message import EmailMessage


def send_email_alert(sender_email, app_password, receiver_email, high_priority_rows):
    if not high_priority_rows:
        print("No high priority items found. No email sent.")
        return

    msg = EmailMessage()
    msg["Subject"] = "High Priority Items Detected"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    body_lines = ["The following high priority items were detected:\n"]

    for row in high_priority_rows:
        body_lines.append(f"ID: {row['id']}")
        body_lines.append(f"Title: {row['title']}")
        body_lines.append(f"Summary: {row['summary']}")
        body_lines.append(f"Recommended Action: {row['recommended_action']}")
        body_lines.append("-" * 40)

    msg.set_content("\n".join(body_lines))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender_email, app_password)
        smtp.send_message(msg)

    print("Alert email sent successfully!")