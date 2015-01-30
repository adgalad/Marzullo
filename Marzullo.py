class parking:
    def __init__(self, capacity):
        self.occupation = []
        self.capacity = capacity
    def addReservation(self,startTime,endTime):
        startTimeVal=int(startTime)
        endTimeVal=int(endTime)
        if(startTimeVal>endTimeVal):
            raise ValueError("Hora de inicio no puede ser mayor a hora final.")
        tupla1 = (startTimeVal,1)
        tupla2 = (endTimeVal,-1)
        self.occupation+=[tupla1,tupla2]
    def fits(self):
        if self.capacity >= len(self.occupation)/2:
            return True
        return False