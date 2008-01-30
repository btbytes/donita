'''
urls.py

Copyright 2008, Pradeep Kishore Gowda <pradeep.gowda@gmail.com>
All rights reserved.
'''
import os
from django.conf.urls.defaults import *
from django.conf import settings

# set this to the directory under which the static files (css, js) files are located.
STATIC_PATH = os.path.join(settings.PROJECT_PATH, 'static')
    
urlpatterns = patterns('',
    # the admin interface
    (r'^admin/', include('django.contrib.admin.urls')),
    # serve static files; not recommended for production usage.
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_PATH}),
    # todo related
    (r'^todo/add/$', 'donita.apps.tada.views.add',),
    (r'^todo/del/$', 'donita.apps.tada.views.remove',),
    # login
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout'),    
    #ajax call for updating items
    (r'^todo/items/$', 'donita.apps.tada.views.get_items',),
    # default logged in view
    (r'^$', 'donita.apps.tada.views.list_items',),
    
    # homepage
    # (r'^$','django.views.generic.simple.direct_to_template', {'template': 'index.html'}),
    )
