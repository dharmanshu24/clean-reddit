#! /usr/bin/python3
import praw
import time
import getpass


def removeComments(username, reddit, requests):
    for comment in reddit.redditor(username).comments.new(limit=None):
        if(requests >= 998):
            print("30s break or else Reddit gods will get angry")
            time.sleep(30)
        print(comment.body.split('\n', 1)[0:79])
        comment.edit('Does this even work?')
        comment.delete()
        requests += 1
    return requests


def removePosts(username, reddit, requests):
    for submission in reddit.redditor(username).submissions.top('all'):
        if(requests >= 998):
            print("30s break or else Reddit gods will get angry")
            time.sleep(30)
        print(submission.title)
        submission.delete()
        requests += 1
    return requests


client_id = input("client_id=")
client_secret = input("client_secret=")
password = getpass.getpass(prompt="password=", stream=None)
username = input("username=")
requests = 0
reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, password=password, user_agent=username, username=username)

print('Removing Posts')
requests += removePosts(username, reddit, requests)

print('Removing Comments')
requests += removeComments(username, reddit, requests)
