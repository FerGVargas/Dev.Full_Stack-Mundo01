function add() { //Adicionar lista
  var entrada = document.getElementById("valor"); 
  var listaValores = document.getElementById("valores"); 
  var node = document.createElement("li"); 
  var textNode = document.createTextNode(entrada.value);
  node.appendChild(textNode); 
  listaValores.appendChild(node);
}

function limpar() { // Limpar lista
  let listaValores = document.getElementById('valores');
  listaValores.innerHTML = '';

  let input = document.getElementById('valor');
  input.value = '';
} 

function ordenar() { // Ordenar lista
  var listaValores = document.getElementById("valores");
  var listaSelecao = document.getElementById("selecao");
  let vetor = [];

  for (let i = 0; i < listaValores.children.length; i++) {
      vetor.push(eval(listaValores.children[i].innerHTML));
  }

  switch (listaSelecao.selectedIndex) { 
      case 0: 
      vetor.sort(function(a, b) {return a - b});
      break;
      case 1: 
      vetor.sorte(function(a, b) {return b - a});
      break;                       
  }
  listaValores.innerHTML = vetor.reduce((html, valor) => html + "<li>" + valor + "</li>", "");

}

function misturar(){ //Mistura lista
  var listaValores = document.getElementById("valores");
  let vetor = [];
  for (let i = 0; i < listaValores.children.length; i++) {
      vetor.push(eval(listaValores.children[i].innerHTML));
  }
  shuffle(vetor, vetor.length);
  listaValores.innerHTML = vetor.reduce((html, valor) => html + "<li>" + valor + "</li>", "");
}

// Swap

const swap = (vector, pos1, pos2) => {
  [vector[pos1], vector[pos2]] = [vector[pos2], vector[pos1]];
};

// Shuffle

const shuffle = (vector, swaps) => {
  for (let i = 0; i < swaps; i++) {
    let pos1 = Math.floor(Math.random() * vector.length);
    let pos2 = Math.floor(Math.random() * vector.length);
    swap(vector, pos1, pos2);
  }
};

// Bubble Sort
const bubbleSort = vector => {
  for (let i = 0; i < vector.length; i++) {
    for (let j = 0; j < vector.length - i - 1; j++) {
      if (vector[j] > vector[j + 1]) {
        swap(vector, j, j + 1);
      }
    }
  }
};

// Selection Sort
const selectionSort = vector => {
  for (let i = 0; i < vector.length - 1; i++) {
    let minIndex = i;
    for (let j = i + 1; j < vector.length; j++) {
      if (vector[j] < vector[minIndex]) {
        minIndex = j;
      }
    }
    if (minIndex !== i) {
      swap(vector, i, minIndex);
    }
  }
};

// Quick Sort
const quickSort = (vector, start = 0, end = vector.length - 1) => {
  if (start >= end) {
    return;
  }

  let pivotIndex = particionamento(vector, start, end);
  quickSort(vector, start, pivotIndex - 1);
  quickSort(vector, pivotIndex + 1, end);
};

 // Particionamento

const particionamento = (vector, start, end, pivot = vector[end]) => {
  let i = start - 1;
  for (let j = start; j <= end - 1; j++) {
    if (vector[j] <= pivot) {
      i++;
      swap(vector, i, j);
    }
  }
  swap(vector, i + 1, end);
  return i + 1;
};

