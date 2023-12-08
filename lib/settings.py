# patreon settings
profileUsername  = "greenteahoney"
postsImagesOnly  = True
postsPublicOnly  = True

# patreon css selectors and xpath
tier    = 'button[aria-label="Sort posts by tier"]'
post    = 'button[aria-label="Sort posts by post type"]'
images  = "//button[contains(div,'Image')]"
public  = "//*[contains(text(), 'Public (')]"
more    = "//*[contains(text(), 'See more posts')]"
likes   = 'div[data-tag="all-posts-layout"] button[data-tag="like-button"]'
comns   = 'div[data-tag="all-posts-layout"] a[data-tag="comment-post-icon"]'
hrefs   = 'div[data-tag="all-posts-layout"] div span[data-tag="post-title"]'
count   = 'span[data-tag="like-count"]'