"""test3_part2

Revision ID: c219a085bbe4
Revises: 722043cdd426
Create Date: 2020-09-13 14:07:48.912750

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c219a085bbe4'
down_revision = '722043cdd426'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_school_test', table_name='school')
    op.drop_column('school', 'test')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('school', sa.Column('test', sa.VARCHAR(length=240), nullable=True))
    op.create_index('ix_school_test', 'school', ['test'], unique=False)
    # ### end Alembic commands ###
