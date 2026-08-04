export type OpportunityType = {
    id: string;
    title: string;

    kalshi_market_ticker: string;
    polymarket_slug: string;
    polymarket_id: string;

    kalshi_yes_ask: number | null;
    kalshi_no_ask: number | null
    polymarket_yes_ask: number | null
    polymarket_no_ask: number | null

    price_difference: number | null
    best_trade: string

    last_updated: string
}