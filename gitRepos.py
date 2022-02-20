
import os



###
# get all the github links from the repos folder
# create a script to clone all the repos
# 
# 
#   


def getRepoUrl(configFile):
        
    # file1 = '/home/adwait/repos/bugbug/.git/config'
    try:
        with open(configFile, 'r') as f:
            data = f.read()

        data = data.split('\n')

        l=[]
        fl=False
        url=''
        for i in range(len(data)):
            if fl:
                lin = data[i].strip()
                lin = lin.split(' ')
                l.append(url+' '+ lin[2])
                fl = False
                
            if data[i][:7] == '[remote':
                fl=True
                url = data[i].split('"')[1]
    except FileNotFoundError:
        l = ['File not Found']
    
    return l

repos = [ f.path for f in os.scandir('/home/adwait/myFolder') if f.is_dir() ]

file2 = open('/home/adwait/Desktop/gitReposMyFolder.txt', 'a')

for repo in repos:

    file1= repo+'/.git/config'
    l=getRepoUrl(file1)

    folder = repo.split('/')[-1]
    file2.write('#' + folder+'\n')
    if not l[0] == 'File not Found': 
        file2.write('cd repos\n')
        file2.write('mkdir '+folder+'\n')
        file2.write('cd '+folder+'\n')
        file2.write('git init\n')
        for s in l:
            file2.write('git remote add ' + s + '\n' )         
            file2.write('git pull '+s.split(' ')[0] +' master\n')
    else:
        file2.write('No git repo\n')
    
    file2.write('\n')
        


