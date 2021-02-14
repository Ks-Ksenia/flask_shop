"""empty message

Revision ID: 8b21666ec35a
Revises: 66c56ba8bf61
Create Date: 2021-02-03 16:29:08.471471

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b21666ec35a'
down_revision = '66c56ba8bf61'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('customer', 'p')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customer', sa.Column('p', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
