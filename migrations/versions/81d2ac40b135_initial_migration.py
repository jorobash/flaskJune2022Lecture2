"""initial migration.

Revision ID: 81d2ac40b135
Revises: 
Create Date: 2022-06-26 12:49:19.271628

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '81d2ac40b135'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('pk', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('author', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('pk')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('books')
    # ### end Alembic commands ###
