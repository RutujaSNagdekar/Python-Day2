
import sounddevice as sd
print(sd.query_devices())

import numpy as np
import sounddevice as sd
import librosa
import soundfile as sf
from glob import  glob

duration=10 # Duration of recording in seconds
#sample_rate =22050 # Sample rate for audio
n_steps_high = +4 # Shift pitch by 12 semitones (1 octave)
# Shi ft pitch by 6
n_steps_mid = -2
#semitones
time_stretch_rate =0.9 # Slightly speed up
#Amplification factor
gain = 1.5


print("Recording...")
#audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float64', device=1)
#sd.wait()
#print("Recording finished.")

aud = glob('AudioMe.mp4')
y, sample_rate = librosa.load(aud[0])

print("Changing pitch...")
pitched_audio_high = librosa.effects.pitch_shift(y, sr=sample_rate, n_steps=n_steps_high)
pitched_audio_mid =librosa.effects.pitch_shift(y, sr=sample_rate, n_steps=n_steps_mid)


#Combine the pitch-shifted sounds
combined_audio = pitched_audio_high + pitched_audio_mid
speed_changed = librosa.effects.time_stretch(combined_audio, rate=time_stretch_rate)
distorted = np.clip(speed_changed * gain, -1.0, 1.0)
print("Pitch changed.")
print("Playing modified audio...")
sf.write('d1.wav', distorted, sample_rate)
sd.play(distorted, samplerate=sample_rate, device=1)
sd.wait()

