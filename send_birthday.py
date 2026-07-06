import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email_templates import random_message, random_song
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
                song_name, song_url = random_song()

                subject = "🎉 Happy Birthday!"

                html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
</head>

<body style="
margin:0;
padding:0;
background:#f3f0ff;
font-family:Arial, Helvetica, sans-serif;
">

<table width="100%" cellpadding="40">

<tr>

<td align="center">

<table
width="650"
cellpadding="0"
cellspacing="0"
style="
background:white;
border-radius:25px;
overflow:hidden;
box-shadow:0 20px 60px rgba(0,0,0,.15);
">

<!-- HEADER -->

<tr>

<td
align="center"
style="
background:linear-gradient(135deg,#ff6ec4,#7873f5);
padding:45px;
color:white;
">

<h1 style="
margin:0;
font-size:42px;
letter-spacing:3px;
">

🎉 Happy Birthday 🎉

</h1>

<p style="
margin-top:15px;
font-size:20px;
opacity:.95;
">

Today is all about YOU!

</p>

</td>

</tr>

<!-- IMAGE -->

<tr>

<td align="center" style="padding-top:35px;">

<img

src="https://images.unsplash.com/photo-1464349153735-7db50ed83c84?w=900"

width="280"

style="
border-radius:20px;
box-shadow:0 15px 35px rgba(0,0,0,.15);
">

</td>

</tr>

<!-- NAME -->

<tr>

<td align="center">

<h2 style="
font-size:34px;
margin-top:35px;
margin-bottom:10px;
color:#444;
">

Dear {name},

</h2>

</td>

</tr>

<!-- MESSAGE -->

<tr>

<td style="padding:0 70px;">

<div style="
background:#fff8ec;
border-left:6px solid #ff9800;
padding:30px;
border-radius:15px;
font-size:21px;
line-height:1.9;
color:#555;
font-style:italic;
">

{greeting.replace(chr(10), "<br>")}

</div>

</td>

</tr>

<!-- QUOTE -->

<tr>

<td align="center" style="padding:45px;">

<p style="
font-size:18px;
color:#777;
line-height:1.8;
">

May this year bring new adventures,
beautiful memories,
and countless reasons to smile.

</p>

</td>

</tr>

<!-- CAKE -->

<tr>

<td align="center">

<div style="font-size:70px;">
🎂
</div>

</td>

</tr>

<!-- FOOTER -->

<tr>

<td
align="center"
style="
background:#fafafa;
padding:35px;
">

<h2 style="
margin:0;
color:#ff4081;
">

Have the Most Amazing Birthday!

</h2>

<p style="
color:#666;
margin-top:20px;
font-size:17px;
">

Wishing you happiness today,
success tomorrow,
and memories that last forever.

</p>

<hr
style="
margin-top:35px;
margin-bottom:25px;
border:none;
border-top:1px solid #ddd;
width:70%;
">

<p style="
font-size:16px;
color:#999;
">

Made with ❤️ especially for you

</p>

</td>

</tr>

</table>

</td>

</tr>

</table>

<a href="{song_url}"
target="_blank"
style="
background:#ff4081;
color:white;
text-decoration:none;
padding:16px 35px;
font-size:18px;
font-weight:bold;
border-radius:40px;
display:inline-block;
">

🎵 Play "{song_name}"

</a>

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