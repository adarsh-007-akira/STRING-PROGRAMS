def finder(string, to_find):
    word=string
    find=to_find
    if find in word:
        print(f"{find} exists in string {string}")
    else:
        print(f"{find} do not exist in string {string}") 
finder("adarsh-007-akira", "akira")