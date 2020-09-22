"""users school code

Revision ID: a3634634894e
Revises: 512518e2904e
Create Date: 2020-09-17 18:25:38.666307

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a3634634894e'
down_revision = '512518e2904e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('school_code_number', sa.String(length=32), nullable=True))
    op.create_index(op.f('ix_user_school_code_number'), 'user', ['school_code_number'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_school_code_number'), table_name='user')
    op.drop_column('user', 'school_code_number')
    # ### end Alembic commands ###
