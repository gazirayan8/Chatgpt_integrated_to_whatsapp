# Chatgpt_integrated_to_whatsapp
he project integrates OpenAI's GPT-3.5 Turbo model with Twilio's WhatsApp API to create a chatbot. Users can send messages to a WhatsApp number, and the chatbot will generate intelligent responses using OpenAI's API. The project allows users to provide their own OpenAI and Twilio credentials during runtime, ensuring flexibility and security.

**How the Project Works**
1)User Message:
A user sends a message to a designated WhatsApp number.

2)Webhook Trigger:
The message is received by the Flask webhook server.

Response Generation:
i-> In the main code: The message is forwarded to OpenAI's GPT-3.5 model, which generates an appropriate response.
ii-> In the mock test code: A simulated response is generated to test the Twilio integration without using OpenAI.

3)Response Sent: 
The generated response is sent back to the user's WhatsApp number using Twilio's API.

**Key Features**
1)Customizable API Integration: 
Users can enter their own API credentials during runtime.
2)Seamless WhatsApp Integration: 
Twilio API handles sending and receiving messages through WhatsApp.
3)OpenAI GPT Model:
Leverages OpenAI’s powerful language model to create intelligent chatbot responses.
4)Mock Test Environment: 
Simulated responses allow users to test the chatbot without using the OpenAI API, saving costs during development.

Notes
i) Make sure you have enabled the Twilio WhatsApp sandbox or configured a proper WhatsApp Business number to use the Twilio integration.
ii) The mock test code is ideal for testing Twilio's functionality without actual OpenAI API usage.
iii) Always safeguard your API keys and credentials in production environments by using environment variables or configuration files instead of hardcoding.
