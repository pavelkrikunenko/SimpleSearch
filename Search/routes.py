from Search import app
from flask import request, render_template, jsonify
from Search.services import search, del_post


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/api/get_posts', methods=['GET'])
def get_posts():
    """
     Принимает на вход строку: result
     И возвращает json содержащий 20 статей которые соответствуют запросу
    """
    if 'request' in request.args:
        search_str = request.args['request']
        result = search(search_str)

        return jsonify(result)


@app.route('/api/del_post/<int:id>')
def delete_post(id):
    """
     Принимает id поста который необходимо удалить
    :param id:
    :return: статус операции
    """
    return del_post(id)
