from datetime import datetime
import json
import re
from time import time
import uuid
from xml.dom.minidom import Identified
from flask import Flask

from flask_restful import Resource, Api
from pytz import timezone

app = Flask(__name__)
api = Api(app)

def generate_uuid():
    indentifier = uuid.uuid4()
    return json.dumps(indentifier, default=str)

def get_utc_now():
    now = datetime.utcnow().replace(tzinfo=timezone.utc)
    return json.dumps(now, default=str)

MEASUREMENTS = [
    {
        'id': '84'
    },
    {

    }
]

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
