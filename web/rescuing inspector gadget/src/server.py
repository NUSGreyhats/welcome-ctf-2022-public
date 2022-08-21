import base64
from flask import Flask, redirect, render_template, render_template_string, request, session
from random import randint, choice
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from constants import FLAG, SECRET_KEY


app = Flask(__name__)
app.secret_key = SECRET_KEY
font = ImageFont.truetype('./arial.ttf', 32)

OPERATORS = ["+", "-", "*"]


def generate_number(max_number: int = 10000, min_number: int = 1):
    """Generate a random positive number from 1 to max_number"""
    return randint(min_number, max_number)


def generate_b64_image(text: str) -> str:
    """Generate a base64 image based on text"""
    img = Image.new('RGB', (500, 200), color=(255, 255, 255))
    ImageDraw.Draw(img).text((0, 100), text, fill=(
        0, 0, 0), align='center', font=font)
    img.resize((10000, 3000), Image.ADAPTIVE)
    buffered = BytesIO()
    img.save(buffered, format="png", optimize=True)
    return base64.b64encode(buffered.getvalue()).decode('utf-8')


def generate_question():
    """Generate questions for the website"""
    acc = []
    for i in range(3):
        if i > 0:
            acc.append(choice(OPERATORS))
        acc.append(str(generate_number()))

    eqn = f"".join(acc)
    return {
        'question': eqn,
        'answer': eval(eqn)
    }


@app.route("/", methods=["GET", "POST"])
def index():
    if 'ans' not in session:
        qn_dict = generate_question()
        session['ans'] = qn_dict['answer']
        session['question'] = qn_dict['question']
        session['score'] = 0

    # Get request from the user
    if request.method == "GET":
        if session['score'] < 5000000:
            return render_template("index.html", question=generate_b64_image(session['question']), score=session['score'])
        return render_template_string(FLAG)

    # Post request from the user
    data = request.form
    if 'ans' not in data:
        return redirect("/")

    # Check if the answer is correct
    try:
        if int(data['ans']) == int(session['ans']):
            session['score'] += 1
        else:
            session['score'] = 0
    except ValueError:
        session['score'] = 0

    qn_dict = generate_question()
    session['ans'] = qn_dict['answer']
    session['question'] = qn_dict['question']
    return redirect("/")
