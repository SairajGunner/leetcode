// Does not work as expected
/**
 * @param {number[]} arr
 * @param {number} k
 * @return {number}
 */
var maxSumAfterPartitioning = function (arr, k) {
  let subArrays = [[]];
  let sum = 0;

  for (let i = 0; i < arr.length; i++) {
    const lastSubArrayLength = subArrays[subArrays.length - 1].length;
    let remainingPlaces = lastSubArrayLength === k ? 0 : k - lastSubArrayLength;
    if (remainingPlaces === 0) {
      subArrays.push([]);
      arr.splice(0, k - 1);
      remainingPlaces = k;
      i = 0;
    }
    const lookBack =
      i < k ? 0 : remainingPlaces === k ? i : i - remainingPlaces;
    console.log("lookBack: ", lookBack);
    const lookFwd = arr.length - i < k ? arr.length - 1 : i + k;
    let window = arr.slice(lookBack, lookFwd);
    console.log("arr: ", arr);
    console.log("window: ", window);
    let highestTemp = window.sort((a, b) => a - b)[window.length - 1];
    arr[i] = highestTemp;
    subArrays[subArrays.length - 1].push(highestTemp);
  }

  subArrays.forEach((subArray) => {
    sum += subArray.reduce((acc, cur) => acc + cur);
  });

  return sum;
};

console.log(maxSumAfterPartitioning([1, 15, 7, 9, 2, 5, 10], 3));
