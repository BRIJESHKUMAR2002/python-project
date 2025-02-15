"""Add text column to Prompt model

Revision ID: ea50459723b1
Revises: 
Create Date: 2024-03-08 14:42:32.512501

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea50459723b1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('prompt', schema=None) as batch_op:
        batch_op.add_column(sa.Column('text', sa.String(length=1000), nullable=True))
        batch_op.drop_column('uploaded_time')
        batch_op.drop_column('status')
        batch_op.drop_column('filename')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('prompt', schema=None) as batch_op:
        batch_op.add_column(sa.Column('filename', sa.VARCHAR(length=255), nullable=True))
        batch_op.add_column(sa.Column('status', sa.VARCHAR(length=20), nullable=True))
        batch_op.add_column(sa.Column('uploaded_time', sa.DATETIME(), nullable=True))
        batch_op.drop_column('text')

    # ### end Alembic commands ###
