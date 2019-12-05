#!/usr/bin/env python
#coding=utf-8
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
import random


def send_sms(phone,code):
    client = AcsClient('LTAI4FgwWVQk9JNhULoMDzQf', 'BeJ8SWrweF7RkmP72X66Oi0VYdZtJU', 'cn-hangzhou')
# phone = '18735539128'
# dx = '65845'
    code = "{'code':%s}"%(code)
    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('dysmsapi.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https') # https | http
    request.set_version('2017-05-25')
    request.set_action_name('SendSms')

    request.add_query_param('RegionId', "cn-hangzhou")
    request.add_query_param('PhoneNumbers', "18735539128")
    request.add_query_param('SignName', "萨坦")
    request.add_query_param('TemplateCode', "SMS_178980506")
    request.add_query_param('TemplateParam', code)

    response = client.do_action(request)
    print(str(response, encoding = 'utf-8'))

#随机生成验证码:6就是6位,True表示生成有字母的，false表示不带字母
def get_code(n=6,alpha=True):
    s = ''     #创建字符串变量，存储生成的验证码
    for i in range(n):    #通过for循环控制验证码位数
        num = random.randint(0,9)    #随机生成数字0-9
        if alpha:   #需要字母验证码，不用传参数，如果不需要字母，关键字alpha=False
            upper_alpha = chr(random.randint(65,90))
            lower_alpha = chr(random.randint(97,122))
            num = random.choice([num,upper_alpha,lower_alpha])
        s = s +str(num)
    return s

if __name__ == '__main__':
    #调用下发短信方法
    send_sms('18735539128', get_code(6, False))
    print(get_code(6,False))   #打印6位数字验证码
    print(get_code(6,False))   #打印6位数字字母混合验证码