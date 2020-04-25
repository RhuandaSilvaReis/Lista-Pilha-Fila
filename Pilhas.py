class Stack:

    def __init__(self):
        self.stack = []
        self.len_stack = 0

    def push(self, e):
        self.stack.append(e)
        self.len_stack += 1

    def pop(self):
        if not self.empty():
            self.stack.pop(self.len_stack - 1)
            self.len_stack -= 1

    def top(self):
        if not self.empty():
            return self.stack[-1]
        return None

    def empty(self):
        if self.len_stack == 0:
            return True
        return False

    def length(self):
        return self.len_stack


p = Stack()
print("Função push sendo utilizada para a inserção.")
p.push(1)
p.push(2)
p.push(3)
print(p.top())
print("\nFunção pop.")
p.pop()
print(p.top())
print("Função top já utilizada acima mostra o topo da pilha.")

print("\nFunção empty.")
print("A pilha está vazia ?", p.empty())

print("\nFunção length.")
print("A quantidade de elementos na pilha é ",p.length())


