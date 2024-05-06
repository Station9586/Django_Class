from django.shortcuts import render
from _myform.models import *
from django.http import HttpResponse, HttpResponseRedirect
# from django import forms
# Create your views here.

# def index (request): 
#     years: range = range(1960, 2025)
#     try: 
#         urid = request.GET['user_id']
#         urpass = request.GET['user_pass']
#         urfcolor = request.GET.getlist('fcolor')
#     except: 
#         urid = None

#     if (urid != None and urpass == '12345'): verified = True
#     else: verified = False

#     return render(request, 'index.html', locals())

def index (request, pid = None, del_pass = None): 
    years: range = range(1960, 2025)
    posts = Post.objects.filter(enabled = True).order_by('-pub_time')[:30]
    moods = Mood.objects.all()
    try: 
        user_id = request.GET['user_id']
        user_pass = request.GET['user_pass']
        user_post = request.GET['user_post']
        user_mood = request.GET['mood']
        user_birth = request.GET['user_birth']
    except:
        user_id = None
        message = '每個都要填才能張貼訊息'

    if (del_pass and pid):
        try: 
            post = Post.objects.get(id = pid)
        except: 
            post = None
        if (post.del_pass == del_pass): 
            post.delete()
            message = '刪除成功'
        else: 
            message = '密碼錯誤'
    elif (user_id != None): 
        mood = Mood.objects.get(status = user_mood)
        post = Post.objects.create(mood = mood, nickname = user_id, message = user_post, del_pass = user_pass, birth = user_birth)
        post.save()
        message = '成功張貼訊息'

    return render(request, 'index.html', locals())

def listing (request):
    posts = Post.objects.filter(enabled = True).order_by('-pub_time')[:150]
    moods = Mood.objects.all()
    return render(request, 'listing.html', locals())

def posting (request): 
    moods = Mood.objects.all()
    years: range = range(1960, 2025)
    try: 
        user_id = request.GET['user_id']
        user_pass = request.GET['user_pass']
        user_post = request.GET['user_post']
        user_mood = request.GET['mood']
        user_birth = request.GET['birth'];
    except:
        user_id = None
        message = '每個都要填才能張貼訊息'
        
    if (user_id != None): 
        mood = Mood.objects.get(status = user_mood)
        post = Post.objects.create(mood = mood, nickname = user_id, message = user_post, del_pass = user_pass)
        post.save()
        message = '成功張貼訊息'

    return render(request, 'posting.html', locals())

def contact (request):
    if (request.method == 'POST'):
        form = ContactForm(request.POST)
        if (form.is_valid()): 
            message = '感謝您的來信'
            user_name = form.cleaned_data['user_name']
            user_city = form.cleaned_data['user_city']
            user_school = form.cleaned_data['user_school']
            user_email = form.cleaned_data['user_email']
            user_message = form.cleaned_data['user_message']
        else: 
            message = '請檢查您輸入的資訊'
    else: 
        form = ContactForm()
    return render(request, 'contact.html', locals())

def post2db (request): 
    moods = Mood.objects.all()
    if (request.method == 'POST'): 
        post_form = PostForm(request.POST)
        if (post_form.is_valid()): 
            message = '資料驗證成功'
            post_form.save()
            return HttpResponseRedirect('/listing')
        else: message = '每一欄都掉要填寫才能張貼訊息'
    else: 
        post_form = PostForm()
        message = '每一欄都掉要填寫才能張貼訊息'
    return render(request, 'post2db.html', locals())