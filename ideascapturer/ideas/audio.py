from os import path
from django.conf import settings
import speech_recognition as sr
import soundfile
from pydub import AudioSegment


def transcribe_audio(audio_file):
    posix_path = settings.MEDIA_ROOT / audio_file.name
    path_str = str(posix_path)

    print(path_str)
    print(soundfile.available_formats())

    # Convert to actually a .wav file (or certain encoding???)
    """ data, samplerate = soundfile.read(path_str)
    new_file_path = settings.MEDIA_ROOT / 'converted_' + audio_file.name
    soundfile.write(new_file_path, data, samplerate, subtype='PCM_16') """

    sound = AudioSegment.from_file(path_str)
    converted_file_name = 'converted_' + audio_file.name
    converted_file_path = str(settings.MEDIA_ROOT / converted_file_name)
    clipped = sound[400:-1000]
    clipped.export(converted_file_path, format="wav")

    print(converted_file_path)
    print(type(converted_file_path))

    # use the audio file as the audio source
    r = sr.Recognizer()
    with sr.AudioFile(converted_file_path) as source:
        audio = r.record(source)  # read the entire audio file

    # recognize speech using Sphinx
    try:
        result = r.recognize_sphinx(audio)
        print("Sphinx thinks you said " + result)
        return result
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))
