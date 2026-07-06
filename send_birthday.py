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
<html lang="en">

<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Happy Birthday</title>

</head>

<body style="margin:0;padding:0;background:#FFF7FB;">

<table role="presentation" width="100%" cellspacing="0" cellpadding="0" style="background:#FFF7FB;padding:25px 10px;">

<tr>

<td align="center">

<table role="presentation"
width="100%"
cellspacing="0"
cellpadding="0"
style="
max-width:620px;
background:#ffffff;
border-radius:24px;
overflow:hidden;
border:1px solid #eeeeee;
font-family:Arial,Helvetica,sans-serif;
">

<!-- TOP RIBBON -->

<tr>

<td
align="center"
style="
background:#ff4f8b;
color:white;
padding:12px;
font-size:15px;
font-weight:bold;
letter-spacing:2px;
">

✨ TODAY IS YOUR DAY ✨

</td>

</tr>

<!-- HEADER -->

<tr>

<td
align="center"
style="
background:#7b61ff;
padding:45px 20px;
color:white;
">

<div style="font-size:48px;">
🎈🎂🎉
</div>

<h1 style="
margin:15px 0 5px;
font-size:38px;
font-weight:bold;
">

Happy Birthday!

</h1>

<p style="
margin:0;
font-size:20px;
opacity:.95;
">

Celebrating YOU today!

</p>

</td>

</tr>

<!-- IMAGE -->

<tr>

<td align="center" style="padding:35px 20px 10px;">

<img
src="https://images.unsplash.com/photo-1464349153735-7db50ed83c84?w=1200"
alt="Birthday Cake"
style="
display:block;
width:90%;
max-width:340px;
height:auto;
border-radius:20px;
">

</td>

</tr>

<!-- NAME -->

<tr>

<td align="center" style="padding:10px 30px;">

<h2 style="
margin:0;
font-size:34px;
color:#444444;
">

Dear {name},

</h2>

<p style="
margin-top:12px;
font-size:18px;
color:#777777;
">

Today is all about celebrating the amazing person you are.

</p>

</td>

</tr>

<!-- MESSAGE -->

<tr>

<td style="padding:15px 28px;">

<div style="
background:#FFF9F5;
border:2px dashed #ffb84d;
border-radius:18px;
padding:28px;
font-size:20px;
line-height:1.9;
color:#555555;
font-style:italic;
text-align:center;
">

{greeting.replace(chr(10), "<br>")}

</div>

</td>

</tr>

<!-- PHILOSOPHICAL QUOTE -->

<tr>

<td align="center"
style="
padding:35px 40px 20px;
">

<p style="
margin:0;
font-size:18px;
line-height:1.8;
color:#666666;
">

"Life isn't measured by the number of birthdays we celebrate,
but by the countless lives we brighten along the way.
May this new chapter bring you purpose, peace and unforgettable memories."

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

<!-- MUSIC BUTTON -->

<tr>

<td align="center" style="padding:30px;">

<a
href="{song_url}"
target="_blank"
style="
background:#ff4f8b;
color:white;
text-decoration:none;
padding:16px 34px;
font-size:18px;
font-weight:bold;
border-radius:40px;
display:inline-block;
">

🎵 Play "{song_name}"

</a>

</td>

</tr>

<!-- WISH -->

<tr>

<td align="center"
style="
padding:10px 40px 35px;
">

<p style="
font-size:18px;
color:#666666;
line-height:1.9;
">

May today surround you with laughter,
tomorrow reward you with success,
and every day ahead remind you
how deeply valued and appreciated you are.

</p>

</td>

</tr>

<!-- DIVIDER -->

<tr>

<td align="center">

<hr style="
width:80%;
border:none;
border-top:1px solid #eeeeee;
">

</td>

</tr>

<!-- FOOTER -->

<tr>

<td
align="center"
style="
padding:35px 30px 40px;
background:#fafafa;
">

<h2 style="
margin:0;
font-size:28px;
color:#ff4f8b;
">

Have an Incredible Birthday!

</h2>

<p style="
margin-top:20px;
font-size:17px;
line-height:1.8;
color:#777777;
">

May your heart stay young,
your dreams stay bold,
and your smile continue
to inspire everyone around you.

</p>

<div style="
font-size:34px;
margin-top:25px;
">

🎈 ✨ 🎁 ❤️ 🎉

</div>

<p style="
margin-top:30px;
font-size:15px;
color:#aaaaaa;
">

Made with ❤️ especially for you.<br>
Have a magical year ahead!

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