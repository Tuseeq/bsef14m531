proc=[]
time=[]
turn=[]
ttime=0
sum1=0
q=input('enter number of process: ')
from random import randint
for i in range(q):
	proc.append(i)
	turn.append(0)
	time.append(0)
	proc[i]=i
	s=input('burst time for p'+repr(proc[i]+1)+': ')
	time[i]=s
print('start')
for i in range(q):
	sum1=sum1+time[i]	
while(sum1>0):
	mini=0
	while(time[mini]==0 and mini<q):
		mini=mini+1
	j=0
	while(j<q):
		if time[j]<>0:
			if time[j]<time[mini]:
				mini=j
		j=j+1
	k=3
	while(k>0 and time[mini]>0):
		s='process ' + repr(proc[mini]+1) + ' is running'
		print(s)
		time[mini]=time[mini]-1
		ttime=ttime+1
		k=k-1
	turn[mini]=ttime
	sum1=0
	for i in range(q):
		sum1=sum1+time[i]
for i in range(q):
	s='turn around time of p'+repr(proc[i]+1)+' ='+repr(turn[i])
	print(s)	
s='all done!'
print(s)
