#-> datová struktura
#-> složitost
#-> Asymptoticka složitost
"""
push - vloží prvek na vrch zásobníku
pop - odstraní vrchol zásobníku
top - dotaz na vrchol zásobníku
isEmpty - dotaz na prázdnost zásobníku (size - dotaz na velikost zásobníku)
"""

class Stack:
    def __init__(self, size):
        self.__items = []
        self.__size = size

    def push(self, item):
        if len(self.__items.append(item)) < self.__size:
            self.__stack.append(item)
            return True

    def pop(self):
            return self.__items.pop()


    def top(self):
        return self.__items[-1]


    def isEmpty(self):
        return len(self.__items) == 0

    def actual_size(self):
        return len(self.__items)

    def max_size(self):
        return self.__size

    def __str__(self):
        return f"Zásobník: {self.__items}"

########

browser_history = Stack(3)

browser_history.push("google.com")
browser_history.push("xpornhub.lol")
browser_history.push("github.com")

print(browser_history)


current_page = browser_history.top()
print(f"Aktuální stránka: {current_page}")


previous_page = browser_history.pop()
print(f"Vracíme se na: {browser_history.top()}")


print(f"Počet navštívených stránek: {browser_history.actual_size()}")


