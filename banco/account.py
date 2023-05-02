
import decimal


class Account:


    def __init__(self, number, owner, balance, limit ) -> None:
        print(f"Creating an object of type account {self}")
        self.__number = number
        self.__owner = owner
        self.__balance = balance
        self.__limit = limit


    def statement(self):
        print(f"Statement {self.__balance} from Owner {self.__owner}")


    def deposit(self, value):
        """_summary_

        Args:
            value (decimal): deposit a value to a Account object
        """
        self.__balance += value
        print(f"New balance of Owner {self.__owner}: {self.__balance}")


    def withdraw(self, value):
        """_summary_

        Args:
            value (decimal): withdraw a valeu from a Account object
        """
        if self.can_withdraw(value):
            self.__balance -= value
            print(f"New balance of Owner {self.__owner}: {self.__balance}")


    def transfer(self, value, destiny):
        """_summary_

        Args:
            value (decimal): value to be transfered
            destiny (Account): destiny of the transfer
        """
        if self.can_withdraw(value):
            self.withdraw(value)
            destiny.deposit()
            print(f"New balance of Owner {self.get_owner()}: {self.get_balance()}")
            print(f"New balance of Owner {destiny.get_owner()}: {destiny.get_balance()}")
        else:
            print("Can't withdraw")

    def __can_withdraw(self, value):
        """_summary_

        Args:
            value (_type_): _description_

        Returns:
            _type_: _description_
        """

        return self.limit >= self.balance + value


    @staticmethod
    def bank_code(self):
        return "001"
    

    @staticmethod
    def bank_codes(self):
        return "{ 'BB': '001', 'Caixa': '104', 'Brdesco': '237' }"


    @property
    def number(self) -> int:
        return self.__number
    

    @property
    def owner(self) -> str:
        return self.__owner


    @property
    def balance(self) -> decimal:
        return self.__balance
    

    @property
    def limit(self) -> decimal:
        return self.__limit


    @limit.setter
    def limit(self, limit: decimal) -> None:
        self.__limit = limit
