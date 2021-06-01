class Hole:
    def __init__(self, name: str, start_address: int, end_address: int):
        self.name = name
        self.start_address = start_address
        self.end_address = end_address
    def str(self):
        return f"(name: {self.name}, start address: {self.start_address}, end address: {self.end_address})"
