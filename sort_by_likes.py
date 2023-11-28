import ps_selenium as sel
import ps_functions as main
import ps_settings as patreon
import ps_loading as progress
from tabulate import tabulate
from selenium.common.exceptions import NoSuchElementException

# start
progress.first = True
driver = sel.webDriver()
main.startThread(progress.loading)

# run
driver.get("https://www.patreon.com/" + patreon.profileUsername + "/posts")
main.bypassCookies(driver)

# filter posts
main.scrollToFilters(driver)
main.filterByImagesOnly(patreon.postsImagesOnly, driver)
main.filterByPublicTier(patreon.postsPublicOnly, driver)

# scroll to bottom
main.scrollToBottom(driver)
main.removeBanner(driver)

# load all posts
main.loadAllPosts(driver)
progress.final = True

# grab web elements
all_likes, all_hrefs = ([] for i in range(2))
match_likes, match_hrefs = sel.findElements(patreon.likes, driver), sel.findElements(patreon.hrefs, driver)

for i in match_likes:
    try:
        sel.findLikes(i, patreon.count, all_likes)
    except NoSuchElementException:
        all_likes.append(0)

for i in match_hrefs:
    try:
        sel.findHrefs(i, all_hrefs)
    except NoSuchElementException:
        all_hrefs.append(i.text)

# combine and print
progress.done = True
posts = [[all_likes[i], all_hrefs[i]] for i in range(len(all_likes))]
print("\n\n" + tabulate(sorted(posts, reverse=True), headers=["Likes", "Post"]) + "\n")