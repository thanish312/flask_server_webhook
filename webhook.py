from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='webhook.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        data = request.json
        logging.info(f"Received webhook data: {data}")  # Log the received data
        body = data.get('Body', None)
        logging.info(f"Filtered body: {body}")  # Log the filtered body
        return jsonify({"message": "Webhook received!"}), 200
    else:
        return jsonify({"message": "Only POST requests are accepted!"}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
