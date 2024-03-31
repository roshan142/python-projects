#Quiz_Game 01/04/24
Questions = ["""
Q1:
    Which of the following file formats is not a video file format?
        1) .MP3
        2) .MP4
        3) .MOV
        4) .AVI 
             """,
             """
Q2:
    What is the full form of GPT in Chat GPT?
        1) GUID Partition Table
        2) Grooved Pegboard Test
        3) Generative Pre-Trained Transformer
        4) Glutamic Pyruvic Trans­aminase
             """,
             """ 
Q3:
    IC chips used in computers are made with -
        1) Gold
        2) Silicon
        3) Copper
        4) Silver
            """,
            """
Q4:
    What is the speed of the computer measured it?
        1) Nanoseconds
        2) Kilo seconds
        3) Gigahertz
        4) Megabytes
            """,
            """
Q5:
    In the context of the Internet, what is the full form of a URL?
        1) User Requested Link
        2) Ultimate Response Location
        3) Unique Request Locator
        4) Uniform Resource Locator
            """,
            """
Q6:
        Which of the following is not an example of a Virtual Assistant?
        1) Alexa
        2) Cortana
        3) Siri
        4) Cortesa
            """,
            """
Q7:
    Which of the following is not a browser?
        1) Android
        2) Firefox
        3) Chrome
        4) Safari       
            """,
            """
Q8:
    The feature(s) of cyber security is /are -
        1) Compliance
        2) Defence against internal threats
        3) Threat prevention
        4) All of the above
            """,
            """
Q9:
    Hard copies can be obtained from -
        1) Scanner
        2) Speaker
        3) Printer
        4) Recorder
            """,
            """
Q10:
    DHCP is mainly used in -
        1) Routing
        2) Converting IP address to domain name
        3) Providing IP address automatically to the devices
        4) Multicasting
            """,]
ans = ["1","3","2","3","4","4","1","4","3","3"]
user_ans = []
score = 0
def ask(q):
    print(Questions[q])
    x = True
    while x:
        a = input("Enter Your Choice:")
        if a not in ["1","2","3","4"]:
            print("Enter a Valid Choice(1/2/3/4)!")
        else:
            x= False
    return a

print("Welcome To Computer Quiz!")
run = input("Do you want to play? :")
if run not in ["yes","y"]:
    quit()
print("Okay Let's Play!")

for i in range(10):
    result = ask(i)
    user_ans.append(result)

for i in range(10):
    if ans[i] == user_ans[i]:
        score += 1
wrong = 10 - score 
print(f"Correct:{score} Incorrect:{wrong}") 




