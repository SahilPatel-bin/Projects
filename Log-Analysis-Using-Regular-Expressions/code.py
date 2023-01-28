import re
import operator
error={}
per_user={}
with open("football.csv") as file:
  lines = file.readlines()
  for line in lines:
    pattern = r": (\w*) ([\w\s']*)[\[[#\d]*\]?[ ]?\(([\w.]*)\)"
    result = re.search(pattern,line.strip())
    if result[1]=="ERROR":
      error[result[2]]= error.get(result[2],0)+1
    if result[3] not in per_user.keys():
      per_user[result[3]]= {}
      per_user[result[3]]["INFO"]=0
      per_user[result[3]]["ERROR"]=0
    if result[1]=="INFO":
      per_user[result[3]]["INFO"]+=1
    elif result[1]=="ERROR":
      per_user[result[3]]["ERROR"]+=1
errors=dict(sorted(error.items(),key=operator.itemgetter(1),reverse=True))
report = dict(sorted(per_user.items()))

with open("errors.csv",'w') as file:
  file.write("Error,Count\n")
  for i in errors:
    file.write(f"{str(i).strip()},{errors[i]}\n")

with open("user_statistics.csv",'w') as file :
  file.write("Username,INFO,ERROR\n")
  for i,j in report.items():
    file.write(f"{str(i).strip()},{j['INFO']},{j['ERROR']}\n")
  
