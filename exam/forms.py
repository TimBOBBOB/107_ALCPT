from django.test import TestCase
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.admin import widgets
from exam.models import talk, grammar, short_conversation, noun, reading, Document, exam, post

class UserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', ' password',)
    
    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password != password2:
            raise forms.ValidationError('密碼不相符')
        return password2

class talkform(forms.ModelForm):

    a = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, }), max_length=40)
    b = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, }), max_length=40)
    c = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, }), max_length=40)
    d = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, }), max_length=40)

    class Meta:
        model = talk
        fields = ('question', 'a', 'b', 'c', 'd', 'answer',)

    def __init__(self, *args, **kwargs):
        super(talkform, self).__init__(*args, **kwargs)
        self.fields['question'].label = '題目'
        self.fields['a'].label = 'a'
        self.fields['b'].label = 'b'
        self.fields['c'].label = 'c'
        self.fields['d'].label = 'd'
        self.fields['answer'].label = '答案'

class grammarform(forms.ModelForm):

    question = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, }), max_length=4000)
    a = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, }), max_length=40)
    b = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, }), max_length=40)
    c = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, }), max_length=40)
    d = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, }), max_length=40)

    class Meta:
        model = grammar
        fields = ('question', 'a', 'b', 'c', 'd', 'answer',)
    def __init__(self ,*args ,**kwargs):
        super(grammarform,self).__init__(*args,**kwargs)
        self.fields['question'].label = '題目'
        self.fields['a'].label = 'a'
        self.fields['b'].label = 'b'
        self.fields['c'].label = 'c'
        self.fields['d'].label = 'd'
        self.fields['answer'].label = '答案'

class short_conversationform(forms.ModelForm):

    a = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, }), max_length=40)
    b = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, }), max_length=40)
    c = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, }), max_length=40)
    d = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, }), max_length=40)

    class Meta:
        model = grammar
        fields = ('question', 'a', 'b', 'c', 'd', 'answer',)
    def __init__(self ,*args ,**kwargs):
        super(short_conversationform,self).__init__(*args,**kwargs)
        self.fields['question'].label = '題目'
        self.fields['a'].label = 'a'
        self.fields['b'].label = 'b'
        self.fields['c'].label = 'c'
        self.fields['d'].label = 'd'
        self.fields['answer'].label = '答案'

class nounform(forms.ModelForm):

    question = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, }), max_length=4000)
    a = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, }), max_length=40)
    b = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, }), max_length=40)
    c = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, }), max_length=40)
    d = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, }), max_length=40)

    class Meta:
        model = noun
        fields = ('question', 'a', 'b', 'c', 'd', 'answer',)
    def __init__(self ,*args ,**kwargs):
        super(nounform,self).__init__(*args,**kwargs)
        self.fields['question'].label = '題目'
        self.fields['a'].label = 'a'
        self.fields['b'].label = 'b'
        self.fields['c'].label = 'c'
        self.fields['d'].label = 'd'
        self.fields['answer'].label = '答案'

class readingform(forms.ModelForm):

    question = forms.CharField(widget=forms.Textarea(attrs={ 'rows': 5, }), max_length=4000)
    a = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, }), max_length=40)
    b = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, }), max_length=40)
    c = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, }), max_length=40)
    d = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, }), max_length=40)

    class Meta:
        model = reading
        fields = ('question', 'a', 'b', 'c', 'd', 'answer',)
    def __init__(self ,*args ,**kwargs):
        super(readingform,self).__init__(*args,**kwargs)
        self.fields['question'].label = '題目'
        self.fields['a'].label = 'a'
        self.fields['b'].label = 'b'
        self.fields['c'].label = 'c'
        self.fields['d'].label = 'd'
        self.fields['answer'].label = '答案'

class check_readingform(forms.ModelForm):
    class Meta:
        model=reading
        fields=['enabled']
    def __init__(self,*args,**kwargs):
        super(check_readingform,self).__init__(*args,**kwargs)
        self.fields['enabled'].label = '審核'


class check_talkform(forms.ModelForm):
    class Meta:
        model=talk
        fields=['enabled']
    def __init__(self,*args,**kwargs):
        super(check_talkform,self).__init__(*args,**kwargs)
        self.fields['enabled'].label = '審核'


class check_nounform(forms.ModelForm):
    class Meta:
        model=noun
        fields=['enabled']

    def __init__(self,*args,**kwargs):
        super(check_nounform,self).__init__(*args,**kwargs)
        self.fields['enabled'].label = '審核'

class check_grammarform(forms.ModelForm):
    class Meta:
        model=grammar
        fields=['enabled']
    def __init__(self,*args,**kwargs):
        super(check_grammarform,self).__init__(*args,**kwargs)
        self.fields['enabled'].label = '審核'

class check_short_conversationform(forms.ModelForm):
    class Meta:
        model=short_conversation
        fields=['enabled']
    def __init__(self,*args,**kwargs):
        super(check_short_conversationform,self).__init__(*args,**kwargs)
        self.fields['enabled'].label = '審核'

class Documentform(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )

class DateInpute(forms.DateInput):
    intput_type = 'date'

class examform(forms.ModelForm):

    ddate = forms.SplitDateTimeField(widget=widgets.AdminSplitDateTime())

    class Meta:
        model = exam
        fields = ('topic', 'ddate',  'member')

    def __init__(self, *args, **kwargs):
        super(examform, self).__init__(*args, **kwargs)
        self.fields['topic'].label = '考卷'
        self.fields['ddate'].label = '考試日期'
        self.fields['member'].label = '受測者'

class postform(forms.ModelForm):

    title = forms.CharField(widget=forms.Textarea(attrs={'rows': 1,}), max_length=40)
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, }), max_length=40)

    class Meta:
        model = post
        fields = ('title', 'text', 'enabled')

    def __init__(self ,*args ,**kwargs):
        super(postform,self).__init__(*args,**kwargs)
        self.fields['title'].label = '公告主題'
        self.fields['text'].label = '公告內容'
        self.fields['enabled'].label = '設為公告'