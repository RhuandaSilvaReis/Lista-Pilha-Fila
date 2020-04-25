class Queue:

    def __init__(self):
        self.queue = []
        self.len_queue = 0

    def push(self, e):
        self.queue.append(e)
        self.len_queue += 1

    def pop(self):
        if not self.empty():
            self.queue.pop(0)
            self.len_queue -= 1

    def empty(self):
        if self.len_queue == 0:
            return True
        return False

    def length(self):
        return self.len_queue

    def front(self):
        if not self.empty():
            return self.queue[0]
        return None

l = Queue()

print("Utilização das funções dentro da pilha.")
print("Função push para adicionar:")
l.push(3)
l.push(2)
l.push(1)
print(l.front())

print("\nFunção pop para a remoção:")
l.pop()
print(l.front())
l.pop()
print(l.front())

print("\nFunção empty para ver se a fila está vazia.")
print("A fila está vazia ? ", l.empty())

print("\nFunção length para ver a quantidaade que está na fila.")
print("Tem {} elementos na fila".format(l.length()))

print("\nFunção front que já foi utilizada, mostra a primera posição da fila.")
print(l.front())
