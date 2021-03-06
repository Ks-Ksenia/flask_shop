"""empty message

Revision ID: 1e41211794ef
Revises: dec9b1d10184
Create Date: 2021-02-02 11:23:48.403130

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e41211794ef'
down_revision = 'dec9b1d10184'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=100), nullable=True),
    sa.Column('Картинка', sa.String(length=200), nullable=True),
    sa.Column('Цена', sa.Integer(), nullable=True),
    sa.Column('Описание', sa.String(length=1000), nullable=True),
    sa.Column('Категория товара', sa.Integer(), nullable=True),
    sa.Column('Коллекция', sa.String(length=20), nullable=True),
    sa.Column('Код товара', sa.String(length=20), nullable=True),
    sa.Column('Артикул', sa.String(length=20), nullable=True),
    sa.Column('Тип', sa.String(length=100), nullable=True),
    sa.Column('Пол', sa.String(length=50), nullable=True),
    sa.Column('Страна', sa.String(length=50), nullable=True),
    sa.Column('Материал', sa.String(length=100), nullable=True),
    sa.Column('Возраст', sa.String(length=10), nullable=True),
    sa.Column('Кол-во элементов', sa.String(length=10), nullable=True),
    sa.Column('Наличие', sa.String(length=10), nullable=True),
    sa.Column('review', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['Категория товара'], ['submenu.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('url'),
    sa.UniqueConstraint('Артикул'),
    sa.UniqueConstraint('Код товара')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')
    # ### end Alembic commands ###
