from flask import Flask, request
from caesar import rotate_string
app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method="POST">
            <label name="rot">Rotate by:</label>
            <input type="text" name="rot" placeholder="0">
            <textarea rows="5" cols="50" name="text" placeholder="Enter your message here...">{0}</textarea>
        <input type="submit" value="Submit Query">
        </form>
    </body>
</html>
"""

@app.route("/", methods=['POST'])
def encrypt():
    rot = request.form['rot'] 
    text = request.form['text']
    encrypted = rotate_string(text,rot)
    return form.format(str(rotate_string(text,rot)))  
    

@app.route("/")
def index():
    return form.format('')

app.run()