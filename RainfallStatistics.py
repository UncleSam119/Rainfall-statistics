import matplotlib.pyplot as plt
# Declaring global variables to be used throughout all functions
sMonthNames = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
               'November', 'December')
iAvgRainfall = []


def getRainFallInput(sMonth):

    # Receives month name and prompts user for rainfall input also with input validation
    fRainfall = -1
    while fRainfall <= 0:
        try:
                fRainfall = float(input('Enter the rainfall for ' + sMonth + ': '))
        except ValueError:
                print('Invalid input, only input numbers!')

    return fRainfall


def inputLoop():
    global iAvgRainfall

    # Main input loop made into its own function to clean up main
    for element in sMonthNames:

        # calling input function and appending results to list
        iAvgRainfall.append(getRainFallInput(element))

   # print(iAvgRainfall)


def getMin():
    # finding min index
    iMin = iAvgRainfall.index(min(iAvgRainfall))

    # matching min index with month name and printing
    print('Lowest rainfall: ' + sMonthNames[iMin])


def getMax():
    # finding max index
    iMax = iAvgRainfall.index(max(iAvgRainfall))

    # matching index with month name and printing
    print('Highest rainfall: ' + sMonthNames[iMax])


def getAvg():
    # calculating average
    iAvg = format(sum(iAvgRainfall) / len(iAvgRainfall), '.2f')

    # converting to string and printing average
    print('Average rainfall: ' + str(iAvg))


def lineGraph():
    # This functions going to produce the line graph

    # months
    x_coords = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    # rainfall
    y_coords = iAvgRainfall

    # building line graph
    plt.plot(x_coords, y_coords, marker='s')

    # title
    plt.title('Rainfall line graph by month')

    # axis labels
    plt.xlabel('Months')
    plt.ylabel('Rainfall')

    # axis limits
    plt.xlim(xmin=-1, xmax=12)
    plt.ylim(ymin=-1, ymax=(max(iAvgRainfall)+1))

    # x axis ticks
    plt.xticks(
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        sMonthNames
    )

    # adding grid
    plt.grid(True)

    # show
    plt.show()


def main():

    inputLoop()
    getMin()
    getMax()
    getAvg()
    lineGraph()



main()

