#! /bin/python

import praw

r = praw.Reddit('AyyLmap by /u/m_shayan'
		'Hosted by /u/HarmonicTimeCube')
r.login('ayylmap', 'dankmemes')


subreddit = r.get_subreddit('androidcirclejerk+ayylmap+casualconversation+anime+amiibo+tutlegoss+m_shayan+harmonictimecube+well_played_life+el_jefe15+jpleo')
target = ["ayy", "ayy!", "Ayy", "Ayy!", "AYY", "AYY!"]
already_done = set()


while True:
	subreddit_comments = subreddit.get_comments()
	for comment in subreddit_comments:
		if comment.body in target and comment.id not in already_done:
			comment.reply(' Lmap! \n \n \n \n \n *^^^I ^^^am ^^^a ^^^bot.* ^^^^/r/ayylmap ')
		already_done.add(comment.id)
