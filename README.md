# ex_reminder
A reminder that can notify you wherever you are.

# requirement
yagmail

# How to use?
```python
sender_email = 'xxx@xxx.com'
# the authorized code is not your password sometime, and it depends on your mail service
authorized_code = 'xxxxx'  
host = 'xxx'  # for example: smtp.163.com
receiver_email = 'xxxx@xxx.com'  # receiver email can be the sender email
subject = ''  # it is optional, and the default value is 'An experiment from ex_reminder!'

sender = reminder(sender_email=sender_email, authorized_code=authorized_code, \
                  host=host, receiver_email=receiver_email, subject=subject)
### processing 
content = 'Loss: 12, Acc:91.53%'
sender.send(content)
```
