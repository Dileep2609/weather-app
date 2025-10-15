from flask import Flask, render_template_string
app = Flask(__name__)

@app.route('/')
def home():
    html = '''
    <h1>Weather App</h1>
    <p>City: London</p>
    <p>Temperature: 20°C</p>
    <p>Condition: Sunny</p>
    '''
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)