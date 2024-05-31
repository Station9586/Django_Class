from django.shortcuts import render, redirect
from _myform.models import *
from django.http import HttpResponse, HttpResponseRedirect
from _myform.forms import *
from django.contrib.sessions.models import Session
from django.contrib import messages
from django.contrib.auth.models import User as USER
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.contrib.auth.decorators import login_required
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
    if (request.user.is_authenticated): 
        username = request.user.username
        useremail = request.user.email
        try: 
            user = USER.objects.get(username = username)
            diary = Diary.objects.filter(user = user).order_by('-date')
        except: pass
    messages.get_messages(request)
    return render(request, 'index.html', locals())
    # print('index', request.session.get('username'))
    # if ('username' in request.session and 'useremail' in request.session):
    #     username = request.session['username']
    #     useremail = request.session['useremail']
    # return render(request, 'index.html', locals())
    # years: range = range(1960, 2025)
    # posts = Post.objects.filter(enabled = True).order_by('-pub_time')[:30]
    # moods = Mood.objects.all()
    # try: 
    #     user_id = request.GET['user_id']
    #     user_pass = request.GET['user_pass']
    #     user_post = request.GET['user_post']
    #     user_mood = request.GET['mood']
    #     user_birth = request.GET['user_birth']
    # except:
    #     user_id = None
    #     message = '每個都要填才能張貼訊息'

    # if (del_pass and pid):
    #     try: 
    #         post = Post.objects.get(id = pid)
    #     except: 
    #         post = None
    #     if (post.del_pass == del_pass): 
    #         post.delete()
    #         message = '刪除成功'
    #     else: 
    #         message = '密碼錯誤'
    # elif (user_id != None): 
    #     mood = Mood.objects.get(status = user_mood)
    #     post = Post.objects.create(mood = mood, nickname = user_id, message = user_post, del_pass = user_pass, birth = user_birth)
    #     post.save()
    #     message = '成功張貼訊息'

    # return render(request, 'index.html', locals())

def listing (request):
    posts = Post.objects.filter(enabled = True).order_by('-pub_time')[:150]
    moods = Mood.objects.all()
    return render(request, 'listing.html', locals())

def posting (request): 
    # moods = Mood.objects.all()
    # years: range = range(1960, 2025)
    # try: 
    #     user_id = request.GET['user_id']
    #     user_pass = request.GET['user_pass']
    #     user_post = request.GET['user_post']
    #     user_mood = request.GET['mood']
    #     user_birth = request.GET['birth'];
    # except:
    #     user_id = None
    #     message = '每個都要填才能張貼訊息'
        
    # if (user_id != None): 
    #     mood = Mood.objects.get(status = user_mood)
    #     post = Post.objects.create(mood = mood, nickname = user_id, message = user_post, del_pass = user_pass)
    #     post.save()
    #     message = '成功張貼訊息'

    # return render(request, 'posting.html', locals())
    if (request.user.is_authenticated): 
        username = request.user.username
        useremail = request.user.email
    messages.get_messages(request)
    if (request.method == 'POST'):
        user = USER.objects.get(username = username)
        diary = models.Diary(user = user)
        post_form = DiaryForm(request.POST, instance = diary)
        if (post_form.is_valid()): 
            messages.add_message(request, messages.INFO, '日記已儲存')
            post_form.save()
            return redirect('/')
            message = '日記已儲存'
        else: 
            messages.add_message(request, messages.INFO, '每一欄都要填寫才能張貼訊息')
    else: 
        post_form = DiaryForm()
        messages.add_message(request, messages.INFO, '每一欄都要填寫才能張貼訊息')
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

def login (request):
    if (request.method == 'POST'): 
        form = LoginForm(request.POST)
        if (form.is_valid()): 
            login_name = request.POST['username']
            login_psw = request.POST['password']
            user = authenticate(username = login_name, password = login_psw)
            if (user is not None): 
                if (user.is_active): 
                    auth.login(request, user)
                    messages.add_message(request, messages.SUCCESS, '登入成功')
                    return redirect('/')
                else:
                    messages.add_message(request, messages.WARNING, '帳號尚未啟用')
            else:
                messages.add_message(request, messages.WARNING, '登入失敗')
            # try: 
            #     user = User.objects.get(name = login_name)
            #     if (user.password == login_psw): 
            #         request.session['username'] = user.name
            #         request.session['useremail'] = user.email
            #         # request.session['message'] = '登入成功'
            #         messages.add_message(request, messages.SUCCESS, '登入成功')
            #         return redirect('/userinfo')
            #     else: 
            #         messages.add_message(request, messages.WARNING, '密碼錯誤')
            # except:
            #         messages.add_message(request, messages.WARNING, '查無此帳號')
            # return HttpResponseRedirect('/index')
        else: 
            messages.add_message(request, messages.WARNING, '請檢查輸入的欄位')
    else: 
        form = LoginForm()

    return render(request, 'login.html', locals())

def logout (request): 
    auth.logout(request)
    messages.add_message(request, messages.INFO, '您已經登出')
    return redirect('/')
    # print('logout', request.session.get('username'))
    # if ('username' in request.session): 
    #     Session.objects.all().delete()
    #     return redirect('/login')
    # return redirect('/')

@login_required(login_url = '/login')
def userinfo (request): 
    if (request.user.is_authenticated): 
        username = request.user.username
    user = USER.objects.get(username = username)
    try: profile = Profile.objects.get(user = user)
    except: profile = Profile(user = user)

    if (request.method == 'POST'):
        profile_form = ProfileForm(request.POST, instance = profile)
        if (profile_form.is_valid()): 
            profile_form.save()
            messages.add_message(request, messages.INFO, '個人資料已儲存')
            return HttpResponseRedirect('/userinfo')
        else: 
            messages.add_message(request, messages.INFO, '請檢查輸入的欄位')
    else: profile_form = ProfileForm()
    # if ('username' in request.session): 
    #     username = request.session['username']
    # else: 
    #     return redirect('/login') 
    # try: 
    #     userinfo = models.User.objects.get(name = username)
    # except:
    #     pass
    return render(request, 'userinfo.html', locals())
