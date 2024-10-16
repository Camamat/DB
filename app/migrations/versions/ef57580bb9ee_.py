"""empty message

Revision ID: ef57580bb9ee
Revises: ceceb3eb4c24
Create Date: 2024-10-15 21:45:12.865538

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ef57580bb9ee'
down_revision: Union[str, None] = 'ceceb3eb4c24'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
