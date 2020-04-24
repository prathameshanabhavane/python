from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from string import Template
from pathlib import Path
from smtplib import SMTP

# print(Path("unnamed.png"))

template = Template(Path("template.html").read_text())

message = MIMEMultipart()
message["from"] = "Jhon Doe"
message["to"] = "test@gmail.com"
message["subject"] = "This is test"
body = template.substitute({"name": "Jhon"})
# body = template.substitute(name="Raj")
message.attach(MIMEText(body, "html"))
message.attach(MIMEImage(Path("unnamed.jpg").read_bytes()))


with SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("abc@gmail.com", "abc@123")
    smtp.send_message(message)
    print("Sent...")
