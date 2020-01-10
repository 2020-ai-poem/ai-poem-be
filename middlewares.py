from django.utils.deprecation import MiddlewareMixin


class Cros(MiddlewareMixin):
    def process_response(self, request, response):
        response['Access-Control-Allow-Origin'] = "http://localhost:3000"
        response['Access-Control-Allow-Methods'] = 'OPTIONS, GET, PUT, POST, DELETE'
        response['Access-Control-Allow-Headers'] = '*'
        response['Access-Control-Allow-Credentials'] = true
        return response
