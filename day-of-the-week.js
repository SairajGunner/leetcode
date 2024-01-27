// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(S, K) {
  const days = [
    { index: 0, day: "Mon" },
    { index: 1, day: "Tue" },
    { index: 2, day: "Wed" },
    { index: 3, day: "Thu" },
    { index: 4, day: "Fri" },
    { index: 5, day: "Sat" },
    { index: 6, day: "Sun" }
  ];
  let dayIndex = days.findIndex((day) => day.day === S);
  const futureDayIndex = dayIndex + K;
  const futureDay = days.find((day) => day.index === futureDayIndex % 7).day;
  console.log(futureDay);
  return futureDay;
}

solution("Wed", 2);
