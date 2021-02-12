from flask import Response
import json


class HttpUtil:
    @staticmethod
    def get_response(data):
        response = Response(
            response = data,
            status=200,
            mimetype='application/json'
        )
        return response

    @staticmethod
    def get_request(request):
        requestHeader = request.headers # NOTE: should use MS-ACL in here
        if request.get_data() == b'':
            requestBody ={}
        else:
            requestBody = json.loads(request.get_data())
        return requestHeader,requestBody