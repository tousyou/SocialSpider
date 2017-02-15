# SocialSpider

1、安装python
version >2.6
2、安装pip
wget https://bootstrap.pypa.io/get-pip.py --no-check-certificate
python get-pip.py

更新pip
pip install --upgrade pip

3、安装scrapy
   yum install python-devel
   yum install openssl-devel
   pip install scrapy
4、安装依赖库
   yum install xorg-x11-server-Xvfb
   pip install pyvirtualdisplay
   pip install selenium
   yum install firefox
依赖驱动geckodriver
https://github.com/SeleniumHQ/selenium/tree/master/py/
tar zxvf geckodriver-v0.14.0-linux64.tar.gz
mv geckodriver /usr/local/bin/.
