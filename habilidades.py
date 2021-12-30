from flask_restful import Resource

habilidades =['Python', 'Java', 'Flask', 'PHP']

class lista_habilidades(Resource):
    def get(self):
        return habilidades