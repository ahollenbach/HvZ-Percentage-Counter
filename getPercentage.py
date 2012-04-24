import urllib2,sys,time
from datetime import datetime

def getNums():
        address = "https://hvz.rit.edu/game/players/"
        html = urllib2.urlopen(address)
        #line before zombie/human stats
        catchLine = 'Current Game Statistics'
        count = 0
        done = False
        while not done:
            cur = html.readline()
            if count>0:
                cur = cur.split()
                curS = cur[3]
                if count==1:
                        zP = curS[3:8]
                        count+=1
                else:
                        hP = curS[3:8]
                        count=0
            if cur[:4] == '<h3>':
                count=1
            if cur == "</html>":
                done = True

        with open("percents.txt", "a") as myFile:
            s = str(datetime.now())+","+str(hP)+","+str(zP)
            myFile.write(s+'\n')
        print(s)
        myFile.close()
        html.close()
def main():
        while True:
                getNums()
                time.sleep(3600)

main()
