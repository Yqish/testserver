from flask import Flask, render_template, url_for, request, session

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html', form=form)
    

if __name__ == '__main__':
    app.run(port = 5000)
