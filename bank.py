answer = input("greeting,").lower().strip()

if answer == "hello" or answer == "hello, newman":
    print("$0")
elif "how you doing?" == answer:
    print("$20")
elif answer == "what's happening?":
    print("$100")
else:
    print("try again")