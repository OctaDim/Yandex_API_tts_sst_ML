from configs_tts.settings import SDK_TTS_CONFIGS
from configs_tts.yandex_credentials import API_KEY

# # TEST
# from tts_data.Test_tts_data_multi import WAV_TXT_ASSOC

# # ХМАО ()
# from tts_data.HMAO_tts_data_multi import WAV_TXT_ASSOC

# # KIROV (confirm_appointment_robot.py)
# from tts_data.Kirov_tts_data_multi import WAV_TXT_ASSOC

# ОМСК (omsk_mfc_robot)
# from tts_data.Omsk_tts_data_multi import WAV_TXT_ASSOC

# # Вычисление максимальной продолжительности wav файлов
# from tts_data.Common_Duration_tts_multi import WAV_TXT_ASSOC

# # Йошкар-Ола (counter reception)
# from tts_data.YoshkarOla_tec1_counter_reception_tts_multi import WAV_TXT_ASSOC

# # Йошкар-Ола (auto informer)
# from tts_data.YoshkarOla_tec1_auto_informer_tts_multi import WAV_TXT_ASSOC

# # Йошкар-Ола (auto caller)
# from tts_data.YoshkarOla_tec1_dept_auto_caller_tts_multi import WAV_TXT_ASSOC

# Йошкар-Ола (auto UL caller)
# from tts_data.YoshkarOla_tec1_UL_dept_auto_caller_tts_multi import WAV_TXT_ASSOC

# Йошкар-Ола (auto GP caller)
from tts_data.YoshkarOla_tec1_GP_dept_auto_caller_tts_multi import WAV_TXT_ASSOC

from utils_Python_SDK.utilities_python_sdk_tts import synthesize_txt_to_wav_py_sdk
from utilties_helpers.get_full_file_path import get_full_file_normal_path


# multi_data_for_tts = WAV_TXT_ASSOC  # In settings VOICE: str = "filipp" (Омск)
# multi_data_for_tts = WAV_TXT_ASSOC  # In settings VOICE: str = "alena" (ХМАО)
multi_data_for_tts = WAV_TXT_ASSOC  # In settings VOICE: str = "alena"  (Йошкар-Ола)

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
    print(f"All data validated [OK] before TTS synthesizing:\n\n")
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

    print(f"TTS FINISHED SUCCESSFULLY [OK]:\n\n")
