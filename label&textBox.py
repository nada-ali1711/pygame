from pygame_functions import *
screenSize(700,700)

instructionLabel = makeLabel("plese enter the max depth",40,10,10,"blue","Agency FB","yellow")
showLabel(instructionLabel)

wordBox = makeTextBox(10,80,300,0,"enter text here",0,24)
showTextBox(wordBox)
entery = textBoxInput(wordBox)
print(entery)
