import time
from random import randint
import threading

class Bank(threading.Thread):
    """Создание класса, его конструкта и методов."""
    balance = 0
    lock = threading.Lock()

    def __init__(self):
        threading.Thread.__init__(self)
        self.Bank = self

    def deposit(self):
        transactions = 100
        while transactions > 0:
            random_num = randint(50, 500)
            if self.balance >= 500 and self.lock.locked() == True:
                self.lock.release()
            self.balance += random_num
            print(f"Пополнение: {random_num}. Баланс: {self.balance}.")
            transactions -= 1
            time.sleep(0.001)

    def take(self):
        transactions = 100
        while transactions > 0:
            transactions -= 1
            random_num = randint(50, 500)
            print(f"Запрос на {random_num}")
            if random_num <= self.balance:
                self.balance -= random_num
                print(f"Снятие: {random_num}. Баланс: {self.balance}")
            else:
                print(f"Запрос отклонен, недостаточно средств.")
                self.lock.acquire()
            time.sleep(0.001)

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')