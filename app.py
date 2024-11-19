from flask import Flask, render_template
import yfinance as yf
import json

app = Flask(__name__)

@app.route('/')
def index():
    # Získání historických dat o Bitcoinu z Yahoo Finance
    btc_data = yf.Ticker("BTC-USD")
    hist = btc_data.history(period="1y")  # Získáme posledních 7 dní
    
    # Převedení dat na formát vhodný pro Chart.js
    dates = hist.index.strftime('%Y-%m-%d').tolist()  # datumy
    prices = hist['Close'].tolist()  # uzavírací ceny

    # Předání dat do šablony
    return render_template('index.html', dates=json.dumps(dates), prices=json.dumps(prices))

if __name__ == '__main__':
    app.run(debug=True)
