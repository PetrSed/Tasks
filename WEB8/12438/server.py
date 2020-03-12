from flask import Flask
from flask import request
from flask import url_for

app = Flask(__name__)


@app.route('/')
def main():
    return "Миссия Колонизация Марса"


@app.route('/choice/<planet_name>', methods=['POST', 'GET'])
def choice(planet_name):
    return f'''<!doctype html>
            <html lang="en">
              <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
               <link rel="stylesheet"
               href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
               integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
               crossorigin="anonymous">
                <title>Варианты выбора</title>
              </head>
              <body>
                <h1>Мое предложение: {planet_name}!</h1>
                <h2>Эта планета близка к Земле;</h2>
                <div class="alert alert-success" role="alert">
                    На ней много необходимых ресурсов;
                </div>
                <div class="alert alert-secondary" role="alert">
                    На ней есть вода и атмосфера;
                </div>
                <div class="alert alert-warning" role="alert">
                    На ней есть небольшое магнитное поле;
                </div>
                <div class="alert alert-danger" role="alert">
                    Наконец, она просто красива!
                </div>
              </body>
            </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
