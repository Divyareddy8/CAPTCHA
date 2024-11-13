
# CAPTCHA Verification Project

This project is a simple web-based CAPTCHA verification system built using Flask and Python. It generates a CAPTCHA as an image with random alphanumeric text, applies slight distortions to make it difficult for bots to decipher, and displays it on a web form. Users are required to enter the displayed CAPTCHA text for verification.

## Features

- **Image-Based CAPTCHA**: Generates CAPTCHA as an image with random alphanumeric characters.
- **Distortion for Security**: Adds slight blurring and random noise lines to make automated recognition more challenging.
- **Session-Based Verification**: Uses Flask sessions to securely store and compare CAPTCHA text.
- **Simple and Clean Interface**: The project includes basic HTML and CSS for a clean CAPTCHA form interface.

## Requirements

To run this project, you'll need:

- Python 3.x
- Flask (for web framework)
- Pillow (for generating CAPTCHA images)

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/YourUsername/Captcha-Verification-Project.git
   cd Captcha-Verification-Project
2. **Install Required Dependencies**: 
Install Flask and Pillow via pip

3. Run the Application:
python app.py

