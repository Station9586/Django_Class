from django import forms
from . import models
from captcha.fields import CaptchaField

class LoginForm (forms.Form): 
    # COLORS = [
    #     ["紅", "紅"],
    #     ["綠", "綠"],
    #     ["藍", "藍"],
    #     ["黃", "黃"],
    #     ["黑", "黑"],
    #     ["白", "白"] 
    # ]
    username = forms.CharField(label = '您的名字', max_length = 10)
    # usercolor = forms.ChoiceField(label = '喜歡的顏色', choices = COLORS)
    password = forms.CharField(label = '密碼', widget = forms.PasswordInput())