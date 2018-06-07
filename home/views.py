from django.shortcuts import render
from django.http import JsonResponse
from home.models import User
from django.views.decorators.csrf import csrf_exempt


# model user

def home(request):

    return render(request, 'home/home.html', {})

@csrf_exempt
def login(request):

    print("ss");

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
        print ("reg--------->",reg)


        return JsonResponse({'return':'success'})

def logout(request):

    if 'user_id' in request.session:
        del request.session['user_id']

    return render(request, 'home/logout.html',{})

def file(request):
    return render(request,'home/file.html')
