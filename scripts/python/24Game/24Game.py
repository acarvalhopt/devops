import re

def split(word):
    return [char for char in word]

def doTheMath(operator, num1, num2, num3, num4,calc_list):
    op1,op2,op3=split(operator)
    math=(str(num1)+op1+str(num2)+op2+str(num3)+op3+str(num4))
    result=eval(math) #do the math inside of the string.
    result = int(result)
    if(result == 24):
        calc=str(math)+"="+str(result) 
        calc_list.append(calc)
        # print(str(math)+"="+str(result))
    return calc_list
    

def operations():
    operators = ['+','-','*','/']
    operation_list=[]
    for i in operators:
        for j in operators:
            for k in operators:
                operation=i+j+k
                # print(operation)
                operation_list.append(operation)
    operation_list = list(dict.fromkeys(operation_list)) #remove duplicates
    return operation_list

def create_board():
    board_list = []

    for op in calc_list:
        board_numbers = re.findall(r'\b\d+\b', op)
        board=''
        for i in board_numbers[:4]:
            board=board+i
        board_list.append(board)
    
    return board_list

operation_list=operations()

start=1
end=10
calc=0
result=0
calc_list=[]

for i in range(start,end):
    for j in range(start,end):
        for k in range(start,end):
            for l in range(start,end):
                for item in operation_list:
                    calc_list=doTheMath(item,i,j,k,l,calc_list)


board_list=create_board()
board_list=list(dict.fromkeys(board_list)) #remove duplicates
print("[INFO] - Possible combinations: " + str(len(board_list)))
#print(board_list)
