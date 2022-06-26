"""empty message

Revision ID: 8bf299607796
Revises: f9cef09fd0dc
Create Date: 2022-06-26 13:46:34.913026

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8bf299607796'
down_revision = 'f9cef09fd0dc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('books', 'reader_pk',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('books', 'reader_pk',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
