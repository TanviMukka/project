from flask import Flask, render_template, request, jsonify
from generator import generate_plan

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('study-planner-mockup.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()

    plan_text = generate_plan(
        subject = data['subject'],
        topic = data['topic'],
        days = int(data['days']),
        hours = int(data['hours']),
        difficulty = data['difficulty']
    )

    return jsonify({"plan": plan_text})

if __name__ == '__main__':
    app.run(debug=True)