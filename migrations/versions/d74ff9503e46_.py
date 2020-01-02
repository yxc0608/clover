"""empty message

Revision ID: d74ff9503e46
Revises: 
Create Date: 2020-01-02 22:24:25.226720

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd74ff9503e46'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('interface',
    sa.Column('id', sa.Integer(), nullable=False, comment='ID'),
    sa.Column('team', sa.String(length=64), nullable=True, comment='团队'),
    sa.Column('project', sa.String(length=256), nullable=True, comment='项目'),
    sa.Column('name', sa.String(length=64), nullable=True, comment='用例名称'),
    sa.Column('method', sa.String(length=64), nullable=True, comment='请求方法'),
    sa.Column('host', sa.String(length=64), nullable=True, comment='测试域名'),
    sa.Column('path', sa.String(length=64), nullable=True, comment='请求路径'),
    sa.Column('header', sa.JSON(), nullable=True, comment='http请求头'),
    sa.Column('params', sa.JSON(), nullable=True, comment='http请求参数'),
    sa.Column('verify', sa.JSON(), nullable=True, comment='响应断言'),
    sa.Column('extract', sa.JSON(), nullable=True, comment='提取响应参数'),
    sa.Column('enable', sa.Integer(), nullable=True, comment='0有效，1无效'),
    sa.Column('created', sa.DateTime(), nullable=True, comment='创建时间'),
    sa.Column('updated', sa.DateTime(), nullable=True, comment='修改时间'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_interface_name'), 'interface', ['name'], unique=False)
    op.create_index(op.f('ix_interface_project'), 'interface', ['project'], unique=False)
    op.create_index(op.f('ix_interface_team'), 'interface', ['team'], unique=False)
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
    op.drop_index(op.f('ix_interface_team'), table_name='interface')
    op.drop_index(op.f('ix_interface_project'), table_name='interface')
    op.drop_index(op.f('ix_interface_name'), table_name='interface')
    op.drop_table('interface')
    # ### end Alembic commands ###
