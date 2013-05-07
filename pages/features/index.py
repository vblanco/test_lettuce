import urllib2
from lettuce import *
from lxml import html
from django.test.client import Client
from nose.tools import assert_equals
from lettuce import step, world
from lettuce.django import django_url

@before.all
def set_browser():
    world.browser = Client()

@step(r'Given I navigate to "(.*)"')
def navigate_to_url(step, url):
    url = django_url(url)
    raw = urllib2.urlopen(url).read()
    world.dom = html.fromstring(raw)

@step(r'I access the url "(.*)"')
def access_url(step, url):
    response = world.browser.get(url)
    world.dom = html.fromstring(response.content)

@step(r'I see the header "(.*)"')
def see_header(step, text):
    header = world.dom.cssselect('h1')[0]
    assert header.text == text
