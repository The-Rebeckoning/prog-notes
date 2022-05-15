class Bill: 
    """
    Object that contains data about a bill such as 
    total amount and period of the bill.
    """
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period
    

class Flatmate:
    """
    Create a flatmate person who lives in the flat
    and pays a share of the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill):
        return bill.amount/2

class PdfReport:
    """
    Create a Pdf file that contains data that contains data
    about the flatmates such as their names, their due amouunt
    """
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatemate2):
        pass


bill = Bill(amount = 120, period = "March 2021")
john = Flatmate(name = "John", days_in_house=  20)
mary = Flatmate(name = "Mary", days_in_house=25)

print (john.pays(bill))

