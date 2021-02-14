"""empty message

Revision ID: d6aa3bf2c51b
Revises: 45558d9ed202
Create Date: 2021-02-09 14:04:25.099481

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6aa3bf2c51b'
down_revision = '45558d9ed202'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customer', sa.Column('order', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'customer', 'order', ['order'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'customer', type_='foreignkey')
    op.drop_column('customer', 'order')
    # ### end Alembic commands ###
