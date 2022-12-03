

def saveFileTemp(ls):
 
   arquivo=open('newfile','w')
   for i in range(0,len(ls)):
      arquivo.write(ls[i]+'\n') 
   arquivo.close()
    
# How to read a file
def readFileTemp():
    import os
    ls=[]
    sTemp=''
    arquivo=open('newfile','r')
    for line in arquivo.readlines():
         sTemp=line[:-1]
         ls.append(sTemp)
    
    arquivo.close()
    
    os.remove('newfile')
    return(ls)
ls=['marco','sergio','barozzi']
saveFileTemp(ls)
readFileTemp()