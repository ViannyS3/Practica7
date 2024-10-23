from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://fonts.googleapis.com/css2?family=Pacifico&display=swap" rel="stylesheet">
        <style>
            body {
                font-family: 'Pacifico', cursive;
                background-color: #f0f8ff;  /* Un color de fondo suave */
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                color: #333;  /* Color del texto */
            }
            h1 {
                font-size: 4rem;
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
            }
        </style>
    </head>
    <body>
        <h1>Hola, soy Vianny desde Docker!</h1>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
