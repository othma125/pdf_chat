#!/usr/bin/python3
""" objects that handle all default RestFul API actions for text blocks """
from models.text_block import TextBlock
from models.document import Document
from models import storage
from api.views import app_views
from flask import abort, jsonify, make_response, request


@app_views.route('/documents/<document_id>/text_blocks', methods=['GET'],
                 strict_slashes=False)
def get_document_text_blocks(document_id):
    """
    Retrieves the list of all text blocks objects of a specific document
    """
    document = storage.get(Document, document_id)
    if not document:
        abort(404)
    return jsonify([text_block.to_dict()
                    for text_block in document.text_blocks])


@app_views.route('/text_blocks/', methods=['GET'],
                 strict_slashes=False)
def get_all_text_blocks():
    """
    Retrieves all text blocks
    """
    text_blocks = storage.all(TextBlock).values()
    if not text_blocks:
        abort(404)
    return jsonify([text_block.to_dict() for text_block in text_blocks])


@app_views.route('/text_blocks/<text_block_id>/', methods=['GET'],
                 strict_slashes=False)
def get_a_text_blocks(text_block_id):
    """
    Retrieves a text block based on id
    """
    text_block = storage.get(TextBlock, text_block_id)
    if not text_block:
        abort(404)
    return jsonify(text_block.to_dict())


@app_views.route('/text_blocks/<text_block_id>/', methods=['DELETE'],
                 strict_slashes=False)
def delete_text_block(text_block_id):
    """
    Deletes a text block based on id
    """
    text_block = storage.get(TextBlock, text_block_id)
    if not text_block:
        abort(404)
    storage.delete(text_block)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/documents/<document_id>/text_blocks', methods=['POST'],
                 strict_slashes=False)
def post_text_block(document_id):
    """
    Creates a text block
    """
    document = storage.get(Document, document_id)
    if not document:
        abort(404)
    if not request.is_json:
        abort(400, description="Not a JSON")

    data = request.get_json()

    if 'content' not in data:
        abort(400, description="Missing content")

    text_block = TextBlock(**data)
    text_block.document_id = data['document_id']
    text_block.save()
    return make_response(jsonify(text_block.to_dict()), 201)


@app_views.route('/text_blocks/<text_block_id>/', methods=['PUT'],
                 strict_slashes=False)
def put_text_block(text_block_id):
    """
    Updates a text block
    """
    text_block = storage.get(TextBlock, text_block_id)
    if not text_block:
        abort(404)
    if not request.is_json:
        abort(400, description="Not a JSON")

    data = request.get_json()

    ignore = 'id', 'document_id', 'created_at', 'updated_at'
    c = True
    for key, value in data.items():
        if key not in ignore:
            setattr(text_block, key, value)
            c = False
    if c:
        abort(400, description="Nothing to update")
    text_block.save()
    return make_response(jsonify(text_block.to_dict()), 200)
