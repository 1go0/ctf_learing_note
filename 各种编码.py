0.md5(ֻ��������(0-9)����ĸ��a-f��,����Ϊ16��32)
ע�ⳤ�ȣ��ַ����滻
#utf-7
	���ģ�+/v+ +ADwAcwBjAHIAaQBwAHQAPgBhAGwAZQByAHQAKAAiAGsAZQB5ADoALwAlAG4AcwBmAG8AYwB1AHMAWABTAFMAdABlAHMAdAAlAC8AIgApADwALwBzAGMAcgBpAHAAdAA+AC0-

	+Axxxxxxxxx- �� UTF-7 ����������ʽ������ֻȡ+ADwAcwBjAHIAaQBwAHQAPgBhAGwAZQByAHQAKAAiAGsAZQB5ADoALwAlAG4AcwBmAG8AYwB1AHMAWABTAFMAdABlAHMAdAAlAC8AIgApADwALwBzAGMAcgBpAHAAdAA+AC0-
	����õ�<script>alert("key:/%nsfocusXSStest%/")</script>-
http://toolswebtop.com/text/process/decode/UTF-7
00.Windows hash
	��������
	nick:1003:8EA9109FDA91D6BFC6EBE8776A153FEB:C6002D00F57F9F399B6263D714AF8C3A:::
	Tips��LMHASH��NTHASH��Ophcrack��֪����windows��hash����
	Windowsϵͳ�µ�hash�����ʽΪ���û�����:RID:LM-HASHֵ:NT-HASHֵ�����磺
	nick:1003:8EA9109FDA91D6BFC6EBE8776A153FEB:C6002D00F57F9F399B6263D714AF8C3A:::
	8EA9109FDA91D6BFC6EBE8776A153FEB:C6002D00F57F9F399B6263D714AF8C3A������������
	�û�����Ϊ��nick
	RIDΪ��1003
	LM-HASHֵΪ��8EA9109FDA91D6BFC6EBE8776A153FEB
	NT-HASHֵΪ��C6002D00F57F9F399B6263D714AF8C3A
	��http://www.objectif-securite.ch/en/ophcrack.php���ܵ�passwdΪhacker521����½���ܵõ�flag
1.ASCII����
	ASCII������¿��Է�����������ɣ�
	��һ�����ǣ�ASCII�Ǵ�ӡ�����ַ�������ASCII�����0-31��;
	�ڶ������ǣ�ASCII��ӡ�ַ���Ҳ����CTF�г��õ���ת��;
#����/����һ����ά����ɨ��һ������
	45 46 45 46 32 45 32 46 46 45 46 32 46 45 46 46 32 46 46 46 32 45 46 46 46 32 46 46 45 45 46 45 32 45 46 46 46 32 46 46 46 32 46 45 46 46 32?
	����������ascii������ascii�����õ�����Щ��
	EFEF2E2FFEF2FEFF2FFF2EFFF2FFEEFE2EFFF2FFF2FEFF2
	�����2�����ǶϿ�����ô�͵õ�
	EFEF
	E
	FFEF
	FEFF
	FFF
	EFFF
	FFEEFE
	EFFF
	FFF
	FEFF
	����������Ħ˹��ɣ�E�ǡ���F��.        ���ǽ��ܾ͵õ�CTFnullSBnullBSL
2.Base64/32/16����
	����ԭ��Base64����Ҫ���3��8λ�ֽ�ת��Ϊ4��6λ���ֽڣ�֮����6λ��ǰ�油����0���γ�8λһ���ֽڵ���ʽ��6λ2�����ܱ�ʾ���������2��6�η���64��
	��Ҳ��Ϊʲô��64���ַ�(A-Z,a-z��0-9��+��/��64�������ַ���=�Ų����ڱ����ַ�����������ַ�)��ԭ��
	Key1һ�����Ǳ�׼��baseȫ��Ͱ��but ����base64����������밡��base32���ǽⲻ�����������漰��python�﷨��http://zhidao.baidu.com/link?url=d4lCkOsTA0RmtoKdb_-9DI2mnmPIJWPoWMvoL-jRANYzq4cZp1wPPw1yvviZo2jeY6Ki8Ds8B4834YShiTlmr_��
	>>> a = 'DaoChangcloud01'
	>>> import base64
	>>> b = base64.b32encode(a)
	>>> print b
	IRQW6Q3IMFXGOY3MN52WIMBR
	>>> c = base64.b32decode(b, True)
	>>> print c
	DaoChangcloud01
	>>> c1='IRQW6Q3IMFXGOY3MN52WIMBr' #�������һ����ĸ�ĳ�Сд����
	>>> base64.b32decode(c1, True)
	'DaoChangcloud01'
	>>> base64.b32decode(c1, False)
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	  File "D:\Python26\lib\base64.py", line 222, in b32decode
		raise TypeError('Non-base32 digit found')
	TypeError: Non-base32 digit found
	����decod����Comeon2012baby �ύ��õ�key2 :2tHEWinNer
3.shellcode����
#!shell
\x54\x68\x65\x7f\x71\x75\x69\x63\x6b\x7f\x62\x72\x6f\x77\x6e\x7f\x66\x6f\x78\x7f\x6a\x75\x6d\x70\x73\x7f\x6f\x76\x65\x72\x7f\x74\x68\x65\x7f\x6c\x61\x7a\x79\x7f\x64\x6f\x67
4.Quoted-printable ����
#!shell
=E6=95=8F=E6=8D=B7=E7=9A=84=E6=A3=95=E8=89=B2=E7=8B=90=E7=8B=B8=E8=B7=B3=E8
=BF=87=E4=BA=86=E6=87=92=E6=83=B0=E7=9A=84=E7=8B=97
5.XXencode����
����ѡ��Ŀɴ�ӡ�ַ��ǣ�+-0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz��һ��64���ַ�����base64��ӡ�ַ���ȣ�����XXencode��һ����-�� �ַ�����һ����/�� �ַ���
6.UUencode����
UUencode�������Ľ���պ�����ASCII�ַ����пɴ�ӡ�ַ���32-�հס�95-���ߣ�\
Դ�ı��� The quick brown fox jumps over the lazy dog
����� M5&AE('%U:6-K(&)R;W=N(&9O>"!J=6UP<R!O=F5R('1H92!L87IY(&1O9PH*
7.URL����
�ڸ��ֽ�ascii��ĵ�16�����ַ�ǰ���%. �� �ո��ַ���ascii����32����Ӧ16������'20'����ôurlencode��������:%20��
#!shell
%54%68%65%20%71%75%69%63%6b%20%62%72%6f%77%6e%20%66%6f%78%20%6a%75%6d%70%73%20%6f%76%65%72%20%74%68%65%20%6c%61%7a%79%20%64%6f%67
8.Unicode����
���������ֱ��뷽ʽ
Դ�ı��� The
&#x [Hex]�� &#x0054;&#x0068;&#x0065;
&# [Decimal]�� &#00084;&#00104;&#00101;
\U [Hex]�� \U0054\U0068\U0065
\U+ [Hex]�� \U+0054\U+0068\U+0065
9.Escape/Unescape����
	Escape/Unescape���ܽ���/�������,�ֽ�%u���룬����UTF-16BEģʽ�� Escape����/����,�����ַ���ӦUTF-16 16���Ʊ�ʾ��ʽǰ���%u��Unescape����/���ܣ�����ȥ��"%u"�󣬽�16�����ַ���ԭ����utf-16ת�뵽�Լ�Ŀ���ַ����磺�ַ����С���UTF-16BE�ǣ���6d93�������Escape�ǡ�%u6d93����
	Դ�ı��� The
	����� %u0054%u0068%u0065
10.HTMLʵ�����
	���http://www.w3school.com.cn/tags/html_ref_entities.html
11.�û���
	�û���(Tap code)��һ���Էǳ��򵥵ķ�ʽ���ı���Ϣ���б���ķ�������ñ������Ϣͨ��ʹ��һϵ�еĵ��������������������û����ǻ���5��5�������Ȱ�˹������ʵ�ֵģ���ͬ��������K��ĸ�����ϵ�C�С�
	�û����:
	#!shell
	  1  2  3  4  5
	1 A  B C/K D  E
	2 F  G  H  I  J 
	3 L  M  N  O  P
	4 Q  R  S  T  U
	5 V  W  X  Y  Z
12.Ī��˹����
	Ħ��˹����(Morse Code)�������������Ѷ���Ħ��˹��1836�귢����һ��ʱͨʱ�ϵ���ͨ����ͬ������˳������ﲻͬӢ����ĸ�����ֺͱ����ŵ��źŴ��룬Ħ��˹������Ҫ������5�����Ĵ�����ɣ�

	�㣨.��
	����-��
	ÿ���ַ���̵�ͣ�٣�ͨ���ÿո��ʾͣ�٣�
	ÿ����֮���еȵ�ͣ�٣�ͨ���� / ���֣�
	�Լ�����֮�䳤��ͣ��
	Ħ��˹������ĸ�����ֶ�Ӧ��
	#!shell
	A  .-    N  -.    .  .-.-.-  +  .-.-.    1  .----
	B  -...  O  ---   ,  --..--  _  ..--.-   2  ..---
	C  -.-.  P  .--.  :  ---...  $  ...-..-  3  ...--
	D  -..   Q  --.-  "  .-..-.  &  .-...    4  ....-
	E  .     R  .-.   '  .----.  /  -..-.    5  .....
	F  ..-.  S  ...   !  -.-.--              6  -....
	G  --.   T  -     ?  ..--..              7  --...
	H  ....  U  ..-   @  .--.-.              8  ---..
	I  ..    V  ...-  -  -....-              9  ----.
	J  .---  W  .--   ;  -.-.-.              0  -----
	K  -.-   X  -..-  (  -.--.           
	L  .-..  Y  -.--  )  -.--.-          
	M  --    Z  --..  =  -...-
��-��-��-��-��- ������˼�ǵ����źţ���ʾ��������Ϣ���͡�
#�û���
�û���(Tap code)��һ���Էǳ��򵥵ķ�ʽ���ı���Ϣ���б���ķ�������ñ������Ϣͨ��ʹ��һϵ�еĵ��������������������û����ǻ���5��5�������Ȱ�˹������ʵ�ֵģ���ͬ��������K��ĸ�����ϵ�C�С�
#�����ı�����
�ı����ܿ��Խ������ı����ݴ���Ϊ�������������ֻ����(���� ���� ��ĸ ���ַ��� �������� ä�� ���� ���� ���� ���� ��ͷ���� ������� ����)�����еȸ�ʽ��ϢҲ�ᱻ������ﵽ���ܵ����á��ڽ����ı�����ʱ�����趨һ�����룬����ֻ��֪��������˲��ܽ����ı���������������֡���ĸ���»��ߣ�����λ��
http://www.qqxiuzi.cn/bianma/wenbenjiami.php
���� ���ģ��Ұ���
     ���ģ���������֤��==
	 ���ģ��Ұ���
	 ���ģ�???��?�L??==
�û����:

#!shell
  1  2  3  4  5
1 A  B C/K D  E
2 F  G  H  I  J 
3 L  M  N  O  P
4 Q  R  S  T  U
5 V  W  X  Y  Z
	
000000000000��λ����
1.դ������
		դ������(Rail-fence Cipher)���ǰ�Ҫ���ܵ����ķֳ�N��һ�飬Ȼ���ÿ��ĵ�1���ַ���ϣ�ÿ���2���ַ����...ÿ��ĵ�N(���һ��������ܲ���N��)���ַ���ϣ���������ȫ�����������������ģ�������2��դ������Ϊ����
	���ģ� The quick brown fox jumps over the lazy dog
	ȥ�ո� Thequickbrownfoxjumpsoverthelazydog
	���飺 Th eq ui ck br ow nf ox ju mp so ve rt he la zy do g
	��һ�飺 Teucbonojmsvrhlzdg
	�ڶ��飺 hqikrwfxupoeteayo
	���ģ� Teucbonojmsvrhlzdghqikrwfxupoeteayo1
	�ӽ��� ������
2.��·����(Curve Cipher)��һ�ֻ�λ���룬��Ҫ����˫��Լ����Կ(Ҳ������··��)��
	���ģ� The quick brown fox jumps over the lazy dog
	����5��7�б�(����Լ������������)
3.����λ����
	������˼~~������������
000000000000�滻����
1.���ذ�ʲ��
	���ذ�ʲ��(Atbash Cipher)��һ������ĸ����������Ϊ������Կ���滻���ܣ�Ҳ��������Ķ�Ӧ��ϵ��
	ABCDEFGHIJKLMNOPQRSTUVWXYZ
	ZYXWVUTSRQPONMLKJIHGFEDCBA
	���ģ� the quick brown fox jumps over the lazy dog
	���ģ� gsv jfrxp yildm ulc qfnkh levi gsv ozab wlt
	�ӽ��� http://www.practicalcryptography.com/ciphers/classical-era/atbash-cipher/
2.��������
	��������(Caesar Cipher����������ܡ������任���任���ܡ�λ�Ƽ���)��һ���滻���ܣ������е�������ĸ������ĸ������󣨻���ǰ������һ���̶���Ŀ����ƫ�ƺ��滻�����ġ�������ƫ������3��ʱ�����е���ĸA�����滻��D��B���E���Դ����ƣ����� �ο� ��
	�ӽ���http://planetcalc.com/1434/
	Ҳ��ʹ����˹�ص�С����Ŷ~~
3.ROT5/13/18/47
	ROT5/13/18/47��һ�ּ򵥵���Ԫλ��˳���滻���롣���������п����ԣ��������ҽ��ܣ���Ҫ����Ӧ�Կ�������������ǻ����Ķ�ȡ��
	ROT5 �� rotate by 5 places �ļ�д����˼����ת5��λ�ã�������ͬ������ֱ�˵˵���ǵı��뷽ʽ��
	ROT5��ֻ�����ֽ��б��룬�õ�ǰ������ǰ���ĵ�5�������滻��ǰ���֣����統ǰΪ0���������5����ǰΪ1���������6���Դ�����˳��ѭ����
	ROT13��ֻ����ĸ���б��룬�õ�ǰ��ĸ��ǰ���ĵ�13����ĸ�滻��ǰ��ĸ�����統ǰΪA���������N����ǰΪB���������O���Դ�����˳��ѭ����
	ROT18������һ�����࣬����û�У����ǽ�ROT5��ROT13�����һ��Ϊ�˺óƺ�����������ΪROT18��
	ROT47�������֡���ĸ�����÷��Ž��б��룬�������ǵ�ASCIIֵ����λ���滻���õ�ǰ�ַ�ASCIIֵ��ǰ���ĵ�47λ��Ӧ�ַ��滻��ǰ�ַ������統ǰΪСд��ĸz��������ɴ�д��ĸK����ǰΪ����0��������ɷ���_������ROT47������ַ���ASCIIֵ��Χ��33��126������ɲο�ASCII���룬������rot13������
	���ģ� the quick brown fox jumps over the lazy dog	
	���ģ� gur dhvpx oebja sbk whzcf bire gur ynml qbt
	�ӽ���http://www.qqxiuzi.cn/bianma/ROT5-13-18-47.php
4.���滻����
	�򵥻�λ����(Simple Substitution Cipher)���ܷ�ʽ����ÿ��������ĸ����֮Ψһ��Ӧ�Ҳ�ͬ����ĸ�滻�ķ�ʽʵ�ֵģ�
	����ͬ���������룬��Ϊ������ĸ�����ĸ���Ǽ򵥵���λ��������ȫ�ǻ��ҵġ� ���磺
	#!shell
	������ĸ : abcdefghijklmnopqrstuvwxyz
	������ĸ : phqgiumeaylnofdxjkrcvstzwb
	���ģ� the quick brown fox jumps over the lazy dog
	���ģ� cei jvaql hkdtf udz yvoxr dsik cei npbw gdm
	��2���ƽ�
	�����������㹻��ʱ�����������ǿ���ͨ����Ƶ���������ƽ�����������ƽ⣬
	�ȽϺõ����ߴ�Ƶ������վ http://quipqiup.com/index.php (��= =ǽ)��
	�����Ƽ�һƪͨ��"��ɽ�㷨"���ƽ���滻���� ���� ���������е��㷨ʵ�ֵĹ������ƽ�ʾ����
5.ϣ������--����������Դ�����
	���� http://www.practicalcryptography.com/ciphers/hill-cipher/
#ϣ������
���ģ� 22,09,00,12,03,01,10,03,04,08,01,17 ��c��
ʹ�õľ����� 1 2 3 4 5 6 7 8 10
������Ľ���.
һ��ϣ������ ����ʵʵд��Python����
#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Url__ = 'Http://www.purpleroc.com'
__author__ = 'Tracy_����'
from numpy import *
Dic = {chr(i+97):i for i in range(26)}
def decode(pwd, org):
    temp = []
    result = []
    while True:
        if len(pwd) % 3 != 0:
            pwd.append(pwd[-1])
        else:
            break
    for i in pwd:
        temp.append(Dic.get(i))
    temp = array(temp)
    temp = temp.reshape(len(pwd)/3, 3)
    #print temp
    #print org
    xx = matrix(temp)*org
    for j in range(len(pwd)/3):
        for i in range(3):
            if (int(xx[j, i]) >= 26):
                result.append(chr(xx[j, i] % 26 + 97))
                #print xx[j, i] % 26
            else:
                #print xx[j, i]
                result.append(chr(xx[j, i] + 97))
    return result
def get_vmatrix(org):
    org_adjoin = org.I*linalg.det(org)
    print org_adjoin
    org_det = int(str(abs(linalg.det(org))).split('.')[0])
    print org_det
    for i in range(1, 26):
        if i * org_det % 26 == 1:
            break
    org_mod = -org_adjoin * i % 26
    org_mod = matrix(org_mod)
    temp = []
    for i in range(org_mod.shape[0]):
        for j in range(org_mod.shape[1]):
            temp.append(int(str(org_mod[i, j]).split('.')[0]))
    org_final = matrix(temp).reshape(org_mod.shape[0], org_mod.shape[1])
    #print org_final
    return org_final
if __name__ == '__main__':
    ''' for test
    pwd = list("act")
    org = matrix(array([[6, 24, 1], [13 , 16, 10], [20, 17, 15]]))
    result = decode(pwd, org)
    print "".join(result)
    deorg = matrix(array([[8, 5, 10], [21 , 8, 21], [21, 12, 8]]))
    result = decode(result, deorg)
    print "".join(result)
    '''
    pwd = "wjamdbkdeibr" #����
    pwd = list(pwd)
    org = matrix(array([[1,2,3],[4,5,6],[7,8,10]])) #���ܾ���
    org_vm = get_vmatrix(org)
    print org_vm
    print "Your flag is :" + "".join(decode(pwd, org_vm))
	

6.��Ȧ����(Pigpen Cipher��ƾŹ������롢������롢���û�����򹲼û�Ա����)����һ���Ը���Ϊ�����ļ����ʽ���롣����ʹ����˹��С�������ԣ�������еĻ�������������������
7.VBscript.Encode http://adophper.com/encode.html
#@~^TgAAAA=='[6*liLa6++p'aXvfiLaa6i[[avWi[[a*p[[6*!I'[6cp'aXvXILa6fp[:6+Wp[:XvWi[[6+XivRIAAA==^#~@ 
������֮��������
&#x45;&#x6e;&#x63;&#x6f;&#x64;&#x65;&#x40;&#x64;&#x65;&#x63;&#x6f;&#x64;&#x65; 
�������ҳ�õ�һ�ֲ��������Ķ���������̨�ɽ⣬���о��Ƿ������ٶ�Ҳ���Զ�ת��ascii
����̨document.write("&#x45;&#x6e;&#x63;&#x6f;&#x64;&#x65;&#x40;&#x64;&#x65;&#x63;&#x6f;&#x64;&#x65;")������
8.
#С��ĳһ���յ�һ�����ţ�����д�˼�����ͬ����ݣ���î�����ȣ����磬��δ�����������ϣ���î�����ȡ��ŵı��滹д�С�+���ӡ�������������ġ�keyֵ��CTF{XXX}
����Ŀ����֪���� ����֧�� + ���ӣ�60����= ���֣�ascii��-->��Ӧ����ĸ
��î��Ϊ��֧֮һ��˳��Ϊ��28�� --> 88 -->  X
���ȣ�Ϊ��֧֮һ��˳��Ϊ��30�� --> 90 -->  Z
���磬Ϊ��֧֮һ��˳��Ϊ��23�� --> 93 -->  S
��δ��Ϊ��֧֮һ��˳��Ϊ��8�� --> 68 -->  D
������Ϊ��֧֮һ��˳��Ϊ��17�� --> 77 -->  M
���ϣ�Ϊ��֧֮һ,˳��Ϊ��10�� --> 70 -->  F
��î��Ϊ��֧֮һ��˳��Ϊ��16�� --> 76 -->  L
���ȣ�Ϊ��֧֮һ��˳��Ϊ��30�� --> 90 -->  Z
�ŵ����룬�������ַ���Ϊ�� XZSDMFLZ
�ŵ������Ի�λ���滻Ϊ�������Գ����Ĺŵ����룺��λդ�����滻������
��������������ϣ�û��һ����ʾ�������Ρ�����
���ȣ�դ�����루������--> ���ܣ�XMZFSLDZ
���ÿ��� --> ���ܣ�SHUANGYU
#
0x1 ����ķ����
����ķ������ʵ��һ���ɶ����Ʋ������滻���롣
����һ�ֶ�ս�ڼ�¾�ʹ�õ����룬һʱ���˾��������룬
��ԭ����Ҫ�ǰѶ���������ÿ7λ�ֳ�һ�飬�ٺ���Կ��ÿһλ��򼴿ɵõ�
import re

key = 'large'
s = '00000100001000001101000001100001010'
key = list(key)
s = re.findall('.{7}',s) 
flag = ''
for i in range(len(s)):
    flag += chr(ord(key[i]) ^ int(s[i],2))
 
print flag
 
0x2 ����˹�ر���Ͳ������˹�ر���
������˹�ر����У�ÿһλ���м���һ���䣬λ�м���������ʱ���źţ����������źţ��Ӹߵ��������ʾ"1"���ӵ͵��������ʾ"0"������һ���ǲ������˹�ر��룬ÿλ�м��������ṩʱ�Ӷ�ʱ������ÿλ��ʼʱ���������ʾ"0"��"1"��������Ϊ"0"��������Ϊ"1"��
http://www.cnblogs.com/BinB-W/p/5045918.html
#!/usr/bin/env python      
#coding:utf-8
import re 
hex1 = 'AAAAA56A69AA55A95995A569AA95565556' # #  0x8893CA58
#hex1 = 'AAAAA56A69AA556A965A5999596AA95656'
def bintohex(s1):
    s2 = ''
    s1 = re.findall('.{4}',s1)
    print 'ÿһ��hex�ָ�:',s1
    for i in s1:
        s2 += str(hex(int(i,2))).replace('0x','')
 
    print 'ID:',s2
def diffmqst(s):
    s1 = ''
    s = re.findall('.{2}',s)
    cc = '01'
    for i in s:
        if i == cc:
            s1 += '0'
        else:
            s1 += '1'
        cc = i  # ��ּ���cc = i
    print '�������˹�ؽ���:',s1
    bintohex(s1)
def mqst(s):  #ֻ��������˹�ر���,�޷�����
    mdict = {'5': '00', '6': '01', '9': '10', 'A': '11'}
    a1 = ''.join(mdict[i] for i in s)
    a2 = ''.join(mdict[i][::-1] for i in s)
    print '����˹�ؽ���:   ',a1 
    print '����˹�ؽ���2:  ',a2
    bintohex(a1)
    bintohex(a2)
if __name__ == '__main__':
    bin1 = bin(int(hex1,16))[2:]
    diffmqst(bin1)
 
    mqst(hex1)
 
0x3 �������� Wheel Cipher

Ҳ�Ƕ�ս�ڼ��ʹ�õ�һ�����룬ԭ���ž��Ǹ���һ��������һ����Կ��������Կ��ÿһ����ת����һλ��������һ������ Ȼ��ÿһ�е��ַ��Ƿ��й���
��ISCC2017�Ͼ�������һ����, �ű�����:

#coding:utf-8
a ="""
ZWAXJGDLUBVIQHKYPNTCRMOSFE
KPBELNACZDTRXMJQOYHGVSFUWI
BDMAIZVRNSJUWFHTEQGYXPLOCK
RPLNDVHGFCUKTEBSXQYIZMJWAO
IHFRLABEUOTSGJVDKCPMNZQWXY
AMKGHIWPNYCJBFZDRUSLOQXVET
GWTHSPYBXIZULVKMRAFDCEONJQ
NOZUTWDCVRJLXKISEFAPMYGHBQ
XPLTDSRFHENYVUBMCQWAOIKZGJ
UDNAJFBOWTGVRSCZQKELMXYIHP
MNBVCXZQWERTPOIUYALSKDJFHG
LVNCMXZPQOWEIURYTASBKJDFHG
JZQAWSXCDERFVBGTYHNUMKILOP
"""
 
b="NFQKSEVOQOFNP"
c="2,3,7,5,13,12,9,1,8,10,4,11,6"
a=a.splitlines()
a.pop(0)
# print a
s = ''
t = []
c=c.split(',')
for i in range(0,len(c)):
    #print a[int(c[i])-1].index(b[i])+1
    index = a[int(c[i])-1].index(b[i])
    a[int(c[i])-1] = a[int(c[i])-1][index:]+a[int(c[i])-1][:index]
    print a[int(c[i])-1]
    t.append(a[int(c[i])-1])
    # print '����',i,'��',int(c[i])-1
 
for y in range(len(t[0])):
    for x in range(0,len(t)):
        s += t[x][y]
 
    print '��'+str(y)+'��',''.join(s)
 
    s = ''
 
0x4 xxencode

XXencode�������ı���ÿ�����ֽ�Ϊ��λ���б��롣������ʣ�µ��������������ֽڣ������Ĳ������㲹�롣�������ֽڹ���24��Bit����6bitΪ��λ��Ϊ4���飬ÿ������ʮ��������ʾ�����ֵ���ֵֻ������0��63֮�䡣������Ӧֵ��λ���ַ����档����ѡ��Ŀɴ�ӡ�ַ��ǣ�+-0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz��һ��64���ַ�����base64��ӡ�ַ���ȣ����Ƕ�һ����-�� �ַ�����һ����/�� �ַ���

Դ�ı���The quick brown fox jumps over the lazy dog

�����hJ4VZ653pOKBf647mPrRi64NjS0-eRKpkQm-jRaJm65FcNG-gMLdt64FjNkc+

���ܵ�ַ:http://web.chacuo.net/charsetxxencode

0x5 UUencode����

UUencode��һ�ֶ����Ƶ����ֵı��룬������unix �ʼ�ϵͳ��ʹ�ã�ȫ�ƣ�Unix-to-Unix encoding��UUencode�������ı���ÿ�����ֽ�Ϊ��λ���б��룬������ʣ�µ��������������ֽڣ������Ĳ������㲹�롣�����ֽڹ���24��Bit����6-bitΪ��λ��Ϊ4���飬ÿ������ʮ��������ʾ�����ֵ��ֽڵ���ֵ�������ֵֻ������0��63֮�䡣Ȼ��ÿ��������32���������Ľ���պ�����ASCII�ַ����пɴ�ӡ�ַ���32-�հס�95-���ߣ��ķ�Χ֮�С�

Դ�ı���The quick brown fox jumps over the lazy dog

����� M5&AE('%U:6-K(&)R;W=N(&9O>"!J=6UP<R!O=F5R('1H92!L87IY(&1O9PH*

���ܵ�ַ:http://web.chacuo.net/charsetuuencode

0x6 Unicode����

Unicode�������������ֱ��뷽ʽ��

Դ�ı���The

&#x [Hex]��The
 
&# [Decimal]��The
 
\U [Hex]��\U0054\U0068\U0065
 
\U+ [Hex]��\U+0054\U+0068\U+0065
 
0x7 Escape/Unescape����

Escape/Unescape���ܽ���/�������,�ֽ�%u���룬����UTF-16BEģʽ�� Escape����/����,�����ַ���ӦUTF-16 16���Ʊ�ʾ��ʽǰ���%u��Unescape����/���ܣ�����ȥ��"%u"�󣬽�16�����ַ���ԭ����utf-16ת�뵽�Լ�Ŀ���ַ����磺�ַ����С���UTF-16BE�ǣ���6d93�������Escape�ǡ�%u6d93����

Դ�ı���The

�����%u0054%u0068%u0065

0x8 ���ذ�ʲ��

���ذ�ʲ��(Atbash Cipher)��һ������ĸ����������Ϊ������Կ���滻���ܣ�Ҳ��������Ķ�Ӧ��ϵ��

ABCDEFGHIJKLMNOPQRSTUVWXYZ
ZYXWVUTSRQPONMLKJIHGFEDCBA
 
���ģ�the quick brown fox jumps over the lazy dog

���ģ�gsv jfrxp yildm ulc qfnkh levi gsv ozab wlt

0x9 dvorak ���̱���

Dvorak������һ�ֽ�������ĸ������һ��������ߴ����ٶȼ��̲��֡�1936����������August Dvorak��ơ����̲�����Ӳ�������ͨ�õ�QWERTY���̣��Լ��̵�һ����ĸ�����6����ĸ��������
#���亯��
����mzdvezc���÷��亯��y=5x+12���ܵõ��ģ��Զ�����ܡ�
ֱ��һ��Python�������
#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Url__ = 'Http://www.purpleroc.com'
__author__ = 'Tracy_����'
def affine(a, b):
    pwd_dic = {}
    for i in range(26):
        pwd_dic[chr(((a*i+b)%26)+97)] = chr(i+97)
    return pwd_dic
if __name__ == '__main__':
    pwd_dic = {}
    pwd = "mzdvezc"   #����mzdvezc  
    plain = []    
    pwd_dic = affine(5, 12)   #5��12 �ֱ�Ϊ����ϵ��
    for i in pwd:        
        plain.append(pwd_dic[i])    
    print "You Flag is: " + "".join(plain)

#������
#####################################################
СҰ������һ��̨������������һ��������Ҫ����ĳ�����룬СҰ�ַ�����һЩ��˿���������ƽ�ô��
������ ��˾�ڲ���Կ����.txt
0xBE, 0x2A, 0x28, 0x48, 0x7A, 0x5C, 0x2A, 0x21, 0xCB, 0x93, 0x0D, 0x2A, 0x70, 
0x36, 0xD3, 0x4E, 0xC9, 0xB6, 0xCF, 0x3C, 0xB6, 0x71, 0x99, 0xF5, 0x46, 0x69, 0xA1, 
0x24, 0xF9, 0x71, 0x70, 0x11, 0x2A, 0x37, 0x31, 0x27, 0x30, 0x16, 0x71, 0x90, 0x26, 
0xC9, 0x18, 0x72, 0xC9, 0x09, 0x4E, 0xC9, 0x0B, 0x5E, 0xC9, 0x4B, 0xC9, 0x2B, 0x4A, 
0xEF, 0x7F, 0x28, 0x48, 0x7A, 0x5C, 0x37, 0x47, 0xD7, 0xBD, 0x15, 0xBA, 0xD7, 0x22, 
0xC9, 0x07, 0x7E, 0xC9, 0x0E, 0x47, 0x3A, 0x41, 0x8F, 0xC9, 0x1B, 0x62, 0x41, 0x9F, 
0x71, 0xBD, 0x05, 0xC9, 0x76, 0xF9, 0x41, 0xB7, 0xDB, 0x4D, 0xFC, 0x44, 0x78, 0x86, 
0x36, 0x4A, 0x83, 0x88, 0x45, 0x41, 0x92, 0x04, 0xA9, 0xB3, 0x79, 0x16, 0x66, 0x5E, 
0x37, 0xA6, 0xC9, 0x1B, 0x66, 0x41, 0x9F, 0x24, 0xC9, 0x7E, 0x39, 0xC9, 0x1B, 0x5E, 
0x41, 0x9F, 0x41, 0x6E, 0xF9, 0xD7, 0x1D, 0xE9, 0x15, 0x23, 0x7F, 0x28, 0x48, 0x7A, 
0x5C, 0x37, 0xEB, 0x71, 0x99, 0x11, 0x2A, 0x35, 0x34, 0x36, 0x64, 0x2A, 0x14, 0x29, 
0x68, 0x7A, 0xC9, 0x86, 0x11, 0x12, 0x12, 0x11, 0xBD, 0x15, 0xBE, 0x11, 0xBD, 0x15, 
0xBA, 0xD2, 0xD2, 0xD2, 0xD2
��ҵ���ܷ�ʽ.txt ��˾�ڲ����еļ�����ʽ��Ϊ�����ܣ���ֻʹ�������ܣ�����KEY��0x42 ���μǣ����ܣ�
������˺�,�����ŵ�һ��exe����ڵ�,Ȼ��,ֱ������exe�Ϳ��Ե���flag.
#####################################################
#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Url__ = 'Http://www.purpleroc.com'
__author__ = 'Tracy_����'
pwd = "BE,  0x2A,  0x28,  0x48,  0x7A,  0x5C,  0x2A,  0x21,  0xCB,  0x93,  0x0D,  0x2A,  \
    0x70,  0x36,  0xD3,  0x4E,  0xC9,  0xB6,  0xCF,  0x3C,  0xB6,  0x71,  0x99,  0xF5,  0x46,  \
    0x69,  0xA1,  0x24,  0xF9,  0x71,  0x70,  0x11,  0x2A,  0x37,  0x31,  0x27,  0x30,  0x16,  \
    0x71,  0x90,  0x26,  0xC9,  0x18,  0x72,  0xC9,  0x09,  0x4E,  0xC9,  0x0B,  0x5E,  0xC9,  \
    0x4B,  0xC9,  0x2B,  0x4A,  0xEF,  0x7F,  0x28,  0x48,  0x7A,  0x5C,  0x37,  0x47,  0xD7,  \
    0xBD,  0x15,  0xBA,  0xD7,  0x22,  0xC9,  0x07,  0x7E,  0xC9,  0x0E,  0x47,  0x3A,  0x41,  \
    0x8F,  0xC9,  0x1B,  0x62,  0x41,  0x9F,  0x71,  0xBD,  0x05,  0xC9,  0x76,  0xF9,  0x41,  \
    0xB7,  0xDB,  0x4D,  0xFC,  0x44,  0x78,  0x86,  0x36,  0x4A,  0x83,  0x88,  0x45,  0x41,  \
    0x92,  0x04,  0xA9,  0xB3,  0x79,  0x16,  0x66,  0x5E,  0x37,  0xA6,  0xC9,  0x1B,  0x66,  \
    0x41,  0x9F,  0x24,  0xC9,  0x7E,  0x39,  0xC9,  0x1B,  0x5E,  0x41,  0x9F,  0x41,  0x6E,  \
    0xF9,  0xD7,  0x1D,  0xE9,  0x15,  0x23,  0x7F,  0x28,  0x48,  0x7A,  0x5C,  0x37,  0xEB,  \
    0x71,  0x99,  0x11,  0x2A,  0x35,  0x34,  0x36,  0x64,  0x2A,  0x14,  0x29,  0x68,  0x7A,  \
    0xC9,  0x86,  0x11,  0x12,  0x12,  0x11,  0xBD,  0x15,  0xBE,  0x11,  0xBD,  0x15,  0xBA,  \
    0xD2,  0xD2,  0xD2,  0xD2"
key = "0x42"
if __name__ == '__main__':
    cipher = pwd.split(',  0x')
    #print "".join(cipher)
    plain = []
    temp = []
    for i in cipher:
        open("../../DATA/BASIC05/basic5.bin","ab").write(chr(int(i, 16) ^ int(key, 16)))
    #print "Flag is: Vk*8wvt&"
	
############################################
�ϴε������ˣ��������ֿ쵽�ˣ��ٸ��ҵ���������������ɡ� http://script.iscc.org.cn/script03/
����ȥ��ȥ������ޣ�����ʵ���ǣ�Ҳ��֪����Ҫ��ɶ���и���ʾת����������1G�� �����ý������NAN������С������
          ���룺99e9999-99e1111 �õ�flag��
          ���������NANMB������ лл�������ô��������flag�����ˡ� flag:{68d43d512ca7214e05acc96cc100515e}
############################################  
�����Ȱ�˹��������
  1  2  3  4   5
1 A  B  C  D   E 
2 F  G  H  I/J K
3 L  M  N  O   P
4 Q  Q  S  T   U
5 V  W  X  Y   Z 
����ʵ����
���ģ� THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
���ģ� 442315 4145241325 1242345233 213453 2445323543 442315 31115554 143422
#�����ƶ�����
���ܽ���ʵ��(ps������ӽ���Ҳ�Ǻ�����������)��
#!python
>>>from pycipher import Playfair
>>>Playfair('CULTREABDFGHIKMNOPQSVWXYZ').encipher('THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG')
#���'UKDNLHTGFLWUSEPWHLISNPCGCRGAUBVZAQIV'
>>>Playfair('CULTREABDFGHIKMNOPQSVWXYZ').decipher('UKDNLHTGFLWUSEPWHLISNPCGCRGAUBVZAQIV')
#���'THEQUICKBROWNFOXIUMPSOVERTHELAZYDOGX'
#ά����������
���ģ� THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
��Կ(ѭ��ʹ�ã���ԿԽ������ƽ��Ѷ�Խ��)�� CULTURE
��2����֪��Կ�ӽ���
#!python
>>>from pycipher import Vigenere
>>>Vigenere('CULTURE').encipher('THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG')
'VBPJOZGMVCHQEJQRUNGGWQPPKNYINUKRXFK'
>>>Vigenere('CULTURE').decipher('VBPJOZGMVCHQEJQRUNGGWQPPKNYINUKRXFK')
'THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG'
#����˹�Ѷ�������(Gronsfeld cipher)
#!python
>>>from pycipher import Gronsfeld
>>>Gronsfeld([2,20,11,45,20,43,4]).encipher('THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG')
'VBPJOZGMVCHQEJQRUNGGWQPPKNYINUKRXFK'
>>>Gronsfeld([2,20,11,45,20,43,4]).decipher('VBPJOZGMVCHQEJQRUNGGWQPPKNYINUKRXFK')
'THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG'
#�Զ���Կ����
#Porta����--Porta����(Porta Cipher)��һ����������ǲ���˹��ҽ��Giovanni Battista della Porta�����Ķ��������룬Porta������м��ܽ��ܹ��̵�����ͬ���ص�
�ܱ�
#!shell
KEYS| A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
----|----------------------------------------------------
A,B | N O P Q R S T U V W X Y Z A B C D E F G H I J K L M
C,D | O P Q R S T U V W X Y Z N M A B C D E F G H I J K L
E,F | P Q R S T U V W X Y Z N O L M A B C D E F G H I J K
G,H | Q R S T U V W X Y Z N O P K L M A B C D E F G H I J
I,J | R S T U V W X Y Z N O P Q J K L M A B C D E F G H I
K,L | S T U V W X Y Z N O P Q R I J K L M A B C D E F G H
M,N | T U V W X Y Z N O P Q R S H I J K L M A B C D E F G
O,P | U V W X Y Z N O P Q R S T G H I J K L M A B C D E F
Q,R | V W X Y Z N O P Q R S T U F G H I J K L M A B C D E
S,T | W X Y Z N O P Q R S T U V E F G H I J K L M A B C D
U,V | X Y Z N O P Q R S T U V W D E F G H I J K L M A B C
W,X | Y Z N O P Q R S T U V W X C D E F G H I J K L M A B
Y,Z | Z N O P Q R S T U V W X Y B C D E F G H I J K L M A
���ģ� THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
��Կ(ѭ��ʹ�ã���ԿԽ������ƽ��Ѷ�Խ��)�� CULTURE
���ܹ��̣�������ĸ'T'������Կ��ĸ'C'�н������������ĸ'F',�Դ����ơ�
���ģ� FRW HKQRY YMFMF UAA OLWHD ALWI JPT ZXHC NGV
���߽��룺http://www.practicalcryptography.com/ciphers/classical-era/porta/
#�������
#!shell
A = aaaaa  I/J = abaaa  R = baaaa

B = aaaab  K = abaab    S = baaab

C = aaaba  L = ababa    T = baaba

D = aaabb  M = ababb    U/V = baabb

E = aabaa  N = abbaa    W = babaa

F = aabab  O = abbab    X = babab

G = aabba  P = abbba    Y = babba

H = aabbb  Q = abbbb    Z = babbb
���ģ� T H E F O X
���ģ� baaba aabbb aabaa aabab abbab babab
#asp�������ܣ�VBScript/JScript.Encode 
 aspencode
����#@~^EQAAAA==VXlj4UmkaYAUmKN3bAYAAA==^#~@?
����http://adophper.com/encode.html���ܼ��ɡ���
#aaencode
?��??= /���䣩? ~�ߩ���   //*��?��*/ ['_']; o=(???)  =_=3; c=(?��?) =(???)-(???); (?��?) =(?��?)= (o^_^o)/ (o^_^o);(?��?)={?��?: '_' ,?��?? : ((?��??==3) +'_') [?��?] ,???? :(?��??+ '_')[o^_^o -(?��?)] ,?��??:((???==3) +'_')[???] }; (?��?) [?��?] =((?��??==3) +'_') [c^_^o];(?��?) ['c'] = ((?��?)+'_') [ (???)+(???)-(?��?) ];(?��?) ['o'] = ((?��?)+'_') [?��?];(?o?)=(?��?) ['c']+(?��?) ['o']+(?��?? +'_')[?��?]+ ((?��??==3) +'_') [???] + ((?��?) +'_') [(???)+(???)]+ ((???==3) +'_') [?��?]+((???==3) +'_') [(???) - (?��?)]+(?��?) ['c']+((?��?)+'_') [(???)+(???)]+ (?��?) ['o']+((???==3) +'_') [?��?];(?��?) ['_'] =(o^_^o) [?o?] [?o?];(?��?)=((???==3) +'_') [?��?]+ (?��?) .?��??+((?��?)+'_') [(???) + (???)]+((???==3) +'_') [o^_^o -?��?]+((???==3) +'_') [?��?]+ (?��?? +'_') [?��?]; (???)+=(?��?); (?��?)[?��?]='\\'; (?��?).?��??=(?��?+ ???)[o^_^o -(?��?)];(o???o)=(?��?? +'_')[c^_^o];(?��?) [?o?]='\"';(?��?) ['_'] ( (?��?) ['_'] (?��?+(?��?)[?o?]+ (?��?)[?��?]+(?��?)+ (???)+ (?��?)+ (?��?)[?��?]+(?��?)+ ((???) + (?��?))+ (???)+ (?��?)[?��?]+(?��?)+ (???)+ ((???) + (?��?))+ (?��?)[?��?]+(?��?)+ ((o^_^o) +(o^_^o))+ ((o^_^o) - (?��?))+ (?��?)[?��?]+(?��?)+ ((o^_^o) +(o^_^o))+ (???)+ (?��?)[?��?]+((???) + (?��?))+ (c^_^o)+ (?��?)[?��?]+(???)+ ((o^_^o) - (?��?))+ (?��?)[?��?]+(?��?)+ (?��?)+ (c^_^o)+ (?��?)[?��?]+(?��?)+ (???)+ ((???) + (?��?))+ (?��?)[?��?]+(?��?)+ ((???) + (?��?))+ (???)+ (?��?)[?��?]+(?��?)+ ((???) + (?��?))+ (???)+ (?��?)[?��?]+(?��?)+ ((???) + (?��?))+ ((???) + (o^_^o))+ (?��?)[?��?]+((???) + (?��?))+ (???)+ (?��?)[?��?]+(???)+ (c^_^o)+ (?��?)[?��?]+(?��?)+ (?��?)+ ((o^_^o) - (?��?))+ (?��?)[?��?]+(?��?)+ (???)+ (?��?)+ (?��?)[?��?]+(?��?)+ ((o^_^o) +(o^_^o))+ ((o^_^o) +(o^_^o))+ (?��?)[?��?]+(?��?)+ (???)+ (?��?)+ (?��?)[?��?]+(?��?)+ ((o^_^o) - (?��?))+ (o^_^o)+ (?��?)[?��?]+(?��?)+ (???)+ (o^_^o)+ (?��?)[?��?]+(?��?)+ ((o^_^o) +(o^_^o))+ ((o^_^o) - (?��?))+ (?��?)[?��?]+(?��?)+ ((???) + (?��?))+ (?��?)+ (?��?)[?��?]+(?��?)+ ((o^_^o) +(o^_^o))+ (c^_^o)+ (?��?)[?��?]+(?��?)+ ((o^_^o) +(o^_^o))+ (???)+ (?��?)[?��?]+(???)+ ((o^_^o) - (?��?))+ (?��?)[?��?]+((???) + (?��?))+ (?��?)+ (?��?)[?o?]) (?��?)) ('_');
#jsfuck
ֻ����[]()!+�����ַ�������ֱ����console����̨���еõ�flag
http://www.jsfuck.com/
#jother
8�������ַ�����:!+()[]{}
ֱ���������(IE����)�Ŀ���̨���������ļ���ִ�н��ܣ�
#brainfuck
ֻ�а��ַ��ţ����еĲ�����������ַ���( > < + - . , [ ] )���������ɡ�
���ģ�hello!
#!shell
+++++ +++++ [->++ +++++ +++<] >++++ .---. +++++ ++..+ ++.<+ +++++ +++++
[->++ +++++ ++++< ]>+++ ++++. <++++ +++[- >---- ---<] >--.< +++++ ++[->
----- --<]> ----- ----- .<
#ook 
#��brainfuck��һ�����ؽ���վ�㣬���ܼ���
	Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook.
	Ook. Ook. Ook. Ook. Ook. Ook! Ook? Ook! Ook! Ook. Ook? Ook. Ook. Ook. Ook.
	Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook.
	Ook. Ook? Ook. Ook? Ook! Ook. Ook? Ook. Ook. Ook. Ook. Ook! Ook. Ook. Ook.
	Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook. Ook? Ook. Ook.
	Ook. Ook. Ook. Ook. Ook. Ook! Ook? Ook! Ook! Ook. Ook? Ook! Ook! Ook! Ook!
	Ook! Ook! Ook? Ook. Ook? Ook! Ook. Ook? Ook! Ook! Ook! Ook! Ook! Ook. Ook.
	Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook. Ook? Ook.
	Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook? Ook! Ook! Ook. Ook? Ook.
	Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook? Ook. Ook? Ook! Ook. Ook? Ook. Ook.
	Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook. Ook? Ook. Ook. Ook. Ook. Ook. Ook.
	Ook. Ook! Ook? Ook! Ook! Ook. Ook? Ook! Ook! Ook! Ook! Ook! Ook! Ook? Ook.
	Ook? Ook! Ook. Ook? Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook. Ook! Ook! Ook!
	Ook! Ook! Ook! Ook! Ook! Ook! Ook. Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook.
	Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook? Ook! Ook! Ook. Ook? Ook!
	Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook? Ook.
	Ook? Ook! Ook. Ook? Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook!
	Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook!
	Ook! Ook. Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook.
	Ook. Ook. Ook. Ook! Ook? Ook! Ook! Ook. Ook? Ook. Ook. Ook. Ook. Ook. Ook.
	Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook? Ook. Ook? Ook! Ook. Ook? Ook.
	Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook. Ook? Ook. Ook. Ook.
	Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook? Ook! Ook! Ook. Ook? Ook. Ook. Ook.
	Ook. Ook. Ook. Ook. Ook. Ook? Ook. Ook? Ook! Ook. Ook? Ook. Ook. Ook! Ook.
	Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook? Ook! Ook! Ook. Ook? Ook!
	Ook! Ook! Ook! Ook! Ook! Ook? Ook. Ook? Ook! Ook. Ook? Ook! Ook! Ook! Ook!
	Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook. Ook? Ook. Ook. Ook. Ook. Ook. Ook.
	Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook? Ook! Ook! Ook. Ook?
	Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook?
	Ook. Ook? Ook! Ook. Ook? Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook!
	Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook.
	Ook. Ook! Ook. Ook. Ook. Ook! Ook. Ook. Ook. Ook! Ook. Ook. Ook. Ook! Ook.
	Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook!
	Ook. Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook.
	Ook. Ook. Ook! Ook? Ook! Ook! Ook. Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook.
	Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook? Ook. Ook? Ook! Ook. Ook? Ook. Ook.
	Ook. Ook. Ook. Ook. Ook! Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook. Ook.
	Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook.
	Ook. Ook. Ook! Ook. Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook. Ook.
	Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook. Ook? Ook. Ook. Ook.
	Ook. Ook. Ook. Ook. Ook! Ook? Ook! Ook! Ook. Ook? Ook. Ook. Ook. Ook. Ook.
	Ook. Ook? Ook. Ook? Ook! Ook. Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook.
	Ook. Ook. Ook. Ook. Ook! Ook. Ook? Ook.
#DES
���ܷ�ʽ:DES
��Կ:6XaMMbM7
����:U2FsdGVkX18IBEATgMBe8NqjIqp65CxRjjMxXIIUxIjBnAODJQRkSLQ/+lHBsjpv1BwwEawMo1c=
������ܲ��ˣ����Ի�����վ���ԣ��Ͼ�Des����ʱ�����䡢���뷽ʽ����Ӱ������ʵ�������վ���ԣ�http://encode.chahuo.com��
����:ctf{67a166801342415a6da8f0dbac591974}
#SHA1����

#��������
����һ�ֽ����ĺ����ֽ���ת�������룬�㷨�൱��:�����õ�ʮ�����ֵİ����ǡ��ɡ������С������ˡ��������������󡱡������������򡱡������������򡱡����ǡ�ʮ���֡����ְ�������ÿһ������������¶���ıʻ�����ͷ��������ʾ���ֵġ��硰�ɡ�������һ��¶��һ��ͷ��Ϊ���֡�һ�������С�������¶��������ͷ��Ϊ���֡���������������������¶���Ÿ���ͷ��Ϊ���֡��š������ǡ����������ҹ�¶��ʮ����ͷ��Ϊ���֡�ʮ�������˵���򾮡����Ǿ�����˵���߰ˡ���������ˡ�
���ģ����ɴ󾮷�������й�
���ģ�9158753624
#ascii�ַ�ƫ��
����
gndk�rlqhmtkwwp}z
����������Ŀ
gndk�rlqhmtkwwp}z�����ʽ����flag{*******}?
���ǱȽ�һ��"gndk"��"flag"��ASCII��
gndk��10���Ƶ�ASCII��ֱ��ǣ�103 110 100 107
flag��10���Ƶ�ASCII��ֱ���  ��102 108  97  103
����ASCII�Դ˼��� 1 2 3 4�������Դ�����
���ǲ�֪����ô����'�'����ַ�����ʱ���ɱ���ַ�������ڻ���'{'
��python����
######�˽��ƣ�ʮ������###С������
��б�ܼ���λ����λ���֣�Ӧ���ǰ˽���ת�����У��˽���תascii���ű���һ��
\x��ʽ�ģ�������16���ƣ�д���ű�16����תascii
\u��ͷ��16����Unicode���룬����Unicodeת���ַ�
������Ӧ����ascii��ʮ���Ʊ�ʾ��תΪ�ַ���ע���Ȱ��м�Ķ���ɾ����
htmlת���ַ���������Python���루��ɾ���м�Ŀո���ϸ�̳̿��Լ�Python HTML�������

����Python html���� 
####��ȱ��hashֵ
С��һֱ����������Ĺ�ϣֵд��ֽ�ϣ����һ��С�Ľ�īˮ���������棬ֻ���õ�ǰ10λ��c2979c7124��С��ֻ�ǵ�������4λ�����ּ���ĸ�����ܰ�С���ָ�����Ĺ�ϣֵ�𣿣���ʾ��flagΪ����Ĺ�ϣֵ��

#! /usr/bin/env python
# -*- coding: utf-8 -*-

import string
import hashlib
import itertools

def md5(cstr):
    m = hashlib.md5()
    m.update(cstr)
    return m.hexdigest().lower()

ls = list(string.lowercase) + list(string.uppercase) + list(string.digits)

s = 'c2979c7124'
for l in list(itertools.permutations(ls,4)):
    p = ''.join(l)
    if md5(p)[0:len(s)] == s:
        print md5(p)
        exit(0)
����
<?php
$str='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
$cou=strlen($str);
for($i=0;$i<$cou-1;$i++){
        for($j=0;$j<$cou-1;$j++){
                for($k=0;$k<$cou-1;$k++){
                        for($l=0;$l<$cou-1;$l++){
                                $ret=md5($str[$i].$str[$j].$str[$k].$str[$l]);
                                if(substr($ret,0,10)=='c2979c7124'){
                                        echo $ret;die();
                                }
                        }
                }
        }
}
?>