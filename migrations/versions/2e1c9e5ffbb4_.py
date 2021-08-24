"""empty message

Revision ID: 2e1c9e5ffbb4
Revises: eb9cb8243358
Create Date: 2021-08-20 23:23:13.094030

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2e1c9e5ffbb4'
down_revision = 'eb9cb8243358'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('planet', 'diameter')
    op.drop_column('planet', 'gravity')
    op.drop_column('planet', 'climate')
    op.drop_column('planet', 'population')
    op.drop_column('planet', 'terrain')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('planet', sa.Column('terrain', mysql.VARCHAR(length=120), nullable=False))
    op.add_column('planet', sa.Column('population', mysql.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('planet', sa.Column('climate', mysql.VARCHAR(length=120), nullable=False))
    op.add_column('planet', sa.Column('gravity', mysql.VARCHAR(length=120), nullable=False))
    op.add_column('planet', sa.Column('diameter', mysql.INTEGER(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###