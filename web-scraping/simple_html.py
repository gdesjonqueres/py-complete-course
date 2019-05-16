from bs4 import BeautifulSoup

SIMPLE_HTML = '''<html>
<head></head>
<body>
<h1>This is the title</h1>
<p class="subtitle">This a lorem ipsum paragraph</p>
<p>Here's another paragraph without a class</p>
<ul>
    <li>Rolf</li>
    <li>Charlie</li>
    <li>Jen</li>
    <li>Jose</li>
</ul>
</body>
</html>'''

simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')


def find_title():
    h1_tag = simple_soup.find('h1')
    print(h1_tag.string)


def find_list_items():
    list_items = simple_soup.find_all('li')
    list_items = [i.string for i in list_items]
    print(list_items)


def find_subtitle():
    paragraph = simple_soup.find('p', {'class': 'subtitle'})
    print(paragraph.string)


def find_other_paragraph():
    paragraphs = simple_soup.find_all('p')
    paragraphs = [p.string for p in paragraphs if 'subtitle' not in p.attrs.get('class', [])]
    print(paragraphs)


find_title()
find_list_items()
find_subtitle()
find_other_paragraph()