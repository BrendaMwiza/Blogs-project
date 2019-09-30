"""Initial Migration

Revision ID: 1618e4f02ec8
Revises: 31d9d8e936b9
Create Date: 2019-09-27 15:15:14.893193

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1618e4f02ec8'
down_revision = '31d9d8e936b9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'bio')
    op.drop_column('users', 'profile_pic_path')
    op.drop_column('users', 'pass_secure')
    op.drop_column('users', 'password_hash')
    op.add_column('writers', sa.Column('bio', sa.String(length=255), nullable=True))
    op.add_column('writers', sa.Column('email', sa.String(length=255), nullable=True))
    op.add_column('writers', sa.Column('pass_secure', sa.String(length=255), nullable=True))
    op.add_column('writers', sa.Column('password_hash', sa.String(length=255), nullable=True))
    op.add_column('writers', sa.Column('profile_pic_path', sa.String(), nullable=True))
    op.create_index(op.f('ix_writers_email'), 'writers', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_writers_email'), table_name='writers')
    op.drop_column('writers', 'profile_pic_path')
    op.drop_column('writers', 'password_hash')
    op.drop_column('writers', 'pass_secure')
    op.drop_column('writers', 'email')
    op.drop_column('writers', 'bio')
    op.add_column('users', sa.Column('password_hash', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('pass_secure', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('profile_pic_path', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('bio', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    # ### end Alembic commands ###