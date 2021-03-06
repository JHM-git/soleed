"""bi+tri

Revision ID: 6abb90432ccc
Revises: dcbb4cfbef86
Create Date: 2020-11-21 13:04:59.769336

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6abb90432ccc'
down_revision = 'dcbb4cfbef86'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('school', sa.Column('bilingual_language', sa.String(length=32), nullable=True))
    op.add_column('school', sa.Column('trilingual_language', sa.String(length=32), nullable=True))
    op.create_index(op.f('ix_school_bilingual_language'), 'school', ['bilingual_language'], unique=False)
    op.create_index(op.f('ix_school_trilingual_language'), 'school', ['trilingual_language'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_school_trilingual_language'), table_name='school')
    op.drop_index(op.f('ix_school_bilingual_language'), table_name='school')
    op.drop_column('school', 'trilingual_language')
    op.drop_column('school', 'bilingual_language')
    # ### end Alembic commands ###
