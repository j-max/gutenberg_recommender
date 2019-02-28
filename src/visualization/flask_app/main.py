from flask import Flask, request, render_template
from recom import recommender, cosine_recommender

app = Flask(__name__)

@app.route('/')
def entry_page():
	return render_template('index.html')

@app.route('/recommend_book/', methods=['GET', 'POST'])
def recommender():
	sample_text = ['sample_text']

	user_input = request.form['sample_text']
	
	book_rec = cosine_recommender(user_input)
	return render_template('index.html', message=book_rec)

if __name__ == '__main__':
	app.run()
