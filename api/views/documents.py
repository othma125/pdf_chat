#!/usr/bin/python3
""" objects that handles all default RestFul API actions for documents """
from models.document import Document
from models.user import User
from models import storage
from api.views import app_views
from flask import abort, jsonify, make_response, request


@app_views.route('/users/<user_id>/documents', methods=['GET'],
                 strict_slashes=False)
def get_user_documents(user_id):
    """
    Retrieves the list of all documents objects of a specific user
    """
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    return jsonify([doc.to_dict() for doc in user.documents])


@app_views.route('/documents/<document_id>/', methods=['GET'], strict_slashes=False)
def get_document(document_id):
    """
    Retrieves a specific document based on id
    """
    doc = storage.get(Document, document_id)
    if not doc:
        abort(404)
    return jsonify(doc.to_dict())


@app_views.route('/documents', methods=['GET'], strict_slashes=False)
def get_all_document():
    """
    Retrieves all documents
    """
    docs = storage.all(Document).values()
    if not docs:
        abort(404)
    return jsonify([doc.to_dict() for doc in docs])


@app_views.route('/documents/<document_id>/', methods=['DELETE'], strict_slashes=False)
def delete_document(document_id):
    """
    Deletes a document based on id
    """
    doc = storage.get(Document, document_id)
    if not doc:
        abort(404)
    storage.delete(doc)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/users/<user_id>/documents', methods=['POST'],
                 strict_slashes=False)
def post_document(user_id):
    """
    Creates a document
    """
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    if not request.is_json:
        abort(400, description="Not a JSON")

    data = request.get_json()

    if 'FileName' not in data:
        abort(400, description="Missing File Name")
    if 'URL' not in data:
        abort(400, description="Missing URL")
    if not Document.is_valid_url(data['URL']):
        abort(400, description="Invalid URL format")
    
    doc = Document(**data)
    doc.UserID = user.id
    doc.save()
    return make_response(jsonify(doc.to_dict()), 201)


@app_views.route('/documents/<document_id>', methods=['PUT'], strict_slashes=False)
def put_document(document_id):
    """
    Updates a document based on id
    """
    doc = storage.get(Document, document_id)
    if not doc:
        abort(404)

    if not request.is_json:
        abort(400, description="Not a JSON")

    ignore = 'id', 'user_id', 'created_at', 'updated_at'

    data = request.get_json()
    c: bool = True
    for key, value in data.items():
        if key not in ignore:
            setattr(doc, key, value)
            c = False
    if c:
        abort(400, description="No attribute is changed")
    storage.save()
    return make_response(jsonify(city.to_dict()), 200)
