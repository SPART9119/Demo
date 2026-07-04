import os

EMAIL = os.getenv("EMAIL_ADDRESS")
PASSWORD = os.getenv("EMAIL_PASSWORD")

SMTP_PROVIDER = os.getenv("SMTP_PROVIDER", "gmail").lower()

if SMTP_PROVIDER == "gmail":
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587

elif SMTP_PROVIDER == "outlook":
    SMTP_SERVER = "smtp.office365.com"
    SMTP_PORT = 587

else:
    raise ValueError("Unsupported SMTP provider.")