### YOUR CODE FOR chocolatePrice() FUNCTION GOES HERE ###
def chocolatePrice(ali_budget, bashir_budget):
    minimum = ali_budget
    if bashir_budget < ali_budget:
        minimum = bashir_budget

    for chocolatePrice in range(1, minimum + 1):
        if((ali_budget % chocolatePrice) == 0 and (bashir_budget % chocolatePrice) == 0):
                MaximumPrice = chocolatePrice
    return (MaximumPrice)
   
#### End OF MARKER





### YOUR CODE FOR calculateProfit() FUNCTION GOES HERE ###
def calculateProfit(ali_budget, bashir_budget):
    if (type(ali_budget)==str or type(bashir_budget)==str):
        return "Not Possible"
    if (ali_budget == 0 or bashir_budget == 0):
        return "Not Possible"
 
    if (ali_budget < 0 or bashir_budget < 0):
        return"Not Possible"
    ali_budget = int(ali_budget)
    bashir_budget = int(bashir_budget)
    
    if ali_budget > bashir_budget:
        profitX = (ali_budget*1.5)-ali_budget
        profitY = (bashir_budget*2)-bashir_budget
        
    else:
        profitX = (ali_budget*2) - ali_Sbudget
        profitY = (bashir_budget*1.5) - bashir_budget
 
    if profitX > profitY:
        return profitX
 
    else:
        return profitY
        
#### End OF MARKER


