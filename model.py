import os
import librosa
import librosa.display
import matplotlib.pyplot as plt

audio_fpath = "./audio/"
audio_clips = os.listdir(audio_fpath)
for i in range(0,4):
 from scipy.io import wavfile


 yt, sr = librosa.load(audio_fpath+audio_clips[i])
 y, index = librosa.effects.trim(yt)
 '''plt.plot(y);
 plt.title('Signal');
 plt.xlabel('Time (samples)');
 plt.ylabel('Amplitude');
 plt.show(block=False)
 plt.pause(1)
 plt.figure().clear()
 plt.close()
 plt.cla()
 plt.clf()
 import numpy as np
 n_fft = 2048
 ft = np.abs(librosa.stft(y[:n_fft], hop_length = n_fft+1))
 plt.plot(ft);
 plt.title('Spectrum');
 plt.xlabel('Frequency Bin');
 plt.ylabel('Amplitude');
 plt.show(block=False)
 plt.pause(1)
 plt.figure().clear()
 plt.close()
 plt.cla()
 plt.clf()
 spec = np.abs(librosa.stft(y, hop_length=1024))
 spec = librosa.amplitude_to_db(spec, ref=np.max)
 librosa.display.specshow(spec, sr=sr, x_axis='time', y_axis='log');
 plt.colorbar(format='%+2.0f dB');
 plt.title('Spectrogram');
 plt.show(block=False)
 plt.pause(1)
 plt.figure().clear()
 plt.close()
 plt.cla()
 plt.clf()
 '''
 import numpy as np
 mel_spect = librosa.feature.melspectrogram(y=y, sr=sr, n_fft=2048, hop_length=1024,n_mels=128)
 mel_spect1 = librosa.power_to_db(mel_spect, ref=np.max)
 librosa.display.specshow(mel_spect1,fmax=8000);
 title='three'+str(i);
# plt.title(title);
 #plt.colorbar();
 plt.gca().set_axis_off()
 plt.subplots_adjust(top=1, bottom=0, right=1, left=0,
                     hspace=0, wspace=0)
 plt.margins(0, 0);
 plt.gca().xaxis.set_major_locator(plt.NullLocator());
 plt.gca().yaxis.set_major_locator(plt.NullLocator());
 plt.savefig('./dataset/experiment/z/'+title,bbox_inches='tight',pad_inches=0);
 plt.show(block=False)
 plt.pause(1)
 plt.figure().clear()
 plt.close()
 plt.cla()
 plt.clf()
 # Saving the array
 #print(mel_spect1.shape)

'''
import librosa
import librosa.display
import IPython.display as ipd
import matplotlib.pyplot as plt
audio_fpath = "./audio/"
audio_clips = os.listdir(audio_fpath)
for i in range(0,22):
 scale, sr = librosa.load(audio_fpath+audio_clips[i])

 yt, index = librosa.effects.trim(scale)
 #filter_banks = librosa.filters.mel(n_fft=1024, sr=22050, n_mels=50)
 #plt.figure(figsize=(10, 10))
 #librosa.display.specshow(filter_banks,
 #                        sr=sr,
 #                        x_axis="linear")
 #plt.colorbar(format="%+2.f")
 #plt.show()
 mel_spectrogram = librosa.feature.melspectrogram(y=yt, sr=sr,  n_mels=10)
 log_mel_spectrogram = librosa.power_to_db(mel_spectrogram)
 #plt.figure(figsize=(5,5))
 librosa.display.specshow(log_mel_spectrogram,
                         x_axis="time",
                         y_axis="mel",
                         sr=sr,cmap='magma')
 #plt.colorbar(format="%+2.f")
 plt.gca().set_axis_off();
 plt.subplots_adjust(top=1, bottom=0, right=1, left=0,
                     hspace=0, wspace=0)
 plt.margins(0, 0);
 plt.gca().xaxis.set_major_locator(plt.NullLocator())
 plt.gca().yaxis.set_major_locator(plt.NullLocator())
 title = 'bird' + str(i);
 #plt.title(title);
 plt.savefig('./dataset/bird/' + title, bbox_inches='tight', pad_inches=0);
 plt.show(block=False);
 plt.pause(1);
 plt.close();
 plt.figure().clear();
 plt.cla();
 plt.clf();
'''
# Load some audio