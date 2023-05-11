import boto3
import wiki
# 有名人検索
def recognize_celebrities_person_name(photo):
    client = boto3.client('rekognition')
    with open('image/'+photo, 'rb') as image:
        response = client.recognize_celebrities(Image={'Bytes': image.read()})
    # 有名人の名前を取得
    for celebrity in response['CelebrityFaces']:
        name = celebrity['Name']
    # その人物の情報を取得する関数を呼び出す
        person_info = wiki.info_big_cast(name)
    # (names,person_info) このタプル型で返却される。
    return (name,person_info)
