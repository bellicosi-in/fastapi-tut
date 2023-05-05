"""add foreign-key to posts table

Revision ID: 795efa1b2ebc
Revises: 2ebf367f1a8d
Create Date: 2023-05-05 21:18:51.984078

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '795efa1b2ebc'
down_revision = '2ebf367f1a8d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('owner_id',sa.Integer(),nullable=False))
    op.create_foreign_key('post_users_fk',source_table="posts",referent_table="users",local_cols=['owner_id'],remote_cols=['id'],ondelete='CASCADE')
    pass


def downgrade() -> None:
    pass
