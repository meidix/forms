"""Initial migrations

Revision ID: 69bf07f52ec2
Revises: 
Create Date: 2020-08-01 14:50:07.779995

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '69bf07f52ec2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('applicants',
    sa.Column('pk', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=30), nullable=False),
    sa.Column('last_name', sa.String(length=45), nullable=False),
    sa.Column('national_id', sa.String(length=10), nullable=False),
    sa.Column('date_of_birth', sa.DateTime(), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('mobile_phone', sa.String(length=11), nullable=False),
    sa.Column('Address', sa.Text(), nullable=True),
    sa.Column('university', sa.String(length=80), nullable=True),
    sa.Column('university_subject', sa.String(length=50), nullable=True),
    sa.Column('university_degree', forms.user_types.ChoiceType(), nullable=False),
    sa.Column('work_reputations', sa.Text(), nullable=True),
    sa.Column('altium_designer', sa.Boolean(), nullable=True),
    sa.Column('arduino', sa.Boolean(), nullable=True),
    sa.Column('code_vision', sa.Boolean(), nullable=True),
    sa.Column('proteus', sa.Boolean(), nullable=True),
    sa.Column('atmel_studio', sa.Boolean(), nullable=True),
    sa.Column('microcontroller', sa.Boolean(), nullable=True),
    sa.Column('power', sa.Boolean(), nullable=True),
    sa.Column('others', sa.Text(), nullable=True),
    sa.Column('resume', sa.LargeBinary(), nullable=True),
    sa.Column('expected_salary', sa.String(length=7), nullable=True),
    sa.PrimaryKeyConstraint('pk'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('mobile_phone'),
    sa.UniqueConstraint('national_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('applicants')
    # ### end Alembic commands ###
