from flask import Flask, render_template
import random
import os

app = Flask(__name__)

# Get list of meme images
MEME_FOLDER = os.path.join('static', 'images')
meme_images = [os.path.join('images', f) for f in os.listdir(MEME_FOLDER) if f.endswith(('.png', '.jpg', '.jpeg', '.gif'))]

@app.route('/')
def index():
    random_meme = random.choice(meme_images)  # Select a random meme
    return render_template('index.html', meme_url=random_meme)  # Pass the selected meme to the template

if __name__ == '__main__':
    app.run(debug=True)
