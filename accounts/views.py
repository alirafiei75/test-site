from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, forms
from django.contrib.auth.decorators import login_required

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/')
        form = forms.AuthenticationForm()
        context = {'form':form}
        return render(request, 'accounts/login.html', context)
    else:
        return redirect('/')

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        form = forms.UserCreationForm()
        context = {'form':form}
        return render(request, 'accounts/signup.html', context)



