# -*- coding: utf-8 -*-
"""
GenPark Accio Market Intelligence Client
Zero-dependency market price dispersion variance calculator, midpoint price elasticity estimator,
and supply chain lead-time safety buffer risk modeler.
"""

import math
from typing import Dict, List, Any, Optional

class GenParkAccioMarketIntelligence:
    """
    Computes cross-marketplace competitor price dispersion, elasticity coefficients,
    and lead-time supply chain volatility.
    """

    def calculate_market_price_dispersion_and_variance(
        self,
        competitor_prices: List[float],
        baseline_price: float
    ) -> Dict[str, Any]:
        """
        Calculates price dispersion, variance, standard deviation, and baseline price Z-score.
        """
        if not competitor_prices or baseline_price <= 0:
            raise ValueError("Competitor prices list cannot be empty and baseline price must be positive.")

        prices = sorted(competitor_prices)
        n = len(prices)
        mean_p = sum(prices) / n

        variance = sum((p - mean_p) ** 2 for p in prices) / max(1, n - 1) if n > 1 else 0.0
        std_p = math.sqrt(variance)

        # Coefficient of variation (CV = std / mean)
        cv = round(std_p / max(1e-9, mean_p), 4)

        # Z-score of baseline price relative to market
        z_score = round((baseline_price - mean_p) / max(1e-9, std_p), 3) if std_p > 0 else 0.0

        # Percentile rank
        rank = sum(1 for p in prices if p <= baseline_price) / float(n)

        min_p = prices[0]
        max_p = prices[-1]
        spread = round(max_p - min_p, 2)
        spread_ratio = round(spread / max(1e-9, min_p), 3)

        return {
            "baseline_price": baseline_price,
            "competitor_count": n,
            "mean_competitor_price": round(mean_p, 2),
            "median_competitor_price": round(prices[n // 2], 2),
            "price_variance": round(variance, 2),
            "price_std_dev": round(std_p, 2),
            "coefficient_of_variation": cv,
            "price_spread_usd": spread,
            "spread_to_min_ratio": spread_ratio,
            "baseline_z_score": z_score,
            "baseline_percentile_rank": round(rank * 100.0, 1),
            "market_position": "PREMIUM_OVERPRICED" if z_score > 1.0 else ("DISCOUNT_UNDERPRICED" if z_score < -1.0 else "AT_MARKET")
        }

    def estimate_competitor_price_elasticity(
        self,
        price_quantity_observations: List[Dict[str, float]]
    ) -> Dict[str, Any]:
        """
        Calculates Price Elasticity of Demand (PED) using the Arc Midpoint formula:
        PED = ((Q2 - Q1) / ((Q1 + Q2)/2)) / ((P2 - P1) / ((P1 + P2)/2))
        """
        if len(price_quantity_observations) < 2:
            raise ValueError("Need at least 2 price-quantity observation pairs.")

        elasticities = []
        for i in range(1, len(price_quantity_observations)):
            p1 = price_quantity_observations[i - 1]["price"]
            q1 = price_quantity_observations[i - 1]["quantity"]
            p2 = price_quantity_observations[i]["price"]
            q2 = price_quantity_observations[i]["quantity"]

            delta_q = q2 - q1
            avg_q = (q1 + q2) / 2.0
            delta_p = p2 - p1
            avg_p = (p1 + p2) / 2.0

            pct_q = delta_q / max(1e-9, avg_q)
            pct_p = delta_p / max(1e-9, avg_p)

            if abs(pct_p) > 1e-6:
                ped = pct_q / pct_p
                elasticities.append(ped)

        avg_ped = round(sum(elasticities) / len(elasticities), 3) if elasticities else -1.0
        abs_ped = abs(avg_ped)

        if abs_ped > 1.2:
            regime = "ELASTIC (Price sensitive: volume drops faster than price increases)"
            pricing_advice = "Discounting or bundling will maximize total gross revenue."
        elif abs_ped < 0.8:
            regime = "INELASTIC (Price insensitive: strong pricing power)"
            pricing_advice = "Price increases will directly expand gross margin with minimal volume loss."
        else:
            regime = "UNITARY_ELASTIC (Proportional response)"
            pricing_advice = "Maintain current pricing; focus on value-add differentiators."

        return {
            "observations_analyzed": len(price_quantity_observations),
            "average_price_elasticity": avg_ped,
            "elasticity_regime": regime,
            "strategic_pricing_advice": pricing_advice,
            "projected_revenue_impact": {
                "price_plus_5_pct": round((1.0 + 0.05) * (1.0 + avg_ped * 0.05) - 1.0, 4) * 100.0,
                "price_minus_5_pct": round((1.0 - 0.05) * (1.0 - avg_ped * 0.05) - 1.0, 4) * 100.0
            }
        }

    def assess_supply_chain_lead_time_risk(
        self,
        lead_time_days_history: List[float],
        supplier_reliability_score: float = 0.85,
        target_service_level_z: float = 1.645
    ) -> Dict[str, Any]:
        """
        Assesses lead time distribution and calculates required safety buffer days for target service level.
        Buffer Days = Z * std_dev + (1 - reliability) * mean
        """
        if not lead_time_days_history:
            raise ValueError("Lead time history cannot be empty.")

        n = len(lead_time_days_history)
        mean_lt = sum(lead_time_days_history) / n
        var_lt = sum((d - mean_lt) ** 2 for d in lead_time_days_history) / max(1, n - 1) if n > 1 else 0.0
        std_lt = math.sqrt(var_lt)

        # Safety buffer days
        service_buffer = target_service_level_z * std_lt
        reliability_penalty = (1.0 - min(1.0, max(0.0, supplier_reliability_score))) * mean_lt
        recommended_buffer_days = round(service_buffer + reliability_penalty, 1)

        # Risk score (0 to 100)
        cv = std_lt / max(1e-9, mean_lt)
        risk_score = round(min(100.0, (cv * 50.0) + ((1.0 - supplier_reliability_score) * 50.0)), 1)

        return {
            "mean_lead_time_days": round(mean_lt, 1),
            "lead_time_std_dev_days": round(std_lt, 1),
            "supplier_reliability_score": supplier_reliability_score,
            "recommended_safety_buffer_days": recommended_buffer_days,
            "total_effective_lead_time_days": round(mean_lt + recommended_buffer_days, 1),
            "supply_chain_risk_score": risk_score,
            "risk_rating": "STABLE" if risk_score < 35.0 else ("MODERATE_VOLATILITY" if risk_score < 65.0 else "HIGH_LEAD_TIME_RISK")
        }
