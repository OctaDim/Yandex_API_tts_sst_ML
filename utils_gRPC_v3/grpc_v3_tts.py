import io
import os
from typing import Optional

import grpc
import pydub
import yandex.cloud.ai.tts.v3.tts_pb2 as tts_pb2
import yandex.cloud.ai.tts.v3.tts_service_pb2_grpc as tts_service_pb2_grpc

from utilties_helpers.validate_dir_file import validate_dirs_file_path


def synthesize_txt_to_wav_grps_v3(text_for_tts: str,
                                  file_export_path: str,
                                  iam_token: Optional[str] = None,
                                  api_key: Optional[str] = None,
                                  voice: str = None,
                                  role: str = None,
                                  speed: float = None,
                                  volume: float = None,
                                  ) -> pydub.AudioSegment | None:
    if not iam_token and not api_key:
        print(f"Error: Define IAM-token or API-key: "
              f"IAM={iam_token}, API={api_key}")
        return

    if not validate_dirs_file_path(file_export_path):
        return

    try:
        # hints == tts parameters (optional)
        hints = []
        hints.append(tts_pb2.Hints(voice=voice)) if voice else None
        hints.append(tts_pb2.Hints(role=role)) if role else None
        hints.append(tts_pb2.Hints(speed=speed)) if speed else None
        hints.append(tts_pb2.Hints(volume=volume)) if volume else None

        request = tts_pb2.UtteranceSynthesisRequest(
            text=text_for_tts,
            output_audio_spec=tts_pb2.AudioFormatOptions(
                container_audio=tts_pb2.ContainerAudio(
                    container_audio_type=tts_pb2.ContainerAudio.WAV)),
            hints=hints,
            loudness_normalization_type=tts_pb2.UtteranceSynthesisRequest.LUFS)

        # Server connection
        cred = grpc.ssl_channel_credentials()
        channel = grpc.secure_channel('tts.api.cloud.yandex.net:443', cred)
        stub = tts_service_pb2_grpc.SynthesizerStub(channel)

        auth_data = f"Bearer {iam_token}" if iam_token else f"Api-Key {api_key}"

        # Synthesis data
        it = stub.UtteranceSynthesis(request, metadata=(
            ('authorization', auth_data),
        ))

        # Assembling the audio in portions
        audio_data = io.BytesIO()
        for response in it:
            audio_data.write(response.audio_chunk.data)
        audio_data.seek(0)
        result = pydub.AudioSegment.from_wav(audio_data)

        with open(file_export_path, 'wb') as file_data:
            result.export(file_data, format='wav')

            file_name = os.path.basename(file_export_path)
            dir_name = os.path.dirname(file_export_path)
            print(f"Result: File <{file_name}> created [OK]: {dir_name}")

    except grpc._channel._Rendezvous as error:
        print(f"Error code: {error._state.code}, error: {error._state.details}")
    except Exception as error:
        print(f"Error: {error}")
        return
