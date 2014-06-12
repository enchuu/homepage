#!/usr/bin/env python2
# -*- coding: utf-8 -*- 

import time
from homepage import *

template_name = 'template.html'
output_name = 'index.html'
search = True
weather = True

hour = time.localtime().tm_hour
title_string='hello'
titles=['example','example','news1','news2']

rss1 = ['http://feeds.bbci.co.uk/news/rss.xml']

rss2 = ['http://www.aljazeera.com/Services/Rss/?PostingId=2007731105943979989']

col1 = [ ('http://example.com', 'example')
        ,('http://example.com', 'example')
        ,('http://example.com', 'example')
        ,('http://example.com', 'example')
        ,('http://example.com', 'example')
        ,('http://example.com', 'example')
        ,('http://example.com', 'example')
        ,('http://example.com', 'example')
        ]
col2 = [ ('http://example.com', 'example')
        ,('http://example.com', 'example')
        ,('http://example.com', 'example')
        ,('http://example.com', 'example')
        ,('http://example.com', 'example')
        ,('http://example.com', 'example')
        ,('http://example.com', 'example')
        ,('http://example.com', 'example')
        ]
col3 = get_rss(rss1)
col4 = get_rss(rss2)
cols=[col1,col2,col3,col4]

search_bar = '<form action="https://duckduckgo.com/" method="get"><input type="text" name="q" id="search" autofocus/></form>'

id = '12404'
weather_string = 'It is currently:<br><br>{0} and {1}°'.format(get_conditions(id), get_temp(id))

template = open(template_name).read()
output = template.format(*(map(lambda i: format_list(cols[i], titles[i]), [0,1,2,3]) + [search_bar if search else ''] + [weather_string if weather else ''] + [title_string]))
output_file = open(output_name, 'w')
output_file.write(output)
