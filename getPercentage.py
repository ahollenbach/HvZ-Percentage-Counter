import urllib2,sys

#line containing player name. next line contains whether human or zombie.
catchLine = '<td><a href="/users/profile.php?uid'
address = "https://hvz.rit.edu/game/players/"

html = urllib2.urlopen(address)

toggle = False
humans = 0
zombies = 0
done = False

while not done:
    cur = html.readline()
    if toggle:
        if cur[4:10] == "Humans":
            humans += 1
        elif cur[4:11] == "Zombies":
            zombies += 1
        #else, do nothing (mod or admin)
    if catchLine == cur[:35]:
        toggle = True

    if cur == "</html>":
        done = True

print "Humans:",humans
print "Zombies:",zombies
