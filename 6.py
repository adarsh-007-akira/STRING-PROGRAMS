def wordCalculator(string):
    word=string
    lst=word.split()
    num=[]
    for i in lst:
        if i == " ":
            pass
        else:
            num.append(len(i))
    print(f"WORDS\n{lst}\nCORRESPONDING LENGTHS\n{num}")
wordCalculator("adarsh-007-akira is my git hub profile.")