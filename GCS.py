import tkinter as tk
from textblob import TextBlob

def get_short_response(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    if "bye" in text.lower() or "goodbye" in text.lower() or "see you" in text.lower():
        return "bye"
    elif sentiment > 0.7:
        return "👍"
    elif sentiment > 0.5:
        return "😊"
    elif sentiment > 0.3:
        return "nice"
    elif sentiment > 0.1:
        return "cool"
    elif sentiment == 0:
        return "hmm"
    elif sentiment > -0.1:
        return "fine"
    elif sentiment > -0.3:
        return "so"
    elif sentiment > -0.5:
        return "😕"
    elif sentiment > -0.7:
        return "oof"
    elif sentiment > -0.9:
        return "nope"
    else:
        return "😢"

def on_submit():
    user_input = text_entry.get("1.0", tk.END).strip()
    response = get_short_response(user_input)
    response_label.config(text=response)

root = tk.Tk()
root.title("AI Short Response")

text_entry = tk.Text(root, height=10, width=50)
text_entry.pack(pady=10)


submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack(pady=5)

response_label = tk.Label(root, text="", font=("Helvetica", 16))
response_label.pack(pady=10)

# Run the application
root.mainloop()
