from configs.settings import SDK_TTS_CONFIGS
from configs.yandex_credentials import API_KEY
from tts_data.Test_tts_data_single import file_name_no_ext, rich_text_for_tts
from utils_Python_SDK.utilities_python_sdk_tts import synthesize_txt_to_wav_py_sdk
from utilties_helpers.get_full_file_path import get_full_file_normal_path


# One wav file TTS synthesising (do not delete!!!)
text = rich_text_for_tts.strip()
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
