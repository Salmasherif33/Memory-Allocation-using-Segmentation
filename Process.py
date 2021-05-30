from typing import List


class Process:
    def __init__(self, index: int, segments: List[dict]):
        self.index = index
        self.segments = segments
