import requests
from send_email import send_email

api_key = "d9d7edc95de74e7dba22790e3ba03d26"
url = "https://newsapi.org/v2/everything?q=tesla&" \
    "from=2023-06-28&sortBy=publishedAt&" \
      "apiKey=d9d7edc95de74e7dba22790e3ba03d26"

# Make a request
request = requests.get(url)

# Using json to turn data into dictionary
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"]:
    body = body + article["title"] + "\n" + article["description"] + 2* "\n"

body = body.encode("utf-8")
send_email(body)




