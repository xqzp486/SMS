# 短信轰炸程序解析
该教程以Python为例介绍了两种常用的短信轰炸方式

# 方法一：调用网站的短信接口
该方法的本质是调用了网站发送短信的接口，模拟了一个HTTP请求（即模拟一个post或者一个get请求）
## 准备requests包
pip命令下载所需的requests包 
~~~ python
pip install requests

