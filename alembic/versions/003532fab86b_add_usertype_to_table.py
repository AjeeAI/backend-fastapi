"""add userType to table

Revision ID: 003532fab86b
Revises: 7baf74900078
Create Date: 2025-10-27 11:56:59.336370

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '003532fab86b'
down_revision: Union[str, Sequence[str], None] = '7baf74900078'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
     op.execute("""
              ALTER TABLE users
              ADD COLUMN userType varchar (100) DEFAULT "student"
              """)

def downgrade() -> None:
    """Downgrade schema."""
    pass
