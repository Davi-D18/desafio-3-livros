from app.extensions import db

class Livros(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    categoria = db.Column(db.Text, nullable=False)
    autor = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text, nullable=False)