"""empty message

Revision ID: 7166e54a6a5d
Revises: d76530b2a992
Create Date: 2021-08-25 23:36:21.590599

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7166e54a6a5d'
down_revision = 'd76530b2a992'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password', sa.String(length=80), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'password')
    # ### end Alembic commands ###
