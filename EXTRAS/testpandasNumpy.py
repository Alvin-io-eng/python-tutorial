# Create a 12‑month financial model for a Nairobi catering company (KES)
import pandas as pd
import numpy as np

# Assumptions
assumptions = {
    "Currency": "KES",
    "Months": 12,
    # Channel mix and unit economics
    "Channels": ["Corporate Catering", "Weddings", "Private Events", "Office Meal Plans", "School/Institution Contracts"],
    "Avg_Pax": [120, 200, 60, 80, 300],  # average guests per event/day served per site
    "Events_per_Month_M1": [6, 1, 8, 16, 2],  # Month 1 baseline: events or service-days (meal plans counted as service-days)
    "Growth_per_Month_%": [8, 6, 5, 10, 4],  # expected MoM growth in event count
    "Price_per_Pax": [1500, 2200, 1300, 450, 300],  # average revenue per guest/day
    "COGS_%": [0.45, 0.48, 0.48, 0.55, 0.60],  # food, disposables, direct labor tied to servings
    "Variable_Overhead_per_Event": [6000, 12000, 4000, 2000, 5000],  # transport, fuel, setup, etc.
    # Marketing & Sales
    "Marketing_Budget_M1": 120000,  # Month 1 marketing budget
    "Marketing_Growth_%": 5,        # MoM increase in marketing
    "CAC_per_Channel": [8000, 15000, 4000, 6000, 20000],  # cost to acquire one event/site/day
    # Fixed costs (monthly)
    "Kitchen_Rent": 120000,
    "Utilities": 30000,
    "Admin_Salaries": 350000,
    "Chefs_Kitchen_Staff": 280000,
    "Transport_Vehicles_Fuel_Maint": 90000,
    "Licenses_Compliance": 15000,
    "Insurance": 20000,
    "Misc_Contingency": 30000
}

months = [f"M{i}" for i in range(1, assumptions["Months"]+1)]

# Build channel projections
channels = assumptions["Channels"]
df_list = []

for idx, ch in enumerate(channels):
    events = []
    e = assumptions["Events_per_Month_M1"][idx]
    g = assumptions["Growth_per_Month_%"][idx] / 100.0
    for m in range(assumptions["Months"]):
        if m == 0:
            events.append(e)
        else:
            e = e * (1 + g)
            events.append(e)
    events = np.round(events, 0).astype(int)

    pax = assumptions["Avg_Pax"][idx]
    price = assumptions["Price_per_Pax"][idx]
    cogs_pct = assumptions["COGS_%"][idx]
    var_ovh = assumptions["Variable_Overhead_per_Event"][idx]

    revenue = events * pax * price
    cogs = revenue * cogs_pct
    var_overhead = events * var_ovh
    gross_profit = revenue - cogs - var_overhead

    df = pd.DataFrame({
        "Month": months,
        "Channel": ch,
        "Events/Service-Days": events,
        "Avg Pax / Day": pax,
        "Price per Pax (KES)": price,
        "Revenue (KES)": revenue,
        "COGS (KES)": np.round(cogs, 0),
        "Variable Overhead (KES)": var_overhead,
        "Channel Gross Profit (KES)": np.round(gross_profit, 0)
    })
    df_list.append(df)

channels_df = pd.concat(df_list, ignore_index=True)

# Marketing spend projection
mkt = []
mkt_budget = assumptions["Marketing_Budget_M1"]
g_mkt = assumptions["Marketing_Growth_%"] / 100.0
for m in range(assumptions["Months"]):
    if m == 0:
        mkt.append(mkt_budget)
    else:
        mkt_budget = mkt_budget * (1 + g_mkt)
        mkt.append(mkt_budget)
marketing_df = pd.DataFrame({"Month": months, "Marketing Spend (KES)": np.round(mkt, 0)})

# Fixed costs projection
fixed_costs = (
    assumptions["Kitchen_Rent"] + assumptions["Utilities"] + assumptions["Admin_Salaries"]
    + assumptions["Chefs_Kitchen_Staff"] + assumptions["Transport_Vehicles_Fuel_Maint"]
    + assumptions["Licenses_Compliance"] + assumptions["Insurance"] + assumptions["Misc_Contingency"]
)
fixed_df = pd.DataFrame({"Month": months, "Fixed Costs (KES)": [fixed_costs]*assumptions["Months"]})

# P&L aggregation
summary = channels_df.groupby("Month").agg({
    "Revenue (KES)": "sum",
    "COGS (KES)": "sum",
    "Variable Overhead (KES)": "sum",
    "Channel Gross Profit (KES)": "sum"
}).reset_index()

summary = summary.merge(marketing_df, on="Month").merge(fixed_df, on="Month")
summary["Operating Profit (KES)"] = summary["Channel Gross Profit (KES)"] - summary["Marketing Spend (KES)"] - summary["Fixed Costs (KES)"]
summary["Gross Margin %"] = (summary["Channel Gross Profit (KES)"] / summary["Revenue (KES)"]).round(3)

# Break-even: month where cumulative operating profit turns positive
summary["Cumulative Operating Profit (KES)"] = summary["Operating Profit (KES)"].cumsum()

# Export to Excel
with pd.ExcelWriter("/mnt/data/Nairobi_Catering_Financial_Model.xlsx", engine="xlsxwriter") as writer:
    # Assumptions sheet
    assump_table = pd.DataFrame({
        "Item": list(assumptions.keys()),
        "Value": [str(v) if not isinstance(v, (int,float)) else v for v in assumptions.values()]
    })
    assump_table.to_excel(writer, index=False, sheet_name="Assumptions")
    channels_df.to_excel(writer, index=False, sheet_name="Channels_Detail")
    marketing_df.to_excel(writer, index=False, sheet_name="Marketing")
    fixed_df.to_excel(writer, index=False, sheet_name="Fixed_Costs")
    summary.to_excel(writer, index=False, sheet_name="P&L_Summary")

# Display the P&L summary to the user
import caas_jupyter_tools
caas_jupyter_tools.display_dataframe_to_user("12-Month P&L Summary (KES)", summary)

"/mnt/data/Nairobi_Catering_Financial_Model.xlsx"
