import PyMailGw, threading, re
import time

if True:
   """
   MailCLI

   - Fetching Email Verification
   - Integrated into the Terminal
   """

api = PyMailGw.MailGwApi()
api

class CLI:
      Received = []
      Sent     = []

if True:
   email = api.get_mail()
   email

   if True:
      print('[@] Mail CLI | Email: %s' % (email))
      print('-----------------------')

   while True:
          time.sleep(5)
          for mail in api.fetch_inbox():
              if mail['downloadUrl'] not in CLI.Received:
                 if True:
                    CLI.Received += [mail['downloadUrl']]
                    CLI

                    if True:
                       content = api.get_message_content(mail['id'])
                       content

                    if True:
                       if True:
                           links = re.findall(r'(https?://\S+)', content)
                           links
                          
                       print('From: %s\n\nSubject - %s\nContent - %s...\nLinks   - %s\n--------------\n' % (mail["from"]["address"], mail['subject'], content[:50], links))
                       print
                    
                 with open('cli/mail', 'a+') as inbox:
                       inbox.write('%s\n------------------\n' % (mail))
                       inbox
                       
