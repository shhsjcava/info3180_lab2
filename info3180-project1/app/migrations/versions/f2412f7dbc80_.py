"""empty message

Revision ID: f2412f7dbc80
Revises: 
Create Date: 2018-03-22 01:56:17.013273

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f2412f7dbc80'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('userid', sa.String(), nullable=False),
    sa.Column('fname', sa.String(length=80), nullable=True),
    sa.Column('lname', sa.String(length=80), nullable=True),
    sa.Column('sex', sa.String(length=10), nullable=True),
    sa.Column('address', sa.String(length=150), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('bio', sa.String(length=255), nullable=True),
    sa.Column('photo', sa.String(length=255), nullable=True),
    sa.Column('date', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('userid')
    )
    op.drop_table('peoples')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('peoples',
    sa.Column('userid', sa.VARCHAR(length=5), autoincrement=False, nullable=False),
    sa.Column('fname', sa.VARCHAR(length=15), autoincrement=False, nullable=True),
    sa.Column('lname', sa.VARCHAR(length=15), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=25), autoincrement=False, nullable=True),
    sa.Column('sex', sa.VARCHAR(length=6), autoincrement=False, nullable=True),
    sa.Column('location', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('bio', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('joined', sa.DATE(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('userid', name=u'peoples_pkey')
    )
    op.drop_table('user')
    # ### end Alembic commands ###
