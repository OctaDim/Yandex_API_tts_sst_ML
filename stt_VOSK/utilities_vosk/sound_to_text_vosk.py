from vosk import Model, KaldiRecognizer
import sys
import os
import wave

def get_text_from_sound(audio_file):
    path_to_model = r"/stt_VOSK/models_vosk/vosk_model_ru_010_2_5GB/vosk-model-ru-0.10"
    model = Model("path_to_vosk_model")
    wf = wave.open(audio_file, "rb")
    rec = KaldiRecognizer(model, wf.getframerate())

    result = ""
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            result = rec.Result()
        else:
            result = rec.PartialResult()

    return result

if __name__ == "__main__":
    # audio_file = sys.argv[1]
    audio_file_path= r"/stt_VOSK/models_vosk/vosk_model_ru_022_1_5GB/vosk-model-ru-0.22/decoder-test.wav"
    print(get_text_from_sound(audio_file_path))
