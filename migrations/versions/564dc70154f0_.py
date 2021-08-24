"""empty message

Revision ID: 564dc70154f0
Revises: b51f8da9d74c
Create Date: 2021-08-20 04:32:03.272947

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '564dc70154f0'
down_revision = 'b51f8da9d74c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('name', table_name='planet')
    op.drop_index('name_2', table_name='planet')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('name_2', 'planet', ['name'], unique=False)
    op.create_index('name', 'planet', ['name'], unique=False)
    # ### end Alembic commands ###