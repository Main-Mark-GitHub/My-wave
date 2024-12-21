# audio_processing.py
import librosa
from .models import Music, Account




def convert(audio_file_path):
    audio_data, sample_rate = librosa.load(audio_file_path, sr=None)
    mfccs = librosa.feature.mfcc(y=audio_data, sr=sample_rate, n_mfcc=13)
    return mfccs.shape


def get_second(id):
    result = (0, 0)
    account = Account.objects.filter(id=id)[0]
    fv_music = Account.get_music(account.favorite_music)
    len_fv = len(fv_music)
    for el in fv_music:
        audio_data, sample_rate = librosa.load(Music.objects.get(id=el).file.path, sr=None)
        mfccs = librosa.feature.mfcc(y=audio_data, sr=sample_rate, n_mfcc=13)
        print(result)
        print(mfccs.shape)
        result = (result[0] + mfccs.shape[0], result[1] + mfccs.shape[1])
    result = (result[0] / len_fv, result[1] / len_fv)
    return result


def compare(first_music, id):
    second_music = get_second(id)
    mfccs = (convert(first_music), second_music)
    difference = (mfccs[0][0] - mfccs[1][0], mfccs[0][1] - mfccs[1][1])
    return (difference[0] + difference[1] / 2) <= 300


def process_audio_files(id):
    result = []
    for audio_file in Music.objects.all():
        music_path = audio_file.file.path
        if compare(music_path, id):
            result.append(audio_file)

    return result




