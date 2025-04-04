"""This module contains the mapping for the rewards that the agent can receive."""
from dataclasses import dataclass


@dataclass
class RewardsMapping:
    """Mapping for the rewards that the agent can receive.

    The mapping can be extended to include additional rewards.
    """
    max_reward: float = 25
    long_life_bonus_rate: float = 0.00001
    game_over: float = -100
    invalid_action: float = -0.1

    clear_line: float = 1
    gap: float = -0.5
    bumpiness: float = -0.3
    height: float = -0.7
    
    
