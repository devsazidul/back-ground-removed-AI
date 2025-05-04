from flask import Flask, render_template, request, send_file
from rembg import remove
from PIL import Image
import io

app = Flask(__name__)

# Route to render the page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle image upload and background removal
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['image']
    if not file:
        return "No file uploaded", 400

    input_image = Image.open(file.stream)
    output_image = remove(input_image)
    
    img_byte_arr = io.BytesIO()
    output_image.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    
    return send_file(img_byte_arr, mimetype='image/png', as_attachment=True, download_name='output.png')

if __name__ == '__main__':
    app.run(debug=True)
