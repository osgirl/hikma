from django.conf.urls import url

from . import views

urlpatterns = [
               # ex: /anticounterfeit/
               url(r'^$', views.index, name='index'),
               # ex: /anticounterfeit/check
               url(r'^check/$', views.check, name='check'),
               # ex: /anticounterfeit/check.css
               #url(r'^check/check.css/$', views.checkCSS, name='checkCSS'),
               # ex: /anticounterfeit/state/cairo
               url(r'^state/$', views.state, name='state'),
               # ex: /anticounterfeit/cairo/city
               url(r'^(?P<state>[a-zA-Z]+)/city$', views.city, name='check'),

]