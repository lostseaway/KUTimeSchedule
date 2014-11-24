import mechanize
import sys
from bs4 import BeautifulSoup

# print 'Number of arguments:', len(sys.argv), 'arguments.'
subject = sys.argv[1]
year = sys.argv[2]
sem = sys.argv[3]
br = mechanize.Browser()
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
req = br.open("https://inter-regis.ku.ac.th/_webcourse_data.php?key_field="+subject+"|"+year+"|"+sem)
sub = br.response().read()
soup = BeautifulSoup(sub)
# print(soup.prettify())
head = soup.p.string.encode("utf-8").replace("\xc2","")
if "Course code not found" in head:
	print head.split(":")[0]
else:
	head = head.split("\xa0")
	for x in range(0,len(head)):
		head[x] = head[x].strip()
	while 'Credit' in head:
		head.remove('Credit')
	while '' in head:
		head.remove('')
	print ("|").join(head)
	sub = soup.findAll("tr")
	out = []
	for s in sub:
		soup = BeautifulSoup(str(s))
		stmp = soup.findAll("td")
		line = []
		tline = []
		for x in stmp:
			line.append(x.string)
		for cts in line:
			if (cts is None) or (len(cts) == 0) or cts == u'\xa0':
				tline.append("NONE")
				continue
			tline.append(str((cts.replace(" ","").replace(u'\xa0',"").encode('utf-8')+" ")).strip())
		out.append(tline)
	for x in out:
		if len(x)==0:
			continue
		print ("|").join(x)

