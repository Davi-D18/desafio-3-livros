from marshmallow import Schema, fields, validate, EXCLUDE
class LivrosSchema(Schema):
    class Meta:
        unknown = EXCLUDE # Ignora campos não declarados

    id = fields.Int(dump_only=True)  # Aparece apenas na resposta

    # Campos de entrada (validação)
    titulo = fields.Str(
        required=True,
        validate=validate.Length(min=5, max=100, error="Título deve ter entre 5 e 100 caracteres")
    )
    categoria = fields.Str(required=True)
    autor = fields.Str(required=True)
    image_url = fields.Str(required=True)