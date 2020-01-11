import os
import json
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

with open('template.html', 'r') as template:
  content = template.read()

with open('users.json', 'r') as users:
  dump = json.load(users)
  l = dump[2]['data']
  email_list = []
  for i in l:
    email_list.append(i['email'])
  print(email_list)


for mail in email_list:
  message = Mail(
      from_email=('testmail@gmail.com', 'Hestia 20'),
      to_emails=mail,
      subject='Hestia Test mail',
      html_content=content)
  try:
      sg = SendGridAPIClient('API_KEY_HERE')
      response = sg.send(message)
      with open('log.txt', 'a') as log:
        log.write(mail + ' : ' + str(response.status_code) + '\n')
      print('Sent to: ' + mail)
  except Exception as e:
      print('Failed sending to : '+ mail + ' : ' + e.message)
      with open('log.txt', 'a') as log:
        log.write(mail + ' : ' + e + '\n')


