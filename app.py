from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    try:
        response = requests.get('https://zenquotes.io/api/random')
        data = response.json()
        quote = data[0]['q']
        author = data[0]['a']
    except Exception as e:
        quote = "Произошла ошибка при получении цитаты."
        author = f"— {e}"
    return render_template('index.html', quote=quote, author=author)

if __name__ == '__main__':
    app.run(debug=True)