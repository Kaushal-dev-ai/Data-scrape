import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders



def send(filename):
   from_add = 'artistrystudio86@gmail.com'
   to_add = 'josephadvik17@gmail.com'
   subject = "Finance Stock Report"

   msg = MIMEMultipart()   
   msg['From'] = from_add
   msg['To'] = to_add
   msg['Subject'] = subject 

   body = "finance stock report is attached" 
   msg.attach(MIMEText(body, 'plain'))

   my_file = open( filename, 'rb') 

   part = MIMEBase('application', 'octet-stream')
   part.set_payload((my_file).read())
   encoders.encode_base64(part)
   part.add_header('Content-Disposition', "attachment; filename= " + filename)
   msg.attach(part)

   message = msg.as_string()



   server = smtplib.SMTP('smtp.gmail.com', 587)
   server.starttls()
   server.login( from_add, 'zdko dzma yiyn upwr')

   #message = " Hey, this is a Sending email through python!"
#server.sendmail('artistrystudio86@gmail.com', 'josephadvik17@gmail.com', message)
   server.sendmail(from_add, to_add, message)

   server.quit()