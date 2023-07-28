import body as body
import requests
from send_email import send_email

topic = "tesla"

api_key = "d9d7edc95de74e7dba22790e3ba03d26"
url = "https://newsapi.org/v2/everything?" \
    f"q={topic}&" \
    "from=2023-06-28&" \
    "sortBy=publishedAt&" \
    "apiKey=d9d7edc95de74e7dba22790e3ba03d26&" \
    "langauge=en"

# Make a request
request = requests.get(url)

# Using json to turn data into dictionary
content = request.json()

body = ""
# Access the article titles and description
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: News today" + "\n" + body + article["title"] + "\n" \
            + article["description"]\
            + "\n" + article["url"] + 2* "\n"

body = body.encode("utf-8")
send_email(body)




