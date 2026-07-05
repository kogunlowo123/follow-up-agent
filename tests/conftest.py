"""Test configuration for Follow-Up Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "follow-up-agent", "category": "Sales"}
