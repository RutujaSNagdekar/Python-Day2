import pandas as pd
import numpy as np
import matplotlib.pylab as pl
import seaborn as sns
from glob import glob
import librosa
import librosa.display
import IPython.display as ipd


aud = glob('Shin-Chan-Title.mp3')  # Glob Takes multiple mp3 files list
ipd.Audio(aud[0])      # IPython.display to play audio

y, sr = librosa.load(aud[0])  # Librosa converts audio in array and gives speech rate

pd.Series(y)
pd.Series(y).plot()


