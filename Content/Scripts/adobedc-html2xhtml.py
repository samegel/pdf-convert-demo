# This is a rough prototype using BeautifulSoup https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# to convert html to XHTML

import os
import sys
import re
from html import HTML
from bs4 import BeautifulSoup

source = sys.argv[1]
target = sys.argv[2]

# Flare topic template
xml_template="""
<?xml version="1.0" encoding="utf-8"?>
<html xmlns:MadCap="http://www.madcapsoftware.com/Schemas/MadCap.xsd" MadCap:lastBlockDepth="8" MadCap:lastHeight="300" MadCap:lastWidth="900">
    <head>
    </head>
    <body></body>
</html>
"""

xml_output = BeautifulSoup(xml_template, "lxml")

with open(source) as s:
	soup = BeautifulSoup(s, "html.parser")

bod = soup.body.extract()

for tag in bod():
	if tag.name == "br":
		tag.decompose()
	elif tag.name == "span":
		tag.unwrap()
	elif tag.name in ["h1", "h2", "h3", "h4", "div", "ol", "ul", "li", "p"]:
		if re.search(r'\w', tag.get_text()) or tag.contents[0].name in ["img", "h1", "h2", "h3", "h4", "div", "li", "ol", "ul", "p", "span"]:
			pass
		else:
			tag.decompose()
	else:
		pass

for tag in bod():
	for attribute in ["class", "id", "name", "style", "bgcolor"]:
		del tag[attribute]

xml_output.body.replace_with(bod)

with open(target, "w") as t:
	t.write(str(xml_output))
