from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from exam.models import UserProfile, Examinees ,Exam_administrator,System_administrator,Score_reviewers,Questions_bank_operator,Questions_bank_administrator
from django.utils import timezone

# Create your views here.


def logining(request):
    template = 'manage/login2.html'
    if request.method == 'GET':
        return render(request, template)
    # POST
    username = request.POST.get('username')
    password = request.POST.get('password')
    if not username or not password:    # Server-side validation
        messages.error(request, '請填資料')
        return render(request, template)
    if UserProfile.objects.count() != 0:
        user = UserProfile.objects.filter(Username=username)
        pwd = UserProfile.objects.filter(Password=password)
        if user and pwd:
                messages.success(request, '登入成功')
                return redirect('manage:Index')
        else:
                messages.error(request, '帳號密碼錯誤')
                return render(request, template)
    else:
        messages.error(request, '用戶不存在')


def index(request):
    template = 'manage/index_base.html'
    User = UserProfile.objects.all()
    if 'username' in request.session:
        username = request.session['username']
        NOWUser = UserProfile.objects.get(FullName=username)

    return render(request, template, locals())


def SAhome(request):
    template = 'manage/SAhome.html'
    User = UserProfile.objects.all().order_by('-Updated')[:10]
    if 'username' in request.session:
        username = request.session['username']
    return render(request, template, locals())


def create(request):
    template = 'manage/create.html'
    if 'username' in request.session:
        username_s = request.session['username']
    if request.method == 'GET':
        return render(request, template, {'username': username_s, })
    # POST
    username = request.POST.get('Username')
    password = request.POST.get('Username')
    authority = request.POST.getlist('Authority')

    if not username or not authority:    # Server-side validation
        messages.error(request, '請填資料')
        return render(request, template,)

    if UserProfile.objects.count() != 0:
        user = UserProfile.objects.filter(Username=username)
        if user:
            messages.error(request, '帳號重複',)
        else:
            UserProfile.objects.create(Username=username, Password=password, Authority=authority, FullName=username,)
            if '1' in authority :
                    System_administrator.objects.create(user=UserProfile.objects.get(Username=username))
            if '2' in authority:
                    Exam_administrator.objects.create(user=UserProfile.objects.get(Username=username))
            if '3' in authority:
                    Questions_bank_administrator.objects.create(user=UserProfile.objects.get(Username=username))
            if '4' in authority:
                    Score_reviewers.objects.create(user=UserProfile.objects.get(Username=username))
            if '5' in authority:
                    Examinees.objects.create(user=UserProfile.objects.get(Username=username))
            if '6' in authority:
                    Questions_bank_operator.objects.create(user=UserProfile.objects.get(Username=username))
            messages.success(request, '新增成功',)
    else:
        UserProfile.objects.create(Username=username, Password=password, Authority=authority, FullName=username,)
        if '1' in authority:
            System_administrator.objects.create(user=UserProfile.objects.get(Username=username))
        if '2' in authority:
            Exam_administrator.objects.create(user=UserProfile.objects.get(Username=username))
        if '3' in authority:
            Questions_bank_administrator.objects.create(user=UserProfile.objects.get(Username=username))
        if '4' in authority:
            Score_reviewers.objects.create(user=UserProfile.objects.get(Username=username))
        if '5' in authority:
            Examinees.objects.create(user=UserProfile.objects.get(Username=username))
        if '6' in authority:
            Questions_bank_operator.objects.create(user=UserProfile.objects.get(Username=username))
        messages.success(request, '新增成功')

    return redirect('SAhome')


def update(request):
    template = 'manage/update.html'
    User = UserProfile.objects.all().order_by('-Updated')
    if 'username' in request.session:
        username = request.session['username']
    # if request.method == 'GET':
    #     return render(request, template, {'User': User, 'username': username})
    return render(request, template, {'User': User, 'username': username})


def datamanage(request):
    template = 'manage/datamanage.html'
    if 'username' in request.session:
        username = request.session['username']
    if request.method == 'GET':
        return render(request, template, {'username': username})
    return render(request, template,)


def backup(request):
    template = 'manage/backup.html'
    if 'username' in request.session:
        username = request.session['username']
    if request.method == 'GET':
        return render(request, template, {'username': username})
    return render(request, template,)


def reloading(request):
    template = 'manage/reloading.html'
    if 'username' in request.session:
        username = request.session['username']
    if request.method == 'GET':
        return render(request, template, {'username': username})
    return render(request, template,)


def updateing(request, id):
    template = 'manage/EVupdate.html'
    if 'username' in request.session:
        username_s = request.session['username']
    instance = get_object_or_404(UserProfile, id=id)
    authority = request.POST.getlist('Authority')
    username = request.POST.get('Username')
    if not authority:    # Server-side validation
        messages.error(request, '請填資料')
        return render(request, template, locals())
    else:
        if '1' not in authority:
            num = UserProfile.objects.filter(Authority__contains='1').count()
            if num <= 1:
                messages.error(request, "系統管理員不可少於一人")
                return render(request, template, locals())
        UserProfile.objects.filter(id=instance.id).update(Authority=authority, Updated=timezone.now())
        if '1' in authority:
            System_administrator.objects.update_or_create(user=UserProfile.objects.get(Username=username))
        if '2' in authority:
            Exam_administrator.objects.update_or_create(user=UserProfile.objects.get(Username=username))
        if '3' in authority:
            Questions_bank_administrator.objects.update_or_create(user=UserProfile.objects.get(Username=username))
        if '4' in authority:
            Score_reviewers.objects.update_or_create(user=UserProfile.objects.get(Username=username))
        if '5' in authority:
            Examinees.objects.update_or_create(user=UserProfile.objects.get(Username=username))
        if '6' in authority:
            Questions_bank_operator.objects.update_or_create(user=UserProfile.objects.get(Username=username))
        return redirect('SAhome')


def resetpwd(request, id):
    User = get_object_or_404(UserProfile, id=id)
    UserProfile.objects.filter(id=User.id).update(Password=User.Username)
    return redirect('updateing', id=id)


def personalmodify(request):
    if 'username' in request.session:
        username = request.session['username']
        NOWUser = UserProfile.objects.get(FullName=username)

    user = UserProfile.objects.get(FullName=username)
    user1 = UserProfile.objects.get(Username=user.Username)
    user2 = Examinees.objects.get(user__Username=user.Username)

    if request.method == "POST":
        psd = request.POST["psd"]
        psd2 = request.POST["psd2"]
        name = request.POST["name"]
        sex = request.POST["sex"]
        department = request.POST["department"]
        clas = request.POST["cy"]
        company = request.POST["company"]
        comp_num = request.POST["comp_num"]

    else:
        psd = user.Password
        psd2 = user.Password
        name = user.FullName
        sex = user2.Sex
        department = user2.Major
        clas = user2.Class
        company = user2.Company
        comp_num = user2.Comp_Num

    if psd == psd2:
        UserProfile.objects.filter(Username=user.Username).update(Password=psd)
    else:
        errormsg = '密碼輸入錯誤，無法更新'

    UserProfile.objects.filter(Username=user.Username).update(FullName=name)
    Examinees.objects.filter(user__Username=user1.Username).update(Sex=sex)
    Examinees.objects.filter(user__Username=user1.Username).update(Major=department)
    Examinees.objects.filter(user__Username=user1.Username).update(Class=clas)
    Examinees.objects.filter(user__Username=user1.Username).update(Company=company)
    Examinees.objects.filter(user__Username=user1.Username).update(Comp_Num=comp_num)

    if request.method == 'GET':
        return render(request, "manage/personalmodify.html", locals())
    else:
        return render(request, "manage/index_base.html", locals())


def personalmodify2(request):
    if 'username' in request.session:
        username = request.session['username']
        NOWUser = UserProfile.objects.get(FullName=username)

    user = UserProfile.objects.get(FullName=username)
    user1 = UserProfile.objects.get(Username=user.Username)

    if request.method == "POST":
        psd = request.POST["psd"]
        psd2 = request.POST["psd2"]
        name = request.POST["name"]

    else:
        psd = user.Password
        psd2 = user.Password
        name = user.FullName

    if psd == psd2:
        UserProfile.objects.filter(Username=user.Username).update(Password=psd)
    else:
        errormsg = '密碼輸入錯誤，無法更新'

    UserProfile.objects.filter(Username=user.Username).update(FullName=name)

    if request.method == 'GET':
        return render(request, "manage/personalmodify2.html", locals())
    else:
        return render(request, "manage/index_base.html", locals())


def newpersonalmodify(request):
    if 'username' in request.session:
        username = request.session.get['username']

    user1 = UserProfile.objects.get(Username=username)
    user2 = Examinees.objects.get(user__Username=username)

    if request.method == "POST":
        psd = request.POST["psd"]
        psd2 = request.POST["psd2"]
        name = request.POST["name"]
        sex = request.POST["sex"]
        department = request.POST["department"]
        clas = request.POST["cy"]
        company = request.POST["company"]
        comp_num = request.POST["comp_num"]

    if psd == psd2:
        UserProfile.objects.filter(Username=user1.Username).update(Password=psd)
    else:
        errormsg = '密碼輸入錯誤，無法更新'

    UserProfile.objects.filter(Username=user1.Username).update(FullName=name)
    Examinees.objects.filter(user__Username=user1.Username).update(Sex=sex)
    Examinees.objects.filter(user__Username=user1.Username).update(Major=department)
    Examinees.objects.filter(user__Username=user1.Username).update(Class=clas)
    Examinees.objects.filter(user__Username=user1.Username).update(Company=company)
    Examinees.objects.filter(user__Username=user1.Username).update(Comp_Num=comp_num)

    if request.method == 'GET':
        return render(request, "manage/newpersonalmodify.html", locals())
    else:
        return render(request, "manage/index_base.html", locals())


def rename(request):
    if request.method == "POST":
        if 'username' in request.session:
            username = request.session['username']
            NOWUser = UserProfile.objects.get(FullName = username)
        name = request.POST['name']
        request.session['username'] = name
        UserProfile.objects.filter(Username=NOWUser.Username).update(FullName=name)
        return render(request, 'manage/index_base.html', locals())
