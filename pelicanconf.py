from __future__ import unicode_literals

AUTHOR = u'Pyninsula Organizers'
SITENAME = u'Pyninsula - Python in the Peninsula!'
SITEURL = 'https://pyninsula.org'
STATIC_PATHS = ['assets']

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LINKS = (
    ("meetup.com", 'https://www.meetup.com/Pyninsula-Python-Peninsula-Meetup/'),
    ("YouTube", 'https://www.youtube.com/channel/UCiT1ZWcRdFLx7PuR3fTjTfA'),
    ("Twitter", 'http://twitter.com/pyninsula'),
    ("GitHub", 'http://github.com/pyninsula/website'),
    ("Python", 'https://python.org/'),
        )

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 10
RELATIVE_URLS = True

TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''

ABOUT_ME = """
<p>
Pyninsula is a group of Bay-Area Python enthusiasts, based in "the
Peninsula", the area north of the South Bay and south of San
Francisco, roughly corresponding to
<a rel="noopener" target="_blank" href="https://en.wikipedia.org/wiki/Area_code_650">the 650 area code</a>.

<p><img width="100%" src="./assets/img/guido_group_2017.jpg" /></p>
</p><p>
Every month, we meet in a new location to socialize, hear
short talks from our community, and (occasionally!) get some work done.
For our next meeting and more information, check out
our <a href="https://www.meetup.com/Pyninsula-Python-Peninsula-Meetup/">meetup.com page</a>.
You can also:

<ul>
  <li><a rel="noopener" target="_blank" href="https://www.youtube.com/channel/UCiT1ZWcRdFLx7PuR3fTjTfA">Watch talks from Pyninsulas past</a></li>
  <li><a href="./pages/give-a-talk.html">Submit a talk</a></li>
  <li><a href="./pages/host-a-pyninsula.html">Host a Pyninsula</a></li>
  <li><a rel="noopener" target="_blank" href="https://www.flickr.com/photos/mahmoudhashemi/albums/72157685497080926">See more photos</a> (and <a rel="noopener" target="_blank" href="https://www.flickr.com/photos/mahmoudhashemi/albums/72157669233092359">even more</a>)</li>
  <li><a rel="noopener" target="_blank" href="http://twitter.com/pyninsula">Follow us on Twitter</a> and <a rel="noopener" target="_blank" href="https://www.meetup.com/Pyninsula-Python-Peninsula-Meetup/?action=join">join our meetup group</a>!
</ul>
</p>
<p>Pyninsula is dedicated to a harassment-free conference experience for everyone. See our <a href="https://pyninsula.org/pages/code-of-conduct.html">Code of Conduct</a>.</p>
"""
