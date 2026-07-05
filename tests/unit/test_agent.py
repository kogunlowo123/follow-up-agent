"""Follow-Up Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_generate_followup():
    """Test Generate a contextual follow-up message based on last interaction."""
    tools = AgentTools()
    result = await tools.generate_followup(prospect_id="test", last_interaction="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_schedule_sequence():
    """Test Schedule a multi-touch follow-up sequence."""
    tools = AgentTools()
    result = await tools.schedule_sequence(prospect_id="test", sequence_steps="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_identify_reengagement():
    """Test Identify stale deals that could be re-engaged."""
    tools = AgentTools()
    result = await tools.identify_reengagement(days_inactive=1, pipeline_stage="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_personalize_touchpoint():
    """Test Personalize a follow-up touchpoint with relevant triggers."""
    tools = AgentTools()
    result = await tools.personalize_touchpoint(prospect_id="test", trigger_event="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.follow_up_agent_agent import FollowUpAgentAgent
    agent = FollowUpAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
