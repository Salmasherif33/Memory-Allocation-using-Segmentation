from Process import Process
from Hole import Hole
from Block import Block
from collections import namedtuple
from typing import List

OldProcess = namedtuple('OldProcess', ['name', 'start_address', 'end_address'])


class MemoryManager:
    def __init__(self, total_memory_size, holes):
        self.total_memory_size = total_memory_size
        self.holes = list(map(lambda hole: Hole('Hole', hole[0], hole[0] + hole[1]), holes))
        self.old_processes = self._deduce_old_processes()
        self.new_processes = []
        self.blocks = []
        self.is_compacted = False

    def allocate_best_fit(self, new_process: Process) -> bool:
        return True

    def allocate_worst_fit(self, new_process: Process) -> bool:
        return True

    def allocate_first_fit(self, new_process: Process) -> bool:
        return True

    def get_memory_map(self) -> List[dict]:
        if not self.is_compacted:
            for i, hole in enumerate(self.holes):
                hole.name = f"Hole{i}"
            segments = []
            for my_process in self.new_processes:
                segments += my_process.get_segments()
            self.blocks = self.holes + self.old_processes + segments
        self.blocks.sort(key=lambda block: block.start_address)
        return list(map(lambda block: {
            'name': block.name,
            'start': block.start_address,
            'end': block.end_address
        }, self.blocks))

    def external_compaction(self):
        self.blocks = []
        segments = []
        for my_process in self.new_processes:
            segments += my_process.get_segments()
        for segment in segments:
            temp_block = Block(segment.name, segment.start_address, segment.end_address)
            self.blocks.append(temp_block)
        for my_process in self.old_processes:
            temp_block = Block(my_process.name, my_process.start_address, my_process.end_address)
            self.blocks.append(temp_block)

        self.blocks.sort(key=lambda block: block.start_address)

        for i, block in enumerate(self.blocks):
            if i > 0 and i + 1 < len(self.blocks):
                temp = self.blocks[i+1].start_address
                self.blocks[i+1].start_address = block.end_address
                self.blocks[i+1].end_address = self.blocks[i+1].start_address + (self.blocks[i+1].end_address - temp)
        hole = Hole('Hole0', self.blocks[len(self.blocks)-1].end_address, self.total_memory_size)
        self.holes = [hole]
        self.blocks += self.holes
        self.is_compacted = True
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


memory = MemoryManager(500, [[20, 40], [80, 80], [200, 200], [450, 30]])

for process in memory.old_processes:
    print(f"{process.start_address} => {process.end_address}")

process = Process(1, [{
        'name': 'code',
        'size': 20,
        'start_address': 20,
        'end_address': 40
    },
     {
         'name': 'Data',
         'size': 80,
         'start_address': 80,
         'end_address': 160
     }])
process2 = Process(2, [{
        'name': 'code',
        'size': 20,
        'start_address': 200,
        'end_address': 220
    },
     {
         'name': 'Data',
         'size': 80,
         'start_address': 240,
         'end_address': 320
     }])

memory.new_processes.append(process)
memory.new_processes.append(process2)

memory.external_compaction()

process3 = Process(3, [{
        'name': 'code',
        'size': 10,
        'start_address': 450,
        'end_address': 460
    },
     {
         'name': 'Data',
         'size': 10,
         'start_address': 470,
         'end_address': 480
     }])

memory.new_processes.append(process3)
memory.external_compaction()
my_list = memory.get_memory_map()

print(my_list)
