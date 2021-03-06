"""empty message

Revision ID: f832bbbc98dc
Revises: 4c18b781abb0
Create Date: 2021-02-02 15:24:15.260866

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f832bbbc98dc'
down_revision = '4c18b781abb0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('Имя', sa.String(length=20), nullable=True))
    op.drop_column('product', 'Категория')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('Категория', sa.VARCHAR(length=20), autoincrement=False, nullable=True))
    op.drop_column('product', 'Имя')
    # ### end Alembic commands ###
