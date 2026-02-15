import os
import resend
from typing import Any

def send_daily_message() -> None:
    # Load API key from environment (never hardcode it!)
    api_key = os.getenv("re_EXTWLh8D_EjU7ZhwdxY3vJ7f8NNkNhXeZ")
    if not api_key:
        print("Error: RESEND_API_KEY environment variable is missing!")
        return

    resend.api_key = api_key

    # IMPORTANT: Use a VERIFIED sender address!
    #   → Go to Resend dashboard → Domains → Add & verify your domain
    #   → Then use e.g. "FELIX FROM RTON <felix@yourdomain.com>"
    # For quick testing: "onboarding@resend.dev" or your sandbox sender works, but limited.
    sender = "FELIX FROM RTON <support@ritonproperties.com>"   # ← CHANGE THIS

    recipient = os.getenv("rickmanricky256@gmail.com")  # Better env var name
    if not recipient:
        print("Error: RECIPIENT_EMAIL environment variable is missing!")
        return

    params: resend.Emails.SendParams = {
        "from": sender,
        "to": [recipient],                  # List of strings — even for 1 recipient
        "subject": "Your Daily Message",
        "html": """
        <h2>Hello!</h2>
        <p>This is your automated daily message FROM KATUMBA ANDREW FELIX.</p>
        <p>WASSWA PLEASE BRING THE LAPTOP WITH U AS U COME FROM WORK</p>
        <p>— Your Automation</p>
        """,
        # Optional extras you can add later:
        # "cc": ["someone@else.com"],
        # "bcc": ["log@yourdomain.com"],
        # "reply_to": "felix@yourdomain.com",
        # "tags": [{"name": "daily", "value": "reminder"}],
    }

    try:
        email: Any = resend.Emails.send(params)  # Returns dict with 'id'
        print(f"Email sent successfully! ID: {email['id']}")
    except resend.ResendError as e:
        print(f"Resend API error: {e}")
        if hasattr(e, 'response'):
            print(f"Full response: {e.response}")
    except Exception as e:
        print(f"Unexpected error sending email: {e}")

if __name__ == "__main__":
    send_daily_message()
