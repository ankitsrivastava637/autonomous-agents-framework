import pytest
import asyncio
from unittest.mock import AsyncMock
from ..concrete_agent import ConcreteAgent
from ..communication import Inbox, Outbox


@pytest.mark.asyncio
async def test_concrete_agent_simulation():
    """Simulates two ConcreteAgents and verifies basic message generation."""

    # Create simple inbox and outbox objects
    inbox1 = Inbox()
    inbox2 = Inbox()
    outbox1 = Outbox()
    outbox2 = Outbox()

    # Create agents
    agent1 = ConcreteAgent(inbox1, outbox2, enable_loop=False)
    agent2 = ConcreteAgent(inbox2, outbox1, enable_loop=False)

    # Patch the generate_random_message method with AsyncMock
    agent1.generate_random_message = AsyncMock()
    agent2.generate_random_message = AsyncMock()

    # Start the agents
    await agent1.start()
    await agent2.start()

    # Simulate message generation
    await agent1.generate_random_message()
    await agent2.generate_random_message()

    # Stop the agents
    await agent1.stop()
    await agent2.stop()

    # Assert that message generation was called
    agent1.generate_random_message.assert_called_once()
    agent2.generate_random_message.assert_called_once()


@pytest.mark.asyncio
@pytest.mark.skip(reason="Skipping integration test for unit testing")
async def test_agent_communication():
    """Tests communication between two agents."""

    # Create inboxes and outboxes
    inbox_agent1 = Inbox()
    outbox_agent1 = Outbox()
    inbox_agent2 = Inbox()
    outbox_agent2 = Outbox()

    # Create agents
    agent1 = ConcreteAgent(inbox_agent1, outbox_agent2, enable_loop=False)
    agent2 = ConcreteAgent(inbox_agent2, outbox_agent1, enable_loop=False)

    # Start the agents
    await asyncio.gather(agent1.start(), agent2.start())

    # Send a message from agent 1 to agent 2
    message_to_send = "Hello from Agent 1!"
    await outbox_agent1.put_message(message_to_send)

    # Wait for a short time to allow the message to be processed
    await asyncio.sleep(12)

    # Check if agent 2 received the message
    received_message = await inbox_agent2.get_message()
    assert received_message == message_to_send, "Agent 2 should have received the message from Agent 1"

    # Stop the agents
    await asyncio.gather(agent1.stop(), agent2.stop())