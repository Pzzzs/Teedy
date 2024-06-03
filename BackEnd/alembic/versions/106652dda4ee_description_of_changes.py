"""description of changes\

Revision ID: 106652dda4ee
Revises: 387a0d1cd5c0
Create Date: 2024-06-02 17:49:30.590750

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '106652dda4ee'
down_revision: Union[str, None] = '387a0d1cd5c0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('course_review',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('student_id', sa.String(length=16), nullable=True),
    sa.Column('course_id', sa.String(length=100), nullable=True),
    sa.Column('rating', sa.Float(), nullable=True),
    sa.Column('difficulty', sa.String(length=50), nullable=True),
    sa.Column('homework', sa.String(length=50), nullable=True),
    sa.Column('grading', sa.String(length=50), nullable=True),
    sa.Column('harvest', sa.String(length=50), nullable=True),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.Column('created_time', sa.DateTime(), nullable=True),
    sa.Column('last_updated_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['student_id'], ['student.student_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('course_review')
    # ### end Alembic commands ###