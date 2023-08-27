AUTHOR = 'vkuehn'
SITENAME = 'mmMover2023_05'
SITEURL = 'https://vkuehn.github.io/mmMover2023_05/'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'de'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),)

# Social widget
SOCIAL = (('none', '#'),
          ('none', '#'),)

DEFAULT_PAGINATION = 2

DISPLAY_PAGES_ON_MENU = True

IGNORE_FILES = ['.ipynb*', '__pycache__']

LOAD_CONTENT_CACHE = False

OUTPUT_PATH = './output/'
PATH = './content'

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True