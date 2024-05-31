from django.db import models
from django import forms
from captcha.fields import CaptchaField
from django.contrib.auth.models import User as USER

# Create your models here.
class Mood (models.Model): 
    status = models.CharField(max_length = 10, null = False)

    def __str__ (self) -> str: return self.status

class Post (models.Model): 
    mood = models.ForeignKey(Mood, on_delete = models.CASCADE)
    nickname = models.CharField(max_length = 10, default="不願意透露")
    message = models.TextField(null = False)
    del_pass = models.CharField(max_length = 10)
    pub_time = models.DateTimeField(auto_now = True)
    enabled = models.BooleanField(default = True)
    birth = models.IntegerField(default = 1960);

    def __str__ (self) -> str: return self.message

class ContactForm (forms.Form): 
    CITY = [
        ['TP', 'Taipei'],
        ['TY', 'Taoyuan'],
        ['TC', 'Taichung'],
        ['TN', 'Tainan'],
        ['KS', 'Kaohsiung'],
        ['NA', 'Others']
    ]
    user_name = forms.CharField(label = 'Your Name', max_length = 50, initial = 'CAT')
    user_city = forms.ChoiceField(label = 'Residence', choices = CITY)
    user_school = forms.BooleanField(label = '是否在學', required = False)
    user_email = forms.EmailField(label = 'Email')
    user_message = forms.CharField(label = 'Message', widget = forms.Textarea)

class PostForm (forms.ModelForm): 
    captcha = CaptchaField()
    class Meta: 
        model = Post
        fields = ['mood', 'nickname', 'message', 'del_pass', 'birth']
    
    def __init__ (self, *args, **kwargs): 
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['mood'].label = '現在心情'
        self.fields['nickname'].label = '暱稱'
        self.fields['message'].label = '心情留言'
        self.fields['birth'].label = '出生年'
        self.fields['del_pass'].label = '設定密碼'
        self.fields['captcha'].label = '你先確定你不是機器人'

class User (models.Model): 
    name = models.CharField(max_length = 50, null=False)
    email = models.EmailField(null = False)
    password = models.CharField(max_length = 50, null = False)
    enabled = models.BooleanField(default = True)

    def __str__ (self) -> str: return self.name


class Profile (models.Model): 
    user = models.OneToOneField(USER, on_delete = models.CASCADE)
    height = models.PositiveIntegerField(default = 160)
    male = models.BooleanField(default = False)
    website = models.URLField(null = True)

    def __str__ (self) -> str: return self.user.username

class Diary (models.Model): 
    user = models.ForeignKey(USER, on_delete = models.CASCADE)
    budget = models.FloatField(default = 0)
    weight = models.FloatField(default = 0)
    note = models.TextField(null = True)
    date = models.DateField()

    def __str__ (self) -> str: return f"{self.date}({self.user})"

class DiaryForm (forms.ModelForm):
    class Meta: 
        model = Diary
        fields = ['budget', 'weight', 'note', 'date']
        widgets = {"date": forms.DateInput(attrs = {"type": "date"})}
    
    def __init__ (self, *args, **kwargs):
        super(DiaryForm, self).__init__(*args, **kwargs)
        self.fields['budget'].label = '今日花費'
        self.fields['weight'].label = '今日體重'
        self.fields['note'].label = '心得'
        self.fields['date'].label = '日期'
    
class ProfileForm (forms.ModelForm): 
    class Meta: 
        model = Profile
        fields = ['height', 'male', 'website']
    
    def __init__ (self, *args, **kwargs): 
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['height'].label = '身高(cm)'
        self.fields['male'].label = "男的？"
        self.fields['website'].label = '個人網站'