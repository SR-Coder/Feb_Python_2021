/* 
  Given an int to represent how much change is needed
  calculate the fewest number of coins needed to create that change,
  using the standard US denominations
*/

const cents1 = 25;
const expected1 = { quarter: 1 };

const cents2 = 50;
const expected2 = { quarter: 2 };

const cents3 = 9;
const expected3 = { nickel: 1, penny: 4 };

const cents4 = 99;
const expected4 = { quarter: 3, dime: 2, penny: 4 };

function fewestCoinChange(cents) {
      var change = {}
      var quarters = Math.floor(cents / 25);
      console.log(quarters);
      cents = cents%25;
      console.log(cents);
      var dimes = Math.floor(cents / 10);
      cents = cents%10;
      var nickles = Math.floor(cents / 5);
      cents = cents%5;
      pennys = cents;

      if(quarters>0){
        change['quarters'] = quarters;
      }
      if(dimes>0){
        change['dimes'] = dimes;
      }
      if(nickles>0){
        change['nickles'] = nickles;
      }
      if(pennys>0){
        change['pennys'] = pennys
      }
      return change
}
console.log(fewestCoinChange(99))
module.exports = { fewestCoinChange };

/*****************************************************************************/
