import datetime

print("python mini project ")
print("predefined responses chatbox")

responses = {
    "hello": "How may I help you",
    "hi": "hello, speak your mind",
    "how are you": "I am fine thank you",
    "date": "today is " + datetime.date.today().strftime("%B %d, %Y"),
    "time": "current time is " + datetime.datetime.now().strftime("%I:%M %p"),
    "default": "Please repeat again",
    "exit": "Goodbye!",
    "quit": "Goodbye!",
    "bye": "Goodbye!"
}

def pinput(u):
    u = u.lower()
    for key in responses:
        if key in u:
            return responses[key]
    return responses["default"]

while True:
    u = input("YOU: ")
    response = pinput(u)
    print("chatbox:", response)
    if u.lower() in ["exit", "quit", "bye"]:
        break
