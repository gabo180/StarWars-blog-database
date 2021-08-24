"""empty message

Revision ID: e9635b8ecab7
Revises: b3fd3d04aa19
Create Date: 2021-08-20 03:58:16.524651

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e9635b8ecab7'
down_revision = 'b3fd3d04aa19'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password', mysql.VARCHAR(length=80), nullable=False))
    # ### end Alembic commands ###