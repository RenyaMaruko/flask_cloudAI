# 各種ライブラリーのインポート
import boto3
import json
def comp_language_detect(text):
    dict = {
        'en':'Kendra',
        'ja':'Takumi',
    }
    # Comprehend サービスクライアントを作成
    comprehend = boto3.client('comprehend', 'us-east-1')
    # 処理対象の文字列を設定
    # 言語を検出
    result = comprehend.detect_dominant_language(Text=text)
    language = result['Languages'][0]['LanguageCode']
    return dict[language]