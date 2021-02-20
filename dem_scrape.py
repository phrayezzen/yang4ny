### Should be noted that this scraper, as are all scrapers, are pretty prone to error.
### Use with caution, double check the numbers pulled. If the webpage format changes, this scraper will fail.
from bs4 import BeautifulSoup as bs
from urllib2 import build_opener
opener = build_opener()
districts = range(23, 88)
boroughs = ('Manhattan', 'Brooklyn', 'Queens', 'Bronx', 'Staten Island')

# race
root = 'https://statisticalatlas.com/state-lower-legislative-district/New-York/Assembly-District-{}/Race-and-Ethnicity'
for d in districts:
    target = bs(opener.open(root.format(str(d))).read())
    counts = [target.get_text().find(i) for i in boroughs]  # also look for which borough this district belongs to
    # search for the first six rectangles with height 14 on the page, then find their percentages
    print d, boroughs[counts.index(max(counts))], target.find("tr", {"title": "Population"}).get_text().strip(), [a.get_text() for a in target.findAll('rect', height=14)[:6]]

# age
root = 'https://statisticalatlas.com/state-lower-legislative-district/New-York/Assembly-District-{}/Age-and-Sex'
for d in districts:
    target = bs(opener.open(root.format(str(d))).read())
    # search for the first five pink rectangles, then find the text (percentages) located at x=393.5
    displays = target.find("rect", {"fill": "#9aceff"}).parent.find_all('text', {'x': '393.5'})
    print d, [di.previous for di in displays][::-1]
