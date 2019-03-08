import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
import datetime #added by R.L at 2019/2/6
import subprocess #added by R.L. at 2019/2/6
import time #added by R.L. at 2019/2/7

#added by R.L. at 2019/2/6
ip = subprocess.check_output(['hostname', '-I'])
#today = datetime.date.today()
#below is added by R.L. at 2019/2/7
mail_message = "Dear Mr. Lin,\n\nMessage text sent automatically. \n" 
mail_message1 = "\nYou can write anything you want. \n" 
mail_message2 = "\nYou can write anything you want.You can write anything you want.You can write anything you want. \n" 
mail_message3 ="\n \n" 
mail_message4 ="\n \n" 
Time_message1 = 'Now is : %s' % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
Time_message2 ="\n " 
Time_message3 = 'Now is : %s' % time.strftime("%b-%d-%Y %H:%M:%S", time.localtime()) 
mail_message5 ="\n\nBest Regard, \n R.L." 
my_msg = '' 
time.sleep(10)    
my_msg = mail_message+ mail_message1+ mail_message2+ mail_message3+ mail_message4+ Time_message1+ Time_message2+ Time_message3+ mail_message5#added by R.L. at 2019/2/7

# Define to/from
sender = 'your_email_address@zoho.com' # @gmai.com or any else 
sender_title = "type something you like, ex: Pi"
recipient = 'receiver_email_address@zoho.com' # @gmai.com or any else 

# Create message
#my_msg = "Message text autosend" % today.strftime('%b %d %Y') % ip[:-2] #added by R.L. at 2019/2/6
#my_msg = 'Message text sent automatically. Today is : %s' % today.strftime('%b %d %Y') #added by R.L. at 2019/2/6
msg = MIMEText(my_msg, 'plain', 'utf-8') #revised by R.L. at 2019/2/6
msg['Subject'] =  Header('type something you like, ex: Sent from python,RPI IP: %s' % ip[:-2], 'utf-8') #revised by R.L. at 2019/2/6
msg['From'] = formataddr((str(Header(sender_title, 'utf-8')), sender))
msg['To'] = recipient

# Create server object with SSL option
server = smtplib.SMTP_SSL('smtp.zoho.com', 465)  # or stmp@gmail.com, 587

# Perform operations via server
server.login('your_email_address@zoho.com', 'your_password')
print("Server Login Successful") #added by R.L. at 2019/2/6
server.sendmail(sender, [recipient], msg.as_string())
print("Sending Message...") #added by R.L. at 2019/2/6
server.quit()
print("Quit Server") #added by R.L. at 2019/2/6
