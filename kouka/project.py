from flask import Flask, render_template, request,send_from_directory
import boto3,polly_synth,textract,comp_language,recognize_celebrities
app = Flask(__name__,static_folder='image')

@app.route('/',methods=['GET'])
def index():
    return render_template('textract.html')

@app.route('/textract',methods=['POST'])
def textract_post():
    try:
        if request.method == 'POST':
            # ファイルを受け取る
            image_file = request.files.get('image_file')
            # ファイルの名前を取得
            image_file_name = image_file.filename
            # 画像を保存
            image_file.save('image/'+image_file_name)
            # 画像ファイルをテキストとして取得
            text = textract.textract_image_to_text(image_file_name)
            # 言語検出
            language = comp_language.comp_language_detect(text)
            # 音声合成
            file_vc = polly_synth.polly_synthesis_mp3(text,image_file_name,language)
            return render_template('textract.html',text=text,file_vc=file_vc)
    except:
            return render_template('textract.html',erro='※画像が正しくありません')

@app.route('/textract')
def textract_page():
    return render_template('textract.html')
# mp3を再生するためのルート
@app.route("/music/<path:filename>")
def play(filename):
    return send_from_directory("music", filename)

@app.route('/recognize_celebrities')
def recognize_celebrities_page():
    return render_template('recognize_celebrities.html')

@app.route('/recognize_celebrities',methods=['POST'])
def recognize_celebrities_post():
    try:
        if request.method == 'POST':
            # ファイルを受け取る
            image_file = request.files.get('image_file')
            # ファイルの名前を取得
            image_file_name = image_file.filename
            # 画像を保存
            image_file.save('image/'+image_file_name)
            # アンパックさせるて受け取る
            big_cast,person_info= recognize_celebrities.recognize_celebrities_person_name(image_file_name)
            return render_template('recognize_celebrities.html',big_cast=big_cast,image_file_name=image_file_name,person_info=person_info)
    except UnboundLocalError:
            return render_template('recognize_celebrities.html',erro='※顔が認識できませんでした。もしくは私が知っているほど有名ではありませんでした。')
    except:       
            return render_template('recognize_celebrities.html',erro='※画像が正しくありません')

if __name__ == '__main__':
    app.run(debug=True)