from flask import Flask, request, render_template, jsonify
from recommendation import get_movie_recommendations, get_movie_suggestions

app = Flask(__name__)  # Corrected __name__

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/suggest', methods=['GET'])
def suggest():
    query = request.args.get("term", "")
    return jsonify(get_movie_suggestions(query))

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    movie_name = data.get("movie_name", "").strip()

    recommendations = get_movie_recommendations(movie_name)
    return jsonify({"recommendations": recommendations})

if __name__ == "__main__":  # Corrected __name__
    app.run(debug=True)










