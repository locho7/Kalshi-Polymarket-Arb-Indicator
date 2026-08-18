import type { OpportunityType } from "../../data/opportunityType.ts";
import { useState, useEffect } from 'react';

function TableHeading(props: { text: string}) {
    return (
        <th className={`m-2 p-4 border-b border-border text-text-primary font-semibold text-l`}>
            {props.text}
        </th>
    )
}

function TableData( props: { text: string, textColor?: string }) {
    return (
    <th className={`m-2 p-4 border-b border-border 
    ${props.textColor ?? 'text-text-primary'} font-normal text-l`}>
        {props.text}
    </th>
    )
}

function OpportunityTable() {
    const [opportunityData, setOpportunityData] = useState<OpportunityType[]>([]);
    const [isInitializing, setIsInitializing] = useState(true);
    const [isRefreshing, setIsRefreshing] = useState(false);
    const [isOnCooldown, setIsOnCooldown] = useState(false)
    const [error, setError] = useState<string | null>(null);

    async function fetchOpportunityData() {
        try {
            setError(null);

            const response = await fetch("http://127.0.0.1:8000/get-opportunities");
            if (!response.ok) {
                throw new Error(`Request failed with status ${response.status}`);
            };
            const data = await response.json();

            setOpportunityData(data);
        } catch (error) {
            setError("Could not load opportunities")
            console.log(error)
        } finally {
            setIsInitializing(false)
        }
    }

    useEffect(() => {
        fetchOpportunityData()
        const intervalID = setInterval(fetchOpportunityData, 30000);
        return () => clearInterval(intervalID)
    }, [])

    if (isInitializing) {
        return (
            <div className="m-5 rounded-xl border border-border bg-background1 p-5 text-text-primary">
                Loading opportunities...
            </div>
        )
    }

    if (error) {
        return (
            <div className="m-5 rounded-xl border border-red-500 bg-background1 p-5 text-red-400">
                {error}
            </div>
        );
    } 
    
    if (opportunityData.length === 0) {
        return (
            <div className="m-5 rounded-xl border border-border bg-background1 p-5 text-text-secondary">
                No opportunities found right now.
            </div>
        );
    }

    async function handleRefresh() {
        setIsRefreshing(true)
        setIsOnCooldown(true)

        await fetchOpportunityData()

        setIsRefreshing(false)
        setTimeout(() => {
            setIsOnCooldown(false);
        }, 5000);
    }

    return (
    <div className="m-5 bg-background1 rounded-xl
         border-1 border-border overflow-hidden">
        <div className="border-b border-border p-5
        flex items-center justify-between">
            <h2 className="text-xl font-semibold text-text-primary">
                Opportunity Table
            </h2>
            <div className="flex items-center gap-4">
                <p className="text-m text-text-secondary">
                    Last updated: {opportunityData[0]?.last_updated ?? "Never"}
                </p>
                <button className="bg-background1 px-3 py-2 font-bold cursor-pointer rounded-lg
                text-text-secondary hover:bg-slate-500 text-2xl disabled:hover:bg-background1 
                disabled:cursor-not-allowed" onClick={handleRefresh} disabled={isRefreshing || isOnCooldown}>
                    {isRefreshing || isOnCooldown ? "..." : "⟳"}
                </button>
            </div>
        </div>
        <table className="w-full border-collapse">
            <tr>
                <TableHeading text="Title" />
                <TableHeading text="Kalshi | Polymarket (Yes, No)" />
                <TableHeading text="Trade"/>
                <TableHeading text="Gross Edge"/>
            </tr>
            {opportunityData.map((opportunity: OpportunityType) => {
                if (opportunity.price_difference === null) return
                return (
                    <tr key={opportunity.id}>
                        <TableData text={opportunity.title} />
                        <TableData text={`(${opportunity.kalshi_yes_ask}, ${opportunity.kalshi_no_ask}) |  
                        (${opportunity.polymarket_yes_ask}, ${opportunity.polymarket_no_ask})`}/>
                        <TableData text={opportunity.best_trade} />
                        <TableData text={`${Math.trunc(100*opportunity.price_difference)}¢`} 
                                   textColor = "text-green-500"/>
                    </tr>
                )
            })}
        </table>
    </div>
    )
}

export default OpportunityTable