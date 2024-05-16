from django.db import models
from django import forms
from captcha.fields import CaptchaField

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


class Contact (models.Model):
    CITY = [
        ['TP', 'Taipei'],
        ['TY', 'Taoyuan'],
        ['TC', 'Taichung'],
        ['TN', 'Tainan'],
        ['KS', 'Kaohsiung'],
        ['NA', 'Others']
    ]
    user_name = models.CharField(max_length = 50)
    user_city = models.CharField(max_length = 10, choices = CITY)
    user_school = models.BooleanField(default = False)
    user_email = models.EmailField()
    user_message = models.TextField()

    def __str__ (self) -> str: return self.user_name

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


class ContactForm2 (forms.ModelForm): 
    class Meta: 
        model = Contact
        fields = '__all__'
    
    def __init__ (self, *args, **kwargs):
        super(ContactForm2, self).__init__(*args, **kwargs)
        self.fields['user_name'].label = '你的名字'
        self.fields['user_city'].label = '你的城市'
        self.fields['user_school'].label = '是否在學'
        self.fields['user_email'].label = '你的信箱'
        self.fields['user_message'].label = '你的訊息'