from flask_restful import Api, Resource

class Index(Resource):

    def get(self):
        return {'hello': 'world'}

# Instânciamos a API do FlaskRestful
api = Api()

def configure_api(app):

    api.add_resource(Index, '/')

    api.init_app(app)
