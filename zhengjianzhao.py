from flask import Flask, request, render_template
from PIL import Image

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/crop', methods=['POST'])
def crop():
    # 获取上传的文件
    file = request.files['file']

    # 裁剪照片
    image = Image.open(file)
    cropped_image = crop_image(image)

    # 将裁剪后的照片保存到服务器上
    filename = 'cropped_image.jpg'
    cropped_image.save(filename)

    # 返回裁剪后的照片
    return send_file(filename, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)
```
