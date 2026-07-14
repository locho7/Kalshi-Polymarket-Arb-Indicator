import type { OpportunityType } from "../data/mockOpportunities";

export function findTrade(opportunity: OpportunityType) {
    if (Math.min(opportunity.kalshiYes + opportunity.polymarketNo, 
                 opportunity.kalshiNo + opportunity.polymarketYes) ===
                 opportunity.kalshiYes + opportunity.polymarketNo) {
        return "YES Kalshi + NO Polymarket";
    } else {
        return "NO Kalshi + YES Polymarket";
    }
}