import re
import sys

#usage message
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("Add Argument", help="Input a string with cardinals stats after your arguement for python file")
args = parser.parse_args()


filename =sys.argv[1]


#create set of team which will hold players names
teamName = set()
teamObj = set()

#helper method to only add to player when there are no duplicates
def addStat(name1,bat1,hit1):
	if name1 not in teamName:
		teamName.add(name1) #add players name to set so its easy to check
		name1=Player(name1,bat1,hit1)
		teamObj.add(name1) #add next player to set with players
	else:
		for key in teamObj:
			if key.name==name1:
				key.update(bat1,hit1)
			
#deline player object
class Player:
	# constructor:
	def __init__(self, name,bats,hits):
		self.name = name
		self.bats= float(bats)
		self.hits= float(hits)
		if self.bats>1:
			self.batAvg=self.hits/self.bats
		else:
			self.batAvg=0;
	def update(self,Ubats,Uhits):
		self.bats= self.bats+float(Ubats)
		self.hits=self.hits+float(Uhits)
		if self.bats>1:
			self.batAvg=self.hits/self.bats
		else:
			self.batAvg=0;
	def toString(self):
		self.batAvg=round(self.batAvg, 3)
		print("{}:{:.3f}".format(self.name,self.batAvg))


#still need to fix bringing in the correct 
with open(filename) as f:
	for line in f:
		regex = re.compile(r"(\w+\s\w+) batted (\d) times with (\d) hits and (\d) runs")
		matches=re.search(regex, line)
		if matches:
			addStat(matches.group(1),matches.group(2),matches.group(3))

#newTeam = sorted(teamObj.batAvg)

teamAvgs=[]
for key in teamObj:
	addAvg=key.batAvg
	teamAvgs.append(addAvg)

teamAvgs.sort()
#print the players
for x in teamAvgs[::-1]:
	for key in teamObj:
		batterAvg=key.batAvg
		if(batterAvg==x):
			key.toString()
