from django.shortcuts import render, redirect
from contact.forms import RegisterForm, RegisterUpdateForm
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm

def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario registrado com sucesso')
            return redirect('contact:login')

    return render(request, 'contact/register.html', {
        'form': form
    })


def login_view(request):

    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Logado com sucesso!')
            return redirect('contact:index')

        #Caso nao logue    
        messages.error(request, 'Login invalido')
    
    return redirect('user:update')


def logout_view(request):
    auth.logout(request)

    return redirect('contact:login')

def user_update(request):
    form = RegisterUpdateForm(instance=request.user)

    if request.method != 'POST':
        return render(request, 'contact/user_update.html', {
            'form': form
        })
    
    form = RegisterUpdateForm(data=request.POST, instance=request.user)

    if not form.is_valid():
        return render(request, 'contact/user_update.html', {
            'form': form
        })
    
    form.save()
    return render(request, 'contact/register.html', {
            'form': form
    })
    