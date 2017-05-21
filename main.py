from flask import Flask, request, redirect, url_for, jsonify
import numpy as np
from model import articles
from flask.ext.cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def index():
    lat = request.args.get('lat')
    lng = request.args.get('lng')
    date = request.args.get('date')
    article = articles.getArticles(lat, lng, date)
    response = jsonify({'results': article})
    response.status_code = 200
    return response


@app.route('/list')
def list():
    word = request.args.get('word')
    articless = articles.getArticlesByWord(word)
    lis = ''
    for article in articless:
        lis += '<div>' + article[0] + '</div>'
    return lis

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
