# Copyright (C) 2024-2025 IOTech Ltd
# SPDX-License-Identifier: Apache-2.0

""""
This module provides utility functions for handling environment variables.
"""

import os

from app_functions_sdk_py.contracts.clients.logger import Logger


def get_env_var_as_bool(logger: Logger, var_name: str, default_value: bool) -> (bool, bool):
    """
    Helper function to get the value of an environment variable as a boolean.
    If the environment variable is not set or contains an invalid value, the default value is
    returned.
    """
    env_value = os.environ.get(var_name)
    if env_value is not None:
        if env_value.lower() == "true":
            return True, True
        if env_value.lower() == "false":
            return False, True
        logger.warn(f"Invalid value for environment variable {var_name}: {env_value}. Using "
                       f"default value {default_value}")
    return default_value, False
