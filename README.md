# RedditPushshiftAPI-DataCollection

Introduction:

Using this program for Pushshift API for data collection:
- install pmaw, pandas and datetime packages in terminal(MacOS) or command prompt(Windows)
- Download an Python IDE (recomended: PyCharm) to run the program on (note: The program can also be run on terminal or command prompt)
- download the file labled main.py in this repository and open it with an IDE

Changes to make to main.py for specified data collection:
- line 17: keyword = "**INSERT WORD/PHRASE YOU WOULD LIKE TO SEARCH REDDIT POSTS FOR**"
- line 18: start_time = int(dt.datetime(**INSERT START YEAR**, **INSERT START MONTH**, **INSERT START DAY**).timestamp())
- line 19: end_time = int(dt.datetime(**INSERT END YEAR**, **INSERT END MONTH**, **INSERT END DAY**).timestamp())
- line 20: limit = **ENTER NUMBER OF ENTRIES YOU WOULD LIKE TO RECIVE**
