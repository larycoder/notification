from flask import Response


class HttpUtil:
    @staticmethod
    def get_response(data):
        response = Response(
            response = data,
            status=200,
            mimetype='application/json'
        )
        return response