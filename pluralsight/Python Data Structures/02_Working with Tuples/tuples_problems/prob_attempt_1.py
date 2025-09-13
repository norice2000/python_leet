from typing import List, Tuple, Dict, Optional, Set
from dataclasses import dataclass
import json

def find_duplicate_configurations(service_configs: List[Tuple[str, int, str]]) -> List[Tuple[str, int, str]]:
    """
    CHALLENGE 1: Find Duplicate Service Configurations
    
    Given a list of service configuration tuples (service_name, port, protocol),
    find which configurations appear more than once (potential conflicts).
    
    Args:
        service_configs: List of tuples (service_name, port, protocol)
    
    Returns:
        List of duplicate configuration tuples
    
    Example:
        configs = [
            ("api-gateway", 80, "http"),
            ("web-server", 80, "http"),    # Same port/protocol - potential conflict!
            ("database", 5432, "tcp"),
            ("api-gateway", 80, "http")    # Exact duplicate
        ]
        Result: [("api-gateway", 80, "http")]
    
    Real-world: Prevents port conflicts in container orchestration
    """
    # TODO: Implement this function
    # instantiate some sets
    # seen_config = []
    # duplicate = []
    # for loop iterate through service_config
    # if config in seen_config
    # append duplicate
    # else
    # append seen_config

    seen_config = set()
    duplicate = set()

    for config in service_configs:
        if config in seen_config:
            # duplicate.append(config)
            duplicate.add(config)
        else:
            # seen_config.append(config)
            seen_config.add(config)
    return list(duplicate)

configs = [
    ("api-gateway", 80, "http"),
    ("web-server", 80, "http"),    # Same port/protocol - potential conflict!
    ("database", 5432, "tcp"),
    ("api-gateway", 80, "http")    # Exact duplicate
]
print(find_duplicate_configurations(configs))