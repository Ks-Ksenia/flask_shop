"""empty message

Revision ID: 1fd52c65d4f7
Revises: 3904cd780e00
Create Date: 2021-02-05 10:48:03.498404

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1fd52c65d4f7'
down_revision = '3904cd780e00'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('cart_product', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'product', 'cart_product', ['cart_product'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'product', type_='foreignkey')
    op.drop_column('product', 'cart_product')
    # ### end Alembic commands ###
