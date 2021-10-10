#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Ben Poile'
SITENAME = 'blog'
SITEURL = 'https://poiley.github.io'
# GITHUB_URL = 'https://github.com/poiley/poiley.github.io'


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

# Blog Roll
LINKS = (('Home', 'https://poile.dev/'),
         ('All Posts', 'https://www.python.org/'),
         ('Resume', 'https://docs.google.com/document/d/1T2MaWT8CHgR9t5hDoQqLDpXZYJ5eKKwgfJBa2nVceo0/edit?usp=sharing'))

# Social widget
SOCIAL = (('Github', 'https://github.com/poiley'),
          ('Spotify', 'https://open.spotify.com/user/qqxne71rxqru593o2cg1y8avg?si=fb593f2b738f4402'),
          ('Twitter', 'https://twitter.com/_poile_'))

DEFAULT_PAGINATION = 3

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'themes/cebong'

#DIRECT_TEMPLATES = (('index', 'blog', 'tags', 'categories', 'archives'))
#PAGINATED_DIRECT_TEMPLATES = (('blog', ))
#TEMPLATE_PAGES = {'home.html': 'index.html',}
