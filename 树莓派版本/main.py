# -*- coding: utf-8 -*-
from pyaudio import PyAudio, paInt16
import numpy as np
from datetime import datetime
import wave
import time
import urllib, urllib2, pycurl
import base64
import json
import os
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

save_count = 0
save_buffer = []
t = 0
sum = 0
time_flag = 0
flag_num = 0
filename = '2.wav'
duihua = '1'
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def get_token():
    apiKey = "Ll0c53MSac6GBOtpg22ZSGAU"
    secretKey = "44c8af396038a24e34936227d4a19dc2"
    auth_url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=" + apiKey + "&client_secret=" + secretKey;
    res = urllib2.urlopen(auth_url)
    json_data = res.read()
    return json.loads(json_data)['access_token']

def dump_res(buf):
    global duihua
    print "字符串类型"
    print (buf)
    a = eval(buf)
    print type(a)
    if a['err_msg']=='success.':
        #print a['result'][0]#终于搞定了，在这里可以输出，返回的语句
        duihua = a['result'][0]
        print duihua

def use_cloud(token):
    fp = wave.open(filename, 'rb')
    nf = fp.getnframes()
    f_len = nf * 2
    audio_data = fp.readframes(nf)
    cuid = "7519663" #产品id
    srv_url = 'http://vop.baidu.com/server_api' + '?cuid=' + cuid + '&token=' + token
    http_header = [
        'Content-Type: audio/pcm; rate=8000',
        'Content-Length: %d' % f_len
    ]

    c = pycurl.Curl()
    c.setopt(pycurl.URL, str(srv_url)) #curl doesn't support unicode
    #c.setopt(c.RETURNTRANSFER, 1)
    c.setopt(c.HTTPHEADER, http_header)   #must be list, not dict
    c.setopt(c.POST, 1)
    c.setopt(c.CONNECTTIMEOUT, 30)
    c.setopt(c.TIMEOUT, 30)
    c.setopt(c.WRITEFUNCTION, dump_res)
    c.setopt(c.POSTFIELDS, audio_data)
    c.setopt(c.POSTFIELDSIZE, f_len)
    c.perform() #pycurl.perform() has no return val

# 将data中的数据保存到名为filename的WAV文件中
def save_wave_file(filename, data):
    wf = wave.open(filename, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(SAMPLING_RATE)
    wf.writeframes("".join(data))
    wf.close()


NUM_SAMPLES = 2000      # pyAudio内部缓存的块的大小
SAMPLING_RATE = 8000    # 取样频率
LEVEL = 1500            # 声音保存的阈值
COUNT_NUM = 20          # NUM_SAMPLES个取样之内出现COUNT_NUM个大于LEVEL的取样则记录声音
SAVE_LENGTH = 8         # 声音记录的最小长度：SAVE_LENGTH * NUM_SAMPLES 个取样

# 开启声音输入
'''
pa = PyAudio()
stream = pa.open(format=paInt16, channels=1, rate=SAMPLING_RATE, input=True,
                frames_per_buffer=NUM_SAMPLES)
'''

token = get_token()
key = '05ba411481c8cfa61b91124ef7389767'
api = 'http://www.tuling123.com/openapi/api?key=' + key + '&info='

#while True:
    # 读入NUM_SAMPLES个取样
    #string_audio_data = stream.read(NUM_SAMPLES)
    # 将读入的数据转换为数组
    #audio_data = np.fromstring(string_audio_data, dtype=np.short)
    # 计算大于LEVEL的取样的个数
    #large_sample_count = np.sum( audio_data > LEVEL )

    #temp = np.max(audio_data)
'''
    if temp > 2000 and t == 0:
        t = 1#开启录音
        print "检测到信号，开始录音,计时五秒"
        begin = time.time()
        print temp
    if t:
        print np.max(audio_data)
        if np.max(audio_data)<1000:
            sum += 1
            print sum
        end = time.time()
        if end-begin>5:
            time_flag = 1
            print "五秒到了，准备结束"
        # 如果个数大于COUNT_NUM，则至少保存SAVE_LENGTH个块
        if large_sample_count > COUNT_NUM:
            save_count = SAVE_LENGTH
        else:
            save_count -= 1

        if save_count < 0:
            save_count = 0

        if save_count > 0:
            # 将要保存的数据存放到save_buffer中
            save_buffer.append(string_audio_data )
        else:
            # 将save_buffer中的数据写入WAV文件，WAV文件的文件名是保存的时刻
            #if  time_flag:
            if len(save_buffer) > 0  or time_flag:
                #filename = datetime.now().strftime("%Y-%m-%d_%H_%M_%S") + ".wav"
                filename = str(flag_num)+".wav"
                flag_num += 1

                save_wave_file(filename, save_buffer)
                save_buffer = []
                t = 0
                sum =0
                time_flag = 0
                print filename, "保存成功正在进行语音识别"
        '''
while(True):
    #os.system('arecord -D "plughw:1,0" -f S16_LE -d 5 -r 8000 /home/luyi/yuyinduihua/2.wav')
    use_cloud(token)
    print duihua
    info = duihua
    duihua = ""
    request = api# + infox
    response = getHtml(request)
    dic_json = json.loads(response)

    #print '机器人: '.decode('utf-8') + dic_json['text']
    #huida = ' '.decode('utf-8') + dic_json['text']
    a = dic_json['text']
    print type(a)
    unicodestring = a

    # 将Unicode转化为普通Python字符串："encode"
    utf8string = unicodestring.encode("utf-8")

    print type(utf8string)
    print str(a)
    url = "http://tsn.baidu.com/text2audio?tex="+dic_json['text']+"&lan=zh&per=0&pit=1&spd=7&cuid=7519663&ctp=1&tok=24.a5f341cf81c523356c2307b35603eee6.2592000.1464423912.282335-7519663"
    os.system('mpg123 "%s"'%(url))
