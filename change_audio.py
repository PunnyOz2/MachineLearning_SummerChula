# change bitrate to 44100
# https://stackoverflow.com/questions/45526996/how-to-change-the-bitrate-of-a-wav-file-in-python

# Path: up.py
import io
import os
from pydub import AudioSegment

# get local file
audioin_dirpath = '../OpenL3-tutorial/audio_in/train/'
audio_files = os.listdir(audioin_dirpath)

for audio_file in audio_files:
    content = AudioSegment.from_mp3(audioin_dirpath + audio_file)
    if content.frame_rate != 44100:
        content = content.set_frame_rate(44100)
    if content.channels != 1:
        content = content.set_channels(1)
    content.export('../OpenL3-tutorial/audio_in/wav/'+ audio_file.split('.')[0] + '.wav', format='wav')