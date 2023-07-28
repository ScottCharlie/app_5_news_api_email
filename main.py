import requests

api_key = "d9d7edc95de74e7dba22790e3ba03d26"
url = "https://newsapi.org/v2/everything?q=tesla&" \
    "from=2023-06-28&sortBy=publishedAt&" \
      "apiKey=d9d7edc95de74e7dba22790e3ba03d26"

# Make a request
request = requests.get(url)

# Using json to turn data into dictionary
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])



