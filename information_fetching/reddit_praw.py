import praw
import requests
from datetime import datetime, timezone
from dotenv import load_dotenv
import os

# Setting up an app using reddit api calls
load_dotenv()
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

# API call - gets submission data
def fetch_top_year_posts(subreddit_name, limit=1000):
    return reddit.subreddit(subreddit_name).top(
        time_filter="year",
        limit=limit
    )

# Processes Submissions returned from the API call
def process_submissions(submissions):
    for sub in submissions:
        print("\n---", sub.title)
        print("Score:", sub.score, "•", "Comments:", sub.num_comments)
        created = datetime.fromtimestamp(sub.created_utc, tz=timezone.utc)
        print("Created At:  ", created.isoformat())

        # get top-10 comments
        sub.comment_sort = 'top'
        sub.comments.replace_more(limit=0)
        for c in sub.comments[:10]:
            ts = datetime.fromtimestamp(c.created_utc, tz=timezone.utc).isoformat()
            print(f"  ▶ {c.score}pts @ {ts} — {c.body[:80].replace(chr(10),' ')}...")