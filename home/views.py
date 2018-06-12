from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from home.models import User
from home.models import Post
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers
from django.utils import timezone
from django.views.generic.base import TemplateView

# model user

def home(request):

    return render(request, 'home/home.html', {})

@csrf_exempt
def login(request):
    print("login start")
    if request.is_ajax():

        login_id = request.POST.get('login_id')
        login_pw = request.POST.get('login_pw')

        try :
            row = User.objects.get(user_id=login_id,password=login_pw)

            request.session['user_id'] = login_id

        except BaseException:
            return JsonResponse({'return':'fail'})

        print ("login id, pw--------->",row)

        return JsonResponse({'return':'success'})

    return render(request, 'home/login.html',{})

@csrf_exempt
def regist(request):
    print("regist start")
    if request.is_ajax():

        sign_id = request.POST.get('sign_id')
        sign_pw = request.POST.get('sign_pw')
        sign_name = request.POST.get('sign_name')

        #reg = User.objects.create(user_id=sign_id,password=sign_pw,name=sign_name)
        try:
             user_reg = User(user_id=sign_id,password=sign_pw,name=sign_name)
             user_reg.save()
            #reg = User.objects.create(user_id=sign_id,password=sign_pw,name=sign_name)
            #reg, created = User.objects.get_or_create(user_id=sign_id,password=sign_pw,name=sign_name)
        except User.DoesNotExist:
            #print ("user_reg--------->",user_reg)
            print ("sign id --------->",sign_id)
            print ("regist fail")
            return JsonResponse({'return':'fail'})
        #print ("reg--------->",reg)


        return JsonResponse({'return':'success'})

def logout(request):

    if 'user_id' in request.session:
        del request.session['user_id']

    return render(request, 'home/logout.html',{})

def file(request):
    return render(request,'home/file.html')

@csrf_exempt
def post_insert(request):
    print('post_list start --------------------> ')

    return render(request, 'home/post_insert.html')

@csrf_exempt
def post_list_data(request):

    print("regist start")

    if request.is_ajax():

        content_title = request.POST.get('content_title')
        Content = request.POST.get('Content')
        user_id = request.POST.get('user_id')
        print(user_id)

        try:
             post_insert = Post(user_id=user_id,title=content_title,content=Content)
             post_insert.save()

             request.session['user_id'] = user_id
            #reg = User.objects.create(user_id=sign_id,password=sign_pw,name=sign_name)
            #reg, created = User.objects.get_or_create(user_id=sign_id,password=sign_pw,name=sign_name)
        except User.DoesNotExist:
            print ("content_title--------->",content_title)
            print ("regist fail")

            return JsonResponse({'return':'fail'})


        return JsonResponse({'return':'success'})

@csrf_exempt
def post_list(request):
    if request.is_ajax():

        id= request.POST.get('id')
        title = request.POST.get('title')
        content = request.POST.get('content')
        user_id = request.POST.get('user_id')

        print("----------------> DEBUG [s]")
        print("id = ", id)
        print("title = ", title)
        print("content = ", content)
        print("user_id = ", user_id)
        print("----------------> DEBUG [e]")

        dataAll = Post.objects.all()
        print("dataAll = ", dataAll)

        hello_list = []
        last_list = {}

        for item in dataAll:
            hello_dict = {}
            print(item.id)
            print(item.title)
            print(item.content)
            print(item.user_id)
            hello_dict['id'] = str(item.id)
            hello_dict['title'] = item.title
            hello_dict['content'] = item.content
            hello_dict['user_id'] = str(item.user_id)
            hello_list.append(hello_dict)

        return JsonResponse({'data': hello_list})


def post_ud(request):
    # obj, created = Post.objects.update_or_create(
    # title='title', content='content', defaults=updated_values)
    return render(request,'home/post_ud.html')

class IndexView(TemplateView): # TemplateView를 상속 받는다.
    template_name = 'home/login.html'