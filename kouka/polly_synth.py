# boto3 をインポート
import boto3
# contextlib をインポート
import contextlib
# os をインポート
import os
import sys

def polly_synthesis_mp3(text,image_file_name,language):
    # リージョンを指定して、Polly サービスクライアントを作成
    polly = boto3.client('polly', 'us-east-1')
    # 音声合成する
    
    result = polly.synthesize_speech(
        Text=text,# 音声合成するテキスト
        OutputFormat='mp3', # 音声のフォーマット
        VoiceId=language,# 音声ID
    )
    # 出力ファイルのパス
    path_name = image_file_name.replace('jpg','mp3')
    path = 'music/'+ path_name
    # 音声のストリームを開く
    with contextlib.closing(result['AudioStream']) as stream:
        # 出力ファイルを開く
        with open(path, 'wb') as file:
        # 音声を読み込んで出力ファイルに書き込む
            file.write(stream.read())
    return path

