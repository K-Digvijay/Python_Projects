import flask
from flask import Flask,render_template,request,jsonify
# from openai import OpenAI
import openai
import base64
import os

from sympy import preview
from io import BytesIO
from dotenv import load_dotenv

load_dotenv()

# client = openai.ChatCompletion.create(api_key=os.getenv('OPENAI_API_KEY'))

app = Flask(__name__)

SYSTEM_PROMT = "You are a LaTeX generation model. The user will give you the name or description of a formula. If you know it you provide the LaTeX code that visualizes it. Nothing more. No text or explanation. Under no circumstances EVER provide anything but LaTeX code. No clarification. No context. Nothing. Make sure the formulas are properly enclosed using dollar signs."

@app.route('/',methods=['GET','POST'])
def index():
    latex_code = None
    latex_image = None

    if request.method == 'POST':
        formula_desc = request.form.get('formula_description')
        response = openai.ChatCompletion.create(model = 'gpt-4o',
        message = [
            {'role':'system','content':SYSTEM_PROMT},
            {'role':'user','content':formula_desc},
        ])
        latex_code = request.choices[0]['message']['content'].strip()

        buffer = BytesIO()
        preview(latex_code,
                viewer = 'ByteIO',
                outputbuffer = buffer,
                euler = False,
                divoptions=['-D','300'])
        latex_image = base64.b64encode(buffer.getvalue()).decode('utf-8')

    return render_template('index.html',latex_code=latex_code,latex_image=latex_image)

if __name__ == "__main__":
    app.run(debug=True)



