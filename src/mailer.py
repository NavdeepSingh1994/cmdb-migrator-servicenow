import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

def send_email_with_pdf(to_address, pdf_path):
    msg = EmailMessage()
    msg["Subject"] = "📄 CMDB Import Report"
    msg["From"] = EMAIL_USER
    msg["To"] = to_address
    msg.set_content(
        "Sehr geehrter Herr Markom, sehr geehrte Frau Zirdum,\n\n"
        "im Anhang finden Sie den aktuellen CMDB-Importbericht, "
        "inklusive aller übermittelten Konfigurationseinträge.\n\n"
        "Mit freundlichen Grüßen\n\n"
        "Navdeep Singh"
    )

    try:
        with open(pdf_path, "rb") as f:
            msg.add_attachment(
                f.read(),
                maintype="application",
                subtype="pdf",
                filename=pdf_path.name
            )

        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login(EMAIL_USER, EMAIL_PASS)
            smtp.send_message(msg)
            print(f"[MAIL OK] PDF wurde an {to_address} gesendet.")
            return True

    except Exception as e:
        print(f"[MAIL FAIL] Fehler beim Senden: {e}")
        return False
