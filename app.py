from flask import Flask, render_template

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Product-specific routes
@app.route('/milk')
def milk():
    return render_template('milk.html')

@app.route('/curd')
def curd():
    return render_template('curd.html')

@app.route('/ghee')
def ghee():
    return render_template('ghee.html')

@app.route('/paneer')
def paneer():
    return render_template('paneer.html')

@app.route('/sweets')
def sweets():
    return render_template('sweets.html')

@app.route('/snacks')
def snacks():
    return render_template('snacks.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
