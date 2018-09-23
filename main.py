from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<html>

<head>
    <style>
        form {{
            background-color:#eee;
            padding:20px;
            margin:0 auto;
            width:540px;
            font:16px sans-serif;
            border-radius:10px;
        }}

        textarea {{ 
            margin:10px 0;
            width:540px;
            height:120px;
        }}
    </style>
</head>

<body>
    <form method='post'>
        <label>Rotate by
            <input type="text" name="rot" value="0">
        </label>
        <h1><textarea name="text">{0}</textarea></h1>
        <input type="submit" value="Submit Query">
    </form>
</body>

</html>
"""

    
@app.route("/", methods=["POST"])
def encrypt():
    rot = request.form['rot']
    text = request.form['text']
    new_message = rotate_string(text,int(rot)) 
    return form.format(new_message) 


    #TO-DO: Return the encrypted string in <h1> tags.
#    return '<h1>' + return_string + '</h1>'

@app.route("/", methods=['GET'])
def index():
    return form.format("")

app.run()
