#!/usr/bin/env python


import twitter
import requests
import smtplib
from email.mime.text import MIMEText
import os

alert_txt_file = '/tmp/alert.txt'
dump_txt_file = '/tmp/dump.txt'

#  Email configuration
email_to = ''
email_from = ''
email_subject = ''
smtp_server = ''

#  Twitter API credentials
consumer_key = ''
consumer_secret = ''
access_token_key = ''
access_token_secret = ''

#  Twitter account we are following
twitter_user = 'dumpmon'

#  Search Term(s)
#  If set to a string, search a single term
#  If set to a tuple, perform search for multiple terms, e.g.
#  search_string = 'abc' or
#  search string = ('term1', 'term2', 'etc',)
search_string = ''


class Dumpmon(object):

    def __init__(self):
        self.status = []
        self.links = []
        self.twitter_user = twitter_user
        self.api = twitter.Api(consumer_key=consumer_key,
                               consumer_secret=consumer_secret,
                               access_token_key=access_token_key,
                               access_token_secret=access_token_secret)

    def get_tweets(self):
        return self.api.GetUserTimeline(screen_name=self.twitter_user)

    def get_links(self):
        for s in self.get_tweets():
            self.links.append(s.text.split(" ")[0])


def get_link_output(link):
    r = requests.get(link)
    return r.text


def remove_old_dump_and_alert_txts():
    if os.path.isfile(dump_txt_file):
        os.remove(dump_txt_file)
    if os.path.isfile(alert_txt_file):
        os.remove(alert_txt_file)


def scrape_info_from_links():
    f = open(dump_txt_file, 'w+')
    for link in tweets.links:
        if link.startswith('http'):
            f.write(get_link_output(link).encode('utf-8'))
    f.close()


def search_for_text():
    alert = open(alert_txt_file, 'w+')
    with open(dump_txt_file) as final:
        for line in final:
            if search_string in line:
                alert.write(line.strip() + '\n')
    alert.close()

def search_for_text_multiple():
    alert = open(alert_txt_file, 'w+')
    with open(dump_txt_file) as final:
        for line in final:
            if any(x in line for x in search_string):
                alert.write(line.strip() + '\n')
    alert.close()

def send_alert_email():
    alert = open(alert_txt_file, 'r')
    msg = MIMEText(alert.read())
    alert.close()
    msg['Subject'] = email_subject
    msg['From'] = email_from
    msg['To'] = email_to
    s = smtplib.SMTP(smtp_server)
    s.sendmail(email_from, email_to, msg.as_string())
    s.quit()


if __name__ == '__main__':
    try:
        tweets = Dumpmon()
        tweets.get_links()
        remove_old_dump_and_alert_txts()
        scrape_info_from_links()
        if isinstance(search_string, tuple):
            search_for_text_multiple()
        else:
            search_for_text()
        if os.stat(alert_txt_file).st_size > 0:
            send_alert_email()
    except Exception, e:
        print e
