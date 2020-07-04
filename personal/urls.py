from django.urls import path
from django.conf.urls import url
from django.utils.translation import gettext_lazy as _
from . import views
urlpatterns=[
    path('',views.index,name="home"),
    path(_('about'),views.about,name="about"),
    path(_('resume'),views.resume,name="resume"),
    path(_('certifications'),views.certifications,name="certifications"),
    path(_('services'),views.services,name="services"),
    path(_('portfolio'),views.portfolio,name="portfolio"),
    path(_('contact'),views.contact,name="contact"),
]