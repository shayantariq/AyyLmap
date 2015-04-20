#! /bin/python3

import praw

r = praw.Reddit('AyyLmap by /u/m_shayan'
		'Hosted at http://www.pythonanywhere.com'
		'https://github.com/M-Shayan/AyyLmap')
r.login('ayylmap', 'password')


subreddit = r.get_subreddit('redditdev+learnprogramming+programmerhumor+androidcirclejerk+ayylmap+casualconversation+amiibo+tutlegoss+m_shayan+harmonictimecub+casualc+ledootgeneration+well_played_life+el_jefe15')
target = ["ayy", "ayy!", "Ayy", "Ayy!", "AYY", "AYY!"]
already_done = set()


while True:
	subreddit_comments = subreddit.get_comments()
	for comment in subreddit_comments:
		if comment.body in target and comment.id not in already_done:
			comment.reply(' [Lmap!](http://i.imgur.com/Gpg9YBR.png) \n \n \n \n \n *^^^^I ^^^^am ^^^^a ^^^^bot.* ^^^^^/r/ayylmap ')
		already_done.add(comment.id)

