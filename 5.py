#Way 1
string="adarsh-007-akira"
print(len(string))
#Way 2
string="adarsh-007-akira"
count=0
for i in string:
    if i == " ":
        pass
    else:
        count+=1
print(count)
#Way 3
string="adarsh-007-akira"
i=0
while i<len(string):
    i+=1
print(i)
#Way 4
string="adarsh-007-akira"
def long(string):
    count=0
    for i in string:
        if i == " ":
            pass
        else:
            count+=1
    return count
long(string)