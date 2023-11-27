#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Users """
from models.user import User
from models import storage
from api.views import app_views
from flask import abort, jsonify, make_response, request


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """
    Retrieves the list of all user objects
    or a specific user
    """
    all_users = storage.all(User).values()
    return jsonify([user.to_dict() for user in all_users])


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """ Retrieves an user """
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route('/users/<user_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_user(user_id):
    """
    Deletes a user Object
    """
    user = storage.get(User, user_id)

    if not user:
        abort(404)

    storage.delete(user)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/users/sign-up', methods=['POST'], strict_slashes=False)
def post_user():
    """
    Creates a user
    """
    if not request.is_json:
        abort(400, description="Not a JSON")

    data = request.get_json()

    if 'email' not in data:
        return make_response(jsonify({'error': "Missing email"}), 400)
    if 'password' not in data:
        abort(400, description="Missing password")
        return make_response(jsonify({'error': "Missing password"}), 400)
    if not User.is_valid_email(data['email']):
        return make_response(jsonify({'error': "Invalid email format"}), 400)

    if storage.get_by(User, 'email', data['email']):
        return make_response(jsonify({'error': "Email already exists"}), 400)
    instance = User(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/users/login', methods=['POST'], strict_slashes=False)
def login_user():
    """
    User login
    """
    if not request.is_json:
        abort(400, description="Not a JSON")

    data = request.get_json()

    if 'email' not in data:
        return make_response(jsonify({'error': "Missing email"}), 400)
    if 'password' not in data:
        return make_response(jsonify({'error': "Missing password"}), 400)
    if not User.is_valid_email(data['email']):
        return make_response(jsonify({'error': "Invalid email format"}), 400)

    user = storage.get_by(User, 'email', data['email'])

    if not user:
        return make_response(jsonify({'error': "Invalid email"}), 400)
    if not user.is_valid_password(data['password']):
        return make_response(jsonify({'error': "Invalid password"}), 400)

    return make_response(jsonify(user.to_dict()), 200)


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def put_user(user_id):
    """
    Updates a user
    """
    user = storage.get(User, user_id)

    if not user:
        abort(404, description="Not found")

    if not request.is_json:
        return make_response(jsonify({'error': "Not a JSON"}), 400)

    ignore = 'id', 'email', 'created_at', 'updated_at'
    c = True
    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(user, key, value)
            c = False
    if c:
        return make_response(jsonify({'error': "Nothing changed"}), 400)
    user.save()
    return make_response(jsonify(user.to_dict()), 200)
