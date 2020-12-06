def main():
    variableX = 2
    print(f'this is my var: {variableX}')
    print(f'string which is before the variable value: {functionX(10)}')
    print(f'string which is before the variable value: {functionX()}')
    text = "yes" if(variableX>3) else "no"
    print(text)
    loopFunction()

def functionX(x = 76):
    x = x + 1
    if(x > 75):
        return x # because of this the output type of this function is not going to be
    elif(x>50 and x<75):
        return 1
    else:
        return 0
    # None data type but number
    # remember if you do not specify returning data type it will always be None
    #print(f'the value is: {x}')

def loopFunction():
    # recap of for loop
    for x in range(9,-1,-1): # start, end (excluded), step
        if(x != 0):
            print(x)
        else:
            print('caboom')

    # recap of while loop
    tempVar = 10
    while(tempVar!=0):
        print('not zero')
        tempVar = tempVar - 1

    temperature = [30,-5,10,18, 20]
    for t in temperature:
        if t<0:
            print('its freezing')
        elif(t>0 and t<10):
            print('its pretty cold')
        elif(t>10 and t<20):
            print('its okay')
        elif(t>20):
            print('its hot')


if __name__ == "__main__": main()
