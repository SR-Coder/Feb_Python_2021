function sumOfAllNumbers(x,y,sum=0){
    sum = sum + x
    if(x===y){
        return sum
    }
    x = x + 1
    return sumOfAllNumbers(x,y,sum)
}

sumOfAllNumbers(1,10)