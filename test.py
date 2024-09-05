from flask import Flask, request, jsonify
from twilio.rest import Client
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Get user credentials
openai_api_key = input("Enter your OpenAI API key: ")
account_sid = input("Enter your Twilio Account SID: ")
auth_token = input("Enter your Twilio Auth Token: ")
twilio_whatsapp_number = input("Enter your Twilio WhatsApp number (e.g., whatsapp:+14155238886): ")

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        incoming_message = request.form.get('Body')
        from_number = request.form.get('From')

        app.logger.debug(f"Received message: {incoming_message} from {from_number}")

        # Use the mock response instead of the actual OpenAI API call
        response_message = get_mock_response(incoming_message)

        app.logger.debug(f"Generated response: {response_message}")

        # Respond to Twilio with the generated message
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=response_message,
            from_=twilio_whatsapp_number,  # User's Twilio Sandbox number
            to=from_number
        )

        return 'Message received', 200

    except Exception as e:
        app.logger.error(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

def get_mock_response(message):
    # Simulated response function
    return f"Simulated response for message: {message}"

if __name__ == '__main__':
    app.run(debug=False)  # Set debug to False for production use
