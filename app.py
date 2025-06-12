from flask import Flask, jsonify, request, render_template
from recommender import get_genres, recommend_movies_by_genre

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['GET'])
def users():
    return jsonify(get_genres())

@app.route('/recommend', methods=['GET'])
def recommend():
    user = request.args.get('user')
    if not user:
        return jsonify([])
    return jsonify(recommend_movies_by_genre(user))

if __name__ == '__main__':
    app.run(debug=True)
