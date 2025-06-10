let factorial = (num) => {
    newNum = 1;
    for (num; num>0; num--) {
        newNum = newNum * num;
        //console.log(newNum);
    }
    return newNum
}
console.log(factorial(4))