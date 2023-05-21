from pmaw import PushshiftAPI
import datetime as dt
import pandas as pd

pd.set_option("display.max_columns", None)                  #Configuration for pandas to show all columns on dataframe
api = PushshiftAPI()                                        #Creating object of the API

def posts_search(keyword, start_time, end_time, limit):
    filters = ['id', 'author', 'created_utc','domain', 'url','title', 'num_comments'] # default columns for data analysis

    posts = list(api.search_submissions(title=keyword, after=start_time, before=end_time, filter=filters, limit=limit))

    return pd.DataFrame(posts)                              #Return dataframe for analysis

def main():

    keyword = "Black in Ukraine"                           #key phrase we are looking for
    start_time = int(dt.datetime(2022, 1, 24).timestamp())  #starting date for search
    end_time = int(dt.datetime(2022, 3, 24).timestamp())   #ending date for search
    limit = 1000                                           #Number of results wanted

    posts_df = posts_search(keyword,start_time, end_time,limit)           #Call function for dataframe creation of posts

    posts_df['datetime'] = posts_df['created_utc'].map(
        lambda t: dt.datetime.fromtimestamp(t))
    posts_df = posts_df.drop('created_utc', axis=1)                #Drop the column on timestamp format
    posts_df = posts_df.sort_values(by='datetime')                 #Sort the Row by datetime
    posts_df["datetime"] = pd.to_datetime(posts_df["datetime"])    #Convert timestamp format to datetime

    # Save the dataset on a csv file
    posts_df.to_csv(f'dataset_{keyword}_posts.csv', sep=',', header=True, index=False,
                columns=['id', 'author', 'datetime', 'domain','url', 'title', 'num_comments'])

if __name__== "__main__" : main()
