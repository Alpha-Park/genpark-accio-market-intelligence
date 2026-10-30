# -*- coding: utf-8 -*-
"""
GenPark Accio Market Intelligence FastMCP Server
"""

import json
from typing import Dict, List, Any, Optional
from mcp.server.fastmcp import FastMCP
from client import GenParkAccioMarketIntelligence

mcp = FastMCP("genpark-accio-market-intelligence")
intel = GenParkAccioMarketIntelligence()

@mcp.tool()
def calculate_market_price_dispersion_and_variance(
    competitor_prices_json: str,
    baseline_price: float
) -> str:
    """
    Calculates price dispersion, variance, standard deviation, and baseline price Z-score.
    """
    prices = json.loads(competitor_prices_json)
    res = intel.calculate_market_price_dispersion_and_variance(prices, baseline_price)
    return json.dumps(res, indent=2)

@mcp.tool()
def estimate_competitor_price_elasticity(
    price_quantity_observations_json: str
) -> str:
    """
    Calculates Price Elasticity of Demand (PED) using the Arc Midpoint formula.
    """
    obs = json.loads(price_quantity_observations_json)
    res = intel.estimate_competitor_price_elasticity(obs)
    return json.dumps(res, indent=2)

@mcp.tool()
def assess_supply_chain_lead_time_risk(
    lead_time_days_history_json: str,
    supplier_reliability_score: float = 0.85,
    target_service_level_z: float = 1.645
) -> str:
    """
    Assesses lead time distribution and calculates required safety buffer days.
    """
    history = json.loads(lead_time_days_history_json)
    res = intel.assess_supply_chain_lead_time_risk(history, supplier_reliability_score, target_service_level_z)
    return json.dumps(res, indent=2)

def main():
    print("Testing Accio Market Intelligence:")
    print(calculate_market_price_dispersion_and_variance("[45.0, 48.0, 52.0, 55.0]", 50.0))

if __name__ == "__main__":
    main()
