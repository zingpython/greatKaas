from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

req = Request("http://www.cmegroup.com/trading/equity-index/us-index/e-mini-sandp500_quotes_settlements_futures.html",
	headers={"User-Agent":"Mozilla/5.0"})

webpage = urlopen(req).read()

soup_object = BeautifulSoup(webpage, "html.parser")

table = soup_object.find("table", {"id":"settlementsFuturesProductTable"})

rows = table.findAll("tr")

new_table = []

for row in rows:
	# print(row)
	# print("----------------------------------")
	row_list = []
	for cell in row.findAll(["th", "td"]):
		row_list.append(cell.get_text())

	new_table.append(row_list)

print(new_table)