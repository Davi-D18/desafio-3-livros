from flask import Blueprint, jsonify, request
from flasgger import swag_from
from marshmallow import ValidationError
from app.schemas.livros_schema import LivrosSchema

from app.services import create_livros, lista_livros
from app.messages.errors.error import InvalidInputError, InternalServerError
from app.messages.sucess.sucess import ResourceCreated

livros_schema = LivrosSchema()
main = Blueprint('main', __name__)

@main.route('/')

def index():
    return jsonify(message="API Livros")
    
@main.route("/livros", methods=['GET'])
@swag_from('../../swagger/get_livros.yml')
def retornar_livros():
    dados = lista_livros()

    # Serializa os dados
    return livros_schema.dump(dados, many=True)
 

@main.route('/livros', methods=['POST'])
@swag_from('../../swagger/post_livro.yml')
def create():
    json_data = request.get_json()
    
    try:
        # Verifica se os dados recebidos estão completos
        data = livros_schema.load(json_data)
    except ValidationError as err:
        raise InvalidInputError(
            message="Dados inválidos ou incompletos",
            details=err.messages
        )
        
    # Recebe o status se o livro foi criado ou não    
    status = create_livros(
        data['titulo'],
        data['categoria'],
        data['autor'],
        data['image_url']
    )

    match(status):
        case 201:
            return ResourceCreated(
                message="Livro criado com sucesso"
            ).to_response()
        case 500:
            return InternalServerError(
                message="Erro interno do servidor"
            ).to_response()