"""
Configuration Module

Loads and validates environment variables required for the
Crypto Market Intelligence MCP project.
"""

import os
from dotenv import load_dotenv


load_dotenv()


DATABRICKS_SERVER_HOSTNAME = os.getenv("DATABRICKS_SERVER_HOSTNAME")
DATABRICKS_HTTP_PATH = os.getenv("DATABRICKS_HTTP_PATH")
DATABRICKS_TOKEN = os.getenv("DATABRICKS_TOKEN")


def validate_config() -> None:
    """
    Validate that all required environment variables exist.
    """

    missing_variables = []

    if not DATABRICKS_SERVER_HOSTNAME:
        missing_variables.append("DATABRICKS_SERVER_HOSTNAME")

    if not DATABRICKS_HTTP_PATH:
        missing_variables.append("DATABRICKS_HTTP_PATH")

    if not DATABRICKS_TOKEN:
        missing_variables.append("DATABRICKS_TOKEN")

    if missing_variables:
        raise EnvironmentError(
            "Missing required environment variables: "
            + ", ".join(missing_variables)
        )