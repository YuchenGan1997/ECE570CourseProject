"""empty message

Revision ID: 1835a635f44d
Revises: 843c810aec1f
Create Date: 2022-04-26 01:47:32.508780

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1835a635f44d'
down_revision = '843c810aec1f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('likes', sa.Integer(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('product', 'likes')
    # ### end Alembic commands ###
