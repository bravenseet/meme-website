import praw
import schedule
import time

with open('passwords.txt') as f:
    keys = f.readlines()

secret_key = keys[0].split('\n')[0]
reddit_pass = keys[1].split('\n')[1]
id_client = keys[2]

def generate():
    user_agent = "saucerer 1.0"
    reddit = praw.Reddit(client_id=id_client,
                          client_secret=secret_key,
                          user_agent=user_agent,
                          check_for_async=False)

    posts = []
    subreddit = reddit.subreddit('memes') 
    hot = subreddit.hot(limit=200)
    for submission in hot:
      posts.append(submission)
    for post in posts:
      with open('list.txt', 'a') as f:
        f.writelines(post.url)
        f.writelines('\n')

#Overwrite the txt file with nothing
def restart():
    with open('list.txt', 'w') as f:
      f.writelines('')

def proof():
    print('done')

#Automate generation
def backend():
    
    restart()
    generate()
    schedule.every(6).hours.at(":00").do(generate)
    schedule.every(5).hours.at(":59").do(restart)
    schedule.every(5).hours.at(":59").do(proof)

    while True:
        schedule.run_pending()
        print('.')
        time.sleep(1)

backend()
proof()