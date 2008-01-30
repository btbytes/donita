'''
views.py

Copyright 2008, Pradeep Kishore Gowda <pradeep.gowda@gmail.com>
All rights reserved.
'''

from django.shortcuts import HttpResponse, render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import Context, RequestContext
from models import Todo
from django.core import serializers
from django.template.loader import get_template

@login_required
def get_items(request):
    items = Todo.objects.filter(user__username__exact = request.user.username).order_by('-pub_date')
    tmpl = get_template('todo_ahah.html')
    return HttpResponse(tmpl.render(Context({'items':items})))

@login_required
def list_items(request):
    if request.user.is_authenticated:
        return render_to_response('tada/todo.html',{},context_instance=RequestContext(request))
    else:
        return render_to_response('tada/index.html',{},context_instance=RequestContext(request))

@login_required    
def add(request):
    if request.method =='POST':
        try:
            action = request['action']
            print 'action is:', action
        except:
            return HttpResponseRedirect('/')
        item = Todo(action=action, status=False, user=request.user)
        item.save()
    return HttpResponseRedirect('/')
    
@login_required
def remove(request):
    print request.user.username 
    if request.method == 'POST':
        try:
            item = Todo.objects.get(pk=request['item_id'])
            user = item.user
            if request.user.username == user.username:
                print item.status,
                item.status = True
                item.save()
                print 'item saved?'
                item = Todo.objects.get(pk=request['item_id'])
                print item.status
            else:
                return HttpResponse("""<img src="/static/css/blueprint/plugins/buttons/icons/cross.png" alt=""/>
                <span>Trying to delete invalid item</span>""")
        except:
            return HttpResponse("""<img src="/static/css/blueprint/plugins/buttons/icons/cross.png" alt=""/>
                <span>Trying to delete non-existant item</span>""")
                
    return HttpResponse("""<img src="/static/css/blueprint/plugins/buttons/icons/tick.png" alt=""/>
                <span>Item deleted</span>""")