from flask import Flask, render_template, request, redirect, url_for, session, send_file
import random
import string
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import io

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Replace with a secure key

# Function to generate random CAPTCHA text
def generate_captcha_text():
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choices(characters, k=6))

# Function to generate CAPTCHA image
def generate_captcha_image(captcha_text):
    width, height = 150, 50
    image = Image.new("RGB", (width, height), (255, 255, 255))
    font = ImageFont.truetype("arial.ttf", 30)  # Use a font available on your system
    draw = ImageDraw.Draw(image)

    # Add random characters to image
    for i, char in enumerate(captcha_text):
        draw.text((10 + i * 20, 10), char, font=font, fill=(0, 0, 0))

    # Add noise
    for _ in range(random.randint(10, 30)):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        draw.line((x1, y1, x1 + random.randint(1, 5), y1 + random.randint(1, 5)), fill=(0, 0, 0), width=1)

    # Apply a filter to distort the image
    image = image.filter(ImageFilter.GaussianBlur(1))
    
    # Save to a byte stream
    byte_stream = io.BytesIO()
    image.save(byte_stream, "PNG")
    byte_stream.seek(0)
    return byte_stream

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form.get("captcha_input")
        if user_input == session.get("captcha"):
            return redirect(url_for("result", success=True))
        else:
            return redirect(url_for("result", success=False))

    # Generate a new CAPTCHA and store it in the session
    captcha_text = generate_captcha_text()
    session["captcha"] = captcha_text
    return render_template("index.html")

@app.route("/captcha_image")
def captcha_image():
    # Generate CAPTCHA image based on the stored CAPTCHA text
    captcha_text = session.get("captcha", "")
    image_stream = generate_captcha_image(captcha_text)
    return send_file(image_stream, mimetype="image/png")

@app.route("/result")
def result():
    success = request.args.get("success") == "True"
    return render_template("result.html", success=success)

if __name__ == "__main__":
    app.run(debug=True)
