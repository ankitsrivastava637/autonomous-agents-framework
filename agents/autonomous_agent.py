import abc
import logging
from typing import Any, Callable, Type

class AutonomousAgent(abc.ABC):
    def __init__(self, inbox: "Inbox", outbox: "Outbox"):
        """
        Initialize the AutonomousAgent.

        :param inbox: The inbox for receiving messages.
        :param outbox: The outbox for sending messages.
        """
        self._inbox = inbox
        self._outbox = outbox
        self._behaviour: Callable[[], Any] = None
        self._message_handlers = {}
        self._logger = logging.getLogger(__name__)

    @abc.abstractmethod
    async def consume_messages(self):
        """Continuously consume messages from the inbox."""
        pass

    @abc.abstractmethod
    async def emit_message(self, message: Any):
        """Emit a message to the outbox."""
        pass

    @abc.abstractmethod
    async def register_message_handler(self, message_type: Type, handler: Callable):
        """Register a message handler for a given message type."""
        pass

    @abc.abstractmethod
    async def handle_message(self, message: Any):
        """
        Handle an incoming message based on its type.

        :param message: The incoming message.
        """
        pass

    async def start(self):
        """Start the agent."""
        self._logger.info("Agent started.")


    async def stop(self):
        """Stop the agent."""
        self._logger.info("Agent stopped.")

    @property
    def inbox(self) -> "Inbox":
        """Get the inbox of the agent."""
        return self._inbox

    @property
    def outbox(self) -> "Outbox":
        """Get the outbox of the agent."""
        return self._outbox
