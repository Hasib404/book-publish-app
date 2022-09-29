"""initial migration

Revision ID: 232a4fbeac0c
Revises: 
Create Date: 2022-08-29 21:54:54.632167

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '232a4fbeac0c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=25), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('author_pseudonym', sa.String(length=256), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('author_pseudonym')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=256), nullable=False),
    sa.Column('description', sa.String(length=256), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('cover_image', sa.String(length=256), nullable=True),
    sa.Column('price', sa.Numeric(precision=5, scale=2), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('description'),
    sa.UniqueConstraint('title')
    )
    op.create_index(op.f('ix_books_cover_image'), 'books', ['cover_image'], unique=False)
    op.create_index(op.f('ix_books_id'), 'books', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_books_id'), table_name='books')
    op.drop_index(op.f('ix_books_cover_image'), table_name='books')
    op.drop_table('books')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###