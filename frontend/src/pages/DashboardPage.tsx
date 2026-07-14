import OpportunityTable from "../components/OpportunityTable/OpportunityTable"
import Header from "../components/Header";

function DashboardPage() {
    return (
    <div className="min-h-screen bg-background0">
        <Header />
        <OpportunityTable />
    </div>
    )
}

export default DashboardPage