import os
import resend

def send_daily_message() -> None:
    api_key = os.getenv("RESEND_API_KEY")
    if not api_key:
        print("Error: RESEND_API_KEY not found!")
        return

    resend.api_key = api_key

    # Use sandbox for testing if domain not verified yet
    sender = "onboarding@resend.dev"  # Switch later after domain verification
    # sender = "FELIX FROM RTON <support@ritonproperties.com>"

    recipients_str = os.getenv("RECIPIENT_EMAILS")  # ← Make sure this matches your secret name
    if not recipients_str:
        print("Error: RECIPIENT_EMAILS not found!")
        print("Example format: email1@gmail.com,email2@yahoo.com")
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