# crawler
collect images from internet
## platform
this code runs on ubuntu
## prepare
1. install Chrome and a corresponding Chrome driver. We can check the Chrome version by:
```angular2html
google-chrome --version
chromedriver -version
```
2. install the chrome driver by:
```angular2html
sudo chmod +x chromedriver
sudo mv chromedriver  /usr/bin/
```
3. install depending packages:
```angular2html
sudo apt-get install xvfb -y
 
pip install selenium
 
pip install pyvirtualdisplay
```

## last step
we can run the testcode, if it works fine, it means we can run the crawler to do our jobs.

## reference
```angular2html
https://blog.csdn.net/sxf1061700625/article/details/122801988
https://blog.csdn.net/Lyn_B/article/details/107461556
```