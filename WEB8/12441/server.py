from flask import Flask

app = Flask(__name__)


@app.route('/')
def main():
    return "Миссия Колонизация Марса"


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def choice(nickname, level, rating):
    return f'''<!doctype html>
            <html lang="en">
              <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
               <link rel="stylesheet"
               href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
               integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
               crossorigin="anonymous">
                <title>Результаты</title>
              </head>
              <body>
                <h1>Результаты отбора</h1>
                <h2>Претендента на участие в миссии {nickname}:</h2>
                <div class="alert alert-success" role="alert">
                    Поздравляем! Ваш рейтинг после {level} этапа отбора
                </div>
               <h3>составляет {rating}!</h3>
                <div class="alert alert-warning" role="alert">
                    Желаем удачи!
                </div>
              </body>
            </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
