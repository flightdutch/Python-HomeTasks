import time
import re           # library: regular expression operartions

class MyPostfixLog:
    # шаблон mail-адресов
    regex = re.compile(("([a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`"
                        "{|}~-]+)*(@|\sat\s)(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?(\.|"
                        "\sdot\s))+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)"))
    # шаблон ipv4-адресов
    reipv4 = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

    def __init__(self, fpl='mail.info', fm=time.strftime('%b'), fd=time.strftime('%d')):
        # self.f_log = fpl
        # self.f_mth = fm
        # self.f_dt = fd
        self.f_log = 'mail.info'
        self.f_mth = 'Feb'
        self.f_dt = '27'

    def f_open(self):
        return open(self.f_log,'r')

    def __str__(self):
        pass

    def get_way_email(self, email):
        pass

    def get_mails_from(self, email):
        f_open = open(self.f_log, 'r')
        lines = f_open.readlines()
        f_open.close()
        s_mails = []
        # r = ''
        for line in lines:
            lst = line.split()
            if lst[0] == self.f_mth and lst[1] == self.f_dt:
                if line.find(email) != -1:
                    # r = re.findall(self.regex, line)
                    # r1 = r[0][0]
                    s_mails.append(re.findall(self.regex, line)[0][0])
        return s_mails


    # выборка по шаблону ipv4: reipv4
    def get_list_ips(self):
        f_open = open(self.f_log, 'r')
        s = f_open.read()
        f_open.close()
        return re.findall(self.reipv4,s)

    # выборка по шаблону email: regex
    def get_list_emails(self):
        f_open = open(self.f_log, 'r')
        s = f_open.read().lower() # file to string and Case is lowered to prevent regex mismatches.
        f_open.close()
        return (email[0] for email in re.findall(self.regex, s) if not email[0].startswith('//'))

    def get_max_size_email(self, fm=time.strftime('%m'), fd = time.strftime('%d')):
        pass

if __name__ == '__main__':
    pl = MyPostfixLog('mail.info')
    print(pl.f_open)
    mails = pl.get_list_emails()
    for line in mails:
        print(line)

