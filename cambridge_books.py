import requests
from requests_html import HTML
import os

"""
https://www.cambridge.org/core/what-we-publish/textbooks
book must have online view available
"""

headers = {
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'https://www.cambridge.org/core/books/'
}

book_link = 'https://www.cambridge.org/core/books/prices-and-quantities/DF45DFA6BE48B9B82C83DF57C85DDC02'
book_name = book_link.split("/")[-2]
book_html = HTML(html=requests.get(book_link).text)
if not os.path.exists(book_name):
	os.makedirs(book_name)

chapter_links = [f"https://www.cambridge.org{link.attrs['href']}" for link in book_html.find("a.part-link")]

for chapter_link in chapter_links:
	chapter_id = chapter_link.split("/")[-1]
	chapter_name = chapter_link.split("/")[-2]
	chapter_html = HTML(html=requests.get(f"https://www.cambridge.org/core/services/online-view/get/{chapter_id}", headers=headers).text).html
	print(chapter_html)

	with open(f"{book_name}/{chapter_name}.html", "w+", encoding="utf8") as f:
		f.write(chapter_html)


print('\ndone')