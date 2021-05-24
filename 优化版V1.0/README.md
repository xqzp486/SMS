# 优化版简介
* 主页版本是简单的教学版，优化版将对一些点进行优化
* 并对一些难点进行介绍
## 1、使用浏览器模拟点击时，会频繁打开浏览器
**我们将对这点进行优化，具体技术设置浏览器驱动参数headless同时禁止GPU图片加载,这样就不会打开浏览器** <br/>
参考资料:微软Edge浏览器文档 <https://docs.microsoft.com/en-us/microsoft-edge/webdriver-chromium/?tabs=python>

* 需要先安装一个包
~~~python
pip install msedge-selenium-tools
~~~

* 然后导入包，并设置参数
~~~python
from msedge.selenium_tools import Edge, EdgeOptions

options = EdgeOptions()
options.use_chromium = True
options.add_argument('headless')
options.add_argument("disable-gpu")
browser = Edge(options=options)
#此时浏览器驱动已经加载完成了，我们无需再在函数中加载
#同时也无需在函数中关闭取得，统一在程序结束关闭驱动
~~~

## 2、seleniume无法定位元素
* **检查标签是否在iframe内**<br/>
如果标签在iframe内，需要先使用方法browser.switch_to.frame()，进入frame内再定位标签
~~~python
    url = 'https://www.med66.com/jibing/guzhe/'
    browser.get(url)
    register_button=browser.find_element_by_xpath('//a[@class="dzhan fl ucRegisterBtn"]')
    register_button.click()
    browser.switch_to.frame("frame1")

    input_phone_number = browser.find_element_by_xpath('//input[@class="input-box01"]')
    input_phone_number.send_keys(phone_number)
    
    sent_msg=browser.find_element_by_xpath('//a[@class="code-btn smsSend"]')
    sent_msg.click()
    time.sleep(sleep_number)
~~~

## 3、注意设置延迟
一些网站对爬虫进行方法措施，所以我们可以设置一下时间延迟，sleep几秒，这样可以避免一些错误<br/>
比如在雪球网，太快点击会触发验证码，通过sleep可以规避<br/>
比如在58同城，太快点击会导致页面元素没有加载上来，会出现无法定位元素的情况<br/>
此时我们可以通过适当的sleep来规避这些错误<br/>

## 4、优化报文头
部分网站在接受post请求以及get请求时，会对cookies进行检验
* **我们可以获取一个cookies**
~~~python
 s = requests.Session()
 s.get('主页的URL',headers = headers)
 cookies = s.cookies
 response = requests.post('接口的URL',data = data,headers = headers,cookies=cookies)
~~~
* **有时候我们无法获取到cookies，那么直接复制cookies，将cookies放入一个临时的header中**
