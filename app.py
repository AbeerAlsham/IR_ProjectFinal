from flask import Flask, render_template, request, jsonify
from controllers import search as search_controller
from controllers import refine
from application import initializer

app = Flask(__name__)

initializer.load()


@app.route('/')
def index():
    return render_template('search.html')


@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query', '')
    dataset = request.form.get('dataset', '')
    language = request.form.get('language', '')
    spellcheck = request.form.get('spellcheck', '')
    
    search_results = search_controller.search_doc(query, dataset, language, spellcheck)
    # Render the results.html template with the search results
    return render_template('results.html', query=query, dataset=dataset, language=language, results=search_results, spellcheck=spellcheck)

    
@app.route('/suggest', methods=['POST'])
def suggest():
    query = request.json['query']
    dataset = request.json['dataset']
    language = request.json['language']
    
    suggestions = refine.suggest(query, dataset)
    
    return jsonify(suggestions)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

