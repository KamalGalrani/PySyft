# stdlib
from enum import Enum
from typing import Optional

# relative
from ...common.serde.serializable import serializable
from ...common.uid import UID
from .credentials import SyftSigningKey


@serializable(recursive_serde=True)
class NodeType(Enum):
    DOMAIN = "domain"
    NETWORK = "network"
    ENCLAVE = "enclave"


class NewNode:
    id: Optional[UID]
    name: Optional[str]
    signing_key: Optional[SyftSigningKey]
    node_type: Optional[NodeType]
