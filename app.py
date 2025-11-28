from flask import Flask, render_template, jsonify
import yfinance as yf
import datetime

app = Flask(__name__)

symbols = {
    "S&P 500": "^GSPC",
    "NASDAQ": "^IXIC",
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Google": "GOOGL",
    "Amazon": "AMZN",
    "Meta": "META",
    "Nvidia": "NVDA",
    "Tesla": "TSLA"
}

def fetch_last_month(symbol):
    end = datetime.datetime.today()
    start = end - datetime.timedelta(days=30)
    data = yf.download(symbol, start=start, end=end)
    return {
        "dates": data.index.strftime("%Y-%m-%d").tolist(),
        "close": data["Close"].round(2).tolist()
    }

@app.route("/")
def index():
    return render_template("index.html", symbols=list(symbols.keys()))

@app.route("/data/<name>")
def data(name):
    symbol = symbols[name]
    return jsonify(fetch_last_month(symbol))

if __name__ == "__main__":
    app.run(port=5000, debug=True)
