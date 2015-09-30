from CW_equations import *
from CW_graphics import *

class CW:
    
    def __init__(self):
        pass
    
    def printTable(self, data):
        f = open("OutputLists.txt", 'w')
        for i in self.outputData:
            f.write("%s\n" % i)
        f.close()

    def main(self):
        entryDisplay = EntryDisplay()
        equations = Equations()
        
        while True:
            if entryDisplay.ready:
              break
        self.outputData = equations.calculate(entryDisplay.getValues())
        
        self.printTable(self.outputData)
 

cW = CW()
cW.main()

    
        
## Select/Deselect window - option to keep individual variables
## available in display window
## Output graph:
##      3, 2d graphs
##      3d graph? (Nodebox)
##      User input orients and displays angle label

## Globe:
## from visual import *
## c = sphere(material = materials.earth)
## Develop curve over time, animate
