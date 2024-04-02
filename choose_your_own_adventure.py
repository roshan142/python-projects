#Make Your Own Interactive Adventure 02/04/24
choice = None
name = input("Enter Your Name:")
print(f"Welcome to Cyberia \nA city where the digital world thrives\n but danger lurks around every corner.\n You are {name}, a skilled computer whiz\n ready to embark on an epic quest to protect Cyberia from cyber threats. \nYour journey begins now...")
print()
print("You're browsing the internet when you stumble upon a cryptic message warning about a looming cyber threat to Cyberia. \nWhat do you do?")
print()
print("""
1. Investigate further by tracing the message's origin.
2. Brush it off as a hoax and continue browsing.
3. Share the message with Maya, a cyber security expert, for her insight.""")
print()
while True:
    choice = input("Choose wisely: (Type the number corresponding to your choice):")
    if choice in ["1","2","3"]:
        break 
if choice == "1":
    print("You manage to trace the message to a hidden forum used by cybercriminals. This leads you to valuable information about their plans and motives.\n and you reach out maya!")
elif choice == "2":
    print("Ignoring the warning, you continue browsing, unaware of the imminent danger lurking in the digital shadows.")
    print("Your Adventure Ends Here....")
    quit()
print()
print("You reach out to Maya, a skilled cyber security expert, and share the mysterious message with her. She agrees to join forces with you to uncover the truth behind the cyber threat. \nWhat's your next move?")
print()
print("""
1. Formulate a plan to infiltrate the cybercriminal organization behind the threat.
2. Research known cyber threats and vulnerabilities to gather more information.
3. Strengthen Cyberia's defenses by implementing security measures to prevent future attacks.
""")
print()
while True:
    choice = input("Choose wisely: (Type the number corresponding to your choice):")
    if choice in ["1","2","3"]:
        break  
print()
if choice == "1":
    print("Working together, you and Maya devise a plan to infiltrate the cybercriminal organization and gather intel.")
elif choice == "2":
    print("Your research provides valuable insights into the cyber threat, helping you better understand its nature and potential impact.")
else:
    print("While fortifying Cyberia's defenses, you remain vigilant for any signs of impending cyber attacks.")
print()
print("With Maya by your side, you're ready to confront the cyber threat head-on. As you delve deeper into the digital realm, you encounter various challenges and adversaries. \nHow do you proceed?")
print()
print("""
1. Engage in a virtual battle against a group of hackers attempting to infiltrate Cyberia's networks.
2. Analyze suspicious software for malware and devise a plan to neutralize it.
3. Harden Cyberia's defenses by implementing robust firewalls and encryption protocols.
""")
print()
while True:
    choice = input("Choose wisely: (Type the number corresponding to your choice):")
    if choice in ["1","2","3"]:
        break
print() 
if choice == "1":
    print("You successfully fend off the hackers' attacks, preventing them from gaining access to sensitive data.")
elif choice == "2":
    print("By analyzing the malware, you uncover its malicious intent and develop a solution to remove it from Cyberia's systems.")
else:
    print("Your proactive measures bolster Cyberia's defenses, making it more resilient against cyber attacks.")
print()
print("As the dust settles and Cyberia begins to recover from the aftermath of the hidden threat, you reflect on the journey that brought you to this moment. What lessons have you learned, and what lies ahead for Cyberia's digital defenders?")
print()
print("""
1. With the hidden threat neutralized, you and Maya vow to remain vigilant, ever ready to face new challenges in the ongoing battle to protect Cyberia from cyber threats.
2. Despite the setbacks, you refuse to be deterred, redoubling your efforts to strengthen Cyberia's cyber security infrastructure and rebuild what was lost.
3. As Cyberia emerges stronger and more resilient than ever, you look towards the future with hope and determination, knowing that together, you can overcome any obstacle that comes your way.
""")
print()
while True:
    choice = input("Choose wisely: (Type the number corresponding to your choice):")
    if choice in ["1","2","3"]:
        break 
print()
if choice == "1":
    print("With the hidden threat neutralized, you and Maya commit to remaining vigilant, ensuring Cyberia remains safe and secure from future cyber threats.")
elif choice == "2":
    print("Despite the setbacks, you refuse to be deterred, redoubling your efforts to strengthen Cyberia's cyber security infrastructure and rebuild what was lost, ensuring Cyberia emerges stronger and more resilient than ever before.")
else:
    print("With Cyberia emerging stronger and more resilient than ever, you look towards the future with hope and determination, confident that together, you can overcome any obstacle that comes your way.")
print()
print("The Adventure Continues.....")
print()
