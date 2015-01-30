from operator import itemgetter

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
        if (self.fits(self.occupation+[tupla1,tupla2])):
            self.occupation+=[tupla1,tupla2]
            return True
        return False

    def fits(self,new):
        temp = sorted(new,key=itemgetter(0,1))#ordena las tuplas por su hora, que es el elemento 0 de las tuplas y luego por la cantidad que es -1 o 1
        count = 0
        for r in temp:
            count+=r[1]
            if(count>self.capacity):
                return False
        return True
