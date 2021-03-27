import requests,re,random,time
from time import sleep as s
from requests_html import HTMLSession

ua_list = []
userlist=re.sub('\r\n', '\n', str(requests.get('http://pastebin.com/raw/VtUHCwE6').text)).splitlines()
for x in userlist:ua_list.append(x)
random.shuffle(ua_list)
def get_useragent():return(str(random.choice(ua_list)))
pers_UA=get_useragent()
headers={'user-agent': pers_UA,'accept-language': 'en-US,en;q=0.9',}


def refresh_opgg():
    opgg_update = requests.post('https://'+Region+'.op.gg/summoner/ajax/renew.json/', headers=headers, data={'summonerId': re.findall(r'Id=[0-9]+', str(opgg_website.content))[0].strip('Id=')})
    if opgg_update.status_code == 200:print('Successfully Updated op.gg profile!')
    elif opgg_update.status_code == 418 or 504:print('Got rate limited, trying to update again in a few seconds; relaying on older stats now.')
    else:
        print('\n'+opgg_update.text)
        print('ERROR: Op.gg responded unexpectedly (Code: '+opgg_update.status_code+'); Copy & Paste this error into Github > Issues.\n')
        s(10)

def get_stats():
    refresh_opgg()
    global r,session
    session = HTMLSession()
    r = session.get('https://'+Region+'.op.gg/summoner/userName='+Username, headers=headers)
    r.html.render(timeout=20)
    website = str(r.html.html)
    
    game_history=[]
    x_val = 1
    for x in range(0, 10):
        game_history.append(r.html.find('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.RealContent > div > div.Content > div.GameItemList > div:nth-child('+str(x_val)+') > div > div.Content > div.GameStats > div.TimeStamp > span', first=True).text+':'+r.html.find('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.RealContent > div > div.Content > div.GameItemList > div:nth-child('+str(x_val)+') > div > div.Content > div.GameStats > div.GameResult', first=True).text)
        x_val+=1
    blacklist = ['day','9 hours','10 hours','11 hours','12 hours','13 hours','14 hours','15 hours','16 hours','17 hours','18 hours','19 hours','20 hours','21 hours','22 hours','23 hours']
    filtered_stats = [f for f in game_history if all([word not in f for word in blacklist])]

    matches=[]
    for j in filtered_stats:
        matches.append(j.split(':'))

    stats_today=[]
    for i in range(len(matches)):
        stats_today.append(matches[i][0])
        stats_today.append(matches[i][1])

    counted_today_dict = {i:stats_today.count(i) for i in stats_today}

    try:
        try:wins = str(counted_today_dict['Victory'])
        except:wins = 0
        try:lose = str(counted_today_dict['Defeat'])
        except:lose = 0
        resp=str('Games: '+str(len(stats_today)/2).split('.')[0]+' | '+'W '+str(wins)+' - '+'L '+str(lose))
        print(resp)
        return resp
    except Exception as e:
        print('Bad request, verify playername and op.gg status...')


if __name__ == '__main__':
    Username = 'YourUsername' #sample: hulksmash1337
    Region = 'YourRegion' #sample: na or euw
    opgg_website = requests.get('https://'+Region+'.op.gg/summoner/userName='+Username, headers=headers)
    while True:
        try:opgg_updt=get_stats()
        except:pass
        with open('stats.txt', 'w', encoding="utf-8") as output:output.write(opgg_updt)
        r.session.close()
        r.close()
        s(60) # time to wait until next update in seconds
