"""add rest of the columns to post


Revision ID: 6b6ba5deb6fc
Revises: 795efa1b2ebc
Create Date: 2023-05-06 00:26:26.658125

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b6ba5deb6fc'
down_revision = '795efa1b2ebc'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts",sa.Column("published",sa.Boolean(),nullable=False,server_default='TRUE'))
    op.add_column('posts',sa.Column('created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('NOW()')))
    pass


def downgrade() -> None:
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    pass
