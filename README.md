# Follow-Up Agent

[![CI](https://github.com/kogunlowo123/follow-up-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/follow-up-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Sales | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Sales follow-up agent that generates timely follow-up messages, manages multi-touch sequences, identifies re-engagement opportunities for stale deals, and tracks follow-up effectiveness.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `generate_followup` | Generate a contextual follow-up message based on last interaction |
| `schedule_sequence` | Schedule a multi-touch follow-up sequence |
| `identify_reengagement` | Identify stale deals that could be re-engaged |
| `personalize_touchpoint` | Personalize a follow-up touchpoint with relevant triggers |
| `measure_effectiveness` | Measure follow-up effectiveness by response and conversion rates |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/follow-up/execute` | Execute primary action |
| `POST` | `/api/v1/follow-up/analyze` | Run analysis |
| `GET` | `/api/v1/follow-up/metrics` | Get metrics |
| `PUT` | `/api/v1/follow-up/configure` | Configure settings |
| `POST` | `/api/v1/follow-up/report` | Generate report |

## Features

- Follow-Up
- Analytics
- Automation

## Integrations

- Salesforce
- Hubspot
- Outreach
- Apollo
- Linkedin Sales Navigator

## Architecture

```
follow-up-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── follow_up_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**CRM + Sales Engagement + LLM**

---

Built as part of the Enterprise AI Agent Platform.
