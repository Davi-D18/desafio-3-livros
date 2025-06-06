"""nova coluna 'paginas' adicionada

Revision ID: 1c9cd7a23a1f
Revises: 6f85bc130709
Create Date: 2025-03-29 20:42:09.341447

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c9cd7a23a1f'
down_revision = '6f85bc130709'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('livros', schema=None) as batch_op:
        batch_op.add_column(sa.Column('paginas', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('livros', schema=None) as batch_op:
        batch_op.drop_column('paginas')

    # ### end Alembic commands ###
