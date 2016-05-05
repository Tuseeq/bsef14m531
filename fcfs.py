proc=[]
btime=[]
turntime=[]
ttime=0
from random import randint
for i in range(5):
	proc.append(0)
	btime.append(0)
	turntime.append(0)
	proc[i]=i+1
	btime[i]=randint(i,i*10+10)
for i in range(5):
	while(btime[i]>0):
		s='process ' + repr(proc[i]) + ' is running'
		print(s)
		btime[i]=btime[i]-1
		ttime=ttime+1
	turntime[i]=ttime
	
for i in range(5):
	s='turn around time for process '+ repr(proc[i])+' is '+ repr(turntime[i])
	print(s)	
