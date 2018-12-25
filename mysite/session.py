from django import forms
from django.shortcuts import render, redirect
from exam.models import UserProfile


class FormLogin(forms.Form):
    username = forms.CharField(label=("帳號"), required=True)
    password = forms.CharField(label=("密碼"), widget=forms.PasswordInput, required=True)


def session(request):
    username = None  # default value
    form_login = FormLogin()
    if request.method == 'GET':

        if 'action' in request.GET:
            action = request.GET.get('action')
            if action == 'logout':
                if request.session.has_key('username'):
                    request.session.flush()
                return redirect('login2')

        if 'username' in request.session:
            username = request.session['username']
            print(request.session.get_expiry_age())  # session lifetime in seconds(from now)
            print(
                request.session.get_expiry_date())  # datetime.datetime object which represents the moment in time at which the session will expire

    elif request.method == 'POST':
        form_login = FormLogin(request.POST)
        if form_login.is_valid():
            username = form_login.cleaned_data['username']
            password = form_login.cleaned_data['password']
            user = UserProfile.objects.get(Username=username)
            if user:
                if username.strip() == user.Username and password.strip() == user.Password:
                    request.session['username'] = user.FullName
                    NOWUser = user
                    if user.Username == user.FullName:
                        return render(request, 'manage/rename.html',
                                  {'username': user.FullName, 'NOWUser': NOWUser,})
                    else:
                        return render(request, 'manage/index_base.html',
                                      {'username': user.FullName, 'NOWUser': NOWUser, })
                else:
                    username = None

    return render(request, 'manage/login2.html', {
        'form': form_login,
        'username': username,
        })