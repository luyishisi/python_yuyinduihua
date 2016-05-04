# -*- coding: utf-8 -*-
import pyaudio
import wave

chunk = 1024

wf = wave.open(r"sweep.wav", 'rb')

p = pyaudio.PyAudio()
print "lalla"
print wf
print "lalla"
# 打开声音输出流
stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
                channels = wf.getnchannels(),
                rate = wf.getframerate(),
                output = True)

# 写声音输出流进行播放
while True:
    data = wf.readframes(chunk)
    if data == "": break
    stream.write(data)

stream.close()
p.terminate()
