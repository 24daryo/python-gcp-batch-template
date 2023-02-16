from email.mime.text import MIMEText
import smtplib

import configs as C

def gmail():
    # メールサーバー情報（Gmailの場合）
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587

    # メール本文
    header = """Subject:"""
    message = """Test Email これはテストメールです。"""
    message_body = MIMEText(header + '\n' + message + '\n\n')
    
    # メール送信処理
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.ehlo()
        server.starttls()
        server.login(C.FROM_EMAIL, C.FROM_PASSWORD)
        server.sendmail(C.FROM_EMAIL, C.TO_EMAIL, str(message_body))
