"""alter user table

Revision ID: d5a1fccb120f
Revises: 
Create Date: 2025-10-23 11:22:37.904822

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd5a1fccb120f'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
               ALTER TABLE users
               ADD COLUMN userType varchar(100) DEFAULT 'student'
               """)
    
    


def downgrade() -> None:
    op.execute("""
               ALTER TABLE users
               DROP COLUMN userType
               """)
    
