/* function addUp (num) {
    let total = 0;
    while (num != 0) {
      total += num;
      num -= 1;
    }
    return total;
  }
  
  let num = ;
  let total = addUp(num);
  console.log(total);
  */

 function minMax (list) {
    let small = 0; 
    let large = 0;
    for (const i in list) {
      small = list[i];
      large = list[i];
    }
    for (const i in list) {
      if (list[i] < small) {
        small = list[i];
      }
      if (list[i] > large) {
        large = list[i];
      }
    }
    return ([small,large]);
  }
  
  
let x = [1,2,3,4,5,6,7,8,9];
let l = minMax(x);
console.log(l)
let j = l[0];
let m = l[1];
console.log(j)
console.log(m)