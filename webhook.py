from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        data = request.json
        print(f"Received webhook data: {data}")
        process_data(data)  # Process the webhook data here
        return jsonify({"message": "Webhook received!"}), 200
    else:
        return jsonify({"message": "Only POST requests are accepted!"}), 400

def process_data(data):
    # Extract the body from the Twilio webhook
    body = data.get('Body', None)
    # Further processing can be done here
    print(f"Filtered body: {body}")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
