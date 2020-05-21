import praw
import pprint

reddit = praw.Reddit(client_id='K7exBzBc-hgC3w',
                     client_secret='4JPP1biCuEaqFSPMoL-iSHessno',
                     user_agent='updawgbot',
                     username='updawgbot',
                     password='updawgbot')
print(reddit.user.me())
mysterise = reddit.redditor("Mysterise")
# pprint.pprint(vars(mysterise))
for submission in mysterise.submissions.new(limit = 5):
    # comment.reply("What the fuck is updawg")
#     comment.
    print(submission.title + str(submission.score))