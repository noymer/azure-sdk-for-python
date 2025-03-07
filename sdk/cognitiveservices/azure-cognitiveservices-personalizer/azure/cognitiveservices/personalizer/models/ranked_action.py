# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class RankedAction(Model):
    """A ranked action with its resulting probability.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Id of the action
    :vartype id: str
    :ivar probability: Probability of the action
    :vartype probability: float
    """

    _validation = {
        "id": {"readonly": True, "max_length": 256},
        "probability": {"readonly": True, "maximum": 1, "minimum": 0},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "probability": {"key": "probability", "type": "float"},
    }

    def __init__(self, **kwargs):
        super(RankedAction, self).__init__(**kwargs)
        self.id = None
        self.probability = None
