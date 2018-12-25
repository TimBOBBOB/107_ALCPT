from django.template.loader import get_template
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from exam import models, forms
from .models import talk, grammar, short_conversation, noun, reading, UserProfile, Examinees, Score, Company, Department, exam, topic, member, post
from .forms import grammarform, short_conversationform, nounform, readingform, examform,postform
from django.db.models import Q
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy
from datetime import datetime, timezone
import json
import random


def exam_manager(request):
    if 'username' in request.session:
        username = request.session['username']
    return render(request, 'exam/exam_manager.html', locals())


def question_manager(request):
    if 'username' in request.session:
        username = request.session['username']
    return render(request, 'question/question_manager.html', locals())


def addquestion(request):
    if 'username' in request.session:
        username = request.session['username']
    return render(request, 'question/addquestion.html', locals())


def addquestion_e(request):
    if 'username' in request.session:
        username = request.session['username']
    return render(request, 'employee/addquestion_e.html', locals())


def updatequestion(request):
    if 'username' in request.session:
        username = request.session['username']
    return render(request, 'question/updatequestion.html', locals())


def listingquestion(request):
    if 'username' in request.session:
        username = request.session['username']
    return render(request, 'question/listingquestion.html', locals())


def review(request):
    if 'username' in request.session:
        username = request.session['username']
    return render(request, 'question/review/review.html', locals())


def addexam(request):
    if 'username' in request.session:
        username = request.session['username']

    if request.method == "POST":
        form = examform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/exam_manager/')
    else:
            form = examform()
    return render(request, 'exam/addexam.html', {'examform': form, 'username':username})


def alterexam(request):
    if 'username' in request.session:
        username = request.session['username']

    template = get_template('exam/alterexam.html')
    try:
        urid=request.GET['q_id']
    except:
        urid = None
    Exam=models.exam.objects.all().order_by('-ddate')
    html = template.render(context=locals(), request=request)
    return HttpResponse(html)


def edit_exam(request,qs):
    if 'username' in request.session:
        username = request.session['username']

    posts=get_object_or_404(models.exam,id=qs)
    if request.method=='POST':
        edit_form_exam=forms.examform(request.POST,instance=posts)
        if   edit_form_exam.is_valid():
           posts=edit_form_exam.save(commit=False)
           posts.save()
           return redirect('alterexam')

        else:
           edit_form_exam=forms.examform(instance=posts)
    else:
        edit_form_exam=forms.examform(instance=posts)

    return render(request, 'exam/edit_exam.html',{'edit_form_exam': edit_form_exam, 'username':username})


def cancleexam(request):
    if 'username' in request.session:
        username = request.session['username']

    template = get_template('exam/cancleexam.html')
    try:
        urid = request.GET['q_id']
    except:
        urid = None
    Exam = models.exam.objects.all().order_by('-ddate')
    html = template.render(context=locals(), request=request)
    return HttpResponse(html)


class delete_exam(DeleteView):
    model = models.exam
    success_url = reverse_lazy('cancleexam')


def list_post(request):
    if 'username' in request.session:
        username = request.session['username']

    template = get_template('exam/list_post.html')
    try:
        urid = request.GET['q_id']
    except:
        urid = None
    Post = models.post.objects.all().order_by('-created')
    html = template.render(context=locals(), request=request)
    return HttpResponse(html)


def new_post(request):
    if 'username' in request.session:
        username = request.session['username']

    if request.method == "POST":
        form = postform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/list_post/')
    else:
            form = postform()
    return render(request, 'exam/new_post.html', {'postform': form, 'username':username})


def edit_post(request,qs):
    if 'username' in request.session:
        username = request.session['username']

    posts=get_object_or_404(models.post, id=qs)
    if request.method=='POST':
        edit_form_post=forms.postform(request.POST, instance=posts)
        if edit_form_post.is_valid():
           posts=edit_form_post.save(commit=False)
           posts.save()
           return redirect('list_post')

        else:
           edit_form_post=forms.postform(instance=posts)
    else:
        edit_form_post=forms.postform(instance=posts)

    return render(request, 'exam/edit_post.html',{'edit_form_post': edit_form_post, 'username':username})


class  delete_post(DeleteView):
    model = models.post
    success_url = reverse_lazy('list_post')


def addexam_simulation(request):
    if 'username' in request.session:
        username = request.session['username']
    return render(request, 'exam/addexam_simulation.html', locals())


def alterexam_simulation(request):
    if 'username' in request.session:
        username = request.session['username']
    return render(request, 'exam/alterexam_simulation.html', locals())


def addexam_computer(request):
    if 'username' in request.session:
        username = request.session['username']

    r1 = talk.objects.none()
    t1 = talk.objects.all()
    w1 = random.sample(range(1, 50), 40)
    data1 = {}
    for d1 in range(1, 41, 1):
        ran1 = w1[d1-1]
        r1 = r1 | talk.objects.filter(id=t1[ran1].id)
        k1 = "q" + str(d1)
        j1 = t1[ran1].id
        data1.setdefault(k1, j1)

    r2 = short_conversation.objects.none()
    t2 = short_conversation.objects.all()
    w2 = random.sample(range(1, 50), 20)
    for d2 in range(41, 61, 1):
        ran2 = w2[d2-41]
        r2 = r2 | short_conversation.objects.filter(id=t2[ran2].id)
        k2 = "q" + str(d2)
        j2 = t2[ran2].id
        data1.setdefault(k2, j2)

    r3 = noun.objects.none()
    t3 = noun.objects.all()
    w3 = random.sample(range(1, 50), 15)
    for d3 in range(61, 76, 1):
        ran3 = w3[d3-61]
        r3 = r3 | noun.objects.filter(id=t3[ran3].id)
        k3 = "q" + str(d3)
        j3 = t3[ran3].id
        data1.setdefault(k3, j3)

    r4 = grammar.objects.none()
    t4 = grammar.objects.all()
    w4 = random.sample(range(1, 50), 15)
    for d4 in range(76, 91, 1):
        ran4 = w4[d4-76]
        r4 = r4 | grammar.objects.filter(id=t4[ran4].id)
        k4 = "q" + str(d4)
        j4 = t4[ran4].id
        data1.setdefault(k4, j4)

    r5 = reading.objects.none()
    t5 = reading.objects.all()
    w5 = random.sample(range(1, 50), 10)
    for d5 in range(91, 101, 1):
        ran5 = w5[d5-91]
        r5 = r5 | reading.objects.filter(id=t5[ran5].id)
        k5 = "q" + str(d5)
        j5 = t5[ran5].id
        data1.setdefault(k5, j5)

    topic.objects.create(text = data1)

    t = topic.objects.get(text = data1)

    return render(request, 'exam/addexam_computer.html', locals())


def check_topic(request):
    if 'username' in request.session:
        username = request.session['username']

    template = get_template('exam/check_topic.html')

    Topic = topic.objects.all()

    if request.method == 'POST':

        t = request.POST['t']

        paper = topic.objects.get(id=t)
        data = {}

        data = eval(paper.text)

        ta = talk.objects.all()
        tq = talk.objects.none()
        tdata = {}
        data2 = {}

        for d in range(1, 41, 1):
            que = "q" + str(d)
            g = int(data[que])
            tq = tq | talk.objects.filter(id=g)

        sa = short_conversation.objects.all()
        sq = short_conversation.objects.none()
        sdata = {}

        for d in range(41, 61, 1):
            que = "q" + str(d)
            g = int(data[que])
            sq = sq | short_conversation.objects.filter(id=g)

        na = noun.objects.all()
        nq = noun.objects.none()
        ndata = {}

        for d in range(61, 76, 1):
            que = "q" + str(d)
            g = int(data[que])
            nq = nq | noun.objects.filter(id=g)

        ga = grammar.objects.all()
        gq = grammar.objects.none()
        gdata = {}

        for d in range(76, 91, 1):
            que = "q" + str(d)
            g = int(data[que])
            gq = gq | grammar.objects.filter(id=g)

        ra = reading.objects.all()
        rq = reading.objects.none()
        rdata = {}

        for d in range(91, 101, 1):
            que = "q" + str(d)
            g = int(data[que])
            rq = rq | reading.objects.filter(id=g)

    html = template.render(context=locals(), request=request)
    return HttpResponse(html)
    return render(request, 'exam/check_topic.html', {'tdata': tdata}, {'sdata': sdata}, {'ndata': ndata},
                  {'gdata': gdata}, {'rdata2': rdata})


def member_show(request):
    if 'username' in request.session:
        username = request.session['username']

    exam = member.objects.all()
    z = UserProfile.objects.none()
    y = Examinees.objects.none()

    if request.method == 'POST':

        i = request.POST['id']
        k = member.objects.get(id=i)
        x = k.text.replace("'", "").lstrip('[').rstrip(']').split(',')
        for mem in x:
            z = z | UserProfile.objects.filter(Username=int(mem))
            y = y | Examinees.objects.filter(user__Username=int(mem)).order_by("user")

        User = zip(z,y)

        context = {
            'exam': exam,
            "User": User,
        }
    return render(request, 'exam/check_member.html', locals())


# def export_excel(request):
#     response = HttpResponse(content_type='application/ms-excel')
#     response['Content-Disposition'] = 'attachment; filename="users.xls"'
#
#     wb = xlwt.Workbook(encoding='utf-8')
#     ws = wb.add_sheet('exam_paper')
#
#     # Sheet header, first row
#     row_num = 0
#
#     font_style = xlwt.XFStyle()
#     font_style.font.bold = True
#
#     columns = ['question', 'a', 'b', 'c', 'd', 'answer', ]
#
#     for col_num in range(len(columns)):
#         ws.write(row_num, col_num, columns[col_num], font_style)
#
#     # Sheet body, remaining rows
#     font_style = xlwt.XFStyle()
#
#     rows = talk.objects.order_by('?')[:40].values_list('question', 'a', 'b', 'c', 'd', 'answer')
#     for row in rows:
#         row_num += 1
#         for col_num in range(len(row)):
#             ws.write(row_num, col_num, row[col_num], font_style)
#
#     wb.save(response)
#     return response

def addquestion_talk(request):
    if 'username' in request.session:
        username = request.session['username']

    q=models.talk.objects.all()
    w=request.POST
    if request.method=="POST":
        addquestion_talk=forms.talkform(request.POST)
        if addquestion_talk.is_valid():
             message="以貯存"
             addquestion_talk.save()
             return HttpResponseRedirect('/review_listing_talk/')
        else:
             message="需要填滿全部的空格"
    else:
        addquestion_talk=forms.talkform()
    message="需要填滿全部的空."
    template=get_template('question/addquestion_talk.html')
    html = template.render(context=locals(), request=request)
    return HttpResponse(html)

class  delete_talk(DeleteView):
    model=models.talk
    success_url = reverse_lazy('listing_talk')

def edit_talk(request,qs):
    if 'username' in request.session:
        username = request.session['username']

    posts=get_object_or_404(models.talk,id=qs)
    if request.method=='POST':
        edit_form_talk=forms.talkform(request.POST,instance=posts)
        if   edit_form_talk.is_valid():
           posts=edit_form_talk.save(commit=False)
           posts.save()
           return redirect('listing_talk')

        else:
           edit_form_talk=forms.talkform(instance=posts)
    else:
        edit_form_talk=forms.talkform(instance=posts)

    return render(request, 'question/update_talk.html',{'edit_form_talk': edit_form_talk, 'username':username})


def search_talk(request):
    if 'username' in request.session:
        username = request.session['username']

    query=request.GET.get('query')
    answer = request.GET.get('dropdown')
    if answer == "question":
        results = models.talk.objects.filter(Q(question__icontains=query))
    elif answer == "a":
        results = models.talk.objects.filter(Q(a__icontains=query))
    elif answer == "b":
        results = models.talk.objects.filter(Q(b__icontains=query))
    elif answer == "c":
        results = models.talk.objects.filter(Q(c__icontains=query))
    elif answer == "d":
        results = models.talk.objects.filter(Q(d__icontains=query))
    elif answer == "answer":
        results = models.talk.objects.filter(Q(answer__icontains=query))
    else:
        results=models.talk .objects.filter()
    context = {
    "posts": results,
    'query':query,
    }
    return render(request,'question/listing_talk.html',context)

def listing_talk(request):
    if 'username' in request.session:
        username = request.session['username']

    template = get_template('question/listing_talk.html')
    try:
        urid=request.GET['q_id']
    except:
        urid = None
    posts=models.talk.objects.filter(enabled=True).order_by('id')
    html = template.render(context=locals(), request=request)
    return HttpResponse(html)

def addquestion_short_conversation(request):
    if 'username' in request.session:
        username = request.session['username']

    q = models.short_conversation.objects.all()
    w = request.POST
    if request.method == "POST":
        addquestion_short_conversation = forms.short_conversationform(request.POST)
        if addquestion_short_conversation.is_valid():
            message = "以貯存"
            addquestion_short_conversation.save()
            return HttpResponseRedirect('/review_listing_short_conversation/')
        else:
            message = "需要填滿全部的空格"
    else:
        addquestion_short_conversation = forms.short_conversationform
    message = "需要填滿全部的空."
    template = get_template('question/addquestion_short_conversation.html')
    html = template.render(context=locals(), request=request)
    return HttpResponse(html)

class delete_short_conversation(DeleteView):
    model = models.short_conversation
    success_url = reverse_lazy('listing_short_conversation')

def edit_short_conversation(request, qs):
    if 'username' in request.session:
        username = request.session['username']

    posts = get_object_or_404(models.short_conversation, id=qs)
    if request.method == 'POST':
        edit_form_short_conversation = forms.short_conversationform(request.POST, instance=posts)
        if edit_form_short_conversation.is_valid():
            posts = edit_form_short_conversation.save(commit=False)
            posts.save()
            return redirect('listing_short_conversation')
        else:
            edit_form_short_conversation = forms.short_conversationform(instance=posts)
    else:
        edit_form_short_conversation=short_conversationform(instance=posts)
    return render(request, 'question/update_short_conversation.html', {'edit_form_short_conversation': edit_form_short_conversation, 'username':username})

def search_short_conversation(request):
    if 'username' in request.session:
        username = request.session['username']

    query = request.GET.get('query')
    answer = request.GET.get('dropdown')
    if answer == "question":
        results = models.short_conversation.objects.filter(Q(question__icontains=query))
    elif answer == "A":
        results = models.short_conversation.objects.filter(Q(a__icontains=query))
    elif answer == "B":
        results = models.short_conversation.objects.filter(Q(b__icontains=query))
    elif answer == "C":
        results = models.short_conversation.objects.filter(Q(c__icontains=query))
    elif answer == "D":
        results = models.short_conversation.objects.filter(Q(d__icontains=query))
    elif answer == "answer":
        results = models.short_conversation.objects.filter(Q(answer__icontains=query))
    else:
        results=models.short_conversation.objects.filter()
    context = {
        "posts": results,
        'query': query,
    }
    return render(request, 'question/listing_short_conversation.html', context)

def listing_short_conversation(request):
    if 'username' in request.session:
        username = request.session['username']

    template = get_template('question/listing_short_conversation.html')
    try:
        urid = request.GET['q_id']
    except:
        urid = None
    posts = models.short_conversation.objects.filter(enabled=True).order_by('id')
    html = template.render(context=locals(), request=request)
    return HttpResponse(html)

def addquestion_noun(request):
    if 'username' in request.session:
        username = request.session['username']

    q=models.noun.objects.all()
    w=request.POST
    if request.method=="POST":
        addquestion_noun=forms.nounform(request.POST)
        if addquestion_noun.is_valid():
             message="以貯存"
             addquestion_noun.save()
             return HttpResponseRedirect('/review_listing_noun/')
        else:
             message="需要填滿全部的空格"
    else:
             addquestion_noun=forms.nounform
    message="需要填滿全部的空."
    template=get_template('question/addquestion_noun.html')
    html = template.render(context=locals(), request=request)
    return HttpResponse(html)

class  delete_noun(DeleteView):
    model=models.noun
    success_url = reverse_lazy('listing_noun')

def edit_noun(request,qs):
    if 'username' in request.session:
        username = request.session['username']

    posts=get_object_or_404(models.noun,id=qs)
    if request.method=='POST':
        edit_form_noun=forms.nounform(request.POST,instance=posts)
        if   edit_form_noun.is_valid():
           posts=edit_form_noun.save(commit=False)
           posts.save()
           return  redirect('listing_noun')
        else:
           edit_form_noun=forms.nounform(instance=posts)
    else:
        edit_form_noun = nounform(instance=posts)
    return render(request, 'question/update_noun.html', {'edit_form_noun': edit_form_noun, 'username':username})


def search_noun(request):
    if 'username' in request.session:
        username = request.session['username']

    query = request.GET.get('query')
    answer=request.GET.get('dropdown')
    if answer=="question" :
        results = models.noun.objects.filter(Q(question__icontains=query))
    elif answer == "A":
        results = models.noun.objects.filter(Q(a__icontains=query))
    elif answer == "B":
        results = models.noun.objects.filter(Q(b__icontains=query))
    elif answer == "C":
        results = models.noun.objects.filter(Q(c__icontains=query))
    elif answer == "D":
        results = models.noun.objects.filter(Q(d__icontains=query))
    elif answer == "answer":
        results = models.noun.objects.filter(Q(answer__icontains=query))
    context = {
        "posts": results,
        'query': query,
    }
    return render(request, 'question/listing_noun.html', context)

def listing_noun(request):
    if 'username' in request.session:
        username = request.session['username']

    template = get_template('question/listing_noun.html')
    try:
        urid=request.GET['q_id']
    except:
        urid = None
    posts=models.noun.objects.filter(enabled=True).order_by('id')
    html = template.render(context=locals(), request=request)
    return HttpResponse(html)

def addquestion_grammar(request):
    if 'username' in request.session:
        username = request.session['username']

    q=models.grammar.objects.all()
    w=request.POST
    if request.method=="POST":
        addquestion_grammar=forms.grammarform(request.POST)
        if addquestion_grammar.is_valid():
             message="以貯存"
             addquestion_grammar.save()
             return HttpResponseRedirect('/review_listing_grammar/')
        else:
             message="需要填滿全部的空格"
    else:
             addquestion_grammar=forms.grammarform
    message="需要填滿全部的空."
    template=get_template('question/addquestion_grammar.html')
    html = template.render(context=locals(), request=request)
    return HttpResponse(html)


class  delete_grammar(DeleteView):
    model=models.grammar
    success_url = reverse_lazy('listing_grammar')


def edit_grammar(request,qs):
    if 'username' in request.session:
        username = request.session['username']

    posts=get_object_or_404(models.grammar,id=qs)
    if request.method=='POST':
        edit_form_grammar=grammarform(request.POST,instance=posts)
        if edit_form_grammar.is_valid():
           posts=edit_form_grammar.save(commit=False)
           posts.save()
           return redirect('listing_grammar')
        else:
           edit_form_grammar=grammarform(instance=posts)
    else:
        edit_form_grammar=grammarform(instance=posts)
    return render(request, 'question/update_grammar.html', {'edit_form_grammar': edit_form_grammar, 'username':username})


def search_grammar(request):
    if 'username' in request.session:
        username = request.session['username']

    query=request.GET.get('query')
    answer = request.GET.get('dropdown')
    if answer == "question":
        results = models.grammar.objects.filter(Q(question__icontains=query))
    elif answer == "A":
        results = models.grammar.objects.filter(Q(a__icontains=query))
    elif answer == "B":
        results = models.grammar.objects.filter(Q(b__icontains=query))
    elif answer == "C":
        results = models.grammar.objects.filter(Q(c__icontains=query))
    elif answer == "D":
        results = models.grammar.objects.filter(Q(d__icontains=query))
    elif answer == "answer":
        results = models.grammar.objects.filter(Q(answer__icontains=query))
    else:
        results=models.grammar.objects.filter()
    context = {
    "posts": results,
    'query':query,
    }
    return render(request,'question/listing_grammar.html',context)


def listing_grammar(request):
    if 'username' in request.session:
        username = request.session['username']

    template = get_template('question/listing_grammar.html')
    try:
        urid=request.GET['q_id']
    except:
        urid = None
    posts=models.grammar.objects.filter(enabled=True).order_by('id')
    html = template.render(context=locals(), request=request)
    return HttpResponse(html)


def addquestion_reading(request):
    if 'username' in request.session:
        username = request.session['username']

    q=models.reading.objects.all()
    w=request.POST
    if request.method=="POST":
        addquestion_reading=forms.readingform(request.POST)
        if addquestion_reading.is_valid():
             message="以貯存"
             addquestion_reading.save()
             return HttpResponseRedirect('/review_listing_reading/')
        else:
             message="需要填滿全部的空格"
    else:
             addquestion_reading=forms.readingform
    message="需要填滿全部的空."
    template=get_template('question/addquestion_reading.html')
    html = template.render(context=locals(), request=request)
    return HttpResponse(html)


class delete_reading(DeleteView):
    model=models.reading
    success_url = reverse_lazy('listing_reading')


def edit_reading(request,qs):
    if 'username' in request.session:
        username = request.session['username']

    posts=get_object_or_404(models.reading,id=qs)
    if request.method=='POST':
        edit_form_reading=forms.readingform(request.POST,instance=posts)
        if   edit_form_reading.is_valid():
           posts=edit_form_reading.save(commit=False)
           posts.save()
           return  redirect('listing_reading')
        else:
           edit_form_reading=forms.readingform(instance=posts)
    else:
        edit_form_reading=forms.readingform(instance=posts)
    return render(request, 'question/update_reading.html', {'edit_form_reading': edit_form_reading, 'username':username})


def search_reading(request):
    if 'username' in request.session:
        username = request.session['username']

    query=request.GET.get('query')
    answer = request.GET.get('dropdown')
    if answer == "question":
        results = models.reading.objects.filter(Q(question__icontains=query))
    elif answer == "A":
        results = models.reading.objects.filter(Q(a__icontains=query))
    elif answer == "B":
        results = models.reading.objects.filter(Q(b__icontains=query))
    elif answer == "C":
        results = models.reading.objects.filter(Q(c__icontains=query))
    elif answer == "D":
        results = models.reading.objects.filter(Q(d__icontains=query))
    elif answer == "answer":
        results = models.reading.objects.filter(Q(answer__icontains=query))
    elif query and answer == 20:
        results=models.reading.objects.filter(Q(a_icontains=query))
    return render(request,'question/listing_reading.html')

def listing_reading(request):
    if 'username' in request.session:
        username = request.session['username']

    template = get_template('question/listing_reading.html')
    try:
        urid=request.GET['q_id']
    except:
        urid = None
    posts=models.reading.objects.filter(enabled=True).order_by('id')
    html = template.render(context=locals(), request=request)
    return HttpResponse(html)

#題庫操作員

def listing_talk2(request):
    if 'username' in request.session:
        username = request.session['username']

    template = get_template('employee/listing_talk_e.html')
    try:
        urid=request.GET['q_id']
    except:
        urid = None
    posts=models.talk.objects.filter(enabled=True).order_by('id')
    html = template.render(context=locals(), request=request)
    return HttpResponse(html)

def addquestion_talk2(request):
    if 'username' in request.session:
        username = request.session['username']

    q=models.talk.objects.all()
    w=request.POST
    if request.method=="POST":
        addquestion_talk2=forms.talkform(request.POST)
        if addquestion_talk2.is_valid():
             addquestion_talk2.save()
             return HttpResponseRedirect('/listing_talk_e/')
        else:
             message="需要填滿全部的空格"
    else:
             addquestion_talk2=forms.talkform()
    message="需要填滿全部的空格"
    template=get_template('employee/addquestion_talk_e.html')
    html = template.render(context=locals(), request=request)
    return HttpResponse(html)

def listing_short_conversation2(request):
    if 'username' in request.session:
        username = request.session['username']

    template = get_template('employee/listing_short_conversation_e.html')
    try:
        urid=request.GET['q_id']
    except:
        urid = None
    posts=models.short_conversation.objects.filter(enabled=True).order_by('id')
    html = template.render(context=locals(), request=request)
    return HttpResponse(html)

def addquestion_short_conversation2(request):
    if 'username' in request.session:
        username = request.session['username']

    q = models.short_conversation.objects.all()
    w = request.POST
    if request.method == "POST":
        addquestion_short_conversation2 = forms.short_conversationform(request.POST)
        if addquestion_short_conversation2.is_valid():
            message = "已儲存"
            addquestion_short_conversation2.save()
            return HttpResponseRedirect('/listing_short_conversation_e/')
        else:
            message = "需要填滿全部的空格"
    else:
        addquestion_short_conversation2 = forms.short_conversationform
    message = "需要填滿全部的空格"
    template = get_template('employee/addquestion_short_conversation_e.html')
    html = template.render(context=locals(), request=request)
    return HttpResponse(html)

def listing_grammar2(request):
    if 'username' in request.session:
        username = request.session['username']

    template = get_template('employee/listing_grammar_e.html')
    try:
        urid=request.GET['q_id']
    except:
        urid = None
    posts=models.grammar.objects.filter(enabled=True).order_by('id')
    html = template.render(context=locals(), request=request)
    return HttpResponse(html)

def addquestion_grammar2(request):
    if 'username' in request.session:
        username = request.session['username']

    q=models.grammar.objects.all()
    w=request.POST
    if request.method=="POST":
        addquestion_grammar2=forms.grammarform(request.POST)
        if addquestion_grammar2.is_valid():
             addquestion_grammar2.save()
             return HttpResponseRedirect('/listing_grammar_e/')
        else:
             message="需要填滿全部的空格"
    else:
             addquestion_grammar2=forms.grammarform
    message="需要填滿全部的空格"
    template=get_template('employee/addquestion_grammar_e.html')
    html = template.render(context=locals(), request=request)
    return HttpResponse(html)

def listing_noun2(request):
    if 'username' in request.session:
        username = request.session['username']

    template = get_template('employee/listing_noun_e.html')
    try:
        urid=request.GET['q_id']
    except:
        urid = None
    posts=models.noun.objects.filter(enabled=True).order_by('id')
    html = template.render(context=locals(), request=request)
    return HttpResponse(html)

def addquestion_noun2(request):
    if 'username' in request.session:
        username = request.session['username']

    q=models.noun.objects.all()
    w=request.POST
    if request.method=="POST":
        addquestion_noun2=forms.nounform(request.POST)
        if addquestion_noun2.is_valid():
             message="已儲存"
             addquestion_noun2.save()
             return HttpResponseRedirect('/listing_noun_e/')
        else:
             message="需要填滿全部的空格"
    else:
             addquestion_noun2=forms.nounform
    message="需要填滿全部的空格"
    template=get_template('employee/addquestion_noun_e.html')
    html = template.render(context=locals(), request=request)
    return HttpResponse(html)

def listing_reading2(request):
    if 'username' in request.session:
        username = request.session['username']

    template = get_template('employee/listing_reading_e.html')
    try:
        urid=request.GET['q_id']
    except:
        urid = None
    posts=models.reading.objects.filter(enabled=True).order_by('id')
    html = template.render(context=locals(), request=request)
    return HttpResponse(html)

def addquestion_reading2(request):
    if 'username' in request.session:
        username = request.session['username']

    q=models.reading.objects.all()
    w=request.POST
    if request.method=="POST":
        addquestion_noun2=forms.nounform(request.POST)
        if addquestion_noun2.is_valid():
             message="已儲存"
             addquestion_noun2.save()
             return HttpResponseRedirect('/listing_reading_e/')
        else:
             message="需要填滿全部的空格"
    else:
             addquestion_noun2=forms.nounform
    message="需要填滿全部的空格"
    template=get_template('employee/addquestion_reading_e.html')
    html = template.render(context=locals(), request=request)
    return HttpResponse(html)

#審核
def review_listing_reading(request):
    if 'username' in request.session:
        username = request.session['username']

    template = get_template('question/review/review_listing_reading.html')
    try:
        urid=request.GET['q_id']
    except:
        urid = None
    posts=models.reading.objects.filter(enabled=False).order_by('id')
    html = template.render(context=locals(), request=request)
    return HttpResponse(html)

def review_reading(request,qs):
    if 'username' in request.session:
        username = request.session['username']

    posts=get_object_or_404(models.reading,id=qs)
    if request.method=='POST':
        review_form_reading=forms.check_readingform(request.POST,instance=posts)
        if   review_form_reading.is_valid():
           posts=review_form_reading.save(commit=False)
           posts.save()
           return  redirect('review_listing_reading')
        else:
            review_form_reading= forms.check_readingform(instance=posts)
    else:
        review_form_reading = forms.check_readingform
        template = get_template('question/review/review_reading.html')
        html = template.render(context=locals(), request=request)
        return HttpResponse(html)

class review_delete_reading(DeleteView):
    model=models.reading
    success_url = reverse_lazy('review_listing_reading')

def review_listing_talk(request):
    if 'username' in request.session:
        username = request.session['username']

    template = get_template('question/review/review_listing_talk.html')
    try:
        urid=request.GET['q_id']
    except:
        urid = None
    posts=models.talk.objects.filter(enabled=False).order_by('id')
    html = template.render(context=locals(), request=request)
    return HttpResponse(html)

def review_talk(request,qs):
    if 'username' in request.session:
        username = request.session['username']

    posts=get_object_or_404(models.talk,id=qs)
    if request.method=='POST':
        review_form_talk=forms.check_talkform(request.POST,instance=posts)
        if   review_form_talk.is_valid():
           posts=review_form_talk.save(commit=False)
           posts.save()
           return  redirect('review_listing_talk')
        else:
            review_form_talk= forms.check_talkform(instance=posts)
    else:
        review_form_talk = forms.check_talkform
        template = get_template('question/review/review_talk.html')
        html = template.render(context=locals(), request=request)
        return HttpResponse(html)

class review_delete_talk(DeleteView):
    model=models.talk
    success_url = reverse_lazy('review_listing_talk')

def review_listing_noun(request):
    if 'username' in request.session:
        username = request.session['username']
    template = get_template('question/review/review_listing_noun.html')
    try:
        urid=request.GET['q_id']
    except:
        urid = None
    posts=models.noun.objects.filter(enabled=False).order_by('id')
    html = template.render(context=locals(), request=request)
    return HttpResponse(html)

def review_noun(request,qs):
    if 'username' in request.session:
        username = request.session['username']
    posts=get_object_or_404(models.noun,id=qs)

    if request.method=='POST':
        review_form_noun=forms.check_nounform(request.POST,instance=posts)
        if   review_form_noun.is_valid():
           posts=review_form_noun.save(commit=False)
           posts.save()

           return  redirect('review_listing_noun')
        else:
            message = "確定審核完畢"
            review_form_noun = forms.check_nounform(instance=posts)
    else:
        review_form_noun = forms.check_nounform
        template = get_template('question/review/review_noun.html')
        html = template.render(context=locals(), request=request)
        return HttpResponse(html)

class review_delete_noun(DeleteView):
    model=models.noun
    success_url = reverse_lazy('review_listing_noun')

def review_listing_grammar(request):
    if 'username' in request.session:
        username = request.session['username']

    template = get_template('question/review/review_listing_grammar.html')
    try:
        urid = request.GET['q_id']
    except:
        urid = None
    posts = models.grammar.objects.filter(enabled=False).order_by('id')
    html = template.render(context=locals(), request=request)
    return HttpResponse(html)

def review_grammar(request, qs):
    if 'username' in request.session:
        username = request.session['username']

    posts = get_object_or_404(models.grammar, id=qs)
    if request.method == 'POST':
        review_form_grammar = forms.check_grammarform(request.POST, instance=posts)
        if review_form_grammar.is_valid():
            posts = review_form_grammar.save(commit=False)
            posts.save()
            return redirect('review_listing_grammar')
        else:
            review_form_grammar = forms.check_grammarform(instance=posts)
    else:
        review_form_grammar = forms.check_grammarform
        template = get_template('question/review/review_grammar.html')
        html = template.render(context=locals(), request=request)
        return HttpResponse(html)

class review_delete_grammar(DeleteView):
    model=models.grammar
    success_url = reverse_lazy('review_listing_grammar')

def review_listing_short_conversation(request):
    if 'username' in request.session:
        username = request.session['username']

    template = get_template('question/review/review_listing_short_conversation.html')
    try:
        urid=request.GET['q_id']
    except:
        urid = None
    posts=models.short_conversation.objects.filter(enabled=False).order_by('id')
    html = template.render(context=locals(), request=request)
    return HttpResponse(html)

def review_short_conversation(request,qs):
    if 'username' in request.session:
        username = request.session['username']

    posts=get_object_or_404(models.short_conversation,id=qs)
    if request.method=='POST':
        review_form_short_conversation=forms.check_short_conversationform(request.POST,instance=posts)
        if   review_form_short_conversation.is_valid():
           posts=review_form_short_conversation.save(commit=False)
           posts.save()
           return  redirect('review_listing_short_conversation')
        else:
            review_form_short_conversation = forms.check_short_conversationform(instance=posts)
    else:
        review_form_short_conversation = forms.check_short_conversationform
        template = get_template('question/review/review_short_conversation.html')
        html = template.render(context=locals(), request=request)
        return HttpResponse(html)

class review_delete_short_conversation(DeleteView):
    model=models.short_conversation
    success_url = reverse_lazy('review_listing_short_conversation')

def checkduplicate_talk(request):
    if 'username' in request.session:
        username = request.session['username']

    template = get_template('question/listing_talk.html')
    posts = models.talk.objects.order_by('question')
    html = template.render(context=locals(), request=request)
    for posts in models.talk.objects.all():
        if models.talk.objects.filter(question=posts.question).count() > 1 and models.talk.objects.filter(
                a=posts.a).count() > 1 and models.talk.objects.filter(
            b=posts.b).count() > 1 and models.talk.objects.filter(
            c=posts.c).count() > 1 and models.talk.objects.filter(
            d=posts.d).count() > 1 and models.talk.objects.filter(answer=posts.answer).count() > 1:
                             posts.delete()
    return HttpResponse(html)

def checkduplicate_short_conversation(request):
    if 'username' in request.session:
        username = request.session['username']

    template = get_template('question/listing_short_conversation.html')
    posts = models.short_conversation.objects.order_by('question')
    html = template.render(context=locals(), request=request)
    for posts in models.short_conversation.objects.all():
        if models.short_conversation.objects.filter(question=posts.question).count() > 1 and models.short_conversation.objects.filter(
                a=posts.a).count() > 1 and models.short_conversation.objects.filter(
            b=posts.b).count() > 1 and models.short_conversation.objects.filter(
            c=posts.c).count() > 1 and models.short_conversation.objects.filter(
            d=posts.d).count() > 1 and models.short_conversation.objects.filter(answer=posts.answer).count() > 1:
                             posts.delete()
    return HttpResponse(html)

def checkduplicate_noun(request):
    if 'username' in request.session:
        username = request.session['username']

    template = get_template('question/listing_noun.html')
    posts = models.noun.objects.order_by('question')
    html = template.render(context=locals(), request=request)
    for posts in models.noun.objects.all():
        if models.noun.objects.filter(question=posts.question).count() > 1:
            if models.noun.objects.filter(question=posts.question).count() > 1 and models.noun.objects.filter(
                    a=posts.a).count() > 1 and models.noun.objects.filter(
                    b=posts.b).count() > 1 and models.noun.objects.filter(
                    c=posts.c).count() > 1 and models.noun.objects.filter(
                    d=posts.d).count() > 1 and models.noun.objects.filter(answer=posts.answer).count() > 1:
                posts.delete()
    return HttpResponse(html)

def checkduplicate_grammar(request):
    if 'username' in request.session:
        username = request.session['username']

    template = get_template('question/listing_grammar.html')
    posts = models.grammar.objects.order_by('question')
    html = template.render(context=locals(), request=request)
    for posts in models.grammar.objects.all():
        if models.grammar.objects.filter(question=posts.question).count() > 1 and models.grammar.objects.filter(
                a=posts.a).count() > 1 and models.grammar.objects.filter(
            b=posts.b).count() > 1 and models.grammar.objects.filter(
            c=posts.c).count() > 1 and models.grammar.objects.filter(
            d=posts.d).count() > 1 and models.grammar.objects.filter(answer=posts.answer).count() > 1:
            posts.delete()
    return HttpResponse(html)

def checkduplicate_reading(request):
    if 'username' in request.session:
        username = request.session['username']

    template = get_template('question/listing_reading.html')
    posts = models.reading.objects.order_by('question')
    html = template.render(context=locals(), request=request)
    for posts in models.reading.objects.all():
        if models.reading.objects.filter(question=posts.question).count() > 1 and models.reading.objects.filter(
                a=posts.a).count() > 1 and models.reading.objects.filter(
            b=posts.b).count() > 1 and models.reading.objects.filter(
            c=posts.c).count() > 1 and models.reading.objects.filter(
            d=posts.d).count() > 1 and models.reading.objects.filter(answer=posts.answer).count() > 1:
            posts.delete()
    return HttpResponse(html)

def view_score(request):
    if 'username' in request.session:
        username = request.session['username']

    exams = Examinees.objects.all()
    scores = Score.objects.all()

    return render(request, 'view_score/view_score.html', locals())

def check_s(request):
    if 'username' in request.session:
        username = request.session['username']

    if request.method == "POST":
        id = request.POST['id']
        s = request.POST['ses']
        m = request.POST['mon']

    else:
        id = '0'
        s = '0'
        m = '0'

    ex = UserProfile.objects.filter(Q(Username__exact=id) | Q(FullName__exact=id))
    se = Examinees.objects.filter(user__Username=id)

    for i in ex:

        if m == '0':
            sc = Score.objects.filter(Ex__user__Username=i.Username).filter(Exam_Date__year=str(int(s) + 1911)).order_by('Exam_Date')
        else:
            sc = Score.objects.filter(Ex__user__Username=i.Username).filter(Exam_Date__year=str(int(s) + 1911)).\
                filter(Exam_Date__month=m).order_by('Exam_Date')

        w = 0.0
        c = 0
        b = 0
        avg = 0.0

        if sc.count() != 0:
            for a in sc:
                b = a.Score
                c = c + b
                w = w + 1

            avg = c / w
            avg = format(avg, "3.2f")
            avg = float(avg)
            if avg >= 80:
                lv = 'A'
            elif 80 > avg >= 75:
                lv = 'B'
            elif 75 > avg >= 70:
                lv = 'C'
            elif 70 > avg >= 65:
                lv = 'D'
            else:
                lv = 'F'
        else:
            lv = '無'
            avg = '無'

        return render(request, 'view_score/check_s.html', locals())


def comp_s(request):
    if 'username' in request.session:
        username = request.session['username']

    if request.method == "POST":
        d = request.POST['comp']
        s = request.POST['ses']
        m = request.POST['mon']

    else:
        d = 0
        s = 0
        m = 0

    comp_name = Company.objects.get(id=d)
    ex = Examinees.objects.filter(Company_id=d)

    per_avg = []
    all_avg = []
    data = []
    i = 0
    j = 0

    for i in ex:
        id = i
        per_avg = peolist(id)
        avg = count_avg(id, s, m)
        per_avg.append(avg)
        data.append(per_avg)
        all_avg.append(avg)

    peo = 0
    for people in ex:
        peo = peo + 1

    p_intest = peo
    scor = 0.0
    for i in all_avg:
        if i == '無':
            i = 0
            p_intest = p_intest - 1
        scor = scor + float(i)
    if p_intest <= 0:
        p_intest = 1
    comp_avg = scor / p_intest
    lv = com_lv(comp_avg)

    return render(request, 'view_score/comp_s.html', locals())


def clas_s(request):
    if request.method == "POST":
        d = request.POST['maj']
        g = request.POST['grade']
        s = request.POST['ses']
        m = request.POST['mon']

    else:
        d = 0
        s = 0
        m = 0
        g = 0

    depa_name = Department.objects.get(id=d)
    ex = Examinees.objects.filter(Q(Major=d) & Q(Class=g))

    per_avg = []
    all_avg = []
    data = []
    i = 0
    j = 0

    for i in ex:
        id = i
        per_avg = peolist(id)
        avg = count_avg(id, s, m)
        per_avg.append(avg)
        data.append(per_avg)
        all_avg.append(avg)

    peo = 0
    for people in ex:
        peo = peo + 1

    p_intest = peo
    scor = 0.0
    for i in all_avg:
        if i == '無':
            i = 0
            p_intest = p_intest - 1
        scor = scor + float(i)
    if p_intest <= 0:
        p_intest = 1
    comp_avg = scor / p_intest
    comp_avg = format(comp_avg, "3.2f")
    lv = com_lv(comp_avg)

    return render(request, 'view_score/clas_s.html', locals())

def check(request):
    if 'username' in request.session:
        username = request.session['username']

    if request.method == "POST":
        id = request.POST['id']
        d = request.POST['date']

    else:
        id = '0'
        d = '0'

    ex = UserProfile.objects.filter(Q(Username__exact=id) | Q(FullName__exact=id))
    se = Examinees.objects.filter(user__Username=id)
    for i in ex:
        sc = Score.objects.filter(Ex__user__Username=i.Username).filter(Exam_Date__contains=d)

    b = 0

    if sc.count() != 0:
        for a in sc:
            b = a.Score
        if b >= 80:
            lv = 'A'
        elif 80 > b >= 75:
            lv = 'B'
        elif 75 > b >= 70:
            lv = 'C'
        elif 70 > b >= 65:
            lv = 'D'
        else:
            lv = 'F'
    else:
        lv = '無'

    return render(request, 'view_score/check.html', locals())


def comp(request):
    if 'username' in request.session:
        username = request.session['username']

    if request.method == "POST":
        c = request.POST['comp']
        d = request.POST['date']

    else:
        c = 0
        d = 0

    comp_name = Company.objects.get(id=c)
    ex = Examinees.objects.filter(Company_id=c)
    sc = Score.objects.filter(Exam_Date__contains=d)

    per_avg = []
    all_avg = []
    data = []
    i = 0
    j = 0

    for i in ex:
        id = i
        per_avg = peolist2(id)
        avg = count_avg2(id, d)
        per_avg.append(d)
        per_avg.append(avg)
        data.append(per_avg)
        all_avg.append(avg)

    peo = 0
    for people in ex:
        peo = peo + 1

    p_intest = peo
    scor = 0.0
    for i in all_avg:
        if i == '無':
            i = 0
            p_intest = p_intest - 1
        scor = scor + float(i)
    if p_intest <= 0:
        p_intest = 1
    comp_avg = scor / p_intest
    comp_avg = format(comp_avg, "3.2f")
    lv = com_lv(comp_avg)

    return render(request, 'view_score/comp.html', locals())


def clas(request):
    if 'username' in request.session:
        username = request.session['username']

    if request.method == "POST":
        d = request.POST["dep"]
        c = request.POST["cla"]
        e = request.POST['date']

    else:
        d = "0"
        c = "0"
        e = "0"

    sc = Score.objects.filter(Exam_Date__contains=e)
    de = Department.objects.get(id=d)
    ex = Examinees.objects.filter(Major=d).filter(Class__contains=c)
    se = UserProfile.objects.filter(Username = ex)

    peo = ex.count()

    per_avg = []
    all_avg = []
    data = []
    i = 0
    j = 0

    for i in ex:
        id = i
        per_avg = peolist2(id)
        avg = count_avg2(id, e)
        per_avg.append(e)
        per_avg.append(avg)
        data.append(per_avg)
        all_avg.append(avg)

    peo = 0
    for people in ex:
        peo = peo + 1

    p_intest = peo
    scor = 0.0
    for i in all_avg:
        if i == '無':
            i = 0
            p_intest = p_intest - 1
        scor = scor + float(i)
    if p_intest <= 0:
        p_intest = 1
    comp_avg = scor / p_intest
    comp_avg = format(comp_avg, "3.2f")
    lv = com_lv(comp_avg)

    return render(request, 'view_score/clas.html', locals())


def count_avg(num=0, s=0, m=0):

    sc = Score.objects.filter(Ex__exact=num).filter(Exam_Date__year=int(s) + 1911). \
        filter(Exam_Date__month=m).order_by('Exam_Date')

    w = 0.0
    c = 0

    if sc.count() != 0:
        for a in sc:
            b = a.Score
            c = c + b
            w = w + 1

        avg = c / w
        avg = format(avg, "3.2f")
    else:
        avg = '無'

    return avg

def count_avg2(num=0, d=0):

    sc = Score.objects.filter(Ex__exact=num).filter(Exam_Date__contains=d).order_by('Exam_Date')

    w = 0.0
    c = 0

    if sc.count() != 0:
        for a in sc:
            b = a.Score
            c = c + b
            w = w + 1

        avg = c / w
        avg = format(avg, "3.2f")
    else:
        avg = '無'

    return avg


def peolist(num):
    ex = UserProfile.objects.filter(Username=num)

    for i in ex:
        p_list = [i.Username, i.FullName]

    return p_list

def peolist2(num):
    ex = UserProfile.objects.filter(Username=num)
    ez = Examinees.objects.filter(user__Username=num)
    for i in ex:
        p_list2 = [i.Username, i.FullName]
        for j in ez:
            p_list2 = [i.Username, i.FullName, j.Company, j.Comp_Num]
    return p_list2

def com_lv(comp_avg):
    comp_avg2 = float(comp_avg)
    if comp_avg2 >= 80:
        lv = 'A'
    elif 80 > comp_avg2 >= 75:
        lv = 'B'
    elif 75 > comp_avg2 >= 70:
        lv = 'C'
    elif 70 > comp_avg2 >= 65:
        lv = 'D'
    else:
        lv = 'F'

    return lv

def subjects(request):
    if 'username' in request.session:
        username = request.session['username']

    Post = post.objects.filter(enabled=True).order_by('-created')
    return render(request, 'subjects/subjects.html', locals())

def member_select(request):
    if 'username' in request.session:
        username = request.session['username']

    template = get_template('exam/member_select.html')

    User1 = UserProfile.objects.all()
    User2 = Examinees.objects.all().order_by("user")
    User = zip(User1, User2)
    context = {
        "User" : User,
    }


    html = template.render(context=locals(), request=request)
    return HttpResponse(html)

def search_member(request):
    if 'username' in request.session:
        username = request.session['username']

    template = get_template('exam/member_select.html')

    if request.method == "GET":
        searchTerm1 = request.GET.get('searchTerm')
        searchTerm2 = request.GET.get('dep')
        searchTerm3 = request.GET.get('comp')
    else:
        searchTerm1 = 0
        searchTerm2 = 0
        searchTerm3 = 0


    results1 = UserProfile.objects.all().filter(Username__icontains=searchTerm1)
    results2 = []

    for i in results1:
        results2.append(Examinees.objects.get(user__Username=i.Username))


    if searchTerm2 != "系別":
        results1 = results1.filter(EE__Major=searchTerm2)
        result2 = []

        for i in results1:
            results2.append(Examinees.objects.get(user__Username=i.Username))


    if searchTerm3 != "中隊":
        results1 = results1.filter(EE__Company=searchTerm3)
        results2 = []

        for i in results1:
            results2.append(Examinees.objects.get(user__Username=i.Username))


    results = zip(results1, results2)

    context = {
    "User" : results,
    'searchTerm' : searchTerm1,
    'dep' : searchTerm2,
    'comp' : searchTerm3,
    }

    return render(request, 'exam/member_select.html', context)

def get_member(request):
    if 'username' in request.session:
        username = request.session['username']

    form = examform()

    check_box_list = request.POST.getlist('c')
    member.objects.create(text=check_box_list)

    return render(request, 'exam/addexam.html', {'examform': form, 'username': username})


def test(request):
    if 'username' in request.session:
        username = request.session['username']

    data = {"-1": "0"}
    with open('data.json', 'w') as f:
        json.dump(data, f)

    List = map(str, range(1, 67))
    List2 = map(str, range(67, 100))
    List3 = map(str, range(1, 57, 5))
    List4 = map(str, range(61, 97, 5))

    ta = talk.objects.all()
    tq = talk.objects.none()
    tw = random.sample(range(1, talk.objects.count()), 40)
    for d in range(0, 40, 1):
        ran = tw[d]
        tq = tq | talk.objects.filter(id=ta[ran].id)

    sa = short_conversation.objects.all()
    sq = short_conversation.objects.none()
    sw = random.sample(range(1, short_conversation.objects.count()), 20)
    for d in range(0, 20, 1):
        ran = sw[d]
        sq = sq | short_conversation.objects.filter(id=sa[ran].id)

    na = noun.objects.all()
    nq = noun.objects.none()
    nw = random.sample(range(1, noun.objects.count()), 15)
    for d in range(0, 15, 1):
        ran = nw[d]
        nq = nq | noun.objects.filter(id=na[ran].id)

    ga = grammar.objects.all()
    gq = grammar.objects.none()
    gw = random.sample(range(1, grammar.objects.count()), 15)
    for d in range(0, 15, 1):
        ran = gw[d]
        gq = gq | grammar.objects.filter(id=ga[ran].id)

    ra = reading.objects.all()
    rq = reading.objects.none()
    rw = random.sample(range(1, reading.objects.count()), 10)
    for d in range(0, 10, 1):
        ran = rw[d]
        rq = rq | reading.objects.filter(id=ra[ran].id)

    return render_to_response('subjects/test.html', locals())
    return render(request, 'subjects/test.html', {'List': List}, {'List2': List2}, {'List3': List3}, {'List4': List4})


def contest(request):
    if 'username' in request.session:
        username = request.session['username']
    with open('data.json', 'r') as f:
        data = json.load(f)

    List = map(str, range(1, 67))
    List2 = map(str, range(67, 100))
    List3 = map(str, range(1, 57, 5))
    List4 = map(str, range(61, 97, 5))

    ta = talk.objects.all()
    tq = talk.objects.none()
    tdata = {}
    data2 = {}
    anslist = {}
    checklist = {}
    for d in range(1, 41, 1):
        que = "q" + str(d)
        g = int(data[que])
        tq = tq | talk.objects.filter(id=g)
        tdata.setdefault(g, data["a" + str(d)])
        data2.setdefault(g, data["a" + str(d)])
        anslist.setdefault(d, data["a" + str(d)])
        checklist.setdefault(d, g)

    sa = short_conversation.objects.all()
    sq = short_conversation.objects.none()
    sdata = {}

    for d in range(41, 61, 1):
        que = "q" + str(d)
        g = int(data[que])
        sq = sq | short_conversation.objects.filter(id=g)
        sdata.setdefault(g, data["a" + str(d)])
        data2.setdefault(g, data["a" + str(d)])
        anslist.setdefault(d, data["a" + str(d)])
        checklist.setdefault(d, g)

    na = noun.objects.all()
    nq = noun.objects.none()
    ndata = {}

    for d in range(61, 76, 1):
        que = "q" + str(d)
        g = int(data[que])
        nq = nq | noun.objects.filter(id=g)
        ndata.setdefault(g, data["a" + str(d)])
        data2.setdefault(g, data["a" + str(d)])
        anslist.setdefault(d, data["a" + str(d)])
        checklist.setdefault(d, g)

    ga = grammar.objects.all()
    gq = grammar.objects.none()
    gdata = {}

    for d in range(76, 91, 1):
        que = "q" + str(d)
        g = int(data[que])
        gq = gq | grammar.objects.filter(id=g)
        gdata.setdefault(g, data["a" + str(d)])
        data2.setdefault(g, data["a" + str(d)])
        anslist.setdefault(d, data["a" + str(d)])
        checklist.setdefault(d, g)

    ra = reading.objects.all()
    rq = reading.objects.none()
    rdata = {}

    for d in range(91, 101, 1):
        que = "q" + str(d)
        g = int(data[que])
        rq = rq | reading.objects.filter(id=g)
        rdata.setdefault(g, data["a" + str(d)])
        data2.setdefault(g, data["a" + str(d)])
        anslist.setdefault(d, data["a" + str(d)])
        checklist.setdefault(d, g)
    with open('data2.json', 'w') as f:
        json.dump(data2, f)

    return render_to_response('subjects/contest.html', locals())
    return render(request, 'subjects/contest.html', {'List': List}, {'List2': List2}, {'List3': List3},
                  {'List4': List4}, {'data2': data2}, {'tdata': tdata}, {'sdata': sdata}, {'ndata': ndata},
                  {'gdata': gdata}, {'rdata2': rdata}, {'anslist': anslist}, {'checklist': checklist})


def realtest(request):
    if 'username' in request.session:
        username = request.session['username']
        NOWUser = UserProfile.objects.get(FullName=username)
    b = 0
    memtext = []
    j = exam.objects.none()

    List = map(str, range(1, 67))
    List2 = map(str, range(67, 100))
    List3 = map(str, range(1, 57, 5))
    List4 = map(str, range(61, 97, 5))

    dt = datetime.now(timezone.utc)
    test = exam.objects.filter(ddate__gte=dt)
    if test.exists():
        for e in test:
            g = int(e.member_id)
            h = member.objects.get(id=g)
            memtext = h.text
            if NOWUser.Username in memtext:
                b += 1
                j = e
                break
            else:
                b += 0
    else:
        return HttpResponseRedirect("/notest/")

    if b > 0:
        if (j.ddate - dt).seconds <= 300:

            data = {}
            paper = topic.objects.get(id=j.topic_id)

            data = eval(paper.text)

            ta = talk.objects.all()
            tq = talk.objects.none()
            tdata = {}
            data2 = {}

            for d in range(1, 41, 1):
                que = "q" + str(d)
                g = int(data[que])
                tq = tq | talk.objects.filter(id=g)

            sa = short_conversation.objects.all()
            sq = short_conversation.objects.none()
            sdata = {}

            for d in range(41, 61, 1):
                que = "q" + str(d)
                g = int(data[que])
                sq = sq | short_conversation.objects.filter(id=g)

            na = noun.objects.all()
            nq = noun.objects.none()
            ndata = {}

            for d in range(61, 76, 1):
                que = "q" + str(d)
                g = int(data[que])
                nq = nq | noun.objects.filter(id=g)

            ga = grammar.objects.all()
            gq = grammar.objects.none()
            gdata = {}

            for d in range(76, 91, 1):
                que = "q" + str(d)
                g = int(data[que])
                gq = gq | grammar.objects.filter(id=g)

            ra = reading.objects.all()
            rq = reading.objects.none()
            rdata = {}

            for d in range(91, 101, 1):
                que = "q" + str(d)
                g = int(data[que])
                rq = rq | reading.objects.filter(id=g)

            with open('data2.json', 'w') as f:
                json.dump(data2, f)
        else:
                return HttpResponseRedirect("/yettest/")
    else:
            return HttpResponseRedirect("/notest/")

    return render_to_response('subjects/realtest.html', locals())
    return render(request, 'subjects/realtest.html', {'List': List}, {'List2': List2}, {'List3': List3},
                  {'List4': List4}, {'data2': data2}, {'tdata': tdata}, {'sdata': sdata}, {'ndata': ndata},
                  {'gdata': gdata}, {'rdata2': rdata}, {'anslist': anslist}, {'checklist': checklist})


def notest(request):
    if 'username' in request.session:
        username = request.session['username']

    return render(request, 'subjects/notest.html', locals())



def yettest(request):
    if 'username' in request.session:
        username = request.session['username']

    return render(request, 'subjects/yettest.html', locals())



def next(request):
    if 'username' in request.session:
        username = request.session['username']

    data = {}

    for d in range(1, 41, 1):
        t = "q" + str(d)
        j = request.GET[t]
        data.setdefault(t, j)
        try:
            data.setdefault("a" + str(d), request.GET["t" + j])
        except BaseException:
            data.setdefault("a" + str(d), "")
    for d in range(41, 61, 1):
        t = "q" + str(d)
        j = request.GET[t]
        data.setdefault(t, j)
        try:
            data.setdefault("a" + str(d), request.GET["s" + j])
        except BaseException:
            data.setdefault("a" + str(d), "")
    for d in range(61, 76, 1):
        t = "q" + str(d)
        j = request.GET[t]
        data.setdefault(t, j)
        try:
            data.setdefault("a" + str(d), request.GET["n" + j])
        except BaseException:
            data.setdefault("a" + str(d), "")
    for d in range(76, 91, 1):
        t = "q" + str(d)
        j = request.GET[t]
        data.setdefault(t, j)
        try:
            data.setdefault("a" + str(d), request.GET["g" + j])
        except BaseException:
            data.setdefault("a" + str(d), "")
    for d in range(91, 101, 1):
        t = "q" + str(d)
        j = request.GET[t]
        data.setdefault(t, j)
        try:
            data.setdefault("a" + str(d), request.GET["r" + j])
        except BaseException:
            data.setdefault("a" + str(d), "")
    with open('data.json', 'w') as f:
        json.dump(data, f)

    return render_to_response('subjects/next.html', locals())

def Continue(request):
    if 'username' in request.session:
        username = request.session['username']

    with open('data.json', 'r') as f:
        data = json.load(f)
    if '-1' in data:
        return HttpResponseRedirect("/test/")

    return render_to_response('subjects/Continue.html', locals())


def score(request):
    if 'username' in request.session:
        username = request.session['username']


    b = 0
    for d in range(1, 41, 1):
        qid = request.GET["q" + str(d)]
        q = talk.objects.filter(id=int(qid))
        x = q[0]
        try:
            if request.GET["t"+ qid] == x.answer:
                b += 1
        except BaseException:
            b += 0
    for d in range(41, 61, 1):
        qid = request.GET["q" + str(d)]
        q = short_conversation.objects.filter(id=int(qid))
        x = q[0]
        try:
            if request.GET["s"+qid] == x.answer:
                b += 1
        except BaseException:
            b += 0
    for d in range(61, 76, 1):
        qid = request.GET["q" + str(d)]
        q = noun.objects.filter(id=int(qid))
        x = q[0]
        try:
            if request.GET["n"+qid] == x.answer:
                b += 1
        except BaseException:
            b += 0
    for d in range(76, 91, 1):
        qid = request.GET["q" + str(d)]
        q = grammar.objects.filter(id=int(qid))
        x = q[0]
        try:
            if request.GET["g"+qid] == x.answer:
                b += 1
        except BaseException:
            b += 0
    for d in range(91, 101, 1):
        qid = request.GET["q" + str(d)]
        q = reading.objects.filter(id=int(qid))
        x = q[0]
        try:
            if request.GET["r"+qid] == x.answer:
                b += 1
        except BaseException:
            b += 0
    data = {"-1": "0"}
    with open('data.json', 'w') as f:
        json.dump(data, f)

    d = {'1':b}

    return render_to_response('subjects/score.html', locals())
    return render(request, 'subjects/score.html',{'d',d})

def score2(request):
    if 'username' in request.session:
        username = request.session['username']
        NOWUser = UserProfile.objects.get(FullName=username)
        NOWUser2 = Examinees.objects.get(user__Username=NOWUser.Username)

    b = 0
    t = []
    for d in range(1, 41, 1):
        qid = request.GET["q" + str(d)]
        q = talk.objects.filter(id=int(qid))
        x = q[0]
        try:
            if request.GET["t"+ qid] == x.answer:
                b += 1
            else:
                t.append(qid)
        except BaseException:
            b += 0
            t.append(qid)
    for d in range(41, 61, 1):
        qid = request.GET["q" + str(d)]
        q = short_conversation.objects.filter(id=int(qid))
        x = q[0]
        try:
            if request.GET["s"+qid] == x.answer:
                b += 1
            else:
                t.append(qid)
        except BaseException:
            b += 0
            t.append(qid)
    for d in range(61, 76, 1):
        qid = request.GET["q" + str(d)]
        q = noun.objects.filter(id=int(qid))
        x = q[0]
        try:
            if request.GET["n"+qid] == x.answer:
                b += 1
            else:
                t.append(qid)
        except BaseException:
            b += 0
            t.append(qid)
    for d in range(76, 91, 1):
        qid = request.GET["q" + str(d)]
        q = grammar.objects.filter(id=int(qid))
        x = q[0]
        try:
            if request.GET["g"+qid] == x.answer:
                b += 1
            else:
                t.append(qid)
        except BaseException:
            b += 0
            t.append(qid)
    for d in range(91, 101, 1):
        qid = request.GET["q" + str(d)]
        q = reading.objects.filter(id=int(qid))
        x = q[0]
        try:
            if request.GET["r"+qid] == x.answer:
                b += 1
            else:
                t.append(qid)
        except BaseException:
            b += 0
            t.append(qid)
    data = {"-1": "0"}
    with open('data.json', 'w') as f:
        json.dump(data, f)

    e = 100 -b
    d = {'1':b}

    Score.objects.create(Error_Num = t, Score = b , Ex = NOWUser2)

    return render_to_response('subjects/score2.html', locals())
    return render(request, 'subjects/score2.html',{'d',d})


def listeningpractice(request):
    if 'username' in request.session:
        username = request.session['username']
    return render(request, 'subjects/listeningpractice.html', locals())

def talkpractice(request):
    if 'username' in request.session:
        username = request.session['username']

    total = [0]
    correct = [0]
    wrong = [0]
    cr = [0]

    t = talk.objects.all()
    w = random.sample(range(1, talk.objects.count()), 1)
    ran = w[0]
    q = talk.objects.filter(id=t[ran].id)

    return render_to_response('subjects/talkpractice.html', locals())
    return render(request, 'subjects/talkpractice.html', {'total': total}, {'correct': correct}, {'wrong': wrong},{'cr': cr})


def talkanswer(request):
    if 'username' in request.session:
        username = request.session['username']

    total = [0]
    correct = [0]
    wrong = [0]
    cr = [0]
    r = talk.objects.all()
    qid = request.GET["q1"]
    q = talk.objects.filter(id=int(qid))
    x = q[0]
    if request.GET[qid] == x.answer:
        total[0] = int(request.GET["total"]) + 1
        correct[0] = int(request.GET["correct"]) + 1
        wrong[0] = int(request.GET["wrong"])
        cr[0] = int(int(correct[0]) / int(total[0]) * 100)
        right = [request.GET[qid]]
        message = ["correct"]
        img = ["https://cdn4.iconfinder.com/data/icons/orb/128/4.png"]
    else:
        total[0] = int(request.GET["total"]) + 1
        wrong[0] = int(request.GET["wrong"]) + 1
        correct[0] = int(request.GET["correct"])
        cr[0] = int(int(correct[0]) / int(total[0]) * 100)
        right = [request.GET[qid]]
        message = ["wrong"]
        img = ["https://cdn3.iconfinder.com/data/icons/musthave/256/Remove.png"]
    return render_to_response('subjects/talkanswer.html', locals())
    return render(request, 'subjects/talkanswer.html', {'total': total}, {'correct': correct}, {'wrong': wrong}, {'cr': cr},{'message': message}, {'right': right}, {'img': img})


def ctalkpractice(request):
    if 'username' in request.session:
        username = request.session['username']

    total = [request.GET["total"]]
    correct = [request.GET["correct"]]
    wrong = [request.GET["wrong"]]
    cr = [request.GET["cr"]]

    t = talk.objects.all()
    w = random.sample(range(1, talk.objects.count()), 1)
    ran = w[0]
    q = talk.objects.filter(id=t[ran].id)

    return render_to_response('subjects/talkpractice.html', locals())
    return render(request, 'subjects/talkpractice.html', {'total': total}, {'correct': correct}, {'wrong': wrong},{'cr': cr})

def short_conversationpractice(request):
    if 'username' in request.session:
        username = request.session['username']

    total = [0]
    correct = [0]
    wrong = [0]
    cr = [0]

    t = short_conversation.objects.all()
    w = random.sample(range(1, short_conversation.objects.count()), 1)
    ran = w[0]
    q = short_conversation.objects.filter(id=t[ran].id)

    return render_to_response('subjects/short_conversationpractice.html', locals())
    return render(request, 'subjects/short_conversationpractice.html', {'total': total}, {'correct': correct}, {'wrong': wrong},{'cr': cr})


def short_conversationanswer(request):
    if 'username' in request.session:
        username = request.session['username']

    total = [0]
    correct = [0]
    wrong = [0]
    cr = [0]
    r = short_conversation.objects.all()
    qid = request.GET["q1"]
    q = short_conversation.objects.filter(id=int(qid))
    x = q[0]
    if request.GET[qid] == x.answer:
        total[0] = int(request.GET["total"]) + 1
        correct[0] = int(request.GET["correct"]) + 1
        wrong[0] = int(request.GET["wrong"])
        cr[0] = int(int(correct[0]) / int(total[0]) * 100)
        right = [request.GET[qid]]
        message = ["correct"]
        img = ["https://cdn4.iconfinder.com/data/icons/orb/128/4.png"]
    else:
        total[0] = int(request.GET["total"]) + 1
        wrong[0] = int(request.GET["wrong"]) + 1
        correct[0] = int(request.GET["correct"])
        cr[0] = int(int(correct[0]) / int(total[0]) * 100)
        right = [request.GET[qid]]
        message = ["wrong"]
        img = ["https://cdn3.iconfinder.com/data/icons/musthave/256/Remove.png"]
    return render_to_response('subjects/short_conversationanswer.html', locals())
    return render(request, 'subjects/short_conversationanswer.html', {'total': total}, {'correct': correct}, {'wrong': wrong}, {'cr': cr},{'message': message}, {'right': right}, {'img': img})


def cshort_conversationpractice(request):
    if 'username' in request.session:
        username = request.session['username']

    total = [request.GET["total"]]
    correct = [request.GET["correct"]]
    wrong = [request.GET["wrong"]]
    cr = [request.GET["cr"]]

    t = short_conversation.objects.all()
    w = random.sample(range(1, short_conversation.objects.count()), 1)
    ran = w[0]
    q = short_conversation.objects.filter(id=t[ran].id)

    return render_to_response('subjects/short_conversationpractice.html', locals())
    return render(request, 'subjects/short_conversationpractice.html', {'total': total}, {'correct': correct}, {'wrong': wrong},{'cr': cr})

def writepractice(request):
    if 'username' in request.session:
        username = request.session['username']
    return render(request, 'subjects/writepractice.html', locals())

def grammarpractice(request):
    if 'username' in request.session:
        username = request.session['username']

    total = [0]
    correct = [0]
    wrong = [0]
    cr = [0]

    t = grammar.objects.all()
    w = random.sample(range(1, grammar.objects.count()), 1)
    ran = w[0]
    q = grammar.objects.filter(id=t[ran].id)

    return render_to_response('subjects/grammarpractice.html', locals())
    return render(request, 'subjects/grammarpractice.html', {'total': total}, {'correct': correct}, {'wrong': wrong},{'cr': cr})


def grammaranswer(request):
    if 'username' in request.session:
        username = request.session['username']

    total = [0]
    correct = [0]
    wrong = [0]
    cr = [0]
    r = grammar.objects.all()
    qid = request.GET["q1"]
    q = grammar.objects.filter(id=int(qid))
    x = q[0]
    if request.GET[qid] == x.answer:
        total[0] = int(request.GET["total"]) + 1
        correct[0] = int(request.GET["correct"]) + 1
        wrong[0] = int(request.GET["wrong"])
        cr[0] = int(int(correct[0]) / int(total[0]) * 100)
        right = [request.GET[qid]]
        message = ["correct"]
        img = ["https://cdn4.iconfinder.com/data/icons/orb/128/4.png"]
    else:
        total[0] = int(request.GET["total"]) + 1
        wrong[0] = int(request.GET["wrong"]) + 1
        correct[0] = int(request.GET["correct"])
        cr[0] = int(int(correct[0]) / int(total[0]) * 100)
        right = [request.GET[qid]]
        message = ["wrong"]
        img = ["https://cdn3.iconfinder.com/data/icons/musthave/256/Remove.png"]
    return render_to_response('subjects/grammaranswer.html', locals())
    return render(request, 'subjects/grammaranswer.html', {'total': total}, {'correct': correct}, {'wrong': wrong}, {'cr': cr},{'message': message}, {'right': right}, {'img': img})


def cgrammarpractice(request):
    if 'username' in request.session:
        username = request.session['username']

    total = [request.GET["total"]]
    correct = [request.GET["correct"]]
    wrong = [request.GET["wrong"]]
    cr = [request.GET["cr"]]

    t = grammar.objects.all()
    w = random.sample(range(1, grammar.objects.count()), 1)
    ran = w[0]
    q = grammar.objects.filter(id=t[ran].id)

    return render_to_response('subjects/grammarpractice.html', locals())
    return render(request, 'subjects/grammarpractice.html', {'total': total}, {'correct': correct}, {'wrong': wrong},{'cr': cr})

def nounpractice(request):
    if 'username' in request.session:
        username = request.session['username']

    total = [0]
    correct = [0]
    wrong = [0]
    cr = [0]

    t = noun.objects.all()
    w = random.sample(range(1, noun.objects.count()), 1)
    ran = w[0]
    q = noun.objects.filter(id=t[ran].id)

    return render_to_response('subjects/nounpractice.html', locals())
    return render(request, 'subjects/nounpractice.html', {'total': total}, {'correct': correct}, {'wrong': wrong},{'cr': cr})


def nounanswer(request):
    if 'username' in request.session:
        username = request.session['username']

    total = [0]
    correct = [0]
    wrong = [0]
    cr = [0]
    r = noun.objects.all()
    qid = request.GET["q1"]
    q = noun.objects.filter(id=int(qid))
    x = q[0]
    if request.GET[qid] == x.answer:
        total[0] = int(request.GET["total"]) + 1
        correct[0] = int(request.GET["correct"]) + 1
        wrong[0] = int(request.GET["wrong"])
        cr[0] = int(int(correct[0]) / int(total[0]) * 100)
        right = [request.GET[qid]]
        message = ["correct"]
        img = ["https://cdn4.iconfinder.com/data/icons/orb/128/4.png"]
    else:
        total[0] = int(request.GET["total"]) + 1
        wrong[0] = int(request.GET["wrong"]) + 1
        correct[0] = int(request.GET["correct"])
        cr[0] = int(int(correct[0]) / int(total[0]) * 100)
        right = [request.GET[qid]]
        message = ["wrong"]
        img = ["https://cdn3.iconfinder.com/data/icons/musthave/256/Remove.png"]
    return render_to_response('subjects/nounanswer.html', locals())
    return render(request, 'subjects/nounanswer.html', {'total': total}, {'correct': correct}, {'wrong': wrong}, {'cr': cr},{'message': message}, {'right': right}, {'img': img})


def cnounpractice(request):
    if 'username' in request.session:
        username = request.session['username']

    total = [request.GET["total"]]
    correct = [request.GET["correct"]]
    wrong = [request.GET["wrong"]]
    cr = [request.GET["cr"]]

    t = noun.objects.all()
    w = random.sample(range(1, noun.objects.count()), 1)
    ran = w[0]
    q = noun.objects.filter(id=t[ran].id)

    return render_to_response('subjects/nounpractice.html', locals())
    return render(request, 'subjects/nounpractice.html', {'total': total}, {'correct': correct}, {'wrong': wrong},{'cr': cr})

def readingpractice(request):
    if 'username' in request.session:
        username = request.session['username']

    total = [0]
    correct = [0]
    wrong = [0]
    cr = [0]

    t = reading.objects.all()
    w = random.sample(range(1, reading.objects.count()), 1)
    ran = w[0]
    q = reading.objects.filter(id=t[ran].id)

    return render_to_response('subjects/readingpractice.html', locals())
    return render(request, 'subjects/readingpractice.html', {'total': total}, {'correct': correct}, {'wrong': wrong},{'cr': cr})


def readinganswer(request):
    if 'username' in request.session:
        username = request.session['username']

    total = [0]
    correct = [0]
    wrong = [0]
    cr = [0]
    r = reading.objects.all()
    qid = request.GET["q1"]
    q = reading.objects.filter(id=int(qid))
    x = q[0]
    if request.GET[qid] == x.answer:
        total[0] = int(request.GET["total"]) + 1
        correct[0] = int(request.GET["correct"]) + 1
        wrong[0] = int(request.GET["wrong"])
        cr[0] = int(int(correct[0]) / int(total[0]) * 100)
        right = [request.GET[qid]]
        message = ["correct"]
        img = ["https://cdn4.iconfinder.com/data/icons/orb/128/4.png"]
    else:
        total[0] = int(request.GET["total"]) + 1
        wrong[0] = int(request.GET["wrong"]) + 1
        correct[0] = int(request.GET["correct"])
        cr[0] = int(int(correct[0]) / int(total[0]) * 100)
        right = [request.GET[qid]]
        message = ["wrong"]
        img = ["https://cdn3.iconfinder.com/data/icons/musthave/256/Remove.png"]
    return render_to_response('subjects/readinganswer.html', locals())
    return render(request, 'subjects/readinganswer.html', {'total': total}, {'correct': correct}, {'wrong': wrong}, {'cr': cr},{'message': message}, {'right': right}, {'img': img})


def creadingpractice(request):
    if 'username' in request.session:
        username = request.session['username']

    total = [request.GET["total"]]
    correct = [request.GET["correct"]]
    wrong = [request.GET["wrong"]]
    cr = [request.GET["cr"]]

    t = reading.objects.all()
    w = random.sample(range(1, reading.objects.count()), 1)
    ran = w[0]
    q = reading.objects.filter(id=t[ran].id)

    return render_to_response('subjects/readingpractice.html', locals())
    return render(request, 'subjects/readingpractice.html', {'total': total}, {'correct': correct}, {'wrong': wrong},{'cr': cr})

def userinfo(request):
    if 'username' in request.session:
        username = request.session['username']
        NOWUser1 = UserProfile.objects.get(FullName = username)
        NOWUser2 = Examinees.objects.get(user__Username=NOWUser1.Username)

    template = get_template('subjects/userinfo.html')
    try:
        urid=request.GET['q_id']
    except:
        urid = None
    score=models.Score.objects.filter(Ex=NOWUser2).order_by('-Exam_Date')
    html = template.render(context=locals(), request=request)
    return HttpResponse(html)