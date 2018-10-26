import pyaudio
import struct
import wave
import numpy as np 
import matplotlib.pyplot as plt 


wf = wave.open('godfather1_family.wav', 'rb')

CHUNK = 1024*1
FORMAT = pyaudio.paInt16
RATE = wf.getframerate()
CHANNELS = wf.getnchannels()

p = pyaudio.PyAudio()
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=CHANNELS,
                rate=RATE,
                output=True)

data = wf.readframes(CHUNK)

fig, ax = plt.subplots()
x = np.arange(0, 1*CHUNK, 2)
line, = ax.plot(x)
ax.set_ylim(0,255)
ax.set_xlim(0,CHUNK/2)

while len(data) > 0:
    stream.write(data)
    #print(len(data))
    data_int = np.array(struct.unpack(str(1*CHUNK) + 'B', data), dtype='b')[::2] + 126
    #print(data_int)
    line.set_ydata(data_int)
    fig.canvas.draw()
    fig.canvas.flush_events()
    fig.show()
    data = wf.readframes(CHUNK)
    
stream.stop_stream()
stream.close()

p.terminate()
