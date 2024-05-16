import asyncio
import logging
from typing import Any, Callable, Type

class Inbox:
    def __init__(self):
        """Initialize the Inbox."""
        self._queue = asyncio.Queue()
        self._logger = logging.getLogger(__name__)
        self._handlers = {}

    async def put_message(self, message: Any):
        """Put a message into the inbox."""
        await self._queue.put(message)
        self._logger.debug("Message put into inbox: %s", message)

    async def get_message(self) -> Any:
        """Get a message from the inbox."""
        message = await self._queue.get()
        self._logger.debug("Message retrieved from inbox: %s", message)
        return message

    async def handle_message(self, message: Any):
        """Handle incoming message."""
        message_type = type(message)
        handler = self._handlers.get(message_type)
        if handler:
            await handler(message)

class Outbox:
    def __init__(self):
        """Initialize the Outbox."""
        self._queue = asyncio.Queue()
        self._logger = logging.getLogger(__name__)

    async def put_message(self, message: Any):
        """Put a message into the outbox."""
        await self._queue.put(message)
        self._logger.debug("Message put into outbox: %s", message)

    async def get_message(self) -> Any:
        """Get a message from the outbox."""
        message = await self._queue.get()
        self._logger.debug("Message retrieved from outbox: %s", message)
        return message