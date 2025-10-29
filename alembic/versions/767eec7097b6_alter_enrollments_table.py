"""alter enrollments table

Revision ID: 767eec7097b6
Revises: 
Create Date: 2025-10-29 20:57:59.154942

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '767eec7097b6'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
        ALTER table enrollments
        ADD COLUMN courseName varchar(100)
        """
    )


def downgrade() -> None:
    """Downgrade schema."""
    pass
