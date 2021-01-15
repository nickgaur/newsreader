

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


if __name__ == '__main__':
    import requests

    news_api = requests.get("https://newsapi.org/v2/top-headlines?",
                            params = {"country": "in", "from": "2021-01-14", "to": "2021-01-14", "language": "en", "pageSize": 100,
                                      "apiKey": "0c8b***********************f60e04a"})

    news_dict = news_api.json()
    for item in news_dict["articles"]:
        speak(item["description"])
