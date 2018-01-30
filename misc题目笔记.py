#遇到一小堆网页，文本，图片的那种文件夹，可以打开所有的文本搜flag或key或者key{
#misc里的莫尔斯电码图片转文本，注意空格的使用啊
1.一串数字
{{8,2,22,97,38,15,0,40,0,75,4,5,7,78,52,12,50,77,91,8},
{49,49,99,40,17,81,18,57,60,87,17,40,98,43,69,48,4,56,62,0},
{81,49,31,73,55,79,14,29,93,71,40,67,53,88,30,3,49,13,36,65},
{52,70,95,23,4,60,11,42,69,24,68,56,1,32,56,71,37,2,36,91},
{22,31,16,71,51,67,63,89,41,92,36,54,22,40,40,28,66,33,13,80},
{24,47,32,60,99,3,45,2,44,75,33,53,78,36,84,20,35,17,12,50},
{32,98,81,28,64,23,67,10,26,38,40,67,59,54,70,66,18,38,64,70},
{67,26,20,68,2,62,12,20,95,63,94,39,63,8,40,91,66,49,94,21},
{24,55,58,5,66,73,99,26,97,17,78,78,96,83,14,88,34,89,63,72},
{21,36,23,9,75,0,76,44,20,45,35,14,0,61,33,97,34,31,33,95},
{78,17,53,28,22,75,31,67,15,94,3,80,4,62,16,14,9,53,56,92},
{16,39,5,42,96,35,31,47,55,58,88,24,0,17,54,24,36,29,85,57},
{86,56,0,48,35,71,89,7,5,44,44,37,44,60,21,58,51,54,17,58},
{19,80,81,68,5,94,47,69,28,73,92,13,86,52,17,77,4,89,55,40},
{4,52,8,83,97,35,99,16,7,97,57,32,16,26,26,79,33,27,98,66},
{88,36,68,87,57,62,20,72,3,46,33,67,46,55,12,32,63,93,53,69},
{4,42,16,73,38,25,39,11,24,94,72,18,8,46,29,32,40,62,76,36},
{20,69,36,41,72,30,23,88,34,62,99,69,82,67,59,85,74,4,36,16},
{20,73,35,29,78,31,90,1,74,31,49,71,48,86,81,16,23,57,5,54},
{1,70,54,71,83,51,54,69,16,92,33,48,61,43,52,1,89,19,67,48}}
解法：
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Security.Cryptography;

namespace Test
{
    class Program
    {
        static void Main(string[] args)
        {
            int[,] a ={{8,2,22,97,38,15,0,40,0,75,4,5,7,78,52,12,50,77,91,8},
                    {49,49,99,40,17,81,18,57,60,87,17,40,98,43,69,48,4,56,62,0},
                    {81,49,31,73,55,79,14,29,93,71,40,67,53,88,30,3,49,13,36,65},
                    {52,70,95,23,4,60,11,42,69,24,68,56,1,32,56,71,37,2,36,91},
                    {22,31,16,71,51,67,63,89,41,92,36,54,22,40,40,28,66,33,13,80},
                    {24,47,32,60,99,3,45,2,44,75,33,53,78,36,84,20,35,17,12,50},
                    {32,98,81,28,64,23,67,10,26,38,40,67,59,54,70,66,18,38,64,70},
                    {67,26,20,68,2,62,12,20,95,63,94,39,63,8,40,91,66,49,94,21},
                    {24,55,58,5,66,73,99,26,97,17,78,78,96,83,14,88,34,89,63,72},
                    {21,36,23,9,75,0,76,44,20,45,35,14,0,61,33,97,34,31,33,95},
                    {78,17,53,28,22,75,31,67,15,94,3,80,4,62,16,14,9,53,56,92},
                    {16,39,5,42,96,35,31,47,55,58,88,24,0,17,54,24,36,29,85,57},
                    {86,56,0,48,35,71,89,7,5,44,44,37,44,60,21,58,51,54,17,58},
                    {19,80,81,68,5,94,47,69,28,73,92,13,86,52,17,77,4,89,55,40},
                    {4,52,8,83,97,35,99,16,7,97,57,32,16,26,26,79,33,27,98,66},
                    {88,36,68,87,57,62,20,72,3,46,33,67,46,55,12,32,63,93,53,69},
                    {4,42,16,73,38,25,39,11,24,94,72,18,8,46,29,32,40,62,76,36},
                    {20,69,36,41,72,30,23,88,34,62,99,69,82,67,59,85,74,4,36,16},
                    {20,73,35,29,78,31,90,1,74,31,49,71,48,86,81,16,23,57,5,54},
                    {1,70,54,71,83,51,54,69,16,92,33,48,61,43,52,1,89,19,67,48}};
            int max = -100000;
            for (int i = 0; i < 20; i++)
                for (int j = 0; j < 17; j++) {
                    int k = a[i, j] * a[i, j + 1] * a[i, j + 2] * a[i, j + 3];
                    if (k > max) max = k;
                }
            for (int i = 0; i < 20; i++)
                for (int j = 0; j < 17; j++)
                {
                    int k = a[j, i] * a[j + 1, i] * a[j + 2, i] * a[j + 3, i];
                    if (k > max) max = k;
                }
            for (int i = 0; i < 17; i++)
                for (int j = 0; j < 17; j++)
                {
                    int k = a[i, j] * a[i + 1, j + 1] * a[i + 2, j + 2] * a[i + 3, j + 3];
                    if (k > max) max = k;
                }
            for (int i = 19; i >2; i--)
                for (int j = 0; j < 17; j++)
                {
                    int k = a[i, j] * a[i - 1, j + 1] * a[i - 2, j + 2] * a[i - 3, j + 3];
                    if (k > max) max = k;
                }
            Console.WriteLine(max);
            Console.ReadLine();
        }
    }
}
得到IL0V3Pr0Gr4m@#!!
#空白表示
%00,%0a,%0d,%0a%0d,%0b,%0c,%a0,null,none
#图片隐写术#
################################################################################################
1． Stegsolve
a) Stegsolve打开-analyse-file format可查看相关信息
i. http://bobao.360.cn/ctf/learning/138.html web 1
b) 对于lsb图片隐藏
同样是用stegsolve打开-data extract-尝试Bit Planes-preview查看相关信息
2.对图片的微处理
A )一些文件用16进制打开后可以看出来是图片，但图片查看器缺无法打开，也许是缺少png头。加上png头后便可以打开.
B )尝试修改图片分辨率，查看flag是否被覆盖
i．http://bobao.360.cn/ctf/learning/137.html 强网杯
c ) 合并的图片文件
对于合成的图片根据文件头可分辨内容
Jpg gif89a
Png png 标志：IHDR 文件头16进制：89 50 4e 47 0d 0a 1a 0a
Rar PK
各类文件头及类型：http://ctf.idf.cn/index.php?g=&m=article&a=index&id=30
D )base64编码后的文件
Data:image/png;base64…….. Base64编码后的png图片，直接放到浏览器上回车得到图片
http://tool.chinaz.com/qrcode/
E）有些图片直接用记事本打开看不到内容，但在linux下用cat filename就会得到意想不到的结果。
3. binwalk
binwalk -e 自动导出，猥琐流啊！功能强大啊！我靠
Binwalk是一个固件的分析工具，旨在协助研究人员对固件非分析，提取及逆向工程用处。简单易用，完全自动化脚本，并通过自定义签名，提取规则和插件模块，还重要一点的是可以轻松地扩展。可用来检测是否有合并的文件。并且可以提取数据。
#使用的时候注意查看不同文件所在的开头数字，别着急，慢慢来嘛
>binwalk 2.png
>结果如下：
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 266 x 205, 8-bit/color RGBA, non-interlaced
80            0x50            Zlib compressed data, default compression, uncompressed size >= 98304
100097        0x18701         RAR archive data
说明这小小的图片还有个.rar压缩包在里面，那就用dd命令提取出来：
dd if=2.png of=2.rar bs=1 skip=100097
if=输入文件名，of=输出文件名，bs=数据块大小（bytes），skip=跳过数据块数。
原文链接：http://blog.csdn.net/shinukami/article/details/45980395 
####winhex里修改图片的长度和宽度也能实现隐写啊
4.dmp文件隐写
在线分析网站：http://www.osronline.com/page.cfm?name=analyze
Ctf地址：http://bobao.360.cn/ctf/learning/153.html
5.右键查看详情。
Linux下会看到比win多的东西。在linux下打开图片。点击细节。
还需要查看exif头等
 
6.视频隐写
fMP4及其他fmpeg可以把一帧帧的视频分割为一张张的图片。具体怎么使用可以在linux下man ffmpeg。
Avi：MSU VideoStego 
7.pdf隐写
wbStego4open
8.音频隐写
#coolpro
#Audacity
#MP3Stego
#用winhex打开文件，发现文件尾部十六进制全部都是35，用windex对文件进行xor运算，最后把文件保存为mp3格式，得到的mp3用coolpro打开，反转播放，读出的内容即为flag
#视频隐写
#### PEN_AND_APPLE
E:\a题库\三叶草极客大挑战第七季\三叶草MISC\PEN_AND_APPLE
这道题有些脑洞，不过也是一种很常见的隐写技术，后来提示与win的type命令有关，可以找到相关资料，type命令可以用于ntfs文件写入，通过工具“`alternatestreamview“`扫描文件得到如下所示
9.vmdk隐写
采用Dsfok-tools来对数据进行隐藏，通常这个工具是用来编辑vmdk文件中的描述符。
http://drops.wooyun.org/tips/12614
10.可执行文件
对于可执行文件的数据隐藏可以使用Hydan
http://drops.wooyun.org/tips/12614
11.NTFS文件系统ida隐藏
http://drops.wooyun.org/tips/12614
##有思路就去试试，说不定就成功了！
12.双图隐写--stegsolve咯
#二维码
遇到二维码先扫啊，微信，qq，浏览器，实在不行上命令行，再不行就反色，binwalk，stegsolve走一波
#gif 动态二维码 
丢到Namo GIF Animator 里，如果显示不全记得从-查看-动画属性里修改长度和宽度
#图片隐写
https://zhuanlan.zhihu.com/p/23127122 本专栏内容丰富，很长姿势
0.有时候百度google识图也能用上
winhex下jpg开头是FF D8 结尾是FF D9
winhex下png开头是89 50
1.改为txt格式，也许有flag
2.改为zip或rar格式，解压也许会有，用图片查看器更改色温，饱和度，亮度，色温等等。属性查看图片备份信息。丢到stegsolve里左右点击看看有啥东西
3.windows下用命令行stegdetect检查是否加密，JPHS破解Jphide加密
H:\ctf\StegDetect-0.4-for-Windows-master>stegdetect.exe  -tjopi -s 10.0 H9QJnHU.jpg    
或者H:\ctf\StegDetect-0.4-for-Windows-master>stegdetect -s 3.0 at.jpg
用来检测该图片用的哪种加密方式
H9QJnHU.jpg与stegdetect同目录
检测出来若为jphide加密，则使用stegbreak破解
H:\ctf\StegDetect-0.4-for-Windows-master>stegbreak -r rules.ini -f password.txt -t p  at.jpg 
必须得用这种格式，password.txt为字典 
Loaded 1 files...
at.jpg : jphide[v5](a)  a为at.jp的jphide密码
Processed 1 files, found 1 embeddings.
Time: 0 seconds: Cracks: 1,      Inf c/s 
若返回pssword中的最后一个密码，则说明破爆破失败
4.kali下binwalk查看图片内是否有藏得其他东西 
# binwalk x.png  x.png位于kali的主文件夹
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 902 x 550, 8-bit/color RGB, non-interlaced
711661        0xADBED         PNG image, 1000 x 562, 8-bit/color RGBA, non-interlaced
711752        0xADC48         Zlib compressed data, compressed, uncompressed size >= 98304
2132968       0x208BE8        Zlib compressed data, default compression, uncompressed size >= 1458
可以看出x.png里面还存在一张png的图片
然后我们可以使用dd命令分离出隐藏文件：
# dd if=x.jpg of=x-1.jpg skip=711752 bs=1

记录了1421497+0 的读入
记录了1421497+0 的写出
1421497字节(1.4 MB)已复制，5.11977 秒，278 kB/秒
输出的图片也在kali的主目录下，kali下有些图片显示不出来，可以拿到windows下查看。
可以参考 dd命令详解 ，这里if是指定输入文件，of是指定输出文件，skip是指定从输入文件开头跳过711752个块后再开始复制，bs设置每次读写块的大小为1字节 。
5.pngcheck.exe -v secret-1.png  利用pngcheck查看png是否存在IDAT异常，因为IDAT是png图片中储存图像像数数据的块
#打开word文档全选--更改字体颜色---有可能猥琐地找到flag
#MP3Stego
Decode.exe -X -P 9158753624 apple.mp3
#mp3stego爆破脚本
#coding=utf-8
import os
import subprocess
for a in open('maple.txt'):  #密码字典
    command='decode -X -P %s mp3.mp3 '% a.strip()
    print command
    p = subprocess.Popen(command, stdin = subprocess.PIPE,
    stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True)
    if "unexpected end of cipher message."not in p.communicate()[1]:
        print p.communicate()
        print command
        Break
#winhex打开先搜一波flag，key
#RGB点画二维码
文本：
255,255,255
255,0,255
.....
#coding=utf-8
from PIL import Image
import re
if __name__ == '__main__':
    x = 280 #宽
    y = 280 #高
    i = 0
    j = 0
     
    c = Image.new("RGB", (x,y))
    file_object = open('hint.txt')
     
    for i in range(0,  x):
        for j in range(0,  y):
            line = file_object.next()
            lst = line.split(",")
            c.putpixel((i, j), (int(lst[0]), int(lst[1]), int(lst[2])))
     
    c.show()
c.save("c.png")
#01画二维码

#wireshark
0.过滤http,https，等协议
1.binwalk一下，看是否藏有其他文件，如果遇到加密zip，可以winhex打开搜搜密码，或者爆破
2.wireshark打开，无需过滤，直接 文件-导出-HTTP-saveall。。。就能看见一个flag.rar
#固件分析
小伙子遇到固件分析提不要怕
binwalk -e xxx.bin 自动提取文件，进入得到的文件夹目录，发现decode.py 运行得到falg
#脚本类 

小明要参加一个高技能比赛，要求每个人都要能够快速口算四则运算，2秒钟之内就能够得到结果，但是小明就是一个小学生没有经过特殊的培训，那小明能否通过快速口算测验呢？
这一题主要是考你如何利用编程，获取算式信息并计算其结果并提交。不可能用人工口算快速得到结果的，不要被题目所迷惑。
直接上代码（我使用的是python编写）
#!/usr/bin/env python
#-*- coding:utf_8 -*-
import re
try:
    import requests
except ImportError:
    raise SystemExit('\nimport module error ,please pip install requests!')
s = requests.Session()
header = {'Cookie': 'PHPSESSID=21043f4dd0550ef63816741ae089ea7f'}
url = 'http://lab1.xseclab.com/xss2_0d557e6d2a4ac08b749b61473a075be1/index.php'
r = s.get(url, headers=header)
c = r.content
#regstr = re.compile(r'[0-9]+[*+]+[0-9]+[*+]+[0-9]+[*+]+\([0-9+]+\)')
#上面这样写的正则表达式有点啰嗦，看下面更简单的
regstr = re.compile(r'[0-9+*()]+[)]')
try:
    obj = regstr.findall(c)
    if obj:
        result = eval(obj[0])
        data = {'v':result}
        r = s.post(url,data=data,headers= header)
        print r.content
finally:
    print 'ok!!!'

#或者这样
#!/usr/bin/env python
# -*- coding: gbk -*-
# -*- coding: utf-8 -*-
# Date: 2014/11/25
# Created by 独自等待
# 博客 http://www.waitalone.cn/
import re

try:
    import requests
except ImportError:
    raise SystemExit('\n[!] requests模块导入错误,请执行pip install requests安装!')

print '\n网络信息安全攻防学习平台脚本关第2题\n'
s = requests.Session()
url = 'http://1.hacklist.sinaapp.com/xss2_0d557e6d2a4ac08b749b61473a075be1/index.php'
r = s.get(url)
res = unicode(r.content, 'utf-8').encode('gbk')
# print res

num = re.findall(re.compile(r'<br/>\s+(.*?)='), res)[0]
print '当前获取到需要口算的表达式及计算结果为:\n\n%s=%d\n' % (num, eval(num))

r = s.post(url, data={'v': eval(num)})
print re.findall(re.compile(r'<body>(.*?)</body>'), r.content)[0]
#bin文件
conf.bin 看来是路由器配置文件 
上工具 routerpassview，打开bin文件，搜索关键字-- 
	