# Sound-Spectrum-Visualizer
An application that will take a filename or folder name, and present a player and sound spectrum visualizer.

Some .wav files have been included for ease of testing (gotta love the Godfather)





====FFT Implementation====
FFT Data is able to be extracted and plotted, but is not done in real time. Doing so will require
collaboration with the GUI team, as well as synchronizing audio playback from the music/sound player.
As of now, SciPy is being used to extract Fourier transform data, and is being plotted with MatPlotLib.
For sprint 2, the FFT Implemenation team will need to consider extracting fft data in raw digital values
to a Numpy array to be passed to the GUI team and decoded into spectrogram bars in real-time.


=====Next Steps====

Alyssa LeJeune - going to work on connecting the FFT to the bar graph and get it working in real time

Wes Nicol - work on integrating the different GUIs (ex: have the graphs pop up when a song is selected in the music player

Allen Van - Similar to Alyssa, but going to work on connecting the Time Domain graph and make it work in real time. 

