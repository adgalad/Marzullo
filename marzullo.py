from operator import itemgetter

class parking:
    def __init__(self, capacity):
        self.occupation = []
        self.capacity = capacity

    def addReservation(self,startTime,endTime):
        startTimeVal=int(startTime)
        endTimeVal=int(endTime)
        if startTimeVal > endTimeVal:
            raise ValueError("startTime must be earlier than endTime.")
        startTuple = (startTimeVal, 1)
        endTuple = (endTimeVal, -1)
        if self.fits(startTuple, endTuple):
            self.occupation += [startTuple, endTuple]
            return True
        return False

    def fits(self, startTuple, endTuple):
        count = 0
        for r in sorted((self.occupation + [startTuple, endTuple]),key=itemgetter(0,1)):
            count+=r[1]
            if(count>self.capacity):
                return False
        return True
