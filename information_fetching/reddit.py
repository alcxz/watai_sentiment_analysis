# from reddit_praw import fetch_top_year_posts, process_submissions
from reddit_basic_api import ObtainAuthKey, RetrieveTopPosts
from datetime import datetime, timezone

def main():
    res = ObtainAuthKey()
    start_dt = datetime(2023,  1,  1, 0, 0, 0, tzinfo=timezone.utc)
    end_dt   = datetime(2023, 12, 31, 23,59,59, tzinfo=timezone.utc)

    start_ts = int(start_dt.timestamp())
    end_ts   = int(end_dt.timestamp())
    data = RetrieveTopPosts(res.json()["access_token"], start_ts, end_ts, 5)
    dateFarEnough = False
    print(len(data))
    for item in data:
        # print(item)
        print("===== Post =====")
        print("Title: ", item["title"])
        print("Score: ", item["score"])
        print("Num Comments: ", item["num_comments"])
        print("Post Date: ", datetime.fromtimestamp(item["created_utc"], tz=timezone.utc).isoformat())




if __name__ == "__main__":
    main()
