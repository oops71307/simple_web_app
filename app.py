import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <style>
            body {
                text-align: center;
                font-family: Arial;
                margin-top: 100px;
            }

            h1 {
                color: blue;
                animation: move 2s infinite alternate;
            }

            @keyframes move {
                from { transform: translateX(-50px); }
                to { transform: translateX(50px); }
            }
        </style>
    </head>
    <body>
        <h1>🚀Hello From Your Python Web App</h1>
        <p>This animation is written inside app.py!</p>
    </body>
    </html>
    """

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
