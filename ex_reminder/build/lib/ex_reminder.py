#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jones
# @File: ex_reminder.py
# @Email: jlin398@wisc.edu
import yagmail

class reminder:
    def __init__(self, sender_email, authorized_code, host, receiver_email, subject='An experiment from ex_reminder!'):
        self.subject = subject
        self.receiver_email = receiver_email
        self.host = host
        self.authorized_code = authorized_code
        self.sender_email = sender_email
        self.yag = yagmail.SMTP(user=self.sender_email, password=self.authorized_code, host=self.host)

    def send(self, content):
        self.yag.send(self.receiver_email, self.subject, content)

