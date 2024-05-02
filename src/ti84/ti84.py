"""

    Author: Daniel Markusson

"""
import math
from typing import Union


class TI84:
    """
        The main calculator class.
    """
    e: float = math.e
    pi: float = math.pi

    def __init__(self):
        pass

    # General math
    def sqrt(self, a: Union[int, float]):
        """_summary_

        Args:
            a (Union[int, float]): _description_

        Returns:
            _type_: _description_
        """
        return math.sqrt(a)
