import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email_templates import random_message
from logger import logger
from datetime import datetime
import pandas as pd

# ==========================
# Email Credentials
# ==========================

EMAIL_ADDRESS = os.environ["EMAIL_ADDRESS"]
EMAIL_PASSWORD = os.environ["EMAIL_PASSWORD"]

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# ==========================
# Today's Date
# ==========================

today = datetime.today()
today_month = today.month
today_day = today.day

# ==========================
# Read CSV
# ==========================

df = pd.read_csv("birthdays.csv")

# ==========================
# Tracking
# ==========================

emails_sent = 0
success = []
failed = []

# ==========================
# Connect to Gmail
# ==========================

server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
server.starttls()

print(f"EMAIL_ADDRESS = {EMAIL_ADDRESS}")
print(f"Password length = {len(EMAIL_PASSWORD)}")
print(f"Password starts with = {EMAIL_PASSWORD[:2]}***")

server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

try:

    birthday_found = False

    for _, row in df.iterrows():

        birth_date = datetime.strptime(row["birth_date"], "%Y-%m-%d")

        if birth_date.month == today_month and birth_date.day == today_day:

            birthday_found = True

            recipient = row["email"]
            name = row["name"]

            try:

                greeting = random_message()

                subject = "🎉 Happy Birthday!"

                html = f"""
<!DOCTYPE html>
<html>
<body style="margin:0;padding:0;background:#f5f5f5;">

<table width="100%" cellpadding="0" cellspacing="0">
<tr>
<td align="center">

<table width="600"
style="
background:white;
border-radius:15px;
padding:40px;
font-family:Arial;
box-shadow:0 0 20px rgba(0,0,0,.2);
">

<tr>
<td align="center">

<h1 style="color:#ff4081;">
🎉 HAPPY BIRTHDAY 🎉
</h1>

<h2>{name}</h2>

<p style="font-size:20px;">
🎈🎈🎈
</p>

<img
src="https://images.unsplash.com/photo-1464349153735-7db50ed83c84?w=700"
width="350"
style="border-radius:15px;">

<p style="font-size:18px;line-height:1.7">
{greeting}
</p>

<h2>🎂🍰🎂</h2>

<p>
Have an amazing birthday!
</p>

<hr>

<p style="color:gray">
Best Wishes ❤️
</p>

</td>
</tr>

</table>

</td>
</tr>
</table>

</body>
</html>
"""

                email = MIMEMultipart("alternative")
                email["Subject"] = subject
                email["From"] = EMAIL_ADDRESS
                email["To"] = recipient

                email.attach(MIMEText(html, "html"))

                server.sendmail(
                    EMAIL_ADDRESS,
                    recipient,
                    email.as_string()
                )

                emails_sent += 1
                success.append(name)

                logger.info(f"Birthday mail sent to {name}")
                print(f"Birthday mail sent to {name}")

            except Exception as e:

                failed.append(name)
                logger.error(f"Failed to send birthday mail to {name}: {e}")
                print(f"Failed to send birthday mail to {name}")

    if not birthday_found:
        print("No birthdays today.")
        logger.info("No birthdays today.")

finally:
    server.quit()

# ==========================
# Summary
# ==========================

print("\n==============================")
print("Birthday Mail Summary")
print("==============================")
print(f"Emails Sent : {emails_sent}")
print(f"Successful  : {success}")
print(f"Failed      : {failed}")

logger.info(f"Emails Sent: {emails_sent}")
logger.info(f"Successful: {success}")
logger.info(f"Failed: {failed}")