let romanEquals = {
    I: 1,
    V: 5,
    X: 10,
    L: 50,
    C: 100,
    D: 500,
    M: 1000
};

let toRomanLazy = (num, romanEquals) => {
    let romanSymbol = ''
    let romanLetters = Object.entries(romanEquals)
    //console.log(romanLetters)

    for (let i = romanLetters.length -1; i >= 0; i--) {
        
    }
}

toRomanLazy(150, romanEquals)