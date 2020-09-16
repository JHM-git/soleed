"""headteacher email added

Revision ID: 336f49710ce9
Revises: 4560b7ad58a9
Create Date: 2020-09-15 17:42:52.481565

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '336f49710ce9'
down_revision = '4560b7ad58a9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('school', sa.Column('headteacher_email', sa.String(length=64), nullable=True))
    op.create_index(op.f('ix_school_headteacher_email'), 'school', ['headteacher_email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_school_headteacher_email'), table_name='school')
    op.drop_column('school', 'headteacher_email')
    # ### end Alembic commands ###
