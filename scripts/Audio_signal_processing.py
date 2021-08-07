import librosa
import librosa.display
import IPython
import IPython.display as ipd
import matplotlib
import matplotlib.pyplot as plt
from playsound import playsound
import numpy as np

#load audio files
dysarthric = "audio/0001.wav"
controlad = "audio/control.wav"


#playsound(dysarthric)

#Loading files and Sampling rate (default)
dysarthric, sr = librosa.load(dysarthric)
controlad, sr2 = librosa.load(controlad)

print(dysarthric.size)

#Duration of 1 sample
sample_duration = 1/sr
print(f"Duration of 1 samples is: {sample_duration:.6f} seconds")

#Duration of audio signal in seconds
duration = sample_duration*len(dysarthric)
print(f"Duration of signal is: {duration:.2f} seconds")

#Visualize waveforms

plt.figure(figsize=(15, 17))
plt.subplot(3, 1, 1)
librosa.display.waveplot(dysarthric, alpha=0.5)
plt.title("Dysarthric speech")
plt.ylim(-1, 1)

plt.figure(figsize=(15, 17))
plt.subplot(3, 1, 1)
librosa.display.waveplot(controlad, alpha=0.5)
plt.title("Control speech")
plt.ylim(-1, 1)


plt.show()


#Calculate the amplitude envelope!

FRAM_SIZE = 1024
HOP_LENGTH = 512

def amplitude_envelope(signal, frame_size, hop_length):
    amplitude_envelope = []


    #calculate amplitude envelope for each frame
    for i in range(0, len(signal), hop_length):
        current_frame_amplitude_envelope = max(signal[i:i+frame_size])
        amplitude_envelope.append(current_frame_amplitude_envelope)

    return np.array(amplitude_envelope)


def fancy_amplitude_envelope(signal, frame_size, hop_length):
    return np.array([max(signal[i:i+frame_size]) for i in range(0, signal.size, hop_length)])

ae_dysarthric = amplitude_envelope(dysarthric, FRAM_SIZE, HOP_LENGTH)
print(len(ae_dysarthric))

ae_control= amplitude_envelope(controlad, FRAM_SIZE, HOP_LENGTH)
print(len(ae_control))

fancy_dys = fancy_amplitude_envelope(dysarthric, FRAM_SIZE, HOP_LENGTH)
print(len(fancy_dys))

#Visualize the amplitude envelope for all the audio files

frames = range(0, ae_control.size)
t = librosa.frames_to_time(frames, hop_length=HOP_LENGTH)
"""
plt.figure(figsize=(15, 17))
plt.subplot(3, 1, 1)
librosa.display.waveplot(dysarthric, alpha=0.5)
plt.plot(t, ae_dysarthric, color="r")
plt.title("Dysarthric speech")
plt.ylim(-1, 1)"""

plt.figure(figsize=(15, 17))
plt.subplot(3, 1, 1)
librosa.display.waveplot(controlad, alpha=0.5)
plt.plot(t, ae_dysarthric, color="r")
plt.title("Control speech")
plt.ylim(-1, 1)

