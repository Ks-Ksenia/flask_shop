"""empty message

Revision ID: 7060227f89ed
Revises: 0e623cbc1983
Create Date: 2021-02-05 15:09:24.698460

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7060227f89ed'
down_revision = '0e623cbc1983'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('product_cart_product_fkey', 'product', type_='foreignkey')
    op.create_foreign_key(None, 'product', 'cart_product', ['cart_product'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'product', type_='foreignkey')
    op.create_foreign_key('product_cart_product_fkey', 'product', 'cart_product', ['cart_product'], ['id'])
    # ### end Alembic commands ###