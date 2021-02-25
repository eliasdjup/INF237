class Cheetah:
    def __init__(self, id, starttime, speed):
        self.id = id
        self.starttime = starttime
        self.speed = speed
    def __repr__(self):
        return "Cheetah(id:"+str(self.id)+",start:"+str(self.starttime)+",speed"+str(self.speed)+")"
    def __str__(self):
        return "Cheetah(id:"+str(self.id)+",start:"+str(self.starttime)+",speed"+str(self.speed)+")"
    

    def __eq__(self, other):
        return self.starttime == other.starttime
        
    def __ne__(self, other):
        return self.starttime  != other.starttime

    def __lt__(self, other):
        return self.starttime < other.starttime

    def __le__(self, other):
        return self.starttime <= other.starttime

    def __gt__(self, other):
        return self.starttime > other.starttime

    def __ge__(self, other):
        return self.starttime >= other.starttime

n = int(input())
seq=[]

for i in range(n):
    line = [float(x) for x in input().split()]

    c = Cheetah(i,line[0],line[1])
    seq.append(c)
seq.sort()

first=[]
last=[]


def pack_size(t):

    fst=seq[0]
    lst=seq[0]
    for c in seq:
        if c.starttime > t:
            continue
        else:
            pos = c.speed*t-(c.starttime*2)
            fstpos = fst.speed*t-(fst.starttime*2)
            print(fst.speed,t,fst.starttime)
            print('fstpos',fstpos)
            if pos > fstpos:
                fst = c
                continue
            lstpos = lst.speed*t-lst.starttime
            if pos < lstpos:
                lst = c

    print('t',t)
    print('fst',fst)
    print('lst',lst)

pack_size(3)




'''
Build a list of cheetahs running first (at any time)
during the race (“upper envelope”) and keep the times in
which they outrun each other, build a similar list for the last
cheetahs (“lower envelope”). Then, find the shortest
distance between the envelopes - the times at which the
distance must be considered is 0 and any time a cheetah is
outrun by another. This allows for O(N.log(N)) solution, see
the example on the next slides.


fremsteCheetah.speed >= backCheetah.speed

'''