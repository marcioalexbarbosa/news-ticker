#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import feedparser
import threading

count = 0

def fetchFirstSecond(feed):
  dict = feedparser.parse(feed)
  for post in dict.entries[:2]:
    print ("* " + post.title + " (" + post.links[0].href + ")")

def fetch():
  global count
  
  threading.Timer(1200.0, fetch).start()

  count = count + 1

  print (str(count) + ("=" * 80))

  fetchFirstSecond('http://rss.home.uol.com.br/index.xml')

  fetchFirstSecond('https://g1.globo.com/rss/g1/')

  fetchFirstSecond('http://feeds.bbci.co.uk/portuguese/rss.xml')

  fetchFirstSecond('https://noticias.r7.com/feed.xml')

  fetchFirstSecond('https://rss.tecmundo.com.br/feed')

fetch()

