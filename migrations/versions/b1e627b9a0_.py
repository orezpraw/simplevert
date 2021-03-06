"""Adds share tracking tables for three different time slices.

Revision ID: b1e627b9a0
Revises: 2b5117cc3df6
Create Date: 2014-03-05 21:48:22.753744

"""

# revision identifiers, used by Alembic.
revision = 'b1e627b9a0'
down_revision = '2b5117cc3df6'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('five_minute_share',
    sa.Column('user', sa.String(), nullable=False),
    sa.Column('time', sa.DateTime(), nullable=False),
    sa.Column('worker', sa.String(), nullable=False),
    sa.Column('value', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('user', 'time', 'worker')
    )
    op.create_table('one_hour_share',
    sa.Column('user', sa.String(), nullable=False),
    sa.Column('time', sa.DateTime(), nullable=False),
    sa.Column('worker', sa.String(), nullable=False),
    sa.Column('value', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('user', 'time', 'worker')
    )
    op.alter_column(u'one_minute_share', u'minute', new_column_name='time')
    op.alter_column(u'one_minute_share', u'shares', new_column_name='value')
    op.add_column(u'one_minute_share', sa.Column('worker', sa.String(), nullable=False, default="", server_default=""))
    op.drop_constraint('one_minute_share_pkey', 'one_minute_share')
    op.create_primary_key('one_minute_share_pkey', 'one_minute_share',
                          ['user', 'time', 'worker'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column(u'one_minute_share', sa.Column('minute', postgresql.TIMESTAMP(), nullable=False))
    op.add_column(u'one_minute_share', sa.Column('shares', sa.INTEGER(), nullable=True))
    op.drop_column(u'one_minute_share', 'worker')
    op.drop_column(u'one_minute_share', 'value')
    op.drop_column(u'one_minute_share', 'time')
    op.drop_table('one_hour_share')
    op.drop_table('five_minute_share')
    ### end Alembic commands ###
