# RedditPushshiftAPI-DataCollection

## Introduction:
This program is intended to search though Reddit for post submissions by a keyword specification. The program utalizes the Pushshift API and the API wrapper pmaw for data collection. The program also allows for specifying data results by a time period.

## Using this program for Pushshift API for data collection:

### 1.) Installations:
- Install pmaw, pandas and datetime packages in terminal(MacOS) or command prompt(Windows)
- Download an Python IDE (recomended: PyCharm) to run the program on (note: The program can also be run on terminal or command prompt)
- Download the file labled main.py in this repository and open it with an IDE

### 2.) Changing main.py for specified data collection:
- line 17: keyword = "* * INSERT WORD/PHRASE YOU WOULD LIKE TO SEARCH REDDIT POSTS FOR * *"
- line 18: start_time = int(dt.datetime(**INSERT START YEAR**, **INSERT START MONTH**, **INSERT START DAY**).timestamp())
- line 19: end_time = int(dt.datetime(**INSERT END YEAR**, **INSERT END MONTH**, **INSERT END DAY**).timestamp())
- line 20: limit = **ENTER NUMBER OF ENTRIES YOU WOULD LIKE TO RECIVE**

### 3.) Running the program:
- Click the green play button on the upper right hand corner of PyCharm 
- Note: Running the program will vary depending on where the user is exicuting the program
