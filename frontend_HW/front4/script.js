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
  let newArr = [];
  for (let i = 0; i < arr.length; i += 2) {
    newArr.push(arr[i]);
  }
  return newArr;
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

console.log();
