
#coding:utf-8

a = {"corpus_no":"6278498246814101490","err_msg":"success.","err_no":0,"result":["开始，听到我声音了吗？ｇ十五秒钟准备结束，"],"sn":"185381614471461826787"}
b = str(a)
'''
print type(eval(b))
c = eval(b)
d = str(c["result"])
print type(d)
print repr(u"你懂得")
#print u"\xe5\xbc\x80\xe5\xa7\x8b\xef\xbc\x8c\xe5\x90\xac\xe5\x88\xb0\xe6\x88\x91\xe5\xa3\xb0\xe9\x9f\xb3\xe4\xba\x86\xe5\x90\x97\xef\xbc\x9f\xef\xbd\x87\xe5\x8d\x81\xe4\xba\x94\xe7\xa7\x92\xe9\x92\x9f\xe5\x87\x86\xe5\xa4\x87\xe7\xbb\x93\xe6\x9d\x9f\xef\xbc\x8c".decode(sys.stdin.encoding)
uu = d.decode('utf-8')
print uu
'''
import codecs
import sys
#reload(sys)
#sys.setdefaultencoding('gbk')
s = '哈哈'
ss = a['result'][0]
print str(ss)
'''
data = str(ss)
if data[:3] == codecs.BOM_UTF8:
    data = data[3:]
    print data.decode("utf-8")'''
