#NOTE input your Maltaisn output file in the line below
with open ('your_file.txt','r') as f1:
    lines = f1.readlines()

with open ('calc-converter-unrefined.txt','w') as f2:
    f2.write('Param\n')
    for i in range (1,7):
        f2.write('""->X__'+str(i)+'\n')
        f2.write('""->Y__'+str(i)+'\n')
    f2.write('ClrDraw\n')
    f2.write('StorePic 1\n')
    count = 0
    for line in lines:
        count +=1
        line = line.rstrip()
        line = line[1:-1]
        coords = line.split(',')
        f2.write('"'+str(coords[0])+'"->X__'+str(count)+'\n')
        f2.write('"'+str(coords[1])[1:]+'"->Y__'+str(count)+'\n')
        if (count == 6):
            f2.write('RecallPic 1\nStorePic1\n')
            count = 0

with open ('calc-converter-unrefined.txt','r') as f3:
    unrefined = f3.readlines()

with open ('calc-converter-final.txt','w') as f4:
    for line in unrefined:
        line = line.replace('t','T')
        line = line.replace('->','→')
        line = line.replace('__1','₁')
        line = line.replace('__2','₂')
        line = line.replace('__3','₃')
        line = line.replace('__4','₄')
        line = line.replace('__5','₅')
        line = line.replace('__6','₆')
        if (line[1] == '-'):
            line = line.replace('-','­',1)
        line = line.replace(' ','')
        line = line.replace('STore','Store')
        line = line.replace('StorePic1','StorePic 1')
        line = line.replace('RecallPic1','RecallPic 1')
        f4.write(line)
    f4.write('RecallPic 1\nStorePic 1')
