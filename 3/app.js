const fs = require('fs')

// const ruksackContend = fs.readFileSync('./3/example.txt', 'utf-8');
const ruksackContend = fs.readFileSync('./3/task.txt', 'utf-8');
let totalPriority = 0
let totalBadgePrio = 0
let itemInThreeRuksack = []

const messageInRows = ruksackContend.split('\r\n')

function ItemPriority(Letter) {

    if(Letter.charCodeAt() >= 97 ) {
        return Letter.charCodeAt() - 96
    } else {
        return Letter.charCodeAt() - 38
    }
    
}

messageInRows.forEach(currRow => {
    partA = currRow.slice(0,currRow.length/2)
    partB = currRow.slice(currRow.length/2,currRow.length)
    for (let index = 0; index < currRow.length/2; index++) {
        if (partB.includes(partA[index])) {
            currNumberScore = ItemPriority(partA[index])
            index = Infinity
        }
        
    }     
    totalPriority += currNumberScore
});

for (let RowsInd = 0; RowsInd < messageInRows.length; RowsInd += 3) {

    for (let LetterInd = 0; LetterInd < messageInRows[RowsInd].length; LetterInd++) {
        const currLetter = messageInRows[RowsInd][LetterInd];

        if(messageInRows[RowsInd+1].includes(currLetter) && messageInRows[RowsInd+2].includes(currLetter)) {
            totalBadgePrio += ItemPriority(currLetter)
            LetterInd = Infinity
        }  
        
    }
    
}

console.log('The sum of priorites is: ' + totalPriority)
console.log('The sum of badge is: ' + totalBadgePrio)