from github import Github 
import linecache
import time
import datetime
import re
ACCESS_TOKEN = '384541efc29c6a870f9d92ae79ec11546968899a'
query="created:>2016-01-01  language:Python django "
githubAccount=Github(ACCESS_TOKEN)





def search_file(repo):
    filenames=[r"urls\.py",r"views\.py",r"settings\.py",r"manage\.py",r".*\.sqlite3"]
    filenames=[re.compile(i) for i in filenames]
    contents =repo.get_contents("")
    while contents : 
        file_content=contents.pop(0)
        if file_content.type =='dir':
            contents.extend(repo.get_contents(file_content.path))
        else :
            for i in filenames : 
                if i.match(file_content.name) : 
                    filenames.remove(i)
                    if len(filenames) ==0 :
                        break 
    return len(filenames) == 0 



filenames='reponamesxx2'

validatednames=open('validatedrepos3','w')

maxlines=10

def wait_forrate(g=githubAccount):
    rate_limit = g.get_rate_limit()
    rate = rate_limit.core
    if rate.remaining == 0:
        
        pause=(rate.reset-datetime.datetime.now()).total_seconds()
        print(f'You have 0/{rate.limit} API calls remaining. Reset time: {rate.reset} and you will wait for {pause} s')
       
        time.sleep(pause)
    else:
        print(f'You have {rate.remaining}/{rate.limit} API calls remaining')


i=0
with open(filenames,'r') as f: 
    for line in f.readlines():
        # wait_forrate(githubAccount)
        reponame=line.split(',')[0]
        print(f'{reponame}, {i}')
        try :
            wait_forrate(githubAccount)
            repo=githubAccount.get_repo(reponame)
        except : 
            f.close()
        i+=1
        if search_file(repo) :
            validatednames.writelines(reponame+'\n')
        else :
            print(f'{repo} doesn\'t seem to be a django project')


