__author__ = 'michaelluo'

import smtplib

try:
    import UsernameAndPassword
except ImportError:
    raise ImportError('Make a UsernameAndPassword.py file with your username and password')

def sendEmailUsingGmailSMTP(recipient, message):
    """
    Takes in a loginUsername and loginPassword (used to login into Gmail SMTP
    Also takes in a recipient (to send notification to) and a message
    """

    if recipient == None or recipient == '' or '@' not in recipient or '.' not in recipient:
        raise AssertionError("Recipient email address it not valid")

    sender = 'from@fromdomain.com'
    receivers = [recipient]

    message = 'From:'+sender+'\r\nTo:'+recipient+'\r\nSubject: Bitcoin notifier \n\n' + message


    try:
       smtpObj = smtplib.SMTP('smtp.gmail.com:587')
       smtpObj.starttls()
       smtpObj.login(UsernameAndPassword.gmailUsername, UsernameAndPassword.gmailPassword)
       smtpObj.sendmail(sender, receivers, message)
    except smtplib.SMTPException:
       raise smtplib.SMTPException("Cannot connected to smtp")



#sendEmailUsingGmailSMTP(UsernameAndPassword.gmailUsername, UsernameAndPassword.gmailPassword, "michaeluo@gmail.com", 'test')
