#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Aart Goossens'
SITENAME = 'AartGoossens.github.io'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = True

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = [
    'render_math',
    'better_codeblock_line_numbering',
    'better_figures_and_images',
]

MATH_JAX = {
    'color': 'black',
}

STATIC_PATHS = [
    'images',
]

RESPONSIVE_IMAGES = True
