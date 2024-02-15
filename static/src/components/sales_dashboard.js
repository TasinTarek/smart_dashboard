/** @odoo-module */

import { registry } from "@web/core/registry"
const { Component, useState } = owl
import { KpiCards } from "./kpi_cards/kpi_cards"

export class Sales extends Component {
    setup(){
        this.state = useState({
            quotations: {
                value: 15,
                percentage: 8,
            },
            period: 90,
        })
    }
    onChangePeriod(){
        
    }
}

Sales.template = "smart_dashboard.SalesTemplate"
Sales.components = {KpiCards}


registry.category("actions").add("smart_dashboard.sales", Sales)