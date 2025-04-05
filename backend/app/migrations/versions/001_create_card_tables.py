"""create card tables

Revision ID: 001
Revises: 
Create Date: 2024-04-05

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '001'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # Create card_sets table
    op.create_table(
        'card_sets',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('set_id', sa.String(50), nullable=False),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('series', sa.String(100)),
        sa.Column('printed_total', sa.Integer()),
        sa.Column('total', sa.Integer()),
        sa.Column('release_date', sa.DateTime()),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), onupdate=sa.text('CURRENT_TIMESTAMP')),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('set_id')
    )

    # Create cards table
    op.create_table(
        'cards',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('card_id', sa.String(50), nullable=False),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('number', sa.String(20), nullable=False),
        sa.Column('rarity', sa.String(50)),
        sa.Column('image_url', sa.String(500)),
        sa.Column('image_small_url', sa.String(500)),
        sa.Column('supertype', sa.String(50)),
        sa.Column('subtypes', mysql.JSON()),
        sa.Column('types', mysql.JSON()),
        sa.Column('hp', sa.Integer()),
        sa.Column('rules', mysql.JSON()),
        sa.Column('set_id', sa.Integer(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), onupdate=sa.text('CURRENT_TIMESTAMP')),
        sa.ForeignKeyConstraint(['set_id'], ['card_sets.id']),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('card_id')
    )

    # Create card_prices table
    op.create_table(
        'card_prices',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('card_id', sa.Integer(), nullable=False),
        sa.Column('normal_low', sa.Float()),
        sa.Column('normal_mid', sa.Float()),
        sa.Column('normal_high', sa.Float()),
        sa.Column('normal_market', sa.Float()),
        sa.Column('holofoil_low', sa.Float()),
        sa.Column('holofoil_mid', sa.Float()),
        sa.Column('holofoil_high', sa.Float()),
        sa.Column('holofoil_market', sa.Float()),
        sa.Column('recorded_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.ForeignKeyConstraint(['card_id'], ['cards.id']),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    op.drop_table('card_prices')
    op.drop_table('cards')
    op.drop_table('card_sets') 