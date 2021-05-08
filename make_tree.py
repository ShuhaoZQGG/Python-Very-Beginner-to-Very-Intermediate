x = {
  'ban': 10,
  'band': 5,
  'bar': 14,
  'can': 32,
  'candy': 7
}

'''
def make_tree(words):
    fill = {}
    for key, value in words.items():
        node = fill
        for c in key:
            if c not in node:
                node[c] = {}
            node = node[c]
        node[f'${key}'] = value
                
    return fill
'''
def make_tree(words):
    trie = {}
    for word, frequency in words.items():
        node = trie
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        
        node[f'${word}'] = frequency
        print(node)
        print(trie)
    return trie

make_tree(x)
print(make_tree(x))

fill = {}
x= {"hello":1}
for key, value in x.items():
    node = fill
    for c in key:
        if c not in node:
          node[c] ={}
        node = node[c]
print(fill)

trie={}
node= trie

if "hi" not in node :
    node["hi"]={}
node=node["hi"]

if "world" not in node:
    node["world"] = {}
node = node["world"]

print (node)
print(trie)     

trie = {}
node = trie
node["hello"] = 1
#node = node["hello"]
print(node)
print(trie)

trie={}
node = trie
node = {"hello":1}
node = node["hello"] 
print(node)
print(trie)
