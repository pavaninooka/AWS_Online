"""
Your module description
"""
{
   "molecules":{
      "lsInsulin":"malwmrllpllallalwgpdpaaa",
      "bInsulin":"fvnqhlcgshlvealylvcgergffytpkt",
      "aInsulin":"giveqcctsicslyqlenycn",
      "cInsulin":"rreaedlqvgqvelgggpgagslqplalegslqkr"
   },
   "weights":{
      "A":89.09,
      "C":121.16,
      "D":133.10,
      "E":147.13,
      "F":165.19,
      "G":75.07,
      "H":155.16,
      "I":131.17,
      "K":146.19,
      "L":131.17,
      "M":149.21,
      "N":132.12,
      "P":115.13,
      "Q":146.15,
      "R":174.20,
      "S":105.09,
      "T":119.12,
      "V":117.15,
      "W":204.23,
      "Y":181.19
   },
   "molecularWeightInsulinActual":5807.63
}
import jsonFileHandler
data = jsonFileHandler.readJsonFile('files/insulin.json')
if data != "" :
    bInsulin = data['molecules']['bInsulin']
    aInsulin = data['molecules']['aInsulin']
    insulin = bInsulin + aInsulin
    molecularWeightInsulinActual = data['molecularWeightInsulinActual']
    print('bInsulin: ' + bInsulin)
    print('aInsulin: ' + aInsulin)
    print('molecularWeightInsulinActual: ' + str(molecularWeightInsulinActual))
else:
    print("Error. Exiting program")
    

# Calculating the molecular weight of insulin  
# Getting a list of the amino acid (AA) weights  
aaWeights = data['weights']
# Count the number of each amino acids  
aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A','C','D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T','V', 'W', 'Y']})  
# Multiply the count by the weights  
molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in
['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T', 'V', 'W', 'Y']}.values())  
print("The rough molecular weight of insulin: " +
str(molecularWeightInsulin))
print("Percent error: " + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))