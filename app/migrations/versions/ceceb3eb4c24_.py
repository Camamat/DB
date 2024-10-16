"""empty message

Revision ID: ceceb3eb4c24
Revises: 79d337033415
Create Date: 2024-10-15 21:19:55.694780

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ceceb3eb4c24'
down_revision: Union[str, None] = '79d337033415'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
