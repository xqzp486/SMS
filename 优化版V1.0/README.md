# 优化版简介
* 主页版本是简单的教学版，优化版将对一些点进行优化
* 并对一些难点进行介绍
## 1、使用浏览器模拟点击时，会频繁打开浏览器
**我们将对这点进行优化，具体技术设置浏览器驱动参数headless同时禁止GPU图片加载,这样就不会打开浏览器**
参考资料:微软给出的文档 <!https://docs.microsoft.com/en-us/microsoft-edge/webdriver-chromium/?tabs=python>

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
