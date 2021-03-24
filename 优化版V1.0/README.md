# 优化版简介
主页版本是简单的教学版，优化版将对以下几个点进行优化
## 1、使用浏览器模拟点击时，会频繁打开浏览器
**我们将对这点进行优化，具体技术设置浏览器驱动参数headless同时禁止GPU图片加载,这样就不会打开浏览器**

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
~~~
