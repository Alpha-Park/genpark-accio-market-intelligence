# genpark-accio-market-intelligence

![Tests](https://img.shields.io/badge/tests-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Dependencies](https://img.shields.io/badge/dependencies-zero-success)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)

GenPark Accio Market Intelligence is a zero-dependency e-commerce pricing and competitive intelligence engine implementing market price dispersion variance and Z-score analytics, arc midpoint price elasticity of demand (PED) modeling, and supply chain lead-time volatility buffer calculations.

```mermaid
flowchart LR
    A[Competitor Price Stream] --> B[Dispersion & Z-Score Engine]
    B --> C[Market Positioning & Spread Metric]
    D[Historical Price-Quantity Pairs] --> E[Arc Midpoint Elasticity Formula]
    E --> F[Elastic / Inelastic Revenue Projection]
    G[Lead Time Days Distribution] --> H[Stochastic Buffer Model]
    H --> I[Safety Buffer Days & Risk Rating]
```

## Features
- **Price Dispersion & Z-Score**: Evaluates competitive pricing distributions, standard deviation, and quartile spreads.
- **Arc Midpoint Elasticity (PED)**: Quantifies volume sensitivity to pricing adjustments and computes prospective revenue impact curves.
- **Supply Chain Lead-Time Risk**: Projects required safety stock buffer days based on supplier historical variance and reliability scores.

## Quickstart

```python
from client import GenParkAccioMarketIntelligence

intel = GenParkAccioMarketIntelligence()
res = intel.calculate_market_price_dispersion_and_variance([39.99, 44.50, 49.00, 52.50, 59.99], 49.00)
print("Market Position:", res["market_position"], "Z-Score:", res["baseline_z_score"])
```

## License
MIT
