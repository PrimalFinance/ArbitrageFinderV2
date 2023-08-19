
import requests

import threading
import queue



proxies = {
    "japan": "https://140.227.69.170:6000",
    "united_states" : "https://52.183.8.192:3128"
}



class ServerManager:
    def __init__(self) -> None:
        self.cur_proxy = None
    '''-----------------------------------'''
    def create_proxy_server(self, region: str = "united_states"):
        proxy = {
            'https': proxies[region]
        }
        self.cur_proxy = proxy
    '''-----------------------------------'''
    def check_valid_proxies(self):
        q = queue.Queue()
        valid_proxies = []
        
        with open("proxies.txt", "r") as f:
            proxies = f.read().split("\n")
            for p in proxies:
                q.put(p)
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''
    def check_IP(self):
        if self.cur_proxy == None:
            self.create_proxy_server()
        
        # Get IP details from "ipinfo.io"
        response = requests.get("https://ipinfo.io/json", proxies=self.cur_proxy)

        print(f"""------------------------
Country: {response.json()['country']}
Region: {response.json()['region']}
""")

    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''
    '''-----------------------------------'''