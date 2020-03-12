from flask import Flask

app = Flask(__name__)


@app.route('/')
def main():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                  <body>
                    <div>Человечество вырастает из детства.</div>
                    <div>Человечеству мала одна планета.</div>
                    <div>Мы сделаем обитаемыми безжизненные пока планеты.</div>
                    <div>И начнем с Марса!</div>
                    <div>Присоединяйся!</div>
                  </body>
                </html>'''


@app.route('/image_mars')
def image():
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="static/img/mars.png" alt="картинка потерялась">
                    <div>Вот она красная планета</div>
                  </body>
                </html>'''


@app.route('/promotion_image')
def promote_image():
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
                    <link rel="stylesheet" href="static/css/style.css" type="text/css">
                    <title>Колонизация</title>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="static/img/mars.png" alt="картинка потерялась">
                    <div class="alert alert-dark" role="alert">Человечество вырастает из детства.</div>
                    <div class="alert alert-success" role="alert">Человечеству мала одна планета.</div>
                    <div class="alert alert-secondary" role="alert">Мы сделаем обитаемыми безжизненные пока планеты.</div>
                    <div class="alert alert-warning" role="alert">И начнём с Марса!</div>
                    <div class="alert alert-danger" role="alert">Присоединяйся!</div>
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
