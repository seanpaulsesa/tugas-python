class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def addl(self, isi):  # Menambahkan parameter isi
        a = Node(isi)
        if self.head is None:
            self.head = a
        else:
            a.next = self.head  # Perbaikan dari a._next
            self.head = a

    def cetak(self):  # Dikeluarkan dari dalam addl
        a = self.head
        while a is not None:
            print(a.data)
            a = a.next


# Contoh penggunaan
mylist = LinkedList()
mylist.addl("7")
mylist.addl("4")
mylist.addl("6")

mylist.cetak()
