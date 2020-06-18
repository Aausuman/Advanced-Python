#
# Assignment 1
#
# Student Name : Aausuman Deep
# Student Number : 119220605
#
# Assignment Creation Date : February 1, 2020

class CreditCard:
    all_cards = []

    def __init__(self, customer_name, bank_name, account_identifier, limit, balance):
        self.__customer_name = customer_name
        self.__bank_name = bank_name
        self.__account_identifier = account_identifier
        self.__limit = limit
        self.__balance = balance
        CreditCard.all_cards.append(self)

    def get_customer_name(self):
        # Getter to return Customer Name
        return self.__customer_name

    def get_bank_name(self):
        # Getter to return Bank Name
        return self.__bank_name

    def get_account_identifier(self):
        # Getter to return Account Identifier
        return self.__account_identifier

    def get_limit(self):
        # Getter to return Account Limit
        return self.__limit

    def get_balance(self):
        # Getter to return Account Balance
        return self.__balance

    def charge(self, price):
        # Reduces balance by the price as long as it does not go beyond the limit
        if self.__balance - price > self.__limit:
            self.__balance -= price
            return True
        else:
            return False

    def make_payment(self, amount):
        # Increases the balance by an amount
        self.__balance += amount

    @staticmethod
    def show_summary():
        # Per Class function to print out all cards' specific information
        cards = sorted(CreditCard.all_cards, key=lambda x: x.__customer_name)
        for card in cards:
            print(card.__customer_name, " ",  card.__account_identifier, " ", card.__balance)


class PriorityQueue:
    all_pairs = []

    def len(self):
        # Returns the number of items in the container
        return len(self.all_pairs)

    def is_empty(self):
        # Checks whether the container class holds any items or not
        if len(self.all_pairs) == 0:
            return True
        else:
            return False

    def add(self, key, value):
        # Inserts a pair to the items
        self.all_pairs.append((key, value))

    def min(self):
        # Returns the pair with minimum key value from the items
        lowest_pair = self.all_pairs[0]
        for i in range(1, len(self.all_pairs)):
            if (self.all_pairs[i])[0] < lowest_pair[0]:
                lowest_pair = self.all_pairs[i]
        return lowest_pair

    def remove_min(self):
        # Returns and removes the pair with minimum key value from the items
        lowest_pair = self.min()
        self.all_pairs.remove(lowest_pair)
        return lowest_pair


# Calling part for Credit Card class

a = CreditCard("Aausuman", "ICICI", 103101, 95000, 150000)
b = CreditCard("Rebecca", "BOI", 103102, 80000, 140000)
c = CreditCard("Francois", "AIB", 103103, 75000, 125000)
CreditCard.show_summary()

# Calling part for Priority Queue class

