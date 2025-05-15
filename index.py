from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    html = """
    <html>
        <head><title>Welcome</title></head>
        <body>
            <h1>Hello from Flask!</h1>
        </body>
    </html>
    """
    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)
