from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS for cross-origin requests

app = Flask(__name__)
CORS(app)  # Enable CORS to allow requests from the frontend (e.g., port 8000)

# Simulated in-memory storage for tech ideas (replace with a real database)
tech_ideas = []

@app.route('/api/post-idea', methods=['POST'])
def post_idea():
    try:
        data = request.get_json()
        title = data.get('title')
        description = data.get('description')

        if not title or not description:
            return jsonify({'error': 'Title and description are required'}), 400

        # Create a new tech idea entry
        new_idea = {
            'id': len(tech_ideas) + 1,
            'title': title,
            'description': description,
            'claimed': False
        }
        tech_ideas.append(new_idea)

        return jsonify({'message': 'Idea posted successfully', 'idea': new_idea}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
