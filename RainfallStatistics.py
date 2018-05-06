
def getRainFallInput(sMonth):
    fRainfall = float(input('Enter the rainfall for ' + sMonth + ': '))
    return fRainfall




def main():

    #Declaring the tuple and the list needed

    sMonthNames = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                   'November', 'December')

    iAvgRainfall = []

    for element in sMonthNames:
        iAvgRainfall.append(getRainFallInput(element))

    #print(iAvgRainfall)

        

main()

