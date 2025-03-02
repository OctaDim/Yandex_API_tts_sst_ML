from dataclasses import dataclass


@dataclass
class SDK_TTS_CONFIGS:
    # volume, norm_type, unsafe_mode, language
    VOICE: str = "alena"
    ROLE: str = "neutral"  # 'good' can be as friendly
    SPEED: float = 1.05
    VOLUME: float = None
    WAV_EXPORT_DIRS_PATH = "results", "py_sdk_tts_wav_files"


@dataclass
class GRPC_V3_TTS_CONFIGS:
    # volume, norm_type, unsafe_mode, language
    VOICE: str = "alena"
    ROLE: str = "neutral"  # 'good' can be as friendly
    SPEED: float = 1.05
    VOLUME: float = None
    WAV_EXPORT_DIRS_PATH = "results", "grpc_v3_tts_wav_files"
