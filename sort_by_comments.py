import ps_selenium as sel
import ps_functions as main
import ps_settings as patreon
import ps_loading as progress
from tabulate import tabulate

# start
sel.setupDriver()
main.startThread(progress.loading)

# run
sel.openProfile(patreon.profileUsername)
main.bypassCookies()

# filter posts
main.scrollToFilters()
main.filterByImagesOnly(patreon.postsImagesOnly)
main.filterByPublicTier(patreon.postsPublicOnly)

# scroll to bottom
main.scrollToBottom()
main.removeBottom()

# load all posts
main.loadAllPosts()

# grab web elements
all_comns, all_hrefs = ([] for _ in range(2))
match_comns, match_hrefs = sel.findElements(patreon.comns), sel.findElements(patreon.hrefs)

# filter web elements
main.appendComments(match_comns, all_comns)
main.appendHrefs(match_hrefs, all_hrefs)

# combine and print
progress.done = True
posts = [[all_comns[i], all_hrefs[i]] for i in range(len(all_comns))]
print("\n\n" + tabulate(sorted(posts, reverse=True), headers=["Comments", "Post"]) + "\n")
