"""empty message

Revision ID: bd47b019a27b
Revises: 2e1c9e5ffbb4
Create Date: 2021-08-20 23:57:21.541643

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bd47b019a27b'
down_revision = '2e1c9e5ffbb4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('planet', sa.Column('population', sa.Integer(), nullable=False))
    op.add_column('planet', sa.Column('terrain', sa.String(length=120), nullable=False))
    op.add_column('planet', sa.Column('climate', sa.String(length=120), nullable=False))
    op.add_column('planet', sa.Column('diameter', sa.Integer(), nullable=False))
    op.add_column('planet', sa.Column('gravity', sa.String(length=120), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('planet', 'gravity')
    op.drop_column('planet', 'diameter')
    op.drop_column('planet', 'climate')
    op.drop_column('planet', 'terrain')
    op.drop_column('planet', 'population')
    # ### end Alembic commands ###
