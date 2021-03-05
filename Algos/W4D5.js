/* 
  Given an array and an item to search for,
  return the index where the item is found,

  return -1 to represent not found
  */

 const arr1 = ["a", "b", "c"];
 const searchItem1 = "c";
 const expected1 = 2;
 
 const arr2 = ["a", "b", "c"];
 const searchItem2 = 5;
 const expected2 = -1;
 
 const arr3 = ["c", "a", "b", "c"];
 const searchItem3 = "c";
 const expected3 = 0;
 
 const arr4 = [];
 const searchItem4 = 5;
 const expected4 = -1;
 
 /**
  * Finds the index from the given array where the given item is found.
  * - Time: O(?).
  * - Space: O(?).
  * @param {Array<any>} arr
  * @param {any} searchItem The item to find.
  * @return {number} The index of found item, or -1 if not found.
  */
 function indexOf(arr, searchItem) {
   // code here
 }
 
 module.exports = { indexOf };

 function indexOf(arr, searchItem) {
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === searchItem) {
      return i;
    }
  }
  return -1;
}
 
 /*****************************************************************************/

 /* 
  Recreate the pop method without using .pop()

  Remove and return the last item from a given array

  After removing an item from an array, what else changes?
*/

const arr1 = [1, 2, 3];
const expected1 = 3;
// what arr1 should be after running pop function
const expectedArr1 = [1, 2];

const arr2 = ["hello"];
const expected2 = "hello";
const expectedArr2 = []; // the only item was removed

const arr3 = ["hello", "world"];
const expected2 = "world";
const expectedArr3 = ["hello"]; // the last item was removed

const arr3 = [];
const expected3 = undefined;

/**
 * Removes the last item from the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<any>} arr
 * @return {any} The removed last item or undefined if the given array was
 *    was empty.
 */
function pop(arr) {
  
}

module.exports = { pop };

function pop(arr) {
  if (arr.length === 0) {
    return undefined;
  }

  const popped = arr[arr.length - 1];
  arr.length = arr.length - 1;
  return popped;
}

/*****************************************************************************/

