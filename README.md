# RedditPushshiftAPI-DataCollection

## Introduction:
This program is intended to search though Reddit for post submissions by a keyword specification and allows for specifying data results by time period. This program also allows for collecting the comments given a specified submission ID. The program utalizes the Pushshift API and the API wrapper pmaw for submission data collection. The program uses the official reddit API praw for comments data collection.

## Using this program for data collection:

### 1.) Installations:
- Install pmaw, pandas and datetime packages in terminal(MacOS) or command prompt(Windows)
- Download an Python IDE (recomended: PyCharm) to run the program on (note: The program can also be run on terminal or command prompt)
- Download the files labled submissionCollection.py and commentCollection in this repository and open it with an IDE

### 2.) Changing program for specified data collection:
submissionCollection.py (Allows for search though Reddit post submissions by a keyword specification)
- line 17: keyword = "* *INSERT WORD/PHRASE YOU WOULD LIKE TO SEARCH REDDIT POSTS FOR* *"
- line 18: start_time = int(dt.datetime(* *INSERT START YEAR* *, * *INSERT START MONTH* *, * *INSERT START DAY* *).timestamp())
- line 19: end_time = int(dt.datetime(* *INSERT END YEAR* *, * *INSERT END MONTH* *, * *INSERT END DAY* *).timestamp())
- line 20: limit = * *ENTER NUMBER OF ENTRIES YOU WOULD LIKE TO RECIVE* *

commentCollection.py (Allows for collecting the comments given a specified submission ID)
- line 21: id_list = ["* *INSERT LIST OF SUBMISSION IDS* *"]


### 3.) Running the program:
- Click the green play button on the upper right hand corner of PyCharm 
- Note: Running the program will vary depending on where the user is exicuting the program
