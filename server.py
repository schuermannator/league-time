from flask import Flask, render_template, request
import scraper
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

if __name__ == '__main__':
    app.run()