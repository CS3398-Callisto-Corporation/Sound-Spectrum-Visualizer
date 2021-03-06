import pyaudio
import struct
import wave
import numpy as np 
import matplotlib.pyplot as plt 
from scipy.fftpack import fft


#this function is callled when a song is choosen on the GUI. The song to be played is passed as the filename as a string
def playSong(songTitle):
    wf = wave.open(songTitle, 'rb')

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
    
    fig, (ax,ax2) = plt.subplots(2, figsize=(5,8))
    x = np.arange(0, 1*CHUNK, 2)
    x_fft = np.linspace(0, RATE, CHUNK)
    
    line, = ax.plot(x)
    line_fft, = ax2.semilogx(x_fft)
    
    
    ax.set_title('Time Domain')
    ax.set_xlabel('Samples')
    ax.set_ylabel('Amplitude')
    ax.set_ylim(0,255)
    ax.set_xlim(0,CHUNK/2)
    
    ax2.set_title('Fourier Domain')
    ax2.set_xlim(20, RATE)
    ax2.set_ylim(0,22)
    
    def handle_close(evt):
        p.terminate()
        stream.close()
        plt.close('all')
    
    while len(data) > 0:
        
        
        stream.write(data)
    
        data_int = struct.unpack(str(1*CHUNK) + 'B', data)
        data_np = np.array(data_int, dtype='b')[::2] + 126
    
        line.set_ydata(data_np)
    
        y_fft = fft(data_int)
        line_fft.set_ydata(np.abs(y_fft[0:CHUNK]) / (CHUNK))
    
        fig.canvas.draw()
        fig.canvas.flush_events()
        fig.show()
        data = wf.readframes(CHUNK)
        
        fig.canvas.mpl_connect('close_event', handle_close)
        
        
    
    
    
    stream.stop_stream()
    stream.close()
    
    p.terminate()

    #the below code is inteneded to close the graph window once the song is finished playing, but we havent gotten it to work yet
    #plt.close('all')



#uncomment to run this file as a standalone file
#playSong('godfather1_naive.wav')