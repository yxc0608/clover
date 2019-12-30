"""empty message

Revision ID: fed59c332f83
Revises: 
Create Date: 2019-12-30 17:53:50.548670

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fed59c332f83'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('team',
    sa.Column('id', sa.Integer(), nullable=False, comment='ID'),
    sa.Column('team', sa.String(length=64), nullable=True, comment='团队'),
    sa.Column('project', sa.String(length=256), nullable=True, comment='项目'),
    sa.Column('owner', sa.String(length=64), nullable=True, comment='负责人'),
    sa.Column('enable', sa.Integer(), nullable=True, comment='0有效，1无效'),
    sa.Column('created', sa.DateTime(), nullable=True, comment='创建时间'),
    sa.Column('updated', sa.DateTime(), nullable=True, comment='修改时间'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_team_owner'), 'team', ['owner'], unique=False)
    op.create_index(op.f('ix_team_project'), 'team', ['project'], unique=False)
    op.create_index(op.f('ix_team_team'), 'team', ['team'], unique=False)
    op.create_table('variable',
    sa.Column('id', sa.Integer(), nullable=False, comment='ID'),
    sa.Column('team', sa.String(length=64), nullable=True, comment='团队'),
    sa.Column('project', sa.String(length=256), nullable=True, comment='项目'),
    sa.Column('owner', sa.String(length=64), nullable=True, comment='负责人'),
    sa.Column('name', sa.String(length=64), nullable=True, comment='变量名'),
    sa.Column('value', sa.String(length=64), nullable=True, comment='变量值'),
    sa.Column('enable', sa.Integer(), nullable=True, comment='0有效，1无效'),
    sa.Column('created', sa.DateTime(), nullable=True, comment='创建时间'),
    sa.Column('updated', sa.DateTime(), nullable=True, comment='修改时间'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_variable_name'), 'variable', ['name'], unique=False)
    op.create_index(op.f('ix_variable_owner'), 'variable', ['owner'], unique=False)
    op.create_index(op.f('ix_variable_project'), 'variable', ['project'], unique=False)
    op.create_index(op.f('ix_variable_team'), 'variable', ['team'], unique=False)
    op.create_index(op.f('ix_variable_value'), 'variable', ['value'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_variable_value'), table_name='variable')
    op.drop_index(op.f('ix_variable_team'), table_name='variable')
    op.drop_index(op.f('ix_variable_project'), table_name='variable')
    op.drop_index(op.f('ix_variable_owner'), table_name='variable')
    op.drop_index(op.f('ix_variable_name'), table_name='variable')
    op.drop_table('variable')
    op.drop_index(op.f('ix_team_team'), table_name='team')
    op.drop_index(op.f('ix_team_project'), table_name='team')
    op.drop_index(op.f('ix_team_owner'), table_name='team')
    op.drop_table('team')
    # ### end Alembic commands ###
