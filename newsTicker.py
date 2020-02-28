#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import feedparser
import threading
import random
from datetime import datetime

count = 0

def fetchFirstSecond(feed):
  dict = feedparser.parse(feed)
  random.shuffle(dict.entries)
  for post in dict.entries[:2]:
    print ("* " + post.title + " ( " + post.links[0].href + " )")

def fetch():
  global count
  
  threading.Timer(1200.0, fetch).start()

  count = count + 1

  now = datetime.now()

  date_time = now.strftime("%d/%m/%Y, %H:%M:%S")

  print (date_time + " - " + str(count) + " " + ("=" * 80))

  fetchFirstSecond('http://rss.home.uol.com.br/index.xml')

  fetchFirstSecond('https://g1.globo.com/rss/g1/')

  fetchFirstSecond('http://feeds.bbci.co.uk/portuguese/rss.xml')

  fetchFirstSecond('https://rss.msn.com/pt-br/')

  fetchFirstSecond('https://gizmodo.uol.com.br/feed/')

fetch()

