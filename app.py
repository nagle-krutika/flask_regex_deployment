from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test_regex', methods=['POST'])
def test_regex():
    regex_pattern = request.form['regex']
    test_text = request.form['test_text']
    
    try:
        matches = re.findall(regex_pattern, test_text)
        return render_template('results.html', matches=matches)
    except re.error as e:
        return render_template('error.html', error=str(e))

@app.route('/validate_email', methods=['POST'])
def validate_email():
    email = request.form['email']
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    
    if re.match(email_regex, email):
        return jsonify({'valid': True, 'message': 'Valid email address'})
    else:
        return jsonify({'valid': False, 'message': 'Invalid email address'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
