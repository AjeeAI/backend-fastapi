"""alter table users

Revision ID: 7baf74900078
Revises: 
Create Date: 2025-10-27 11:46:58.910019

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7baf74900078'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
   op.execute("""
              ALTER TABLE users
              ADD COLUMN gender varchar (10) DEFAULT "male"
              """)


def downgrade() -> None:
    op.execute("""
              ALTER TABLE users
              DROP COLUMN userType
              """)
