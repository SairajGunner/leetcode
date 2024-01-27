const banana = ["B", "A", "N", "A", "N", "A"];
let sArray = [];

function containsBanana() {
  let result = true;
  for (const character of banana) {
    const charIndex = sArray.indexOf(character);
    if (charIndex === -1) {
      result = false;
      break;
    } else {
      sArray.splice(charIndex, 1);
    }
  }
  return { result: result, remaining: sArray };
}

function solution(S) {
  // Implement your solution here
  sArray = S.split("");
  let timesFound = 0;
  if (S.length < 6) {
    return 0;
  } else {
    while (containsBanana().result) {
      timesFound += 1;
    }
  }
  return timesFound;
}
