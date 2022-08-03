class Evaluate:
 
  def __init__(self, size):
    self.top = -1
    self.size_of_stack = size
    self.stack = []

  def isEmpty(self):
    if self.top==-1:
      return True
    else:
      return False


  def pop(self):
    if not self.isEmpty():
     self.stack.pop()
      


  def push(self, operand):
   if self.top!= self.size_of_stack-1:
    self.stack.append(operand)
      
   
    

  def validate_postfix_expression(self, expression):
   a=0
   b=0
   for element in expression:
    if element.isnumeric():
     a=a+1
    else:
     b=b+1
    if b==a-1:
     return True
    else:
     return False
      
    
      

  def evaluate_postfix_expression(self, expression):
   stack=[]
   for i in expression:
    if i.isnumeric():
     stack.append(int(i))
    if len(stack)>=2:
     if i=='+':
      stack[-2]=stack[-2] + stack[-1]
      stack.pop()
     elif i=='-':
      stack[-2]=stack[-2] - stack[-1]
      stack.pop()
     elif i=='*':
      stack[-2]=stack[-2] * stack[-1]
      stack.pop()
     elif i=='/':
      stack[-2]=stack[-2] / stack[-1]
      stack.pop()
     elif i=='^':
      stack[-2]=stack[-2] ^ stack[-1]
      stack.pop()
   return int(stack[-1])
      
    
    


# Do not change the following code
postfix_expression = input()  # Read postfix expression
tokens = postfix_expression.split()
evaluate = Evaluate(len(tokens))
if evaluate.validate_postfix_expression(tokens):
    print(evaluate.evaluate_postfix_expression(tokens))
else:
    print('Invalid postfix expression')
