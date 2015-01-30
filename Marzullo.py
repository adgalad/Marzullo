class parking:
    def __init__(self, capacity):
        self.lista = []
        self.capacity = capacity

    def fits(self, startTime, endTime):
        if self.capacity > 0:
            return True
        return False