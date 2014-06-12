#!/usr/bin/env python2
# -*- coding: utf-8 -*- 

import feedparser
import pywapi

def shorten_title(entree):
    link = entree[0]
    title = entree[1]
    if ('nyaa' in link):
        title = title.split('] ')[1].replace('- ', '').split('[')[0]
    elif ('batoto' in link):
        parts = title.split(' - ')
        title = parts[0] + ' ' + parts[2].split(':')[0][3:]
    return (link, title)

def get_rss(feeds):
    entrees = []
    for link in feeds:
        entrees += feedparser.parse(link)['items']
    entrees.sort(key = lambda entree: entree['published_parsed'])
    entrees.reverse()
    entrees = map(lambda entree: (entree['link'], entree['title']), entrees)[0:8]
    return map(lambda entree: shorten_title(entree), entrees)

def get_conditions(code):
    weather = pywapi.get_weather_from_weather_com(code)
    return weather['current_conditions']['text']

def get_temp(code):
    weather = pywapi.get_weather_from_weather_com(code)
    return weather['current_conditions']['temperature']

def format_link(link, name):
    name = name.encode('utf8')
    str = '<li><a href="{link}">{name}</a>'
    return str.format(**locals())

def format_list(list, title):
    value = '<h1>{title}</h1><div class="linkList"><ul>'.format(**locals())
    for item in list:
        value += format_link(*item)
    value += '</ul></div>'
    return value

