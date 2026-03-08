# fusion.py
"""Sensor fusion utilities combining multiple inputs."""

from typing import Dict, Any


def fuse_sensors(*sources: Dict[str, Any]) -> Dict[str, Any]:
    """Simple averaging fusion for numeric values."""
    fused = {}
    for src in sources:
        for k, v in src.items():
            if isinstance(v, (int, float)):
                fused.setdefault(k, []).append(v)
    return {k: sum(vals) / len(vals) for k, vals in fused.items()}
