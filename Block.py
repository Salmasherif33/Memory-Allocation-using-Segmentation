class Block:
    def __init__(self, name: str, start_address: int, size: int):
        self.name = name
        self.start_address = start_address
        self.size = size

    def __str__(self):
        return f"(name: {self.name}, start address: {self.start_address}, end address: {self.end_address})"

    def __repr__(self):
        return f"(name: {self.name}, start address: {self.start_address}, end address: {self.end_address})"

    def __eq__(self, other):
        return (self.start_address == other.start_address) and (self.size == other.size)

    @property
    def end_address(self):
        return self.start_address + self.size
