// Team 
// SoftDev pd0
// K27 -- Basic functions in JavaScript
// 2022-02-03r
// --------------------------------------------------

var fac = function(n){
    if (n == 1){
        return 1
    }
    return n * fac(n - 1)
}

var fib = function(n){
    if (n <= 1){
        return n
    }
    return fib(n - 1) + fib (n - 2)
}

// as a duo...
// pair programming style,
// implement a fact and fib fxn


//Do whatever you think is needed. Think: S I M P L E.   Think: S M A R T.
