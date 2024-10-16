"""empty message

Revision ID: ee2305b064bb
Revises: 65c8f9edc63c
Create Date: 2024-10-16 19:36:52.078924

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ee2305b064bb'
down_revision: Union[str, None] = '65c8f9edc63c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
