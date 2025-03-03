import os

from configs.yandex_credentials import BASE_DIR


def get_full_file_normal_path(all_dirs_path: tuple[str],
                              file_name: str
                              ) -> str:
    results_wav_path = os.path.join(BASE_DIR, *all_dirs_path, file_name)
    normalized_path = os.path.normpath(results_wav_path)

    return normalized_path
