"""NSS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Yemian import views as Yemian_views #彭鑫负责的前端页面 APP应用包
from Merchant import views as Mer_views #蒋浩负责的商家 APP应用包
from Userinformation import views as User_views #万燚炜负责的用户 APP应用包
from offer import views as offer_views #彭睿杰负责点餐 APP应用包


urlpatterns = [
    path('',Yemian_views.index), #主页面
    path('register/',User_views.register), #用户注册
    path('home/',User_views.home) #用户个人信息
    path('home/namechange/'.User_views.nameChange), #用户名修改
    path('home/topup/',User_views.topUp),   #用户充值
    path('home/pwchange/',User_views.passwordChange), #用户密码修改


    path('mer/', Mer_views.index), #商家登录注册
    path('mer/register/',Mer_views.register),  #商家注册
    path('mer/home',Mer_views.home), #商家个人
    path('mer/home/pwchange',Mer_views.pwChange), #商家密码修改
    path('mer/home/namechange',Mer_views.nameChange), #商家名字修改

    path('list/',offer_views.index), #商家列表
    path('list/dish/',offer_views.dishindex), #商家菜品列表

]
