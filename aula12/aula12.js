let varA = 'a'; //b
let varB = 'b'; //c
let varC = 'c'; //a

const Vartmp = varA;
varA = varB;
varB = varC;
varC = Vartmp;

console.log(varA, varB, varC);