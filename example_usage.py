# -*- coding: utf-8 -*-
import json
from client import GenParkAccioMarketIntelligence

intel = GenParkAccioMarketIntelligence()

# 1. Competitor Price Dispersion & Z-Score
comp_prices = [39.99, 44.50, 49.00, 52.50, 59.99, 64.00, 69.99]
disp = intel.calculate_market_price_dispersion_and_variance(comp_prices, baseline_price=49.00)
print(f"Price Dispersion: Mean=${disp['mean_competitor_price']} | StdDev=${disp['price_std_dev']} | Z-Score={disp['baseline_z_score']} ({disp['market_position']})")

# 2. Arc Midpoint Price Elasticity of Demand (PED)
price_qty = [
    {"price": 45.0, "quantity": 1200},
    {"price": 50.0, "quantity": 1050},
    {"price": 55.0, "quantity": 880}
]
ped_res = intel.estimate_competitor_price_elasticity(price_qty)
print()
print(f"Price Elasticity: PED={ped_res['average_price_elasticity']} ({ped_res['elasticity_regime']})")
print(f"  Advice: {ped_res['strategic_pricing_advice']}")
print(f"  Projected Rev Impact (+5% price): {ped_res['projected_revenue_impact']['price_plus_5_pct']}%")

# 3. Supply Chain Lead Time Risk & Buffer Days
lead_times = [14.0, 16.5, 15.0, 22.0, 14.5, 18.0, 15.5]
lt_risk = intel.assess_supply_chain_lead_time_risk(lead_times, supplier_reliability_score=0.90)
print()
print(f"Supply Chain Risk: Score={lt_risk['supply_chain_risk_score']}/100 ({lt_risk['risk_rating']})")
print(f"  Mean Lead Time: {lt_risk['mean_lead_time_days']}d | Recommended Safety Buffer: {lt_risk['recommended_safety_buffer_days']}d")
