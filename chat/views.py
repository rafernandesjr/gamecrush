from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.safestring import mark_safe
from gamecrush.models import User
import json

def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name, auth_id, user_id):
    user_sel = User.objects.get(id = user_id)
    name = user_sel.name
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'auth_id': auth_id,
        'name': name
    })