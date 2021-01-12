from django.shortcuts import render, redirect
from .forms import UserRegisteratonForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisteratonForm(request.POST) 
        if form.is_valid():
            form.save();
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}!')
            return redirect('vlog-home')   
    else:
        form = UserRegisteratonForm()
    return render(request, 'users/register.html' , {'form': form})
    
