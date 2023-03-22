import urllib.request

# 下载网页
url_page = 'http://www.baidu.com'

# url代表的是下载路径，filename文件名字
# 在python中参数可以写变量名 也可以直接写值
urllib.request.urlretrieve(url_page,'baidu.html')


# 下载图片
url_image = 'https://imp.cmsk1979.com/im-admin/img/login-bg.aa0ae5c7.png'

urllib.request.urlretrieve(url_image,'logo.jpg')


# 下载视频
url_vodie = ''

urllib.request.urlretrieve(url_vodie,'dome.mp4')