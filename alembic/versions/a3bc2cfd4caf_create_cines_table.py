"""create cines table

Revision ID: a3bc2cfd4caf
Revises: 
Create Date: 2024-10-08 11:42:41.381617

"""
# pylint: disable=E1101
# pylint: disable=C0411

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a3bc2cfd4caf'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'account',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
    )



def downgrade() -> None:
    op.drop_table('account')
