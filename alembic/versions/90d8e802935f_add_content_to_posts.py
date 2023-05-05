"""add content to posts

Revision ID: 90d8e802935f
Revises: 3db4c45d37bd
Create Date: 2023-05-05 05:01:09.790375

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90d8e802935f'
down_revision = '3db4c45d37bd'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',sa.Column("content",sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
