#!/usr/bin/python3
""" Flask Application """
from models import storage
from api.views import app_views
from flask import Flask, make_response, jsonify
from flask_cors import CORS
from flasgger import Swagger
from flasgger.utils import swag_from
# from os import getenv

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
CORS(app, resources={r"/api/*": {"origins": "*"}})


# USER=admin PASSWORD=admin_pwd DB=pdf_chat_db HOST=localhost python3 -m api.app


@app.teardown_appcontext
def close_db(error):
    """ Close Storage """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)


app.config['SWAGGER'] = {
    'title': 'pdf chat Restful API',
    'uiversion': 3
}

Swagger(app)

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=3000, threaded=True, debug=True)
