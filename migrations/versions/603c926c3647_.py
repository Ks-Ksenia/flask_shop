"""empty message

Revision ID: 603c926c3647
Revises: 03af2f3eddcc
Create Date: 2021-02-03 14:57:20.243866

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '603c926c3647'
down_revision = '03af2f3eddcc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cart',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('total_products', sa.Integer(), nullable=True),
    sa.Column('final_price', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_column('product', 'Имя')
    op.add_column('user', sa.Column('cart', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'user', 'cart', ['cart'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.drop_column('user', 'cart')
    op.add_column('product', sa.Column('Имя', sa.VARCHAR(length=20), autoincrement=False, nullable=True))
    op.drop_table('cart')
    # ### end Alembic commands ###