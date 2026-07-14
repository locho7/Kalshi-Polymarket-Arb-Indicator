export type OpportunityType = {
    title: string;
    category: string;
    kalshiYes: number;
    kalshiNo: number;
    polymarketYes: number;
    polymarketNo: number;
    lastUpdated: string;
}

export const mockOpportunities: OpportunityType[] = [
    {
        title: "Btc Up or Down",
        category: "Crypto-5M",
        kalshiYes: 0.52,
        kalshiNo: 0.48,
        polymarketYes: 0.54,
        polymarketNo: 0.46,
        lastUpdated: "07-03-2026-20:13:52"
    },
    {
        title: "Mexico vs England",
        category: "Sports-Soccer-World Cup",
        kalshiYes: 0.51,
        kalshiNo: 0.49,
        polymarketYes: 0.53,
        polymarketNo: 0.47,
        lastUpdated: "07-03-2026-20:14:43"
    },
    {
        title: "Highest temperature in LA today?",
        category: "Climate And Weather-Daily Temperature",
        kalshiYes: 0.68,
        kalshiNo: 0.32,
        polymarketYes: 0.63,
        polymarketNo: 0.37,
        lastUpdated: "07-03-2026-20:14:34"
    }
]


