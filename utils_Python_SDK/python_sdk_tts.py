import os.path
from typing import Optional

from speechkit import configure_credentials, creds, model_repository

from utilties_helpers.validate_dir_file import validate_dirs_file_path


def synthesize_txt_to_wav_py_sdk(text_for_tts: str,
                                 file_export_path: str,
                                 iam_token: Optional[str] = None,
                                 api_key: Optional[str] = None,
                                 voice: str = None,
                                 role: str = None,
                                 speed: float = None,
                                 volume: float = None
                                 ) -> None:
    if not iam_token and not api_key:
        print(f"Error: Define IAM-token or API-key: "
              f"IAM={iam_token}, API={api_key}")
        return

    if not validate_dirs_file_path(file_export_path):
        return

    tts_model = model_repository.synthesis_model()
    tts_model.voice = voice
    tts_model.role = role
    tts_model.speed = speed
    tts_model.volume = volume

    try:
        configure_credentials(
            yandex_credentials=creds.YandexCredentials(
                iam_token=iam_token,
                api_key=api_key))

        result = tts_model.synthesize(text=text_for_tts,
                                      raw_format=False)
        result.export(out_f=file_export_path, format="wav")

        file_name = os.path.basename(file_export_path)
        dir_name = os.path.dirname(file_export_path)
        print(f"Result: File <{file_name}> created [OK]: {dir_name}")

    except Exception as error:
        print(f"Error: {error}")
