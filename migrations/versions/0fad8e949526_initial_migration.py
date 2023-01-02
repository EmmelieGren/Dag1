"""Initial migration.

Revision ID: 0fad8e949526
Revises: 
Create Date: 2023-01-02 13:15:27.694838

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0fad8e949526'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Customer',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('Name', sa.String(length=50), nullable=False),
    sa.Column('City', sa.String(length=40), nullable=False),
    sa.Column('TelephoneCountryCode', sa.Integer(), nullable=False),
    sa.Column('Telephone', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('Id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Customer')
    # ### end Alembic commands ###
