from pmaw import PushshiftAPI
import pandas as pd
import praw

reddit = praw.Reddit(client_id="69xO_MRhRBIQGprtVEZIbA",
    client_secret="GgPpkwrp_BPNduxYQ-dOcxfmrykfhQ",
    user_agent="test")

pd.set_option("display.max_columns", None)                  #Configuration for pandas to show all columns on dataframe

def posts_search(keyword, start_time, end_time, limit):
    filters = ['id', 'author', 'created_utc','domain', 'url','title', 'num_comments'] # default columns for data analysis

    posts = list(api.search_submissions(title=keyword, after=start_time, before=end_time, filter=filters, limit=limit))

    return pd.DataFrame(posts)                              #Return dataframe for analysis

def main():

    try:
        id_list = ["tjoppi","tjx71z","tk97gn","tktz86","tkw5dl"]
        for i in id_list:
            print("in")
            comment_list = []
            submission = reddit.submission(i)
            submission.comments.replace_more(limit=None)
            for comment in submission.comments.list():
                comment_list.append(comment.__dict__)
            comments_df = pd.DataFrame(comment_list)
            comments_df.to_csv(f'dataset_{i}_comments.csv')
    except:
        print("An exception occurred")

if __name__== "__main__" : main()
