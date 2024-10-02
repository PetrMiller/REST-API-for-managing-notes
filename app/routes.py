from flask import Blueprint, jsonify, request
from .models import Note
from . import db
from .services import create_note, get_all_notes

note_bp = Blueprint('notes', __name__)

@note_bp.route('/notes', methods=['GET'])
def list_notes():
    notes = get_all_notes()
    return jsonify([{"id": note.id, "title": note.title, "content": note.content} for note in notes])

@note_bp.route('/notes', methods=['POST'])
def add_note():
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    
    note = create_note(title, content)
    return jsonify({"id": note.id, "title": note.title, "content": note.content}), 201
