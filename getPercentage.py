##Andrew Hollenbach <anh7216@rit.edu>
import urllib2,sys,time
from datetime import datetime

def getNums():
        address = "https://hvz.rit.edu/game/players/"
        html = urllib2.urlopen(address)
        count = 0
        done = False
        while not done:
            cur = html.readline()
            #If on a target line
            if count>0:
                cur = cur.split()
                curS = cur[3]
                #If first line after catchLine,
                if count==1:
                        #parse the zombie percentage
                        zP = curS[3:8]
                        count+=1
                else:
                        #parse the human percentage
                        hP = curS[3:8]
                        count=0
            #only line containing <h3> immediately precedes the statistics
            if cur[:4] == '<h3>':
                count=1
            #if end of document, stop
            if cur == "</html>":
                done = True
        #append to file
        with open("percents.txt", "a") as myFile:
            s = str(datetime.now())+","+str(hP)+","+str(zP)
            myFile.write(s+'\n')
        #echo to terminal
        print(s)
        myFile.close()
        html.close()
def main():
        #calls every 1 hour
        while True:
                getNums()
                time.sleep(3600)

main()
