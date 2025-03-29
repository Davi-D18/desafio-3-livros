from app.repositories.livros_repository import inserir_livros, obter_livros

def lista_livros():
    return obter_livros()


def create_livros(titulo, categoria, autor, image_url):
    try:
        livro_formatado = {
            "titulo": titulo.title().strip(),
            "categoria": categoria.title().strip(),
            "autor": autor.title().strip(),
            "image_url": image_url
        }
        inserir_livros(livro_formatado['titulo'], livro_formatado['categoria'], livro_formatado['autor'], livro_formatado['image_url'])
        return 201
    except Exception:
        return 500
