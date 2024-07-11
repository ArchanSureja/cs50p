class Jar :
    def __init__(self,capacity=12):
        if capacity < 0:
            raise ValueError("Capacity cannot be negative")
        else:
            self._capacity = capacity
            self._size = 0

    def __str__(self):
        cookies = ""
        for i in range(self._size):
            cookies += "🍪"
        return cookies
           
        
    def deposit(self,n):
        if self._size + n > self._capacity:
            raise ValueError("Capacity is full")
        else:
            self._size += n
    
    def withdraw(self,n):
        if self._size-n<0:
            raise ValueError("Jar is empty")
        else:
            self._size -= n

    @property
    def capacity(self):
        return f"Capacity : {self._capacity}"
    
    def size(self):
        return f"Size : {self._size}"

def main():
    jar = Jar()
    jar.capacity
    jar.size
    jar1 = Jar(10)
    jar1.capacity 
    jar1.size 
    jar1.deposit(5)
    print(jar1)
    jar1.withdraw(4)
    print(jar1)

main()
