# pip install beautifulsoup4

from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

print(soup.title)       # <title>Angela's Personal Site</title>
print(soup.title.name)  # title
print(soup.title.string)# Angela's Personal Site


print(soup.prettify())

# Get all anchor tags
all_anchor_tag = soup.find_all(name="a")
print(all_anchor_tag)


# To find a particular element using ID
heading = soup.find(name="h1", id="name")
print(heading)


# To find a particular element using CLASS
selection_heading = soup.find(name="h3", class_="heading")
print(selection_heading)
print(selection_heading.get("class"))


# Using SELECTOR
name = soup.select_one(selector="#name")
print(name)
