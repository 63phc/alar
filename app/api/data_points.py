from flask import request
from flask_restx import Resource, Api

from app.service.data_points import DataAPI

rest_api = Api()
ns = rest_api.namespace('/')


@ns.route('/data/1')
class HelloWorld(Resource):
    def get(self):
        a = [{"id": i, "name": f"Test {i}"} for i in range(1, 11)]
        b = [{"id": i, "name": f"Test {i}"} for i in range(31, 41)]
        return a + b


@ns.route('/data/2')
class HelloWorld(Resource):
    def get(self):
        a = [{"id": i, "name": f"Test {i}"} for i in range(11, 21)]
        b = [{"id": i, "name": f"Test {i}"} for i in range(41, 51)]
        return a + b


@ns.route('/data/3')
class HelloWorld(Resource):
    def get(self):
        a = [{"id": i, "name": f"Test {i}"} for i in range(21, 31)]
        b = [{"id": i, "name": f"Test {i}"} for i in range(51, 61)]
        return a + b


@ns.route('/data')
class HelloWorld(Resource):
    def get(self):
        d = DataAPI(host=request.headers['Host'])
        return d.get_data()
