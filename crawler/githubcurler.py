import requests

headers = {'Authorization': 'token 384541efc29c6a870f9d92ae79ec11546968899a'}
creationdate='2017-01-01'


reponames=open('reponamesxx2','a')
# pushed_date='2020-02-04T00:31:46Z'
url= f'https://api.github.com/search/repositories?q=created:>{creationdate}+pushed:<{pushed_date}+language:Python+django&sort=updated&order=desc&per_page=100'
for i in range(0,11):
    url=url+f'&page={i}'
    r=requests.get(url,headers=headers)
    if r.ok : 
        lines='\n'.join(f'{x["full_name"]},{x["pushed_at"]}' for x in r.json()['items'])
    else :
        break
    reponames.writelines(lines+'\n')
reponames.close()

pushed_date=lines.split(',')[-1]