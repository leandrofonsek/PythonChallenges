from collections import deque

lista = deque()
# inserir on beginning
lista.appendleft("Leandro")
lista.appendleft("Karen")

# insert at the end
lista.append("Thiego")
lista.append("Karina")

# insert at position
lista.insert(2, "Izabel")
print(lista)
print("-------------")
# remove from beginning
removed = lista.popleft()
print("Removed: {}".format(removed))
print(lista)

# remove from end
removed = lista.pop()
print("Removed: {}".format(removed))
print(lista)

print("-------------")

# remove from position
removed = lista.remove("Izabel")
print(lista)

print(lista[0])