from Block import Block
from typing import List

import copy


class MemoryManager:
    def __init__(self, total_memory_size, holes):
        self.total_memory_size = total_memory_size
        self.holes = list(map(lambda hole: Block('Hole', hole[0], hole[1]), holes))
        self.old_processes = self._deduce_old_processes()
        self.new_processes = []
        self._update_holes()

    def allocate_best_fit(self, new_process) -> bool:
        # perform deep copy to not corrupt original holes
        holes_copy = copy.deepcopy(self.holes)

        for segment in new_process.segments:
            # remove holes that its size smaller than segment sizenew_processes
            filtered_holes = list(filter(lambda hole: hole.size >= segment.size, holes_copy))

            # if there no holes that can fit the segment, then we can't allocate the whole process
            if len(filtered_holes) == 0:
                return False

            # best hole is the smallest size
            best_hole = min(filtered_holes, key=lambda hole: hole.size)
            holes_copy.remove(best_hole)

            self._bind_address_to_segment(segment, best_hole, holes_copy)

        # allocation succeeded
        self.new_processes.append(new_process)
        self.holes = holes_copy
        return True

    def allocate_worst_fit(self, new_process) -> bool:
        # perform deep copy to not corrupt original holes
        holes_copy = copy.deepcopy(self.holes)

        for segment in new_process.segments:
            # worst hole is the largest whole
            worst_hole = max(holes_copy, key=lambda hole: hole.size)
            holes_copy.remove(worst_hole)

            # if the largest hole can't fit the segment then we can't allocate the process
            if worst_hole.size < segment.size:
                return False

            self._bind_address_to_segment(segment, worst_hole, holes_copy)

        # allocation succeeded
        self.new_processes.append(new_process)
        self.holes = holes_copy
        return True

    def allocate_first_fit(self, new_process) -> bool:
        # perform deep copy to not corrupt original holes
        holes_copy = copy.deepcopy(self.holes)

        for segment in new_process.segments:
            # remove holes that its size smaller than segment size
            filtered_holes = list(filter(lambda hole: hole.size >= segment.size, holes_copy))

            # if there no holes that can fit the segment, then we can't allocate the whole process
            if len(filtered_holes) == 0:
                return False

            # get first hole
            first_hole = min(filtered_holes, key=lambda hole: hole.start_address)
            holes_copy.remove(first_hole)

            self._bind_address_to_segment(segment, first_hole, holes_copy)

        # allocation succeeded
        self.new_processes.append(new_process)
        self.holes = holes_copy
        return True

    def get_memory_map(self) -> List[dict]:
        self.holes.sort(key=lambda hole: hole.start_address)
        for i, mem_hole in enumerate(self.holes):
            mem_hole.name = f"Hole{i}"

        all_segments = self._get_all_processes_segments()

        blocks = self.holes + self.old_processes + all_segments
        blocks.sort(key=lambda block: block.start_address)
        return list(map(lambda block: {
            'name': block.name,
            'start': block.start_address,
            'end': block.end_address
        }, blocks))

    def external_compaction(self):
        all_segments = self._get_all_processes_segments()

        blocks = all_segments + self.old_processes
        blocks.sort(key=lambda block: block.start_address)

        current_position = 0
        for mem_block in blocks:
            mem_block.start_address = current_position
            current_position = mem_block.end_address

        hole = Block('Hole', blocks[-1].end_address, self.total_memory_size - blocks[-1].end_address)
        self.holes = [hole]

    def get_new_processes(self):
        return list(map(lambda process: {
            'name': f"P{process.index}",
            'number of segments': len(process.segments),
        }, self.new_processes))

    def get_old_processes(self):
        return list(map(lambda process: {
            'name': process.name,
            'start address': process.start_address,
            'size': process.size
        }, self.old_processes))

    def deallocate(self, block_name):
        # try to find the block in all new processes
        for process in self.new_processes:
            if process.name == block_name:
                self.new_processes.remove(process)
                self._update_holes()
                return

        # then it must be in old processes
        process_found = list(filter(lambda block: block.name == block_name, self.old_processes))[0]
        self.old_processes.remove(process_found)
        self._update_holes()

    def _deduce_old_processes(self) -> List[Block]:
        # handle corner case when there are no holes
        if len(self.holes) == 0:
            return [Block('Old0', 0, self.total_memory_size)]

        old_processes = []
        index = 0
        current_position = 0

        # get old processes between every two consequent holes and between memory start address (0) and first hole
        self.holes.sort(key=lambda hole: hole.start_address)
        for mem_hole in self.holes:
            if mem_hole.start_address > current_position:
                old_processes.append(Block(f"Old{index}", current_position, mem_hole.start_address - current_position))
                index += 1
            current_position = mem_hole.end_address

        # get the old process between last hole and memory end address (total_memory size), if any
        last_hole = self.holes[-1]
        if last_hole.end_address < self.total_memory_size:
            old_processes.append(Block(f"Old{index}", last_hole.end_address,
                                       self.total_memory_size - last_hole.end_address))

        return old_processes

    def _get_all_processes_segments(self):
        segments = []
        for process in self.new_processes:
            segments += process.segments

        return segments

    @staticmethod
    def _bind_address_to_segment(segment, hole, holes):
        segment.start_address = hole.start_address
        new_hole_size = hole.end_address - segment.end_address
        if new_hole_size > 0:
            holes.append(Block('Hole', segment.end_address, new_hole_size))

    def _update_holes(self):
        all_processes = self._get_all_processes_segments() + self.old_processes
        all_processes.sort(key=lambda segment: segment.start_address)

        current_position = 0
        holes = []

        for process in all_processes:
            if process.start_address > current_position:
                holes.append(Block(f"Hole", current_position, process.start_address - current_position))
            current_position = process.end_address

        last_process = all_processes[-1]
        if last_process.end_address < self.total_memory_size:
            holes.append(Block(f"Hole", last_process.end_address, self.total_memory_size - last_process.end_address))

        self.holes = holes
