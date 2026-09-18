from flask import Flask, render_template, request, jsonify
from generator import generate_plan

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('study-planner-mockup.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()

    required_fields = ['subject', 'topic', 'days', 'hours', 'difficulty']
    if not data or not all(data.get(f) for f in required_fields):
        return jsonify({"error": "Please fill in all fields."}), 400

    try:
        plan_text = generate_plan(
            subject = data['subject'],
            topic = data['topic'],
            days = int(data['days']),
            hours = int(data['hours']),
            difficulty = data['difficulty']
        )
    except ValueError:
        return jsonify({"error": "Days and hours must be valid numbers."}), 400
    except Exception as e:
        return jsonify({"error": f"Failed to generate plan: {e}"}), 500

    return jsonify({"plan": plan_text})

if __name__ == '__main__':
    app.run(debug=True)