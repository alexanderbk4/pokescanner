"""add card details

Revision ID: 002
Revises: 001
Create Date: 2024-04-05

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '002'
down_revision = '001'
branch_labels = None
depends_on = None

def upgrade():
    # Add new columns to card_sets
    op.add_column('card_sets', sa.Column('ptcgo_code', sa.String(10)))
    op.add_column('card_sets', sa.Column('symbol_url', sa.String(500)))
    op.add_column('card_sets', sa.Column('logo_url', sa.String(500)))

    # Add new columns to cards
    op.add_column('cards', sa.Column('level', sa.String(10)))
    op.add_column('cards', sa.Column('evolves_from', sa.String(100)))
    op.add_column('cards', sa.Column('abilities', mysql.JSON()))
    op.add_column('cards', sa.Column('attacks', mysql.JSON()))
    op.add_column('cards', sa.Column('weaknesses', mysql.JSON()))
    op.add_column('cards', sa.Column('resistances', mysql.JSON()))
    op.add_column('cards', sa.Column('retreat_cost', mysql.JSON()))
    op.add_column('cards', sa.Column('converted_retreat_cost', sa.Integer()))
    op.add_column('cards', sa.Column('flavor_text', sa.String(500)))
    op.add_column('cards', sa.Column('artist', sa.String(100)))
    op.add_column('cards', sa.Column('national_pokedex_number', sa.Integer()))

    # Update card_prices table
    op.drop_column('card_prices', 'normal_low')
    op.drop_column('card_prices', 'normal_mid')
    op.drop_column('card_prices', 'normal_high')
    op.drop_column('card_prices', 'normal_market')
    op.drop_column('card_prices', 'holofoil_low')
    op.drop_column('card_prices', 'holofoil_mid')
    op.drop_column('card_prices', 'holofoil_high')
    op.drop_column('card_prices', 'holofoil_market')

    op.add_column('card_prices', sa.Column('tcgplayer_url', sa.String(500)))
    op.add_column('card_prices', sa.Column('tcgplayer_holofoil_low', sa.Float()))
    op.add_column('card_prices', sa.Column('tcgplayer_holofoil_mid', sa.Float()))
    op.add_column('card_prices', sa.Column('tcgplayer_holofoil_high', sa.Float()))
    op.add_column('card_prices', sa.Column('tcgplayer_holofoil_market', sa.Float()))
    op.add_column('card_prices', sa.Column('cardmarket_url', sa.String(500)))
    op.add_column('card_prices', sa.Column('cardmarket_average_sell_price', sa.Float()))
    op.add_column('card_prices', sa.Column('cardmarket_low_price', sa.Float()))
    op.add_column('card_prices', sa.Column('cardmarket_trend_price', sa.Float()))
    op.add_column('card_prices', sa.Column('cardmarket_low_price_ex_plus', sa.Float()))
    op.add_column('card_prices', sa.Column('cardmarket_avg1', sa.Float()))
    op.add_column('card_prices', sa.Column('cardmarket_avg7', sa.Float()))
    op.add_column('card_prices', sa.Column('cardmarket_avg30', sa.Float()))

def downgrade():
    # Remove columns from card_sets
    op.drop_column('card_sets', 'ptcgo_code')
    op.drop_column('card_sets', 'symbol_url')
    op.drop_column('card_sets', 'logo_url')

    # Remove columns from cards
    op.drop_column('cards', 'level')
    op.drop_column('cards', 'evolves_from')
    op.drop_column('cards', 'abilities')
    op.drop_column('cards', 'attacks')
    op.drop_column('cards', 'weaknesses')
    op.drop_column('cards', 'resistances')
    op.drop_column('cards', 'retreat_cost')
    op.drop_column('cards', 'converted_retreat_cost')
    op.drop_column('cards', 'flavor_text')
    op.drop_column('cards', 'artist')
    op.drop_column('cards', 'national_pokedex_number')

    # Restore original card_prices columns
    op.drop_column('card_prices', 'tcgplayer_url')
    op.drop_column('card_prices', 'tcgplayer_holofoil_low')
    op.drop_column('card_prices', 'tcgplayer_holofoil_mid')
    op.drop_column('card_prices', 'tcgplayer_holofoil_high')
    op.drop_column('card_prices', 'tcgplayer_holofoil_market')
    op.drop_column('card_prices', 'cardmarket_url')
    op.drop_column('card_prices', 'cardmarket_average_sell_price')
    op.drop_column('card_prices', 'cardmarket_low_price')
    op.drop_column('card_prices', 'cardmarket_trend_price')
    op.drop_column('card_prices', 'cardmarket_low_price_ex_plus')
    op.drop_column('card_prices', 'cardmarket_avg1')
    op.drop_column('card_prices', 'cardmarket_avg7')
    op.drop_column('card_prices', 'cardmarket_avg30')

    op.add_column('card_prices', sa.Column('normal_low', sa.Float()))
    op.add_column('card_prices', sa.Column('normal_mid', sa.Float()))
    op.add_column('card_prices', sa.Column('normal_high', sa.Float()))
    op.add_column('card_prices', sa.Column('normal_market', sa.Float()))
    op.add_column('card_prices', sa.Column('holofoil_low', sa.Float()))
    op.add_column('card_prices', sa.Column('holofoil_mid', sa.Float()))
    op.add_column('card_prices', sa.Column('holofoil_high', sa.Float()))
    op.add_column('card_prices', sa.Column('holofoil_market', sa.Float())) 