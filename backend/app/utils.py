from typing import Optional
    
def find_price_difference(k_yes:float, k_no:float, p_yes:float, p_no:float) -> Optional[float]:
    return 1.00 - min(k_yes + p_no, k_no + p_yes)

def find_trade(k_yes:float, k_no:float, p_yes:float, p_no:float) -> str:
    if min(k_yes + p_no, k_no + p_yes) == k_yes + p_no:
        return "YES Kalshi + NO Polymarket"
    return "NO Kalshi + YES Polymarket"