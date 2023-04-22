import imaplib
import email

def get_inbox():
    host = "imap.gmail.com"
    username = "email"
    password = "password"
    mail = imaplib.IMAP4_SSL(host)
    mail.login(username, password)
    mail.select("inbox")
    _, search_data = mail.search(None, 'FROM "info@info.timhortons.ca" SUBJECT " is your Tim Hortons login code"')
    lis = search_data[0].split()
    numbb = lis[-1]
    email_data = {}
    _, data = mail.fetch(numbb, '(RFC822)')
    _, b = data[0]
    email_message = email.message_from_bytes(b)
    email_data['subject'] = email_message['subject']
    return ((email_data['subject'])[0:7])

print(get_inbox())
