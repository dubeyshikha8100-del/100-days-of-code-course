import requests

API_KEY = "9570b02b2fae41478c0644005d86f186"


print("Enter your news type \n>business of 1\n>entertainment for 2\n>general for 3\n>health for 4\n>science for 5\n>sports for 6\n>technology for 7 ") 
type = input("Enter:")

if type == "1":
    # Example: Get top headlines (India, आप चाहो तो 'us' कर सकते हो)
    url = f"https://newsapi.org/v2/business-eadlines?country=in&apiKey={API_KEY}"

    response = requests.get(url)
    data = response.json()

    if data.get("status") != "ok":
        print("Error fetching news:", data)
    else:
        articles = data.get("articles", [])
        if not articles:
            print("No news articles found.")
        else:
            for i, article in enumerate(articles, start=1):
                print(f"{i}. {article['title']}")
