# Clean-reddit
Remove past comments and posts from reddit

# Installation
1. Install pip3

`sudo apt-get install pip3`

2. Install praw

`pip3 install praw`
 
# Usage
Create Reddit application
1. Open your Reddit application preferences by clicking [here](https://www.reddit.com/prefs/apps/).
2. Add a new application. It doesn't matter what it's named, but calling it "clean-reddit" makes it easier to remember.
3. Select "script".
4. Redirect URL does not matter for script applications, so enter something like http://127.0.0.1:8080
5. Once created, you should see the name of your application followed by 14 character string. Enter this 14 character
   string as your `client_id`.
6. Copy the 27 character "secret" string into the `client_secret` field.

Username and password are simply your Reddit login credentials for the account that will be used.

Run the `cleanReddit.py` file

`python3 cleanReddit.py`

Enter `client_id`,`client-secret`,`password`,`username` and just wait untill everything is deleted
