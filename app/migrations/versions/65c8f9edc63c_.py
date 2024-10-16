"""empty message

Revision ID: 65c8f9edc63c
Revises: ef57580bb9ee
Create Date: 2024-10-16 19:01:43.427661

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '65c8f9edc63c'
down_revision: Union[str, None] = 'ef57580bb9ee'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
