from app.models.livros import Livros
from app.extensions import db

def obter_livros():
    return Livros.query.all()

def inserir_livros(titulo, categoria, autor, image_url, paginas):
    livros = Livros(titulo=titulo, categoria=categoria, autor=autor, image_url=image_url, paginas=paginas)
    db.session.add(livros)
    db.session.commit()
    return livros

