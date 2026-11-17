---
description: Proactive Market Intelligence Agent. Conducts autonomous research, competitor tracking, and trend forecasting for global markets.
license: MIT
metadata:
  last_deployed: "2026-04-25"
  version: "1.0.0"
  source: "https://www.accio.com/"
---

# Accio Market Intelligence

This skill transforms an agent into a dedicated researcher that proactively monitors global market shifts. It is designed for businesses that need to stay ahead of fast-moving e-commerce and tech trends.

## MCP runtime requirements

The standard-library-only policy applies to direct `client.py` use. Running `mcp_server.py` requires Python 3.10+ and the official `mcp` SDK (`mcp>=1.0.0,<2`) from `requirements.txt`. Install it into your chosen environment from the repository checkout:

```bash
python -m pip install -r requirements.txt
```

Configure the MCP client with that environment's absolute Python executable path and the absolute path to `mcp_server.py`. The client launches a local STDIO process; a GitHub URL is not a remote MCP endpoint.

## Instructions
1. **Autonomous Browsing:** Navigate the web to collect data on competitors, pricing, and consumer sentiment.
2. **Trend Forecasting:** Analyze gathered data to identify emerging patterns and predict upcoming market demands.
3. **Recursive Monitoring:** Set up "watchers" to alert the user when specific market conditions or competitor actions occur.
4. **Structured Intelligence:** Format findings into "Intelligence Briefs" with clear actionable insights.

## Examples
- "Find the top 5 trending products in the US beauty market right now and summarize why they are popular."
- "Monitor my top 3 competitors and send me a weekly report on their new product launches and pricing changes."
