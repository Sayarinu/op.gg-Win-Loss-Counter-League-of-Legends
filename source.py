import requests,re,random,time,datetime
from time import sleep as s
from requests_html import HTMLSession
ua_list = []
userlist=re.sub('\r\n', '\n', str(requests.get('http://pastebin.com/raw/VtUHCwE6').text)).splitlines()
for x in userlist:ua_list.append(x)
random.shuffle(ua_list)
def get_useragent():return(str(random.choice(ua_list)))
pers_UA=get_useragent()
headers={'user-agent': pers_UA,'accept-language': 'en-US,en;q=0.9',}

if __name__ == '__main__':
    Username = 'PPMD' #sample: hulksmash1337
    Region = 'euw' #sample: na or euw
    opgg_website = requests.get('https://'+Region+'.op.gg/summoner/userName='+Username.replace(' ','+'), headers=headers)
    while True:
        try:
            global r,session,current_time,possible_update
            session = HTMLSession()
            r = session.get('https://'+Region+'.op.gg/summoner/userName='+Username.replace(' ','+'), headers=headers)
            r.html.render(timeout=20)
            website = str(r.html.html)
            opgg_update = requests.post('https://'+Region+'.op.gg/summoner/ajax/renew.json/', headers=headers, data={'summonerId': re.findall(r'Id=[0-9]+', str(opgg_website.content))[0].strip('Id=')})
            if opgg_update.status_code == 200:
                current_time = time.time()
                possible_update=int(current_time)+180
                print("Successfully Updated "+Username+"'s op.gg profile! Waiting until next possible Update @ "+datetime.datetime.fromtimestamp(possible_update).strftime('%H:%M:%S'))
                game_history=[]
                x_val = 1
                for x in range(0, 10):
                    game_history.append(r.html.find('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.RealContent > div > div.Content > div.GameItemList > div:nth-child('+str(x_val)+') > div > div.Content > div.GameStats > div.TimeStamp > span', first=True).text+':'+r.html.find('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.RealContent > div > div.Content > div.GameItemList > div:nth-child('+str(x_val)+') > div > div.Content > div.GameStats > div.GameResult', first=True).text)
                    x_val+=1
                blacklist = ['day','10 hours','11 hours','12 hours','13 hours','14 hours','15 hours','16 hours','17 hours','18 hours','19 hours','20 hours','21 hours','22 hours','23 hours']
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
                    opgg_updt=str('Games: '+str(len(stats_today)/2).split('.')[0]+' | '+'W '+str(wins)+' - '+'L '+str(lose))
                    print(opgg_updt)
                    with open('stats.txt', 'w', encoding="utf-8") as output:output.write(opgg_updt)
                except Exception as e:
                    print('Bad request, verify playername and op.gg status...')
                s(possible_update-current_time)
            elif opgg_update.status_code == 418 or 504:
                current_time = time.time()
                possible_update=int(re.search(r"e='(.*)' data-t", r.text)[1])+180
                print('Player rate limited: '+Username+' | waiting until next possible Update @ '+datetime.datetime.fromtimestamp(possible_update).strftime('%H:%M:%S')+' ; relaying on older stats now')
                s(possible_update-current_time)
            else:
                print('\n'+opgg_update.text)
                print('\nERROR: Op.gg responded unexpectedly (Code: '+opgg_update.status_code+'); Copy & Paste this error into Github > Issues.\n')
                s(30)
        except Exception as e:
            print(e)
            pass
        r.session.close()
        r.close()
