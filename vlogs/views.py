from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# info = [
#     {
#         'title': 'Osamas Effects',
#         'content': 'Music Videos',
#         'status': True
#     },
#     {
#         'title': 'Shujja Edits',
#         'content': 'Music Videos',
#         'status': True
#     },
#     {
#         'title': 'OS Edits',
#         'content': 'Funny Videos',
#         'status': False
#     }
# ]

# Create your views here.
def index(request):
    context = {
    "info": Post.objects.all()
    }
    return render(request, 'vlogs/index.html', context)
    
def about(request):
    return render(request, 'vlogs/about.html', {'title' : 'About'})

    
def login(request):
    return render(request, 'vlogs/login.html', {'title' : 'Login'})