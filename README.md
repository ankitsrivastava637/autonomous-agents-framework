
# Autonomous Agents Framework
Welcome to the Autonomous Agents Framework! This Python project provides a flexible and scalable framework for implementing autonomous agents that communicate asynchronously.

## Overview
Autonomous agents are entities capable of interacting with their environment through asynchronous message passing. They exhibit both reactivity, responding to incoming messages, and proactivity, generating messages based on internal state or local time. This framework aims to abstract away the complexities of asynchronous communication, allowing developers to focus on implementing agent behaviors.

## Features
Asynchronous Communication: Agents communicate asynchronously via message passing.
Reactivity and Proactivity: Agents exhibit reactivity by handling incoming messages and proactivity by generating messages based on internal logic.
Message Handlers: Support for registering message handlers to react to specific message types.
Behaviors: Support for registering proactive behaviors that generate messages based on internal state or local time.


## Installation
To use the Autonomous Agents Framework, follow these steps:

## Clone the repository:

```bash
git clone https://github.com/ankitsrivastava637/autonomous-agents-framework.git
cd autonomous-agents-framework
```

## Set up a virtual environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate  # Activate virtual environment
venv\Scripts\activate   # For Windows : Activate virtual environment
pip install -r requirements.txt
```

## Usage
## To create and run autonomous agents using this framework, follow these steps:

- Define your agent class by subclassing AutonomousAgent.
- Implement message handlers to react to incoming messages.
- Implement behaviors to generate messages proactively.
- Instantiate your agent and start it by running the main.py file


## Testing
The project includes unit tests and integration tests to ensure the correctness of the framework. During unit test, integration test will be skipped automatically. 
To run the tests, use the following command:

```bash
pytest
```

