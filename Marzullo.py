class parking:
    def __init__(self, capacity):
        self.occupation = []
        self.capacity = capacity

    def addReservation(self,startTime,endTime):
        startTimeVal=int(startTime)
        endTimeVal=int(endTime)
        if(startTimeVal>endTimeVal):
            raise ValueError("startTime must be earlier than endTime.")
        tupla1 = (startTimeVal,1)
        tupla2 = (endTimeVal,-1)
        self.occupation+=[tupla1,tupla2]

    def fits(self):
        count = 0
        for r in sorted(self.occupation):
            count += r[1]
            if count > self.capacity:
                return False
        return True
