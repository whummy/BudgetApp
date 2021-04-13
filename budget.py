class Budget:

  def __init__(self,category):
    self.category = category
    self.total_budget = 0
    self.description = ""

  def deposit(self, amount, description=""):
    self.total_budget += amount
    self.description = description
    print('deposit successful')
    
  def withdrawal(self,amount,description=""):
    if self.total_budget > 0:
      self.total_budget -= amount
      self.description = description
      print('withdrawal successful')
    else:
      print('insufficient funds')

  def get_balance(self):
    return self.total_budget

  def transfer(self,amount,category):
    if self.total_budget > 0:
      self.total_budget -= amount
      category.deposit(amount)
      print('transfer successful')
    else:
      print('insufficient funds')