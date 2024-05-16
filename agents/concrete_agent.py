import asyncio
import logging
import random
from typing import Any, Callable, Type
from .autonomous_agent import AutonomousAgent

class ConcreteAgent(AutonomousAgent):
    def __init__(self, inbox: "Inbox", outbox: "Outbox", enable_loop: bool = True):
        """
        Initialize the ConcreteAgent.

        :param inbox: The inbox for receiving messages.
        :param outbox: The outbox for sending messages.
        :param enable_loop: Whether to enable the agent's loop (default is True).
        """
        super().__init__(inbox, outbox)
        self._logger = logging.getLogger(__name__)
        self._enable_loop = enable_loop
        self._task = None  # To hold the task running the agent loop

    async def consume_messages(self):
        """Continuously consume messages from the inbox."""
        await super().consume_messages()
        self._logger.debug("Consumed message")

    async def emit_message(self, message: Any):
        """Emit a message to the outbox."""
        await super().emit_message(message)
        self._logger.debug(f"Emitted message: {message}")

    async def handle_message(self, message: Any):
        """Handle an incoming message."""
        await super().handle_message(message)
        if "hello" in message:
            self._logger.info("Received hello message: %s", message)

    async def register_behaviour(self, behaviour: Callable[[], Any]):
        """
        Register a behaviour to be executed by the agent.

        :param behaviour: The behaviour function to register.
        """
        self._behaviour = behaviour
        self._logger.info("Behaviour registered: %s", behaviour)

    async def register_message_handler(self, message_type: Type, handler: Callable):
        """Register a message handler for a given message type."""
        self._message_handlers[message_type] = handler
        self._logger.debug("Message handler registered for type: %s", message_type)

    async def _handle_message(self, message: Any):
        """
        Handle incoming messages.

        :param message: The incoming message.
        """
        if "hello" in message:
            self._logger.info("Received hello message: %s", message)    

    async def generate_random_message(self, duration: int = 10):
        """Generate random 2-word messages for a specified duration."""
        start_time = asyncio.get_event_loop().time()
        end_time = start_time + duration

        while asyncio.get_event_loop().time() < end_time:  
            message = " ".join(random.sample(["hello", "sun", "world", "space", "moon", "crypto", "sky", "ocean", "universe", "human"], 2))
            await self._handle_message(message)
            await self.emit_message(message)    
            self._logger.debug("Generated message: %s", message)
            await asyncio.sleep(2)  # Sleep for 2 seconds between messages

    async def start_loop(self, duration: int = 10):
        """Start the agent loop."""
        self._task = asyncio.create_task(self.generate_random_message(duration))
        await self._task

    async def stop_loop(self):
        """Stop the agent loop."""
        if self._task:
            self._task.cancel()

    async def stop(self):
        """Stop the agent."""
        await self.stop_loop()
        await super().stop()
