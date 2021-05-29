from Process import Process


class MemoryManager:
    def __init__(self, total_memory_size, holes):
        pass

    def allocate_best_fit(self, new_process: Process) -> bool:
        return True

    def allocate_worst_fit(self, new_process: Process) -> bool:
        return True

    def allocate_first_fit(self, new_process: Process) -> bool:
        return True

    def get_memory_map(self) -> list:
        return []

    def external_compaction(self):
        pass
