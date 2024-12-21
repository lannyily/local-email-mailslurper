import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = "localhost"
smtp_port = 2500
from_email = "erlanny.rego@gmail.com"
to_email = "erlanny.rego@ufpi.edu.br"
subject = "Teste de e-mail"
body = "Este é um e-mail de teste enviado pelo MailSlurper!"


msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.sendmail(from_email, to_email, msg.as_string())
        print("E-mail enviado com sucesso!")
except Exception as e:
    print(f"Erro ao enviar e-mail: {e}")
