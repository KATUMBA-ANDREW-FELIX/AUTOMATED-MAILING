import os
from dotenv import load_dotenv
import resend

load_dotenv()  # Loads .env if you have one

def send_daily_message() -> None:
    api_key = os.getenv("RESEND_API_KEY")
    if not api_key:
        print("Error: RESEND_API_KEY not found!")
        return

    resend.api_key = api_key

    # Use sandbox for testing if domain not verified yet
    sender = "onboarding@resend.dev"  # Switch to "FELIX FROM RTON <support@ritonproperties.com>" after verification
    # sender = "FELIX FROM RTON <support@ritonproperties.com>"

    # Load comma-separated emails from env var
    recipients_str = os.getenv("RECIPIENT_EMAILS")
    if not recipients_str:
        print("Error: RECIPIENT_EMAILS not found in env or .env!")
        print("Example: export RECIPIENT_EMAILS=email1@gmail.com,email2@yahoo.com")
        return

    # Split into list and strip any extra spaces
    recipients = [email.strip() for email in recipients_str.split(",")]

    if not recipients:
        print("No valid recipients found after splitting!")
        return

    print(f"Sending to: {', '.join(recipients)}")  # Helpful debug

    params = {
        "from": sender,
        "to": recipients,  # ← This is the key change: now a list!
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
        # Optional: print more details for debugging
        # print("Full response:", email)
    except Exception as e:  # Catch-all for API/network/validation errors
        print(f"Error sending email: {e}")
        # Optional: add more debug info
        import traceback
        traceback.print_exc()  # Prints full stack trace if needed