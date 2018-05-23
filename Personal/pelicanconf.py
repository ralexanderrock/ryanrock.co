#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ryan Rock'
SITENAME = u"Home"
SITETITLE = AUTHOR
SITESUBTITLE = ''
SITELOGO = '/images/profile.jpg'
SITEURL = 'http://www.ryanrock.co'

COPYRIGHT_YEAR = '2018'
TIMEZONE = 'America/Chicago'
DEFAULT_LANG = u'en'

PATH = 'content'
STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {'extra/custom.css': {'path': 'static/custom.css'}}
CUSTOM_CSS = 'static/custom.css'

PLUGINS = ['pelican_vimeo']

# URL settings(http://docs.getpelican.com/en/stable/settings.html#url-settings)
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'

DEFAULT_PAGINATION = 6
DEFAULT_CATEGORY = 'News'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = "/home/rar/Utilities/pelican/pelican-themes/Flex"

MAIN_MENU = True

# Blogroll
LINKS = (("Ephemera", 'http://www.ephemera.net/'),
         ('Juicebox', 'http://www.juicebox.club/'))

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/ryan-rock-9a7430b6'),
          ('twitter', 'https://twitter.com/ralexanderrock'),
          ('instagram','https://www.instagram.com/ralexanderrock/'),
          ('github', 'https://github.com/ralexanderrock'))

# Menu items
MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
