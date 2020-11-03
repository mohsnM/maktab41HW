let list1 = [3, 5, 9, 21, 43];
let list2 = [87, 34, 21, 43, 234];
let list3 = [[2, 3], 5, [[[2, 9], 4], 4], 1, 0];
let list4 = [32, 23, 12, 65, 65, 12, 54];

const deleteByIndex = (arr, index) => {
  arr.splice(index, 1);
  return arr;
};

const combineAndSort = (...arr) => {
  let combine = [];
  for (let i = 0; i < arr.length; i++) {
    combine = combine.concat(arr[i]);
  }
  combine.sort((a, b) => {
    return a - b;
  });
  return combine;
};

const flatArray = (arr) => {
  arr = arr.join();
  return arr.match(/[0-9]*[^,]/g);
};

const findByItem = (arr, item) => {
  return `index: ${arr.indexOf(item)}, item: ${item}`;
};

const replaceByItem = (arr, currentItem, newItem) => {
  let currentItemIndex = arr.indexOf(currentItem);
  arr[currentItemIndex] = newItem;
  return arr;
};

const extractNumberFromSrting = (str) => {
  return str.match(/[0-9]/g);
};

const removeDuplicateItems = (arr) => {
  return arr.filter((a, b) => arr.indexOf(a) === b);
};

/* the code above is main code of project */

let code, result, arg1, arg2, arg3;
code = document.getElementById("code");
arg1 = document.getElementById("arg1");
arg2 = document.getElementById("arg2");
arg3 = document.getElementById("arg3");
result = document.getElementById("result");

const toArray = (str) => {
  return str.match(/[0-9]*[^\][,\s]/g);
};

function callDeleteByIndex() {
  code.innerHTML = "deleteByIndex = " + deleteByIndex + ";";
  result.innerHTML ="[" + deleteByIndex(toArray(arg1.value), +arg2.value) + "]";
}

function callCombineAndSort() {
  code.innerHTML = "combineAndSort = " + combineAndSort + ";";
  result.innerHTML = "[" + combineAndSort(toArray(arg1.value)) + "]";
}

function callFlatArray() {
  code.innerHTML = "flatArray = " + flatArray + ";";
  result.innerHTML = "[" + flatArray(toArray(arg1.value)) + "]";
}

function callFindByItem() {
  code.innerHTML = "findByItem = " + findByItem + ";";
  result.innerHTML = findByItem(toArray(arg1.value), arg2.value);
}

function callReplaceByItem() {
  code.innerHTML = "replaceByItem = " + replaceByItem + ";";
  result.innerHTML = "[" + replaceByItem(toArray(arg1.value), arg2.value, arg3.value) + "]";
}

function callExtractNumberFromSrting() {
  code.innerHTML = "extractNumberFromSrting = " + extractNumberFromSrting + ";";
  result.innerHTML = extractNumberFromSrting(arg1.value);
}

function callRemoveDuplicateItems() {
  code.innerHTML = "removeDuplicateItems = " + removeDuplicateItems + ";";
  result.innerHTML = "[" + removeDuplicateItems(toArray(arg1.value)) + "]";
}
