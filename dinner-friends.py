import random

friends_list = []

while True:
    question = (
        input(
            "Tell me the name of your friend so it can be in the list (If you want to exit, put 'exit'): "
        )
        .strip()
        .lower()
    )
    if question == "exit":
        print("You just stopped adding friends in the list...")
        break
    elif question:
        friends_list.append(question)

if friends_list:
    payer = random.choice(friends_list)
    print(f"The friend that will pay it will be {payer}")
else:
    print("No one were added in the friend list")
