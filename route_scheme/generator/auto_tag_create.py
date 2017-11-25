from tags.models import Tag
f = open("tags.txt")
line = f.readline()
while line:  
    print line
    line = f.readline()

f.close()  
