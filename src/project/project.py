

#Input data
dataset  = [["Sunny","No"],
        ["Overcast","Yes"],
        ["Rainy","Yes"],
        ["Sunny","Yes"],
        ["Sunny","Yes"],
        ["Overcast","Yes"],
        ["Rainy","No"],
        ["Rainy","No"],
        ["Sunny","Yes"],
        ["Rainy","Yes"],
         ["Sunny","No"],
        ["Overcast","Yes"],
        ["Overcast","Yes"],
        ["Rainy","No"]]
listClasses = []
listValues = []
countTotal = len(dataset)
   
print(" DATA SET")
for i in range(len(dataset)):
        vector = dataset[i]
        print(vector)
print()




def getClassesAndValues(dataset):
    separated = dict()

   # count total of observations
    countTotal = len(dataset)
    print(countTotal)

    #get list of unique classes and values
    for i in range(len(dataset)):
        vector = dataset[i]
        class_value = vector[0]
        value = vector[1]
        if(class_value not in listClasses):
             listClasses.append(class_value)
        if(value not in listValues):
             listValues.append(value)
    
   
    
    result = {}
    for c in listClasses:
        result[c] = {}
        for v in listValues:
            result[c][v] = 0
   # print(result)
    return result

classesAndValues = getClassesAndValues(dataset);




        
# frequency table

def getFrenquencyTable(data,classesValuesList):
  
  
    for i in range(len(data)):
        vector = data[i]
        class_value = vector[0]#get class
        value = vector[1] # get value
        classesValuesList[class_value][value] += 1
       
        
                   
        
    return classesValuesList

freqTable = getFrenquencyTable(dataset,classesAndValues)
print(" CLASSES AND VALUES ")

for i in freqTable:
    print(i)
    print( freqTable[i])

def getPClass(freqTab, Class):
    
    countClass = 0

   
    for k in freqTab[Class].values():
             countClass += k
             

    return countClass/countTotal


def getPValue(freqTab, value):
    
    countValues = 0

    for key1 in freqTab:
            for key2 in freqTab[key1]:
                    if value == key2:
                            countValues += freqTab[key1][key2]

    return countValues/countTotal

print()
print(" CLASSES PROBABILITIES ")
for cl in listClasses:
        print(cl)
        print(getPClass(freqTable, cl))

print()

print(" VALEUS PROBABILITIES ")
for vl in listValues:
        print(vl)
        print(getPValue(freqTable,vl))



               

#P(C|V)
def ProbClassGivenValue(freqTab,Class,Value):
        countValues = 0
        Total = 0

        for cl in freqTab: 
                for vl in freqTab[cl]:
                        if vl == Value:
                                Total += freqTab[cl][vl]
                                if cl == Class:
                                        countValues += freqTab[cl][vl]


                        
                                
                      
        return countValues/Total
        
      
        
print()  
print("Probability of a Class given a value: P(C|V)")

for CLASS in listClasses:
        for VALUE in listValues:
                print(CLASS,' ',VALUE, ' ', ProbClassGivenValue(freqTable,CLASS,VALUE))

        
def testNavieBayes(newValue,CLASS):

        probValue = getPValue(freqTable,newValue)
        probClass = getPClass(freqTable, CLASS)
        probClassGivenValue = ProbClassGivenValue(freqTable,CLASS,newValue)
        #using Navie Bayes P(V|C) = P(V)/P(C)*P(C|V)
        probValueGivenClass = (probValue*probClassGivenValue)/probClass

        return probValueGivenClass
print()
print("TEST NAVIE BAYES")
for CLASS in listClasses:
        for VALUE in listValues:
                print("Probability ", VALUE, " given data class: ", CLASS)
                print( testNavieBayes(VALUE,CLASS))

        
        

          
