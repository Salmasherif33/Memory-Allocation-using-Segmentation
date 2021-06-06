from typing import List
from Block import Block


class Process:
    def __init__(self, index: int, segments: List[dict]):
        self.index = index
        self.segments = list(map(lambda segment:
                                 Block(f"P{self.index}: " + segment['name'], 0, segment['size']), segments))

    def remove_segment(self, segment_name) -> bool:
        segments_found = list(filter(lambda block: block.name == segment_name, self.segments))
        # if segment not found return false
        if len(segments_found) == 0:
            return False

        self.segments.remove(segments_found[0])
        return True

