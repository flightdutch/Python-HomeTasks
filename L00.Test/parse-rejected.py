import re
import smtplib

theFile = open('/var/log/mail.info', 'r')
FILE = theFile.readlines()
theFile.close()
printList = []

def sendMail( printList ):
  "send email"
  results = '\n'.join(printList)

  SERVER = "localhost"
  FROM = "no-reply@example.com"
  TO = ["receiver@example.com"] # must be a list
  SUBJECT = "server name: rejected sender domains"

  # Prepare actual message
  message = """\
From: %s
To: %s
Subject: %s
%s
""" % (FROM, ", ".join(TO), SUBJECT, results)

  # Send the mail
  send = smtplib.SMTP(SERVER)
  send.sendmail(FROM, TO, message)
  send.quit()

  return;


# Parse log file
for line in FILE:
  if ('Sender address rejected: Domain not found' in line): # or ('Totals' in line):
    sender = re.search('(from=<)([\w\.-]+@[\w\.-]+)(>)', line)
    receiver = re.search('(to=<)([\w\.-]+@[\w\.-]+)(>)', line)

    # Clean sender
    spat = re.compile('(from=<|>)')
    sender = spat.sub('', sender.group())

    # Clean receiver
    rpat = re.compile('(to=<|>)')
    receiver = rpat.sub('', receiver.group())

    # Add to list
    printList.append( sender + '\t' + receiver )

    # Remove duplicates
    printList = list(set(printList))

# Send email
sendMail(printList)