from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        review = request.form['review']
        blob = TextBlob(review)
        polarity = blob.sentiment.polarity
        if polarity > 0:
            result = "Positive"
        elif polarity < 0:
            result = "Negative"
        else:
            result = "Neutral"
    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
