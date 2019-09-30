"""Initial one

Revision ID: 261ee862d4e2
Revises: 1618e4f02ec8
Create Date: 2019-09-28 22:58:53.985327

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '261ee862d4e2'
down_revision = '1618e4f02ec8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_users_email', table_name='users')
    op.drop_table('users')
    op.drop_constraint('blogs_user_id_fkey', 'blogs', type_='foreignkey')
    op.drop_column('blogs', 'user_id')
    op.drop_constraint('comments_user_id_fkey', 'comments', type_='foreignkey')
    op.drop_column('comments', 'user_id')
    op.drop_constraint('subscriptions_user_id_fkey', 'subscriptions', type_='foreignkey')
    op.drop_column('subscriptions', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('subscriptions', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('subscriptions_user_id_fkey', 'subscriptions', 'users', ['user_id'], ['id'])
    op.add_column('comments', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('comments_user_id_fkey', 'comments', 'users', ['user_id'], ['id'])
    op.add_column('blogs', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('blogs_user_id_fkey', 'blogs', 'users', ['user_id'], ['id'])
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='users_pkey')
    )
    op.create_index('ix_users_email', 'users', ['email'], unique=True)
    # ### end Alembic commands ###