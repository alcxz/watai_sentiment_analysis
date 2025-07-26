import requests
import requests.auth
from dotenv import load_dotenv
import os

load_dotenv()

APP_USER = os.getenv("REDDIT_CLIENT_ID")
APP_PASS = os.getenv("REDDIT_CLIENT_SECRET")
USER_AGENT = os.getenv("REDDIT_USER_AGENT")
USER_USER = os.getenv("REDDIT_USER")
USER_PASS = os.getenv("REDDIT_PASS")


def ObtainAuthKey():
    client_auth = requests.auth.HTTPBasicAuth(APP_USER, APP_PASS)
    post_data = {"grant_type": "password", "username": USER_USER, "password": USER_PASS}
    headers = {"User-Agent": USER_AGENT}
    response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
    
    return response

def RetrieveTopPosts(accessToken, start_ts, end_ts, limit=15):
    headers = {"Authorization": f"bearer {accessToken}", "User-Agent": USER_AGENT}
    params = {
        # "t": "year",
        "q": f"timestamp:{start_ts}..{end_ts}",
        "syntax": "cloudsearch",
        "restrict_sr":  "on",
        "sort": "top",
        "limit": limit,
        "count": 0
    }
    response = requests.get("https://oauth.reddit.com/r/wallstreetbets/search", headers=headers, params=params)
    response.raise_for_status()
    data = response.json()["data"]["children"]
    print(response.json())
    return [item["data"] for item in data]
