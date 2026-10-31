# Scam Message Investigator

## Project Description
Scam Message Investigator is an AI-powered web application that analyzes suspicious SMS, email, and WhatsApp messages to identify potential scams and phishing attempts. It uses the Gemma 3:1B language model through Ollama to examine messages and generate a detailed investigation report.

## Features
- Analyze suspicious messages using AI.
- Identify potential scam risk levels (High, Medium, Low).
- Detect common warning signs and suspicious patterns.
- Generate explanations for suspicious messages.
- Provide safety recommendations to users.
- Simple and user-friendly web interface.

## Technologies Used
- Python
- Streamlit
- Ollama
- Gemma 3:1B
- Requests

## Project Structure
```text
Scam_Message_Investigator/
│
├── app.py
├── requirements.txt
└── README.md
```

## How It Works
1. Enter a suspicious message into the application.
2. Click the Investigate Message button.
3. The message is sent to the Gemma AI model.
4. The AI analyzes the message and identifies possible warning signs.
5. An investigation report is generated with risk level, explanation, and safety recommendations.

## Expected Output
The application generates an investigation report containing:
- Risk Level
- Warning Signs
- Explanation
- Safety Recommendations
- <img width="1300" height="1039" alt="image" src="https://github.com/user-attachments/assets/de7204db-aace-40f0-b6b0-2eebb44da2be" />

## Conclusion
The Scam Message Investigator project successfully demonstrates how Artificial Intelligence can be used to identify potential scam and phishing messages. By using Python, Streamlit, Ollama, and the Gemma 3:1B model, the application analyzes suspicious messages, identifies warning signs, determines possible risk levels, and provides useful safety recommendations. This project helps users become more aware of online scams and encourages safer digital communication. It also provides practical experience in AI integration and Python application development.
