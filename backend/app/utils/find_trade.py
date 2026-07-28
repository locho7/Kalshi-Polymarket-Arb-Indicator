# def find_trade(op: Opportunity) -> str:
#     if not (op.kalshi_yes_ask and op.kalshi_no_ask
#        and op.polymarket_yes_ask and op.polymarket_no_ask):
#         return "NO TRADE"
#     if (min(op.kalshi_yes_ask + op.polymarket_no_ask,
#             op.kalshi_no_ask + op.polymarket_yes_ask)
#             == op.kalshi_yes_ask + op.polymarket_no_ask):
#         return "YES Kalshi + NO Polymarket"
#     else: return "NO Kalshi + YES Polymarket"

def find_trade(k_yes:float, k_no:float, p_yes:float, p_no:float) -> str:
    if min(k_yes + p_no, k_no + p_yes) == k_yes + p_no:
        return "YES Kalshi + NO Polymarket"
    return "NO Kalshi + YES Polymarket"