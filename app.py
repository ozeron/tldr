from flask import Flask
from flask_restful import Api

from src.api import SummaryFromText, Home

app = Flask(__name__)
api = Api(app)
api.add_resource(Home, '/')
api.add_resource(SummaryFromText, '/api/summary_from_text')

if __name__ == '__main__':
    app.run()
