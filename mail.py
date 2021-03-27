import smtplib #Protocol de trimitere de mailuri de la noi catre destinatie
from email.mime.multipart import *
from email.mime.text import *

fromADD = "sender@gmail.com"   #de unde pleaca mailul
toADD = "Receiver@yahoo.com"  #unde merge mailul
subiect ="Ehloo Frend"  #subiectul mailului

print("Creating the message")

msg = MIMEMultipart()  # Creeam o instanta de clasa mail
msg["From"] = fromADD  #Valorea From
msg["To"] = toADD  #Valorea To
msg["Subject"] = subiect  #Valorea Subiect

mesaj = "Te salut din programul meu scris in Python" #Ce mesaj va avea mailul
msg.attach(MIMEText(mesaj,'plain')) #Atassam mesajul intr-o forma de text plain

print ("Connecting to server")

server = smtplib.SMTP("smtp.gmail.com", 587) # portul 587 este mailul criptat,25 este public
server.starttls() # Incepe protocolul, conexiunea

server.login(fromADD, "Password") # Introduce contul de google

server.sendmail(fromADD,toADD, msg.as_string()) #Trimite mailul

print ("Done sending")