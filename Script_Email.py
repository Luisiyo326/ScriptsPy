import smtplib
from email.message import EmailMessage

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject']= subject
    msg['to'] = to

    user = "YOUR EMAIL"
    msg['from'] = user
    password = 'YOUR PASSWORD'

    server = smtplib.SMTP("smtp.gmail.com", 587) #Host junto al puerto
    server.starttls()
    server.login(user , password)
    server.send_message(msg)

    server.quit()

if __name__ == '__main__':
    email_alert("header del correo","body del correo","Destinatario:email@address.com")
    #Codifo diseñado por Luisiyo326 
    #Contacto: https://github.com/Luisiyo326