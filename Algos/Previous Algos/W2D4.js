
/* 
  Given a string,
  return a new string with the duplicates excluded
  Bonus: Keep only the last instance of each character.
*/

const str1 = "abcABC";
const expected1 = "abcABC";

const str2 = "helloo";
const expected2 = "helo";

/**
 * De-dupes the given string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str A string that may contain duplicates.
 * @return {string} The given string with any duplicate characters removed.
 */
/**
 * - Time: O(n) linear.
 * - Space: O(2n) -> O(n) linear.
 */
function stringDedupe(str) {
  let distinctStr = "";
  const seen = {};

  // loop backwards to include last occurrence
  for (let i = str.length - 1; i >= 0; --i) {
    if (!seen[str[i]]) {
      distinctStr = str[i] + distinctStr;
      seen[str[i]] = true;
    }
  }
  return distinctStr;
}

module.exports = { stringDedupe };

/*****************************************************************************/

/* 
  Given a string containing space separated words
  Reverse each word in the string.
  If you need to, use .split to start, then try to do it without.
*/

const str1 = "hello";
const expected1 = "olleh";

const str2 = "hello world";
const expected2 = "olleh dlrow";

const str3 = "abc def ghi";
const expected3 = "cba fed ihg";

/**
 * Reverses the letters in each words in the given space separated
 * string of words. Does NOT reverse the order of the words themselves.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str Contains space separated words.
 * @return {string} The given string with each word's letters reversed.
 */
function reverseWordsSplit(wordsStr) {
  const words = wordsStr.split(" ");
  let wordsReversed = "";

  for (const word of words) {
    let reversedWord = "";

    for (let i = word.length - 1; i >= 0; --i) {
      reversedWord += word[i];
    }

    // add a space in front of word if it's not the first word
    if (wordsReversed.length > 0) {
      reversedWord = " " + reversedWord;
    }
    wordsReversed += reversedWord;
  }
  return wordsReversed;
}

module.exports = { reverseWords };

/*****************************************************************************/