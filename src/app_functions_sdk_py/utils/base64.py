# Copyright (C) 2024-2025 IOTech Ltd
# SPDX-License-Identifier: Apache-2.0

"""
This module provides utility functions for handling base64 encoding.
"""

import base64


def is_base64_encoded(data: bytes) -> bool:
    """ is_base64_encoded checks if the input data is base64 encoded """
    # to check if incoming bytes is base64 encoded or not, we can decode, then re-encode. If the
    # re-encoded string is equal to the encoded string, then it is base64 encoded.
    try:
        return base64.b64encode(base64.b64decode(data)) == data
    except Exception:  # pylint: disable=broad-except
        # for cases where exception raised, we can assume it is not base64 encoded so return False
        return False
