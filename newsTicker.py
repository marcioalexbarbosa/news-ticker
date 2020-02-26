#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import feedparser
import threading

def fetchFirstSecond(feed):
  dict = feedparser.parse(feed)
  for post in dict.entries[:2]:
    print ("* " + post.title + " (" + post.links[0].href + ")")

def fetch():
  threading.Timer(1200.0, fetch).start()

  print ("=" * 80)

  fetchFirstSecond('http://rss.home.uol.com.br/index.xml')

  fetchFirstSecond('https://g1.globo.com/rss/g1/')

  fetchFirstSecond('http://feeds.bbci.co.uk/portuguese/rss.xml')

  fetchFirstSecond('https://noticias.r7.com/feed.xml')

  fetchFirstSecond('https://rss.tecmundo.com.br/feed')

fetch()

