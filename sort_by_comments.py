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
all_comns, all_hrefs = ([] for _ in range(2))
match_comns, match_hrefs = sele.findElements(patreon.comns), sele.findElements(patreon.hrefs)

# filter web elements
main.appendComms(match_comns, all_comns)
main.appendHrefs(match_hrefs, all_hrefs)

# combine and print
progress.done = True
posts = [[all_comns[i], all_hrefs[i]] for i in range(len(all_comns))]
print("\n\n" + tabulate(sorted(posts, reverse=True), headers=["Comments", "Post"]) + "\n")
