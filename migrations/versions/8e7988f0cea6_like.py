"""like

Revision ID: 8e7988f0cea6
Revises: 6101ae5690c2
Create Date: 2023-05-01 11:49:36.368345

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e7988f0cea6'
down_revision = '6101ae5690c2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('like',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_created', sa.DateTime(timezone=True), nullable=True),
    sa.Column('author', sa.Integer(), nullable=False),
    sa.Column('upload_id', sa.Integer(), nullable=False),
    sa.Column('comment_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author'], ['user.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['comment_id'], ['comment.id'], ),
    sa.ForeignKeyConstraint(['upload_id'], ['upload.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('like')
    # ### end Alembic commands ###
