from dataclasses import dataclass


@dataclass
class SDK_TTS_CONFIGS:  # volume, norm_type, unsafe_mode, language
    # TEST ALENA (alena, intonation "neutral", can be 'good' as friendly)
    # VOICE: str = "alena"
    # ROLE: str = "neutral"
    # SPEED: float = 1.05
    # VOLUME: float = None
    # WAV_EXPORT_DIRS_PATH = ("audio_wav_results", "py_sdk_tts_wav_files", "test_voice_robots")


    # KIROV (alena, intonation "neutral", can be 'good' as friendly)
    # VOICE: str = "alena"
    # ROLE: str = "neutral"
    # SPEED: float = 1.05
    # VOLUME: float = None
    # WAV_EXPORT_DIRS_PATH = ("audio_wav_results", "py_sdk_tts_wav_files", "Kirov", "confirm_appointment")


    # OMSK (filipp, no intonation can be defined)
    # VOICE: str = "filipp"
    # ROLE: str = None
    # SPEED: float = 1.05
    # VOLUME: float = None
    # WAV_EXPORT_DIRS_PATH = ("audio_wav_results", "py_sdk_tts_wav_files", "Omsk", "mfc")


    # YOSHKAROLA (alena, intonation "neutral", can be 'good' as friendly)
    VOICE: str = "alena"
    ROLE: str = "neutral"
    SPEED: float = 1.05
    VOLUME: float = None
    WAV_EXPORT_DIRS_PATH = ("audio_wav_results", "py_sdk_tts_wav_files", "yoshkarola_tec1_GP_debt_auto_caller")
    # WAV_EXPORT_DIRS_PATH = ("audio_wav_results", "py_sdk_tts_wav_files", "yoshkarola_tec1_UL_debt_auto_caller")
    # WAV_EXPORT_DIRS_PATH = ("audio_wav_results", "py_sdk_tts_wav_files", "yoshkarola_tec1_debt_auto_caller")
    # WAV_EXPORT_DIRS_PATH = ("audio_wav_results", "py_sdk_tts_wav_files", "yoshkarola_tec1_auto_informer")
    # WAV_EXPORT_DIRS_PATH = ("audio_wav_results", "py_sdk_tts_wav_files", "yoshkarola_tec1_counter_reception")
    # WAV_EXPORT_DIRS_PATH = ("audio_wav_results", "py_sdk_tts_wav_files", "HMAO", "appointment")
    # WAV_EXPORT_DIRS_PATH = ("audio_wav_results", "py_sdk_tts_wav_files", "HMAO", "TEST-DELETE")
    # WAV_EXPORT_DIRS_PATH = ("audio_wav_results", "py_sdk_tts_wav_files", "common_duration_get")


    # # HMAO (alena, intonation "neutral", can be 'good' as friendly)
    # VOICE: str = "alena"
    # ROLE: str = "neutral"
    # SPEED: float = 1.05
    # VOLUME: float = None
    # # WAV_EXPORT_DIRS_PATH = ("audio_wav_results", "py_sdk_tts_wav_files", "HMAO", "mfc (28.05.2025)-1 (28.05.2025)")
    # WAV_EXPORT_DIRS_PATH = ("audio_wav_results", "py_sdk_tts_wav_files", "HMAO", "questions_extra")
    # WAV_EXPORT_DIRS_PATH = ("audio_wav_results", "py_sdk_tts_wav_files", "HMAO", "sound_root_directory")
    # WAV_EXPORT_DIRS_PATH = ("audio_wav_results", "py_sdk_tts_wav_files", "HMAO", "status")
    # WAV_EXPORT_DIRS_PATH = ("audio_wav_results", "py_sdk_tts_wav_files", "HMAO", "appointment")
    # WAV_EXPORT_DIRS_PATH = ("audio_wav_results", "py_sdk_tts_wav_files", "HMAO", "TEST-DELETE")


    # (alena, intonation "neutral", can be 'good' as friendly)
    # VOICE: str = "alena"
    # ROLE: str = "neutral"
    # SPEED: float = 1.05
    # VOLUME: float = None
    # WAV_EXPORT_DIRS_PATH = ("audio_wav_results", "py_sdk_tts_wav_files", "ATTENTION_DEFINE_ROBOT_DIRECTORY")


@dataclass
class GRPC_V3_TTS_CONFIGS:
    pass
    # volume, norm_type, unsafe_mode, language
    # VOICE: str = "filipp"  # Omsk_mfc
    # VOICE: str = "alena"
    # ROLE: str = None  # for "filipp" no intonation can be defined
    # ROLE: str = "neutral"  # for "alena" can be 'good' as friendly
    # SPEED: float = 1.05
    # VOLUME: float = None
    # WAV_EXPORT_DIRS_PATH = ("audio_wav_results",
    #                         "grpc_v3_tts_wav_files",
    #                         "Omsk")


@dataclass
class BOTO_V3_CONFIGS:
    pass
    # SERVICE_NAME: str = "s3"
    # ENDPOINT_URL: str = "https://storage.yandexcloud.net"
    # TO_STORAGE_PATH = "audio_wav_results", "s3_to_storage_files"
    # FROM_STORAGE_PATH = "audio_wav_results", "s3_from_storage_files"
