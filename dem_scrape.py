from bs4 import BeautifulSoup as bs
from urllib2 import build_opener
opener = build_opener()
districts = range(23, 88)
boroughs = ('Manhattan', 'Brooklyn', 'Queens', 'Bronx', 'Staten Island')

# race
root = 'https://statisticalatlas.com/state-lower-legislative-district/New-York/Assembly-District-{}/Race-and-Ethnicity'
for d in districts:
    target = bs(opener.open(root.format(str(d))).read())
    counts = [target.get_text().find(i) for i in boroughs]
    print d, boroughs[counts.index(max(counts))], target.find("tr", {"title": "Population"}).get_text().strip(), [a.get_text() for a in target.findAll('rect', height=14)[:6]]

# age
root = 'https://statisticalatlas.com/state-lower-legislative-district/New-York/Assembly-District-{}/Age-and-Sex'
for d in districts:
    target = bs(opener.open(root.format(str(d))).read())
    displays = target.find("rect", {"fill": "#9aceff"}).parent.find_all('text', {'x': '393.5'})
    print d, [di.previous for di in displays][::-1]
