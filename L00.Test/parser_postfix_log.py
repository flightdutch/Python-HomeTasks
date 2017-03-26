# http://stackoverflow.com/questions/26282338/parse-maillog-in-python
import re, sys

lines = []
queue_id = []
f_h = open('maillog', 'r')

def Find_Email(pattern,text):
    email = re.search(pattern, text)
    if email:
        lines.append(text)
        q_id = re.search('[A-F0-9]{10}', text)
        print(text)
        if q_id:
            queue_id.append(q_id.group())


for line in f_h:
    Find_Email(r'recipient@gmil.com',line)