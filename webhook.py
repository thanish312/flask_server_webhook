from flask import Flask, request, jsonify
import logging
import os

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG,  # Set to DEBUG to capture all logs
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("webhook.log"),  # Log to file
                        logging.StreamHandler()  # Log to console
                    ])

@app.route('/webhook', methods=['POST'])
def webhook():
    app.logger.debug("Webhook endpoint hit.")  # Debug log for endpoint hit
    if request.method == 'POST':
        data = request.json
        app.logger.debug(f"Received webhook data: {data}")  # Log the received data
        if data is None:
            app.logger.error("No JSON data received.")  # Log error if no data
            return jsonify({"error": "No JSON data received."}), 400
        
        body = data.get('Body', None)
        app.logger.debug(f"Filtered body: {body}")  # Log the filtered body
        return jsonify({"message": "Webhook received!", "body": body}), 200
    else:
        app.logger.error("Only POST requests are accepted!")  # Log error for wrong method
        return jsonify({"error": "Only POST requests are accepted!"}), 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use PORT env variable or default to 5000
    app.run(debug=True, host='0.0.0.0', port=port)
