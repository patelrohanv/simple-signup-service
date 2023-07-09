# userapp/views.py
from django.shortcuts import render
from .forms import UserForm
from .models import User

def user_create_view(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "userapp/create_users.html", context)

def user_list_view(request):
    users = User.objects.all()
    return render(request, 'userapp/list_users.html', {'users': users})