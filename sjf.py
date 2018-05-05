
print("Enter the number of processes: ")
n=int(input())
burstTime = []
waitTime=[]
turnAT=[]
avgWT=0
avgTAT=0
processes=[]
for i in range(0,n):
	processes.insert(i,i+1)
print("Enter the burst time of processes: \n")
burstTime=list(map(int, raw_input().split()))
for i in range(0,len(burstTime)-1):
	for j in range(0,len(burstTime)-i-1):
		if(burstTime[j]>burstTime[j+1]):
			temp=burstTime[j]
			burstTime[j]=burstTime[j+1]
			burstTime[j+1]=temp
			temp=processes[j]
			processes[j]=processes[j+1]
			processes[j+1]=temp
waitTime.insert(0,0)
turnAT.insert(0,burstTime[0])
for i in range(1,len(burstTime)):
	waitTime.insert(i,waitTime[i-1]+burstTime[i-1])
	turnAT.insert(i,waitTime[i]+burstTime[i])
	avgWT+=waitTime[i]
	avgTAT+=turnAT[i]
avgWT=float(avgWT)/n
avgTAT=float(avgTAT)/n
print("\n")
print("Process\t	Burst Time\t	Waiting Time\t		TurnAround Time\t")
for i in range(0,n):
	print(str(processes[i])+"\t\t"+str(burstTime[i])+"\t\t"+str(waitTime[i])+"\t\t"+str(turnAT[i]))
	print("\n")
	print("Average waiting time: "+ str(avgWT))
print("Average TurnAround time: "+ str(avgTAT))