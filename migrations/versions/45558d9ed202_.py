"""empty message

Revision ID: 45558d9ed202
Revises: c8884ac79178
Create Date: 2021-02-09 11:26:38.481364

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45558d9ed202'
down_revision = 'c8884ac79178'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('number', sa.Integer(), nullable=True),
    sa.Column('first_name', sa.String(length=150), nullable=True),
    sa.Column('last_name', sa.String(length=150), nullable=True),
    sa.Column('email', sa.String(length=150), nullable=True),
    sa.Column('phone', sa.String(length=150), nullable=True),
    sa.Column('delivery', sa.String(length=50), nullable=True),
    sa.Column('address', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_constraint('cart_product_product_fkey', 'cart_product', type_='foreignkey')
    op.create_foreign_key(None, 'cart_product', 'product', ['product'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'cart_product', type_='foreignkey')
    op.create_foreign_key('cart_product_product_fkey', 'cart_product', 'product', ['product'], ['id'], ondelete='CASCADE')
    op.drop_table('order')
    # ### end Alembic commands ###