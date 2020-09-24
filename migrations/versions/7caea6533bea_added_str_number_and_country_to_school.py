"""added str number and country to school

Revision ID: 7caea6533bea
Revises: a3634634894e
Create Date: 2020-09-22 15:58:56.696223

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7caea6533bea'
down_revision = 'a3634634894e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('school', sa.Column('country', sa.String(length=32), nullable=True))
    op.add_column('school', sa.Column('street_number', sa.String(length=32), nullable=True))
    op.create_index(op.f('ix_school_country'), 'school', ['country'], unique=False)
    op.create_index(op.f('ix_school_street_number'), 'school', ['street_number'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_school_street_number'), table_name='school')
    op.drop_index(op.f('ix_school_country'), table_name='school')
    op.drop_column('school', 'street_number')
    op.drop_column('school', 'country')
    # ### end Alembic commands ###