from flask import Flask, render_template, request

app = Flask(__name__)

# Simple Chatbot Logic
def get_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Welcome to Afzaal's Cafe! 😊 How can I help you today?"
    elif "menu" in user_input:
        return "We serve coffee, tea, cakes, and sandwiches. ☕🍰🥪"
    elif "coffee" in user_input:
        return "Our coffee is freshly brewed with love! ❤️ Would you like one?"
    elif "price" in user_input:
        return "Our coffee price 250pkr for chocolate ❤️ and for simple 150pkr. Would you like one?"
    elif "bye" in user_input:
        return "Goodbye! Have a sweet day! 🍩"
    else:
        return "I'm just a simple cafe bot 🤖, but I can help with orders and suggestions!"

@app.route("/", methods=["GET", "POST"])
def index():
    user_input = ""
    bot_response = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        bot_response = get_response(user_input)
    return render_template("index.html", user_input=user_input, bot_response=bot_response)

if __name__ == "__main__":
    app.run(debug=True)
