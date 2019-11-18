import os
import time
import traceback

import speech_recognition
from pydub import AudioSegment

r = speech_recognition.Recognizer()

data_path = "./data10000/"


def get_file_count():
    l = os.listdir(data_path + "audio/")
    return len(l)


def increase_wav(i):
    audio_name = data_path + "audio/" + str(i) + ".mp3"
    sound = AudioSegment.from_mp3(audio_name)
    silence = AudioSegment.silent(duration=300)
    processed_sound = silence + sound + silence
    processed_sound.export(data_path + 'processed_audio/processed_' + str(i) + '.wav', format="wav")


def recognize(i):
    with speech_recognition.AudioFile(data_path + 'processed_audio/processed_' + str(i) + '.wav') as source:
        audio = r.record(source)
        result = r.recognize_google(audio, language='zh-tw')
        print(result)
        return result


if __name__ == "__main__":
    fo = open(data_path + "number_captcha_match.txt", "a")
    for count in range(get_file_count()):
        try:
            increase_wav(count)
            captcha = recognize(count)
            fo.write(str(count) + "," + captcha + "\n")
            os.rename(data_path + 'image/' + str(count) + '.png',
                      data_path + 'processed_image/' + captcha + '.png')
            # 每50筆存一下
            if count % 50 == 0:
                fo.close()
                fo = open(data_path + "number_captcha_match.txt", "a")
        except Exception as e:
            print(traceback.format_exc())
    fo.close()

