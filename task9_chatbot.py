"""Task 9 - Intelligent Chatbot (admission, fees, academic schedule)"""

print("College AI chatbot")
print("Type 'bye' to exit")

while True:
    try:
        user = input("You: ").lower()
    except EOFError:
        break

    if user == "bye":
        print("Bot: Thank you! Have a nice day")
        break
    elif "admission" in user:
        print("Bot: Admissions are open. Please visit the college admission office.")
    elif "fee" in user or "fees" in user:
        print("Bot: The course fee details are available at the college office.")
    elif "schedule" in user or "academic" in user:
        print("Bot: The academic schedule is available on the college website.")
    else:
        print("Bot: Sorry, I don't understand your question.")
