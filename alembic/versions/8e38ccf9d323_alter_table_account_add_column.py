"""alter table account add column

Revision ID: 8e38ccf9d323
Revises: a3bc2cfd4caf
Create Date: 2024-10-08 11:56:41.870380

"""
# pylint: disable=E1101
# pylint: disable=C0411

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8e38ccf9d323'
down_revision: Union[str, None] = 'a3bc2cfd4caf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('account', sa.Column('last_transaction_date', sa.DateTime))


def downgrade() -> None:
    op.drop_column('account', 'last_transaction_date')
