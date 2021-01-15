

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


if __name__ == '__main__':
    import requests

    news_api = requests.get("https://newsapi.org/v2/top-headlines?",
                            params = {"country": "in", "from": "2021-01-14", "to": "2021-01-14", "language": "en", "pageSize": 100,
                                      "apiKey": "0c8b8ea8354d4f58a9d3c522df60e04a"})

    # print(news_api.text)
    news_dict = news_api.json()
    for item in news_dict["articles"]:
        speak(item["description"])