from collections import deque

# book = dict()
# book = {}

# book["apple"] = 0.67
# book["milk"] = 1.49
# book["avocado"] = 1.57

# print(book.get("apple2s") == True)

graph = {}
graph["you"] = ['alice', 'bob', 'claire']
graph["bob"] = ["anuj", 'peggy']
graph['alice'] = ["peggy"]
graph["claire"] = ["thom", 'jonny']
graph['anuj'] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

search_queue = deque()
search_queue += graph["you"]