"""empty message

Revision ID: 55361a39ed87
Revises: 69eb73ad883d
Create Date: 2024-04-25 09:20:29.372937

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '55361a39ed87'
down_revision = '69eb73ad883d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('author', sa.String(length=255), nullable=False),
    sa.Column('genre', sa.String(length=100), nullable=True),
    sa.Column('published_year', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('books')
    # ### end Alembic commands ###
