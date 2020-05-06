"""add new class

Revision ID: 9f13cadaf283
Revises: 7834fc295ea8
Create Date: 2018-07-02 17:33:17.636643

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f13cadaf283'
down_revision = '7834fc295ea8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('votes', sa.Column('pitch_id', sa.Integer(), nullable=True))
    op.drop_constraint('votes_content_id_fkey', 'votes', type_='foreignkey')
    op.create_foreign_key(None, 'votes', 'pitches', ['pitch_id'], ['id'])
    op.drop_column('votes', 'content_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('votes', sa.Column('content_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'votes', type_='foreignkey')
    op.create_foreign_key('votes_content_id_fkey', 'votes', 'pitches', ['content_id'], ['id'])
    op.drop_column('votes', 'pitch_id')
    # ### end Alembic commands ###