import type { OpportunityType } from "../data/mockOpportunities";

export function priceDifference(opportunity: OpportunityType):number {
    return 1.00 - Math.min(opportunity.kalshiYes +
                           opportunity.polymarketNo, 
                           opportunity.kalshiNo + 
                           opportunity.polymarketYes)
}
