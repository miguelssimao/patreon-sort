import lib.selenium as sele
import lib.activity as main
from tabulate import tabulate
import lib.settings as patreon
import lib.progress as progress

# start
main.startThread()
sele.setupDriver()

# run
sele.openProfile(patreon.profileUsername)
main.bypassCookies()

# filter posts
main.filterPosts(patreon.postsImagesOnly, patreon.postsPublicOnly)

# load all posts
main.loadAllPosts()

# grab web elements
all_likes, all_hrefs = ([] for _ in range(2))
match_likes, match_hrefs = sele.findElements(patreon.likes), sele.findElements(patreon.hrefs)

# filter web elements
main.appendLikes(match_likes, all_likes)
main.appendHrefs(match_hrefs, all_hrefs)

# combine and print
progress.done = True
posts = [[all_likes[i], all_hrefs[i]] for i in range(len(all_likes))]
print("\n\n" + tabulate(sorted(posts, reverse=True), headers=["Likes", "Post"]) + "\n")
