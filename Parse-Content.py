def parse_content(content):
    content = content.split()
    content = {content[i]:int(content[i+1]) for i in range(0,len(content),2)}
    return content

x= "ban 10\nband 5\nbar 14\ncan 32\ncandy 7"
print(x)
print(parse_content(x))

