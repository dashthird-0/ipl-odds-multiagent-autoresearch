# Legality Note

## What This Project Does

Cricket Pricing Room reads public market-implied probabilities from Polymarket's
documented public data API. It uses these prices as one input to a multi-agent
reasoning system that produces probability-band memos for IPL matches.

## What This Project Does Not Do

- Does not place trades on any platform
- Does not recommend trades or positions
- Does not automate orders
- Does not interact with any trading frontend
- Does not advise users to access geo-restricted interfaces
- Does not facilitate, encourage, or enable betting activity

## Polymarket API Access

Polymarket's public data API endpoints are:
- `https://gamma-api.polymarket.com` — market discovery, event data, prices
- `https://clob.polymarket.com` — orderbook data

These are documented, public, read-only endpoints that do not require authentication.
They are distinct from Polymarket's trading frontend (which is geo-restricted in India
under the Promotion and Regulation of Online Gaming Act, 2025).

The API subdomains are accessible from India without VPN. ISP-level DNS blocking
affects the main `polymarket.com` domain but not the API subdomains.

## Indian Regulatory Context

India's Promotion and Regulation of Online Gaming Act (2025) restricts:
- Real-money online gaming/betting platforms
- Trading frontends of prediction markets
- VPN access to blocked gambling/betting sites

It does not restrict:
- Academic or personal research using public data
- Reading publicly accessible API endpoints
- Analyzing publicly available price data

This project operates in the research space. It reads public data to study how
multi-agent reasoning systems calibrate against market prices.

## Naming Conventions

To maintain the research framing, this project never uses:
- "Edge," "alpha," "value bet," "trading signal," "odds"

It uses:
- "Market-implied probability," "model band," "fair value band," "directional view"

## Disclaimer (as used in README)

> Cricket Pricing Room reads public market-implied probabilities from Polymarket's
> documented public API. The system does not place trades, recommend trades, automate
> orders, or advise users to access restricted trading interfaces. Polymarket's trading
> frontend is geo-restricted in India; this project does not interact with that interface.
> The public market data API is queried for research purposes only — to study how
> multi-agent reasoning systems calibrate against public market prices.
