from dataclasses import dataclass


@dataclass
class SDK_TTS_CONFIGS:
    # volume, norm_type, unsafe_mode, language
    VOICE: str = "filipp"
    # VOICE: str = "alena"
    ROLE: str = None  # 'good' can be as friendly
    # ROLE: str = "neutral"  # 'good' can be as friendly
    SPEED: float = 1.05
    VOLUME: float = None
    WAV_EXPORT_DIRS_PATH = "actions_results", "py_sdk_tts_wav_files"


@dataclass
class GRPC_V3_TTS_CONFIGS:
    # volume, norm_type, unsafe_mode, language
    VOICE: str = "filipp"
    # VOICE: str = "alena"
    ROLE: str = None  # 'good' can be as friendly
    # ROLE: str = "neutral"  # 'good' can be as friendly
    SPEED: float = 1.05
    VOLUME: float = None
    WAV_EXPORT_DIRS_PATH = "actions_results", "grpc_v3_tts_wav_files"


@dataclass
class BOTO_V3_CONFIGS:
    SERVICE_NAME: str = "s3"
    ENDPOINT_URL: str = "https://storage.yandexcloud.net"
    TO_STORAGE_PATH = "actions_results", "s3_to_storage_files"
    FROM_STORAGE_PATH = "actions_results", "s3_from_storage_files"
