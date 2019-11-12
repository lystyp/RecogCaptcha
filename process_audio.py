import os
import time
import traceback

import speech_recognition
from pydub import AudioSegment

r = speech_recognition.Recognizer()

def increase_wav(i):
    audio_name = "./audio/" + str(i) + ".mp3"
    sound = AudioSegment.from_mp3(audio_name)
    silence = AudioSegment.silent(duration=300)
    processed_sound = silence + sound + silence
    processed_sound.export('./processed_audio/processed_' + str(i) + '.wav', format="wav")


def recognize(i):
    with speech_recognition.AudioFile('./processed_audio/processed_' + str(i) + '.wav') as source:
        audio = r.record(source)
        result = r.recognize_google(audio, language='zh-tw')
        print(result)
        return result


if __name__ == "__main__":
    fo = open("number_captcha_match.txt", "a")
    for count in range(945):
        try:
            increase_wav(count)
            captcha = recognize(count)
            fo.write(str(count) + "," + captcha + "\n")
            os.rename('processed_image\\' + str(count) + '.png',
                      'processed_image\\' + captcha + '.png')
            # 每50筆存一下
            if count % 50 == 0:
                fo.close()
                fo = open("number_captcha_match.txt", "a")
        except Exception as e:
            print(traceback.format_exc())
    fo.close()

