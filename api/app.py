#!/usr/bin/python3
""" Flask Application """
import models
import api
from models import storage
from api.views import app_views
from flask import Flask, make_response, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
CORS(app, resources={r"/api/*": {"origins": "*"}})


# USER=admin PASSWORD=admin_pwd DB=pdf_chat_db HOST=localhost python3 -m api.app

@app.route('/api/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of API """
    return jsonify({"status": "OK"})

@app.teardown_appcontext
def close_db(error):
    """ Close Storage """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)


@app.errorhandler(400)
def bad_request(error):
    """
    responses:
      404:
        description: dynamic message displayed
    """
    message = error.description if error.description and error.description != '' else "Bad Request"
    return make_response(jsonify({'error': message}), 400)


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000, debug=True)
