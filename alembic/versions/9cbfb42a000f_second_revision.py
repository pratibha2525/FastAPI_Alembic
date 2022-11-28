"""second revision

Revision ID: 9cbfb42a000f
Revises: 27601ffb1e9c
Create Date: 2022-09-29 11:26:18.336122

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9cbfb42a000f'
down_revision = '27601ffb1e9c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('faculty_std_id_fkey', 'faculty', type_='foreignkey')
    op.drop_column('faculty', 'std_id')
    op.add_column('student', sa.Column('F_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'student', 'student', ['F_id'], ['id'])
    op.drop_column('student', 's_subject')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('student', sa.Column('s_subject', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'student', type_='foreignkey')
    op.drop_column('student', 'F_id')
    op.add_column('faculty', sa.Column('std_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('faculty_std_id_fkey', 'faculty', 'student', ['std_id'], ['id'])
    # ### end Alembic commands ###
