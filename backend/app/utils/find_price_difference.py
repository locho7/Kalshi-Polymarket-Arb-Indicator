from typing import Optional
# def find_price_differenece(op: Opportunity) -> Optional[float]:
#     if (op.kalshi_yes_ask and op.kalshi_no_ask and
#         op.polymarket_yes_ask and op.polymarket_no_ask):
#         return 1.00 - min(op.kalshi_yes_ask + op.polymarket_no_ask,
#                           op.kalshi_no_ask + op.polymarket_yes_ask)
    
def find_price_difference(k_yes:float, k_no:float, p_yes:float, p_no:float) -> Optional[float]:
    return 1.00 - min(k_yes + p_no, k_no + p_yes)
