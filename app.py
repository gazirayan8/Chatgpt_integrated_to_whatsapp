from flask import Flask, request, jsonify
import openai
from twilio.rest import Client
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Prompt user to input their OpenAI API key, Twilio credentials, and WhatsApp number
openai_api_key = input("Enter your OpenAI API key: ")
account_sid = input("Enter your Twilio Account SID: ")
auth_token = input("Enter your Twilio Auth Token: ")
twilio_whatsapp_number = input("Enter your Twilio WhatsApp number (e.g., whatsapp:+14155238886): ")

# Set OpenAI API key
openai.api_key = openai_api_key

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        incoming_message = request.form.get('Body')
        from_number = request.form.get('From')
        
        app.logger.debug(f"Received message: {incoming_message} from {from_number}")
        
        # Generate a response from OpenAI's GPT model using the new API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Replace with your chosen model
            messages=[
                {"role": "user", "content": incoming_message}
            ]
        )
        response_message = response.choices[0].message['content'].strip()

        app.logger.debug(f"Generated response: {response_message}")
        
        # Respond to Twilio with the generated message
        client = Client(account_sid, auth_token)
        
        client.messages.create(
            body=response_message,
            from_=twilio_whatsapp_number,  # User-specified Twilio WhatsApp number
            to=from_number
        )

        return 'Message received', 200

    except Exception as e:
        # Log the error for debugging
        app.logger.error(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False)

 

 



