class BudgetManager:
    def __init__(self, amount):
        self.available = amount
        self.budgets = {}
        self.expenditure = {}
    def add_budget(self, name, amount):
        if name in self.budgets:
            raise ValueError("Budget exists")
        if amount > self.available:
            raise ValueError("Insufficient Funds") 
        self.budgets[name] = amount
        self.available -= amount
        self.expenditure[name] = [] #Previously 0,
        return self.available #Start change_budget = hack and tweak
    def change_budget(self,name, new_amount):
        if name not in self.budgets:
            raise ValueError("Budget does not exist")
        old_amount = self.budgets[name]
        if new_amount > old_amount + self.available:
            raise ValueError("Insufficient funds")
        self.budgets[name] = new_amount
        self.available -= new_amount - old_amount
        return self.available #End change_budget 
    def spend(self, name, amount):
        if name not in self.expenditure:
            raise ValueError("No such budget")
        self.expenditure[name].append(amount) # hack and tweak
        budgeted = self.budgets[name]
        spent = sum(self.expenditure[name]) # hack and tweak 2
        return budgeted - spent
    def print_summary(self):
        print("Budget           Budgeted  Spent       Remaining")
        print("--------------  ---------  ----------  ----------")
        total_budgeted = 0
        total_spent = 0
        total_remaining = 0 
        for name in self.budgets:
            budgeted = self.budgets[name]
            spent = sum(self.expenditure[name]) # hack and tweak 2 continued
            remaining = budgeted - spent
            print(f'{name:15s} {budgeted:10.2f} {spent:10.2f} '
                  f'{remaining:10.2f}')
            total_budgeted += budgeted
            total_spent += spent
            total_remaining += remaining
        print("----------------- ----------- ------------ --------")
    
    
