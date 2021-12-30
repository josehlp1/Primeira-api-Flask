from flask import Flask, request
from flask_restful import Resource, Api
import json
from habilidades import lista_habilidades

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
     'id': 0,
     'nome': 'Rarafel',
     'habilidades':['Python', 'Flask']
     },
    {
     'id': 1,
     'nome': 'José',
     'habilidades':['Python', 'Django']
     }
]

class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            msg = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status': 'erro', 'msg': msg}
        except Exception:
            msg = 'Erro deseconhecido. Procure o administrador da API'
            response = {'status': 'erro', 'msg': msg}
        return response
    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados
    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status': 'sucesso', 'msg': 'Registro excluido'}

class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]


api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(lista_habilidades, '/habilidades/')



if __name__ == '__main__':
    app.run(debug=True);
