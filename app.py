from flask import Flask\napp = Flask(__name__)\n@app.route('/')\ndef home():\n    return '🚀 Hello, World! Your site is live!'\n\nif __name__ == '__main__':\n    app.run(host='0.0.0.0', port=10000)
