from configs.settings import SDK_TTS_CONFIGS
from configs.yandex_credentials import API_KEY
from queries.data_multi_for_tts import multi_data_for_tts
from utils_Python_SDK.utilities_python_sdk_tts import synthesize_txt_to_wav_py_sdk
from utilties_helpers.get_full_file_path import get_full_file_normal_path

# Multi wav files TTS synthesising
validated_data = True
for file_name, answer_text in multi_data_for_tts.items():
    if not file_name and not answer_text:
        print(f"No file name and answer text [XXX]: "
              f"file_name={file_name} "
              f"answer_text={answer_text}\n")
        validated_data = False
        continue
    if not file_name:
        print(f"No file name [XXX]: file_name={file_name}\n")
        validated_data = False
        continue
    if not answer_text:
        print(f"No answer text [XXX]: "
              f"file_name={file_name}, "
              f"answer text={answer_text}\n")
        validated_data = False
        continue

if validated_data:
    for file_name_no_ext, answer_text in multi_data_for_tts.items():
        text = answer_text.strip()
        file_name_no_ext = file_name_no_ext.strip()
        file_name_with_ext = file_name_no_ext + ".wav"
        file_export_path = SDK_TTS_CONFIGS.WAV_EXPORT_DIRS_PATH

        normal_path = get_full_file_normal_path(all_dirs_path=file_export_path,
                                                file_name=file_name_with_ext)

        synthesize_txt_to_wav_py_sdk(api_key=API_KEY,
                                     text_for_tts=text,
                                     file_export_path=normal_path,
                                     voice=SDK_TTS_CONFIGS.VOICE,
                                     role=SDK_TTS_CONFIGS.ROLE,
                                     speed=SDK_TTS_CONFIGS.SPEED,
                                     volume=SDK_TTS_CONFIGS.VOLUME)
