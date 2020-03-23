from flask import Flask
from flask import request
from flask import url_for

app = Flask(__name__)


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                             <link rel="stylesheet"
                            href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                             integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                             crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1>Загрузка фотографии</h1>
                              <h3>для участии в миссии</h3>
                            <form method="post" class="login_form" enctype="multipart/form-data">
                             <div class="form-group">
                                    <label for="photo">Приложите фотографию</label>
                                    <input type="file" class="form-control-file" id="photo" name="file">
                                <button type="submit" class="btn btn-primary">Отправить</button>
                           </form>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        file = request.files['file'].read()
        form = request.files['file'].filename.split('.')[-1]
        with open(f'static/img/img.{form}', 'wb') as f:
            f.write(file)
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                             <link rel="stylesheet"
                             href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                             integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                             crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1>Загрузка фотографии</h1>
                              <h3>для участии в миссии</h3>
                            <form method="post" class="login_form" enctype="multipart/form-data">
                              <div class="form-group">
                                    <label for="photo">Приложите фотографию</label>
                                   <input type="file" class="form-control-file" id="photo" name="file">
                                </div>
                              <img src="/static/img/img.{form}" alt="здесь должна была быть ваша картинка">
                                <button type="submit" class="btn btn-primary">Отправить</button>
                            </form>
                          </body>
                        </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
