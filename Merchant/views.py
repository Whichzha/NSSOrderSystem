from django.shortcuts import render,HttpResponse
from Merchant import models
import hashlib
import json

# Create your views here.

def index(request): #商家登录注册页面
    return render(request,'Merchant.html')

def home(request):
    merUsername = request.post.get('id')
    mid = getMerchantId(merUsername)
    if mid == 0:
        webBoxPrint("商家名不存在!")
    elif mid == -1:
        webBoxPrint("SQL Error!")
    else:
        flag = getMerchantMenu(mid)
        if flag == -1:
            webBoxPrint("ID不存在")
        elif flag == -2:
            webBoxPrint("SQL Error!")
        else:
            return #菜单

def pwChange(mid):
    flag = updateMerchantPassword(mid,newPassword)
    if flag == 1:
        webBoxPrint("密码修改成功")
    elif flag == 2:
        webBoxPrint("商家不存在")
    else:
        webBoxPrint("SQL Error!")

def namechange(mid):
    flag = updateMerchantName(UID,NewMerchantName)
    if flag == 1:
        webBoxPrint("商家名字修改成功")
    elif flag == 2:
        webBoxPrint("商家不存在")
    else:
        webBoxPrint("SQL Error!")

    






'''
def get_md5(str): #商家密码加密
    md5 = hashlib.md5()
    md5.update(str.encode('utf-8'))
    return md5.hexdigest()

def register(request): #商家注册 
    print('register')
    Mid = 0 #注册信息初始化,Mid = 0 为未成功，>0为成功, -1 为数据库错误
    if not request.method == 'POST':
        return HttpResponse(json.dumps({'code': 0, 'msg': '请求类型错误'}), content_type="application/json")

    datas = json.loads(request.body)
    merUsername = datas["username"]
    merPassword = datas["password"]
    err = None

    if len(merUsername) > 20 or len(merPassword) > 20:
        err = '用户名或者密码长度过长'
    if len(merUsername) < 8 or len(merPassword) < 8:
        err = '用户名或密码长度过短（不应短于8位）'

    # 报错信息
    if not err == None:
        return HttpResponse(json.dumps({'code': 0, 'msg': err}), content_type="application/json")

    #密码储存在数据库
    md5pw = get_md5(merPassword)#[0:20]

    try:
        Mid = insertMerchant(merUsername,md5pw)
    except:
        return HttpResponse("未知错误！")

    if Mid == -1:
        return HttpResponse("数据库错误")
    elif Mid == 0:
        return HttpResponse("商家名字已存在")
    elif Mid > 0:
        print("注册成功！")
        return mid

    return Mid
'''
