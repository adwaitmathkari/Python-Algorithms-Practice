import re

#this dict will store the conversion values in terms of a standard unit
dict1 = { "centimetres":"0.01 m", "metres":"1 m", "inches":"0.0254 m", 
        "feet":"0.3048 m", 
        "grams":"1 g", "kilograms":"1000 g", "pounds":"453.592 g", 
        "litres":"1 l", "mililitres":"0.001 l", "quarts":"0.946353 l", "gallons":"3.78541 l" }



def convert(s1):
    # takes in string 'how many litres in 1 quarts' and return the answer 
    
    #split the string s1 at " " a space 
    list_s1 = re.split(r'\s', s1)
    #find the numerical value in the string 
    val = re.findall(r'\d+', s1)
    
    # get the name of the first unit value and the last unit value whicha re at positions 2 and 6
    unit1 = list_s1[2]
    unit2 = list_s1[6]

    #get unit values here m, g, l.
    lunit1=dict1[unit1].split()
    lunit2=dict1[unit2].split()
    
    #compare units
    if lunit1[1] != lunit2[1]:
        print("Units do not match!!!!")
        return
    else:
        #formula for conversion
        return (float(lunit2[0])*float(val[0])/float(lunit1[0]))

print(convert(input()))