from typing import List
from Block import Block


class Process:
    def __init__(self, index: int, segments: List[dict]):
        self.index = index
        self.segments = list(map(lambda segment:
                                 Block(f"P{self.index}: " + segment['name'], 0, segment['size']), segments))
        self.name = f'P{index}'

    def __eq__(self, other):
        return self.index == other.index
