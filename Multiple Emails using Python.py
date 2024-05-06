
import smtplib as s

ob = s.SMTP("smtp.gmail.com", 587)
ob.ehlo()
ob.starttls()
ob.login("Email", "Password")  #Enter Login Credentials
subject = "Test Python"
body = "I Love Python."
message = "subject:{\n\n{}\n\n{}".format(subject, body)
list_add = ["", ""]  # Enter Receiver's Emails

ob.sendmail("Sender's Email Here", list_add, message)
print("Mail Sent")
ob.quit()