"""empty message

Revision ID: 79d337033415
Revises: b19e6de66ad5
Create Date: 2024-10-15 20:48:58.802692

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '79d337033415'
down_revision: Union[str, None] = 'b19e6de66ad5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
