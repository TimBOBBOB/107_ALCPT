from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

select = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        )


class UserProfile(models.Model):
    Username = models.CharField(max_length=10)
    Password = models.CharField(max_length=20)
    FullName = models.CharField(max_length=10)
    Authority = models.CharField(max_length=25)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Username



class System_administrator(models.Model):
    user = models.OneToOneField(UserProfile, related_name='SA')

    def __str__(self):
        return self.user.Username


class Score_reviewers(models.Model):
    user = models.OneToOneField(UserProfile, related_name='SR')

    def __str__(self):
        return self.user.Username


class Questions_bank_administrator(models.Model):
    user = models.OneToOneField(UserProfile, related_name='QBA')

    def __str__(self):
        return self.user.Username


class Questions_bank_operator(models.Model):
    user = models.OneToOneField(UserProfile, related_name='QBO')

    def __str__(self):
        return self.user.Username


class Exam_administrator(models.Model):
    user = models.OneToOneField(UserProfile, related_name='EA')

    def __str__(self):
        return self.user.Username


class Examinees(models.Model):
    user = models.OneToOneField(UserProfile, related_name='EE')
    Class = models.IntegerField(blank=True, default=1)
    Sex = models.CharField(max_length=3,blank=True)
    Major = models.OneToOneField(to="Department", to_field="id", default=5)
    Company = models.OneToOneField(to="Company", to_field="id", default=6)
    Comp_Num = models.IntegerField(blank=True, default=1)

    def __str__(self):
        return self.user.Username


class talk(models.Model):
    question = models.FileField(upload_to='documents/')
    a = models.CharField(max_length = 200)
    b = models.CharField(max_length = 200)
    c = models.CharField(max_length = 200)
    d = models.CharField(max_length = 200)
    answer = models.CharField(max_length = 4,choices=select)
    enabled = models.BooleanField(default=False)
    pub_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


class grammar(models.Model):
    question = models.TextField(max_length = 200)
    a = models.CharField(max_length = 200)
    b = models.CharField(max_length = 200)
    c = models.CharField(max_length = 200)
    d = models.CharField(max_length = 200)
    answer = models.CharField(max_length = 4,choices=select)
    enabled = models.BooleanField(default=False)
    pub_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question


class short_conversation(models.Model):
    question = models.FileField(upload_to='documents/')
    a = models.CharField(max_length = 200)
    b = models.CharField(max_length = 200)
    c = models.CharField(max_length = 200)
    d = models.CharField(max_length = 200)
    answer = models.CharField(max_length = 4,choices=select)
    enabled = models.BooleanField(default=False)
    pub_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


class noun(models.Model):
    question = models.TextField(max_length = 200)
    a = models.CharField(max_length = 200)
    b = models.CharField(max_length = 200)
    c = models.CharField(max_length = 200)
    d = models.CharField(max_length = 200)
    answer = models.CharField(max_length = 4,choices=select)
    enabled = models.BooleanField(default=False)
    pub_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question


class reading(models.Model):
    question = models.TextField(max_length = 400)
    a = models.CharField(max_length = 200)
    b = models.CharField(max_length = 200)
    c = models.CharField(max_length = 200)
    d = models.CharField(max_length = 200)
    answer = models.CharField(max_length = 4,choices=select)
    enabled = models.BooleanField(default=False)
    pub_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Score(models.Model):
    Exam_Date = models.DateTimeField(auto_now_add=True)
    Error_Num = models.TextField(max_length=100, blank=True)
    Score = models.IntegerField()
    Ex = models.ForeignKey(to="Examinees", to_field="user", null=True)

    def __str__(self):
        return str(self.Ex)


class Company(models.Model):
    Name = models.CharField(max_length=5)

    def __str__(self):
        return self.Name


class Department(models.Model):
    Name = models.CharField(max_length=3)

    def __str__(self):
        return self.Name


class exam(models.Model):
    topic = models.ForeignKey(to="topic", to_field="id")
    ddate = models.DateTimeField()
    member = models.ForeignKey(to="member", to_field="id")

    def lifespan(self):
        return self.ddate.strftime('%Y/%m/%d')

    def __str__(self):
        return str(self.lifespan())


class topic(models.Model):
    Created = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length = 400)

    def lifespan(self):
        return self.Created.strftime('%Y/%m/%d')

    def __str__(self):
        return str(self.id)


class member(models.Model):
    Created = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length = 400)

    def lifespan(self):
        return self.Created.strftime('%Y/%m/%d (%H+8):%M')

    def __str__(self):
        return str(self.id)


class post(models.Model):
    title = models.TextField(max_length=200)
    text = models.TextField(max_length=400)
    enabled = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def lifespan(self):
        return self.created.strftime('%Y/%m/%d')

    def __str__(self):
        return self.title