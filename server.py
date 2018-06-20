from flask import Flask, render_template, request
import scraper
import logging
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def enter_name():
    summoner_name = request.form['text']
    lengths = scraper.process(summoner_name)
    labels = list(lengths.keys())[::-1]
    values = list(lengths.values())[::-1]
    max_ = max(values)
    return render_template('chart.html', values=values, labels=labels, max=max_)

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)