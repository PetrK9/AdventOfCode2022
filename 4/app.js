const fs = require('fs')

// const areasForClean = fs.readFileSync('./4/example.txt', 'utf-8');
const areasForClean = fs.readFileSync('./4/task.txt', 'utf-8');

FulloverLapCount = 0
AnyOverLapCount = 0;

const messageInRows = areasForClean.split('\r\n')

function PrepareIntOverlap(CurrElf) {
    const slitElf = CurrElf.split('-')
    let outputBoders = []

    slitElf.forEach(border => {
        outputBoders.push(parseInt(border))
    });

    return outputBoders
}

function FindOverLaps(ElfA, ElfB) {

    console.log(ElfA + ' | ' + ElfB)
    BordersA = PrepareIntOverlap(ElfA)
    BordersB = PrepareIntOverlap(ElfB)

    FulloverLapCount += CountFullOverLap(BordersA, BordersB)
    AnyOverLapCount += AnyOverlap(BordersA, BordersB)
}

function CountFullOverLap(BordersA, BordersB) {

    if ((BordersA[0] <= BordersB[0]) && (BordersA[1] >= BordersB[1])) {
        console.log("OverLap")
        return 1
    }
    if ((BordersA[0] >= BordersB[0]) && (BordersA[1] <= BordersB[1])) {
        console.log("OverLap")
        return 1
    }

    console.log("No full overlap")
    return 0

}

function AnyOverlap(BordersA, BordersB) {

    let OverLapB = false
    let OverLapA = false

    if ((BordersA[0] < BordersB[0]) && (BordersA[1] < BordersB[0])) {
        OverLapA = true

    }
    if ((BordersB[0] < BordersA[0]) && (BordersB[1] < BordersA[0])) {
        OverLapB = true
    }

    if (OverLapA || OverLapB) {
        console.log("No Full or partial overlap!!")
        return 0

    } else {
        console.log("Full or partial overlap")
        return 1
    }
}

messageInRows.forEach(currRow => {

    currElfs = currRow.split(',');
    FindOverLaps(currElfs[0], currElfs[1])

});

console.log('=============')
console.log('Count of Full Overlap: ' + FulloverLapCount)
console.log('Count of Full or partial Overlap: ' + AnyOverLapCount)