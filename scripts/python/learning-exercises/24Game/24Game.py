import re

def split(word):
    return [char for char in word]

def doTheMath(operator, num1, num2, num3, num4,calc_list):
    op1,op2,op3=split(operator)
    math=(str(num1)+op1+str(num2)+op2+str(num3)+op3+str(num4))
    result=int(eval(math)) #do the math inside of the string.
    if(result == 24):
        # print(str(math)+"="+str(result))
        calc_list.append(math)
    return calc_list
    

def getOperations():
    operators = ['+','-','*','/']
    operation_list=[]
    #do all operations combinations with 3 operators.
    for i in operators:
        for j in operators:
            for k in operators:
                operation=i+j+k
                # print(operation)
                operation_list.append(operation)
    operation_list = list(dict.fromkeys(operation_list)) #remove duplicates
    return operation_list

def createBoard(calc_list):
    board_list = []
    
    for op in calc_list:
        board_numbers = re.findall(r'\b\d+\b', op) #remove operators and keep the numbers.
        board=''
        for i in board_numbers:
            board=board+i
        board_list.append(board)
    
    return board_list

def generateCombinations(start,end):
    operation_list=getOperations()
    calc_list=[]
    for i in range(start,end):
        for j in range(start,end):
            for k in range(start,end):
                for l in range(start,end):
                    for item in operation_list:
                        calc_list=doTheMath(item,i,j,k,l,calc_list)
    
    return calc_list

if __name__ == "__main__":
    
    calc_list=[]
    calc_list=generateCombinations(1,10)
    # print("[DEBUG] - calc_list with result 24:")
    # print('\n'.join(map(str, calc_list)))
    board_list=createBoard(calc_list)
    print("[DEBUG] - board_list:")
    print('\n'.join(map(str, board_list)))
    board_list=list(dict.fromkeys(board_list)) #remove duplicates
    print("[INFO] - Possible combinations: " + str(len(board_list)))

######
#TODO: GRAPHICS
######