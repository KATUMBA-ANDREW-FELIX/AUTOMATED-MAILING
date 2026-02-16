import os
from dotenv import load_dotenv
import resend

print("=== DEBUG START ===")
print("Current folder:", os.getcwd())
print(".env file exists?", os.path.exists('.env'))
print("dotenv found and loaded?", load_dotenv())
print("All env vars (partial):", {k: v[:10]+"..." if v else None for k,v in os.environ.items() if k in ["RESEND_API_KEY", "RECIPIENT_EMAILS"]})

load_dotenv()  # still good to keep

def send_daily_message() -> None:
    api_key = os.getenv("RESEND_API_KEY")
    if not api_key:
        print("Error: RESEND_API_KEY not found!")
        return

    print("API key loaded (starts with):", api_key[:10] + "...")

    resend.api_key = api_key

    sender = "onboarding@resend.dev"

    recipients_str = os.getenv("RECIPIENT_EMAILS")
    if not recipients_str:
        print("Error: RECIPIENT_EMAILS not found!")
        return

    recipients = [email.strip() for email in recipients_str.split(",")]

    if not recipients:
        print("No valid recipients found!")
        return

    print(f"Sending to: {', '.join(recipients)}")

    params = {
        "from": sender,
        "to": recipients,
        "subject": "Your Daily Message",
        "html": """
        <h2>Hello!</h2>
        <p>This is your automated daily message FROM KATUMBA ANDREW FELIX.</p>
        <p><strong>WASSWA PLEASE BRING THE LAPTOP WITH U AS U COME FROM WORK</strong></p>
        <p>— Your Automation</p>
        """,
    }

    try:
        email = resend.Emails.send(params)
        print(f"Email sent successfully! ID: {email['id']}")
    except Exception as e:
        print(f"Error sending email: {e}")
        import traceback
        traceback.print_exc()

# This is the missing piece – call the function!
send_daily_message()