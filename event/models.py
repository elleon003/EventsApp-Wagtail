from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.search import index


class EventIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]

    max_count = 1
    subpage_types = ['EventPage']


class EventPage(Page):
    date = models.DateField("Event Date")
    start_time = models.TimeField("Start Time")
    end_time = models.TimeField("End Time")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('start_time'),
        FieldPanel('end_time'),
        FieldPanel('intro'),
        FieldPanel('body')
    ]

    parent_page_types = ['EventIndexPage']
    subpage_types = []

    