# 各種ライブラリのインポート
import boto3
import json
import sys

# 画像からテキスト取得
def textract_image_to_text(image_file_name):
    # Textractサービスクライアントを作成
    textract = boto3.client('textract', 'us-east-1')
    # 画像ファイルを開く
    with open('image/'+image_file_name, 'rb') as file:
        # 文字列を検出
        result = textract.detect_document_text(
            Document={'Bytes': file.read()})
    text=""
    # 検出されたブロックを順番に処理
    for block in result['Blocks']:
        # ブロックタイプが行かどうかを調べる
        if block['BlockType'] == 'LINE':
            text += block['Text']
    return text

