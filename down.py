import aiohttp
import asyncio

from bs4 import BeautifulSoup
async def get_html(session, url):
    async with session.get(url, ssl=False) as res:
        return await res.text()
    
async def main(url):
    async with aiohttp.ClientSession() as session:
        html = await get_html(session, url)
        name = url[33:-52]
        soup = BeautifulSoup(html,'html.parser')
        
        
        
        
        down = (soup.find('strong',attrs={'class':'stat-summary'})).text
   
        
        with open('newdownloads.txt','a') as f:
            f.write(name)
            f.write(' ')
            f.write(down)
            f.write('\n')
            print('done',name)
            
        


urls=[]
l=['url1','url2','url3','url n']      #Insert the names of projects here
for na in l:
    urls.append(f'https://sourceforge.net/projects/{na}/files/stats/timeline?dates=1999-02-18+to+2019-05-19')
loop = asyncio.get_event_loop()
loop.run_until_complete(
    asyncio.gather(*(main(url) for url in urls))
)
    
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
