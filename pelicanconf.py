#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ryan Rock'
SITENAME = u"Home"
SITETITLE = AUTHOR
SITESUBTITLE = ''
SITELOGO = '/images/profile.jpg'
SITEURL = ''

COPYRIGHT_YEAR = '2019'

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

TIMEZONE = 'America/Chicago'
DEFAULT_LANG = u'en'

PATH = 'content'
STATIC_PATHS = ['images', 'extra', 'articles', 'pages']
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
    'extra/form.css': {'path': 'static/form.css'},
    'extra/404.shtml': {'path': '404.shtml'}
    }

CUSTOM_CSS = 'static/custom.css'
FORM_CSS = 'static/form.css'

PLUGINS = ['pelican_vimeo']
DISQUS_SITENAME = 'ryanrock'

GOOGLE_SITE_VERIFICATION = 'mUIKMHFEAUvK3vL-7vS-47kQ6CGDuZUNom5WW7z9Hek'

# URL settings(http://docs.getpelican.com/en/stable/settings.html#url-settings)
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

DEFAULT_PAGINATION = 6
DEFAULT_CATEGORY = 'News'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = "./theme"
PYGMENTS_STYLE = 'monokai'
MAIN_MENU = True

# Blogroll
LINKS = (("Ephemera", 'http://www.ephemera.net/'),
         ("Terraformarium", 'http://www.terraformarium.com'),
         ('Juicebox', 'http://www.juicebox.club/'))

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/ryan-rock-9a7430b6'),
          ('twitter', 'https://twitter.com/ralexanderrock'),
          ('instagram','https://www.instagram.com/ralexanderrock/'),
          ('github', 'https://github.com/ralexanderrock'))

# Menu items
MENUITEMS = (('Biography', '/biography.html'),
             ('Quotes','/quoteblog.html'),
             ('Subscribe', '/subscribe.html'))

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
