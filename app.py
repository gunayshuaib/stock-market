from flask import Flask, render_template, jsonify
import yfinance as yf
from datetime import datetime, timedelta

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
    end = datetime.today()
    start = end - timedelta(days=30)
    ticker = yf.Ticker(symbol)
    df = ticker.history(start=start, end=end)
    
    if df.empty:
        return {"dates": [], "close": []}
    
    df = df.reset_index()
    df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
    return {"dates": df['Date'].tolist(), "close": df['Close'].round(2).tolist()}

@app.route("/")
def index():
    return render_template("index.html", symbols=list(symbols.keys()))

@app.route("/data/<name>")
def data(name):
    symbol = symbols.get(name)
    if not symbol:
        return jsonify({"dates": [], "close": []})
    return jsonify(fetch_last_month(symbol))

if __name__ == "__main__":
    app.run(port=5000, debug=True)
