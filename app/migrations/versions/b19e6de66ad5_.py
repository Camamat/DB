"""empty message

Revision ID: b19e6de66ad5
Revises: 53c5494ed898
Create Date: 2024-10-15 20:47:33.043573

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b19e6de66ad5'
down_revision: Union[str, None] = '53c5494ed898'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
