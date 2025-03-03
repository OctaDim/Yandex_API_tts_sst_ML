from configs.settings import GRPC_V3_TTS_CONFIGS
from configs.yandex_credentials import API_KEY
from queries.data_multi_for_tts import file_name_no_ext, rich_text_for_tts
from utils_gRPC_v3.utilities_grpc_v3_tts import synthesize_txt_to_wav_grps_v3
from utilties_helpers.get_full_file_path import get_full_file_normal_path


text = rich_text_for_tts.strip()
file_name_no_ext = file_name_no_ext.strip()
file_name_with_ext = file_name_no_ext + ".wav"
file_export_path = GRPC_V3_TTS_CONFIGS.WAV_EXPORT_DIRS_PATH

normal_path = get_full_file_normal_path(all_dirs_path=file_export_path,
                                        file_name=file_name_with_ext)

synthesize_txt_to_wav_grps_v3(api_key=API_KEY,
                              text_for_tts=text,
                              file_export_path=normal_path,
                              voice=GRPC_V3_TTS_CONFIGS.VOICE,
                              role=GRPC_V3_TTS_CONFIGS.ROLE,
                              speed=GRPC_V3_TTS_CONFIGS.SPEED,
                              volume=GRPC_V3_TTS_CONFIGS.VOLUME)
