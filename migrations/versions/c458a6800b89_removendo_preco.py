"""Removendo preco

Revision ID: c458a6800b89
Revises: a108d0ec64d0
Create Date: 2023-07-18 00:10:43.067307

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c458a6800b89'
down_revision = 'a108d0ec64d0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('produto', schema=None) as batch_op:
        batch_op.drop_column('preco')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('produto', schema=None) as batch_op:
        batch_op.add_column(sa.Column('preco', sa.INTEGER(), nullable=True))

    # ### end Alembic commands ###
