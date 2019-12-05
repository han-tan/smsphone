
from django.shortcuts import render
from django.http import request
from django.http.response import HttpResponse, JsonResponse
#导入缓存对象
from django.core.cache import cache
from utils import aliyunsms, restful
import json
from utils.restful import result
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url

from django.core.mail import send_mail  
from utils.forms import RegisterForm

# 首页显示验证码
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
def index(request):
    #跳转页面时,初始化图文验证码表单项,传递到index页面
    hashkey = CaptchaStore.generate_key()
    image_url = captcha_image_url(hashkey)
    register_form = RegisterForm()
    return render(request, 'index.html',locals())
    

#测试Redis存储
def test_redis(request):
    #使用缓存对象,操作Redis
    cache.set('name','tom',60) #存
    print(cache.has_key('name'))#判断
    print(cache.get('name'))#获取
    
    return HttpResponse("测试Redis")
 
# 发送短信
def send_sms(request):
    #接口地址:/duanxin/send_sms/?phone=xxxx
    # 1 获取手机
    phone = request.GET.get('phone')
    print('手机:'+phone)
    # 2 生成6位随机码
    code = aliyunsms.get_code(6, False)
    # 3 缓存到redis
    cache.set(phone,code,30*60)#60s有效
    print('是否写入redis成功:',cache.has_key(phone))
    print('打印code:',cache.get(phone))
    # 4 发短信
    result =aliyunsms.send_sms(phone, code)
    return HttpResponse(result)
 
#短信验证
def  check_sms(request):
    #/duanxin/check_sms/?phone=xxx&code=xx
    # 1 后去电话和code
    phone = request.GET.get('phone')
    code = request.GET.get('code')
    # 2 获取Resis中code
    cache_code = cache.get(phone)
    # 3 判断
    if code == cache_code:
        return  restful.ok("OK", data=None)
    else:
        return restful.page_error("False", data=None)





















    
