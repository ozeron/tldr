from flask_restful import Resource
from flask import request, jsonify
from src.model.summary import build

class Home(Resource):
    def get(self):
        return {'status': 'ok'}


class SummaryFromText(Resource):
    def post(self):
        try:
            if not request.content_type == 'application/json':
                return self._content_type_error()
            content = request.get_json()
            if 'text' not in content or len(content['text']) == 0:
                return self._empty_text_exception()
            text = content['text']
            summary = build(text)
            return jsonify(text=summary, status='ok')
        except Exception as e:
            return jsonify(message=str(e), status='error')

    def _content_type_error(self):
        return jsonify(
            message='set content_type to application/json',
            status='error')

    def _empty_text_exception(self):
        return jsonify(
            message='set text dict key to generate summary',
            status='error')
