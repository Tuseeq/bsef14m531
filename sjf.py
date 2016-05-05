proc=[]
time=[]
turntime=[]
ttime=0
q=input('enter number of processes: ')
for i in range(q):
	proc.append(i)
	time.append(1)
	turntime.append(0)
	proc[i]=i
	s='enter burst time for process'+repr(proc[i]+1)+' '
	t=input(s)
	time[i]=t
print('start')
for i in range(q):
	mini=0
	while(time[mini]==0 and mini<5):
		mini=mini+1
	j=1
	while(j<q):
		if time[j]<>0:
			if time[j]<time[mini]:
				mini=j
		j=j+1
	while(time[mini]>0):
		s='process ' + repr(proc[mini]+1) + ' is running'
		print(s)
		time[mini]=time[mini]-1	
		ttime=ttime+1
	turntime[i]=ttime
for i in range(q):
	s='turn around time for p'+repr(proc[i]+1)+' = '+repr(turntime[i])
	print(s)
s='all done!'
print(s)
