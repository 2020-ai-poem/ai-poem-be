from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from .models import userData
import random,json,requests
from django.core.mail import send_mail

session = requests.Session()
# Create your views here.
@csrf_exempt
def email_check(request):
  resData = {'isOk': False, 'errmsg': '未知错误'}
  print(request.POST)
  if request.method == 'POST':
    email = request.POST.get('email')
    print(email)
    if userData.objects.filter(email = email):
      resData['errmsg']='该邮箱已注册'
    else:
      number = str(random.randrange(1000, 9999))
      send_mail('AI写诗邮箱验证', '您的验证码为'+number+'若非本人请忽略。', 'shuaipoem@163.com',
                [email], fail_silently=False)
      resData['number'] = number
      resData['isOk'] = True
    jsonData = json.dumps(resData)
    return HttpResponse(jsonData,content_type="application/json")

@csrf_exempt
def sign_up(request):
  resData = {'isOk': False, 'errmsg': '未知错误'}
  print(request.POST)
  if request.method == 'POST':
    print(request.POST)
    email = request.POST.get('email')
    print(email)
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username,password)
    if userData.objects.filter(username=username):
      resData['errmsg'] = '该用户名已存在'
    else:
      usernow = userData.objects.create(
        username=username,
        email=email,
        password=password,
      )
      print(usernow)
      resData['isOk'] = True
    jsonData = json.dumps(resData)
    return HttpResponse(jsonData,content_type="application/json")

@csrf_exempt
def sign_in(request):
  res_data = {'isOk': False, 'errmsg': '未知错误'}
  if request.method == 'POST':
    info = request.POST.get('info')
    password = request.POST.get('password')
    print(info,password)
    email = userData.objects.filter(email=info)
    if email.exists():
      usernow = email[0]
      if usernow.password == password:
        request.session['userid'] = usernow.id
        res_data['userId'] = usernow.id
        res_data['email'] = usernow.email
        res_data['userName'] = usernow.username
        res_data['birthDate'] = usernow.birthData
        res_data['age'] = usernow.age
        res_data['sex'] = usernow.gender
        res_data['isOk'] = True
      else:
        res_data['errmsg'] = '密码错误'
    else:
      usename = userData.objects.filter(username=info)
      if usename.exists():
        usernow = usename[0]
        if usernow.password == password:
          request.session['userid'] = usernow.id
          res_data['userId'] = usernow.id
          res_data['email'] = usernow.email
          res_data['userName'] = usernow.username
          res_data['birthDate'] = usernow.birthData
          res_data['age'] = usernow.age
          res_data['sex'] = usernow.gender
          res_data['isOk'] = True
        else:
          res_data['errmsg'] = '密码错误'
      else:
        res_data['errmsg'] = '用户名或邮箱错误'
    print(res_data)
    jsonData = json.dumps(res_data)
    return HttpResponse(jsonData,content_type='application/json')

@csrf_exempt
def modify_info(request):
    res_data = {'isOk': False, 'errmsg': '未知错误'}
    if request.method == 'POST':
        userid = request.session.get('userid')
        print(userid)
        if userid:
            usernow = userData.objects.get(id = userid)
            username = request.POST.get('userName',usernow.username)
            password = request.POST.get('password',usernow.password)
            gender = request.POST.get('sex',usernow.gender)
            age = request.POST.get('age',usernow.age)
            birthData = request.POST.get('birthDate',usernow.birthData)
            email = request.POST.get('email',usernow.email)
            if username != usernow.username:
                usernameTest = userData.objects.filter(username=username)
                if usernameTest.exists():
                    res_data['errmsg'] = '该用户名已存在'
                    jsonData = json.dumps(res_data)
                    return HttpResponse(jsonData, content_type='application/json')
            usernow.username = username
            usernow.password = password
            usernow.gender = gender
            usernow.age = age
            usernow.birthData = birthData
            usernow.email = email
            usernow.save()
            res_data['isOk'] = True
        else: res_data['errmsg'] = "请先登录"
        jsonData = json.dumps(res_data)
        return HttpResponse(jsonData, content_type='application/json')

@csrf_exempt
def sign_out(request):
    res_data = {'isOk': False, 'errmsg': '未知错误'}
    if request.method == 'POST':
        userid = request.session.get('userid')
        print(userid)
        if userid:
            res_data['isOk'] = True
            request.session['userid'] = ''
    jsonData = json.dumps((res_data))
    return HttpResponse(jsonData,content_type='application/json')

@csrf_exempt
def get_userinfo(request):
    res_data = {'isOk': False, 'errmsg': '未知错误'}
    if request.method == 'POST':
        userid = request.session.get('userid')
        if userid:
            usernow = userData.objects.get(id=userid)
            res_data['email'] = usernow.email
            res_data['userName'] = usernow.username
            res_data['userId'] = usernow.id
            res_data['age'] = usernow.age
            res_data['sex'] = usernow.gender
            res_data['birthDate'] = usernow.birthData
            res_data['isOk'] = True
        else:
            res_data['errmsg'] = '请先登录'
    jsonData = json.dumps((res_data))
    return HttpResponse(jsonData, content_type='application/json')
