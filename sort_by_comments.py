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
all_comns, all_hrefs = ([] for i in range(2))
match_comns, match_hrefs = sel.findElements(patreon.comns, driver), sel.findElements(patreon.hrefs, driver)

for i in match_comns:
    try:
        sel.findComments(i, all_comns)
    except NoSuchElementException:
        all_comns.append(0)

for i in match_hrefs:
    try:
        sel.findHrefs(i, all_hrefs)
    except NoSuchElementException:
        all_hrefs.append(i.text)

# combine and print
progress.done = True
posts = [[all_comns[i], all_hrefs[i]] for i in range(len(all_comns))]
print("\n\n" + tabulate(sorted(posts, reverse=True), headers=["Comments", "Post"]) + "\n")