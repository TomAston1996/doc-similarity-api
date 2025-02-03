"""initial migration

Revision ID: f55c9b676c3c
Revises: 
Create Date: 2025-02-03 15:14:33.520562

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa 
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'f55c9b676c3c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('document')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('document',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('content', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('created', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='document_pkey')
    )
    # ### end Alembic commands ###
