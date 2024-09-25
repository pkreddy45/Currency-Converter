from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "a9b45491b7fe84334ac483d8" 
API_URL = "https://api.exchangerate-api.com/v4/latest/USD"  

@app.route('/', methods=['GET', 'POST'])
def index():
    converted_amount = None
    target_currency = None

    if request.method == 'POST':
        amount = request.form['amount']
        target_currency = request.form['target_currency'].upper()

        # Make an API call with the API key included in the request
        response = requests.get(f"{API_URL}?apikey={API_KEY}")
        data = response.json()

        # Check if the target currency exists in the API data
        if target_currency in data['rates']:
            conversion_rate = data['rates'][target_currency]
            converted_amount = float(amount) * conversion_rate
        else:
            converted_amount = "Currency not supported."

    if request.method == 'Get':
        converted_amount = None     

    return render_template('index.html', converted_amount=converted_amount, target_currency=target_currency)

if __name__ == '__main__':
    app.run(debug=True)
