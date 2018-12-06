import easyimap
import smtplib
import requests
from django.http import HttpResponse
import email, imaplib
import html2text




# return HttpResponse("Failed")

class getmailclass():
    def getmailfunc():
        h = html2text.HTML2Text()
        h.ignore_links = False
        login = 'govtechinternship@gmail.com'
        print("login assigned")
        password = 'mcONLINE123'
        print("password assigned")
        imapper = easyimap.connect('imap.gmail.com', login, password)
        print("imap connect successful")
        for mail_id in imapper.listids(limit=1):
            print("inside for loop")
            mail = imapper.mail(mail_id)
            print(mail.body)
            incasehtml = h.handle(mail.body)
            print("HTML cleaned: " + incasehtml)
            return incasehtml, mail.from_addr
            break
        return incasehtml, mail.from_addr


    