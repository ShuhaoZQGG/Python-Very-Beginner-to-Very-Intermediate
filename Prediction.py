import collections
import functools
import operator

def get_leaves(node):
    leaves = {}
    for label, child in node.items():
        if not isinstance(child,dict):
            leaves[label[1:]] = child
            continue
        leaves.update(get_leaves(child))
    return leaves

x = {
  'ban': 10,
  'band': 5,
  'bar': 14,
  'can': 32,
  'candy': 7
}

print(get_leaves(x))
'''
def predict(tree, numbers):
    leaves = [tree]
    for number in numbers:
        leaves = [leaf[letter] for letter in  keymap[number] for leaf in leaves if letter in leaf]

    words = {}
    for node in leaves:
        words.update(get_leaves(node))
    
    return sorted(words.item(),key=operator.itemgetter(1), reverse = True)
'''

y = {'b': {'a': {'n': {'$ban': 10, 'd': {'$band': 5}}, 'r': {'$by': 7}}}}            

def predict(tree, numbers):
    leaves = [tree]
    for number in numbers:
        letters = keymap[number]
        leaves = [leaf.get(letter, None) for letter in letters for leaf in leaves]
        while True:
            try:
                leaves.remove(None)
            except ValueError:
                break
    words = {}
    for node in leaves:
        while node:
            letter, child = node.popitem()
            if not isinstance(child, dict):  # We have a word!
                word, frequency = letter[1:], child
                words[word] = frequency
                continue
            leaves.append(child)
    return sorted(words.items(), key=operator.itemgetter(1), reverse=True)

