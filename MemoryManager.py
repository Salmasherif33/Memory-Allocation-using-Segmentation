from Process import Process
from Hole import Hole
from collections import namedtuple
from typing import List

OldProcess = namedtuple('OldProcess', ['name', 'start_address', 'end_address'])


class MemoryManager:
    def __init__(self, total_memory_size, holes):
        self.total_memory_size = total_memory_size
        self.holes = list(map(lambda hole: Hole('Hole', hole[0], hole[0] + hole[1]), holes))
        self.old_processes = self._deduce_old_processes()
        self.new_processes = []

    def allocate_best_fit(self, new_process: Process) -> bool:
        return True

    def allocate_worst_fit(self, new_process: Process) -> bool:
        return True

    def allocate_first_fit(self, new_process: Process) -> bool:
        return True

    def get_memory_map(self) -> List[dict]:
        for i, hole in enumerate(self.holes):
            hole.name = f"Hole{i}"
        segments = []
        for process in self.new_processes:
            segments += process.get_segments()

        blocks = self.holes + self.old_processes + segments
        blocks.sort(key=lambda block: block.start_address)

        result = list(map(lambda block: {
            'name': block.name,
            'start': block.start_address,
            'end': block.end_address
        }, blocks))

        return result

    def external_compaction(self):
        pass

    def _deduce_old_processes(self) -> List[OldProcess]:
        # handle corner case when there are no holes
        if len(self.holes) == 0:
            return [OldProcess('Old0', 0, self.total_memory_size)]

        old_processes = []
        index = 0
        current_position = 0

        # get old processes between every two consequent holes and between memory start address (0) and first hole
        for hole in sorted(self.holes, key=lambda hole: hole.start_address):
            if hole.start_address > current_position:
                old_processes.append(OldProcess(f"Old{index}", current_position, hole.start_address))
                index += 1
            current_position = hole.end_address

        # get the old process between last hole and memory end address (total_memory size), if any
        last_hole = self.holes[-1]
        if last_hole.end_address < self.total_memory_size:
            old_processes.append(OldProcess(f"Old{index}", last_hole.end_address, self.total_memory_size))

        return old_processes
