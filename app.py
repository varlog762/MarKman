from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def render_entry():
    return render_template('entry.html')


if __name__ == '__main__':
    app.run()
