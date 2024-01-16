//string = texto | number = numero | undefined = sem valor na variável | null = nulo | boolean = true, false.

const nome = 'joão'; //string
const nome2 = "joão"; //string
const nome3 = `joão`; //string

const num = 34; //number
const num2 = 24.23; // number

let nomeAluno; //undefined -> não aponta pra local nenhum na memória
const sobrenomeAluno = null; // nulo -> não aponta pra local nenhum na memória    
const aprovado = true; // boolean = true, false (lógico)

const a = [1, 2];
const b = a;

console.log (a, b); // [1,2] [1,2]

b.push(3);

console.log(a,b); // ´[]

let a1 = 2;
const b1 = a1;

console.log(a1,b1); //2 2

a1 = 3;

console.log(a1,b1);// 3 2 