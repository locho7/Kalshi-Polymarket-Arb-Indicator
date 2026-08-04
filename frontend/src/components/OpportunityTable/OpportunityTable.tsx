import type { OpportunityType } from "../../data/opportunityType.ts";
import { useState, useEffect } from 'react';

function TableHeading(props: { text: string }) {
    return (
        <th className="m-2 p-4 border-b border-border text-text-primary font-semibold text-l">
            {props.text}
        </th>
    )
}

function TableData( props: { text: string }) {
    return (
    <th className="m-2 p-4 border-b border-border text-text-primary font-normal text-l">
        {props.text}
    </th>
    )
}

function OpportunityTable() {
    const [opportunityData, setOpportunityData] = useState<OpportunityType[]>([]);

    async function fetchOpportunityData() {
        try {
            const response = await fetch("http://127.0.0.1:8000/get-opportunities");
            const data = await response.json();
            setOpportunityData(data);
        } catch (error) {
            throw new Error("Error fetching opportunity data");
        }
    }

    useEffect(() => {
        fetchOpportunityData()
        const intervalID = setInterval(fetchOpportunityData, 30000);
        return () => clearInterval(intervalID)
    }, [])

    return (
    <div className="m-5 bg-background1 rounded-xl
         border-1 border-border overflow-hidden">
        <table className="w-full border-collapse">
            <tr className="border-b border-border">
                <h2 className="p-5 text-xl font-semibold text-text-primary">
                    Opportunity Table
                </h2>
            </tr>
            <tr>
                <TableHeading text="Title" />
                <TableHeading text="Trade" />
                <TableHeading text="Price Difference" />
                <TableHeading text="Last Updated" />
            </tr>
            {opportunityData.map((opportunity: OpportunityType) => {
                if (opportunity.price_difference === null) return
                return (
                    <tr key={opportunity.id}>
                        <TableData text={opportunity.title} />
                        <TableData text={opportunity.best_trade} />
                        <TableData text={`${Math.trunc(100*opportunity.price_difference)}¢`} />
                        <TableData text={opportunity.last_updated} />
                    </tr>
                )
            })}
        </table>
    </div>
    )
}

export default OpportunityTable