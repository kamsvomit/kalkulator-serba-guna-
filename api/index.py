import sys
import os

# Supaya bisa import tools.py dari root
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, render_template, request, jsonify
from tools import tools_registry

app = Flask(
    __name__,
    template_folder=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates'),
)

@app.route('/')
def index():
    tools_list = [
        {
            'id'         : key,
            'name'       : tool['name'],
            'category'   : tool['category'],
            'description': tool['description'],
        }
        for key, tool in tools_registry.items()
    ]
    return render_template('index.html', tools=tools_list)

@app.route('/tool/<tool_id>')
def get_tool(tool_id):
    if tool_id not in tools_registry:
        return 'Tool not found', 404
    return render_template(f'tools/{tool_id}.html')

@app.route('/api/<tool_id>', methods=['POST'])
def api_tool(tool_id):
    if tool_id not in tools_registry:
        return jsonify({'error': 'Tool not found'}), 404
    data   = request.get_json()
    result = tools_registry[tool_id]['handler'](data)
    return jsonify(result)

# Vercel butuh variable 'app' di level module
