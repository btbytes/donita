'''
models.py

Copyright 2008, Pradeep Kishore Gowda <pradeep.gowda@gmail.com>
All rights reserved.
'''

from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    user = models.ForeignKey(User)
    action = models.CharField(max_length=140, )
    status = models.BooleanField()
    pub_date = models.DateTimeField(auto_now_add=True)
    
    class Admin:
        list_display = ('user', 'action', 'status', 'pub_date')
        list_filter = ('pub_date',)
        search_fields = ('action',)
    def __str__(self):
        return self.action