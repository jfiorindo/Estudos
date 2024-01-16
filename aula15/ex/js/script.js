const numero = Number(prompt('digite um número'));
const numerotitulo = document.getElementById('numero-titulo');
const raizquadrada = document.getElementById('raiz-quadrada');
const inteiro = document.getElementById('inteiro');
const nen = document.getElementById('nen');
const ArredondaMin = document.getElementById('arredondarmin');
const ArredondaMax = document.getElementById('arredondarmax');
const decimo = document.getElementById('decimo');

numerotitulo.innerHTML = numero

raizquadrada.innerHTML = `<p> a raiz quadrada do seu número é: ${Math.sqrt(numero)} <p>`;
inteiro.innerHTML = `<p> ${numero} é inteiro?: ${Number.isInteger(numero)} <p>`;
nen.innerHTML = `<p> é NaN? : ${(Number.isNaN(numero))} <p>`;
ArredondaMin.innerHTML = `<p> número arredondado pra baixo: ${Math.floor(numero)} <p>`;
ArredondaMax.innerHTML = `<p> número arredondado pra cima: ${Math.ceil(numero)} <p>`;
decimo.innerHTML = `<p> número com duas casas decimais: ${(numero.toFixed(2))} <p>`;




