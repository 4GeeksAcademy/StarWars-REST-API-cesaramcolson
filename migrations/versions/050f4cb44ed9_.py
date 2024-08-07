"""empty message

Revision ID: 050f4cb44ed9
Revises: 4674ee172618
Create Date: 2024-08-07 20:51:21.467306

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '050f4cb44ed9'
down_revision = '4674ee172618'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorite', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date', sa.DateTime(timezone=True), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorite', schema=None) as batch_op:
        batch_op.drop_column('date')

    # ### end Alembic commands ###
