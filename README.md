# CyberShield - Smart Phishing URL Detection System

CyberShield is a lightweight, AI-inspired web application designed to detect and analyze suspicious or phishing URLs in real-time. Built as part of academic learning and cybersecurity skill development, it provides quick risk assessments and security recommendations for users.

## Features
- *Real-Time URL Analysis:* Evaluates URLs against common phishing patterns (IP addresses, excessive hyphens, suspicious subdomains).
- *Risk Scoring:* Computes a risk score out of 100 with clear risk levels (Low, Medium, High).
- *Interactive Web Interface:* Clean, modern dark-themed UI built for quick testing.

## Tech Stack
- *Backend:* Python, Flask
- *Frontend:* HTML5, CSS3, JavaScript
- *Development Tools:* Visual Studio Code, Git

## Project Structure
cybershield/
│
├── app.py              # Main Flask backend application and URL analysis logic
├── requirements.txt    # Project dependencies list
├── static/
│   └── style.css       # Custom styling and UI design
└── templates/
    └── index.html      # Frontend user interface

## Installation & Setup
1. *Clone or download* this repository to your local machine.
2. Open the project folder in VS Code.
3. Install the required dependencies using pip:
   pip install flask
4. Run the application:
   python app.py
5. Open your web browser and navigate to:
   http://127.0.0.1:5000

## Usage
- Enter any website URL into the input field on the home dashboard.
- Click *Scan URL* to analyze the link.
- Review the generated risk score and threat warnings.

## Author
Developed by **Deepika Rathod** as part of B.Tech Computer Science and Engineering (AI) coursework.
