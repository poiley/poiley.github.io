#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Ben Poile'
SITENAME = 'blog'
SITEURL = ''

PATH = 'content'
OUTPUT_PATH = 'output'

STATIC_PATHS = ['articles', 'downloads']

ARTICLE_PATHS = ['articles',]
ARTICLE_URL = 'articles/{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{date:%m}/{slug}.html'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 3

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'themes/cebong'

#DIRECT_TEMPLATES = (('index', 'blog', 'tags', 'categories', 'archives'))
#PAGINATED_DIRECT_TEMPLATES = (('blog', ))
#TEMPLATE_PAGES = {'home.html': 'index.html',}
