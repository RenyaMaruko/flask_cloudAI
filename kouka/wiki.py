import wikipedia
# 日本語の情報を指定
wikipedia.set_lang("jp")
def info_big_cast(name):
    # 人物名を指定
    person_name = name
    # Wikipediaから情報を取得
    person_info = wikipedia.summary(person_name)
    # 情報を返却
    return (person_info)
