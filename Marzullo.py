class parking:
    def __init__(self, capacity):
        self.lista = []
        self.capacity = capacity

    def fits(self, startTime, endTime):
        return self.capacity > 0