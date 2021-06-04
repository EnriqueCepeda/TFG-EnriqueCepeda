"""3

Revision ID: f8ede628b0a1
Revises: 3be05348d9f5
Create Date: 2021-06-02 17:35:35.830612

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f8ede628b0a1'
down_revision = '3be05348d9f5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('energytransaction',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sender_id', sa.Integer(), nullable=True),
    sa.Column('receiver_id', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.TIMESTAMP(), nullable=False),
    sa.ForeignKeyConstraint(['receiver_id'], ['building.id'], ),
    sa.ForeignKeyConstraint(['sender_id'], ['building.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_energytransaction_id'), 'energytransaction', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_energytransaction_id'), table_name='energytransaction')
    op.drop_table('energytransaction')
    # ### end Alembic commands ###