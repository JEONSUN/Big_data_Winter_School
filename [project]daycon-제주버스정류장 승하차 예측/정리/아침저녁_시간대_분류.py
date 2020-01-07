import csv
 
trans = open('trans190530.csv', 'r')
mfw = open('morning190530.csv', 'w',newline='')
efw = open('evening190530.csv', 'w', newline='')

#6~10 등교 # 16~20 시 하교

mwr = csv.writer(mfw)
ewr = csv.writer(efw)

rdrtrans = csv.reader(trans)

#20190530070604

#070604%1000000
data =trans.readline()
header = data.split(",")
mwr.writerow(header)
ewr.writerow(header)
for linetrans in rdrtrans:
   time = int(linetrans[33].replace('/',''))
   if time >70000 and time <100000 : 
             mwr.writerow(linetrans)    
   elif time >160000 and time < 200000 : 
             ewr.writerow(linetrans)    

trans.close()
mfw.close()
efw.close()
