"""Initial migration

Revision ID: 312623b8599b
Revises: 
Create Date: 2023-08-03 16:19:58.147456

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '312623b8599b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contact',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=255), nullable=True),
    sa.Column('last_name', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_contact_id'), 'contact', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_contact_id'), table_name='contact')
    op.drop_table('contact')
    # ### end Alembic commands ###
