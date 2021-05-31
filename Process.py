from typing import List
from collections import namedtuple

Segment = namedtuple('Segment', ['name', 'start_address', 'end_address'])


class Process:
    def __init__(self, index: int, segments: List[dict]):
        self.index = index
        self.segments = segments

    def get_segments(self):
        segments_list = []
        for segment in self.segments:
            segments_list.append(Segment(f"P{self.index}: " + segment['name'],
                                         segment['start_address'], segment['end_address']))

        return segments_list
