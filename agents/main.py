import asyncio
import logging
from agents.concrete_agent import ConcreteAgent
from agents.communication import Inbox, Outbox

async def main(duration: int = 10):
    # Set up logging
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    logger.info("Starting the application...")

    # Create inbox and outbox for agent 1
    inbox_agent1 = Inbox()
    outbox_agent1 = Outbox()

    # Create inbox and outbox for agent 2
    inbox_agent2 = Inbox()
    outbox_agent2 = Outbox()

    # Create two instances of ConcreteAgent for testing (loop enabled)
    agent1 = ConcreteAgent(inbox_agent1, outbox_agent2, enable_loop=False)  # Disable loop initially
    agent2 = ConcreteAgent(inbox_agent2, outbox_agent1, enable_loop=False)  # Disable loop initially

    logger.info("Testing agents initialized.")

    # Start testing agents
    await asyncio.gather(
        agent1.start(),
        agent2.start()
    )

    logger.info("Testing agents started.")

    # Start agent loops
    await asyncio.gather(
        agent1.start_loop(duration),
        agent2.start_loop(duration)
    )

    # Run the agents for the specified duration
    await asyncio.sleep(duration)

    # Stop agent loops
    await asyncio.gather(
        agent1.stop_loop(),
        agent2.stop_loop()
    )

    logger.info("Testing agent loops stopped.")

    # Stop testing agents
    await agent1.stop()
    await agent2.stop()

    logger.info("Testing agents stopped.")

if __name__ == "__main__":
    asyncio.run(main())
